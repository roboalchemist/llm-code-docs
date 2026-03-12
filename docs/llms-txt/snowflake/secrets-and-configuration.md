# Source: https://docs.snowflake.com/en/developer-guide/streamlit/app-development/secrets-and-configuration.md

# Manage secrets and configure your Streamlit app

Streamlit apps often need to access sensitive information such as API keys, passwords, and other credentials. How you manage
secrets in your Streamlit app depends on the runtime environment you’re using. Streamlit in Snowflake provides secure, built-in mechanisms
for accessing secrets in both warehouse and container runtimes. For Streamlit configuration, each runtime has
different restrictions, too.

In the Streamlit library, apps use a `.streamlit/` directory to store configuration and secrets:

* `.streamlit/config.toml`: Customizes app settings such as theme, layout, and server behavior.
* `.streamlit/secrets.toml`: Stores sensitive information like API keys and credentials (in local development).

Streamlit in Snowflake supports these files with some limitations depending on your runtime environment. The following table
summarizes the support for these files in warehouse and container runtimes:

| Feature | Warehouse runtime | Container runtime |
| --- | --- | --- |
| `config.toml` support | Limited subset of configuration options | Broader subset of configuration options |
| `secrets.toml` support | Not supported | Supported, but only recommended for non-secret environment variables |

For `secrets.toml`, Streamlit in Snowflake provides a more secure, built-in secrets management system that is recommended
for managing sensitive information. The following sections describe how to use Snowflake secrets in your apps.

## Managing your connection to Snowflake

To manage your connection to Snowflake, you can use [`st.connection("snowflake")`](https://docs.streamlit.io/develop/api-reference/connections/st.connections.snowflakeconnection). This allows you to connect to Snowflake from both
your local development environment and your deployed app.

```python
import streamlit as st

conn = st.connection("snowflake")
session = conn.session()

session.sql("SELECT 1").collect()
```

In warehouse runtimes, you can also use Snowpark’s [`get_active_session()`](/developer-guide/snowpark/reference/python/latest/snowpark/api/snowflake.snowpark.context.get_active_session) function to get the active session.

```python
import streamlit as st
from snowflake.snowpark.context import get_active_session

# ONLY IN WAREHOUSE RUNTIMES
session = get_active_session()
session.sql("SELECT 1").collect()
```

> **Important:**
>
> `get_active_session()` isn’t thread-safe and can’t be used in container runtimes.

## Secrets in container runtimes

Container runtimes don’t have access to the `_snowflake` module because they run outside of the stored procedure
environment. To access secrets in a container runtime, you must create SQL functions that use the `_snowflake` module
and then call those functions from your Streamlit app. For Cortex API calls, you must use `requests`.

If you upgrade an older Streamlit app to a container runtime, the following `_snowflake` functions should
be replaced with stored procedures. This is described in the next section.

* `get_generic_secret_string`
* `get_oauth_access_token`
* `get_username_password`
* `get_cloud_provider_token`
* `get_secret_type`

Additionally, the following `_snowflake` function should be replaced with a manual API call,
authenticated with a session token. This is described in a later section, Calling a Cortex Agent in a container runtime.

* `send_snow_api_request`

### Access a secret in a container runtime

To access a secret in a container runtime do the following steps:

1. Create a secret in your Snowflake account. See [CREATE SECRET](../../../sql-reference/sql/create-secret.md).

   ```sqlexample
   CREATE OR REPLACE SECRET my_secret
     TYPE = GENERIC_STRING
     SECRET_STRING = 'my_secret_value';
   ```

2. Create a function to access your secret. See [Python API for Secret Access](../../external-network-access/secret-api-reference.md).

   ```sqlexample
   CREATE OR REPLACE FUNCTION get_my_secret()
     RETURNS STRING
     LANGUAGE PYTHON
     RUNTIME_VERSION = 3.12
     HANDLER = 'get_my_secret'
     EXTERNAL_ACCESS_INTEGRATIONS = (my_eai)
     SECRETS = ('my_secret' = my_secret)
     AS
   $$
   import _snowflake

   def get_my_secret():
     return _snowflake.get_generic_secret_string('my_secret')
   $$;
   ```

3. Create your Streamlit app with the container runtime:

   ```sqlexample
   CREATE STREAMLIT my_container_app
     FROM '@my_stage/app_folder'
     MAIN_FILE = 'streamlit_app.py'
     RUNTIME_NAME = 'SYSTEM$ST_CONTAINER_RUNTIME_PY3_11'
     COMPUTE_POOL = my_compute_pool
     QUERY_WAREHOUSE = my_warehouse
     EXTERNAL_ACCESS_INTEGRATIONS = (my_eai);
   ```

4. In your Streamlit app code, call the SQL function to retrieve the secret:

   ```python
   import streamlit as st

   # Get the Snowflake connection
   conn = st.connection("snowflake")
   session = conn.session()

   # Call the function to retrieve the secret
   secret = session.sql("SELECT get_my_secret()").collect()[0][0]
   ```

### Using `.streamlit/secrets.toml` for non-secret environment variables

While you can technically add a `.streamlit/secrets.toml` file to your app’s source
directory, this is **not recommended for storing actual secrets**. The `secrets.toml`
file is stored as plain text in your staged files, which is not a security best practice.

However, `secrets.toml` can be useful for storing non-sensitive configuration values or environment-specific settings
that you want to access via `st.secrets` in your code or that a dependency requires as an environment variable:

```toml
# .streamlit/secrets.toml
# ONLY USE FOR NON-SECRET CONFIGURATION VALUES
app_name = "My Streamlit App"
api_endpoint = "https://api.example.com"
max_results = 100
```

You can then access these values in your app through `st.secrets` or as environment variables:

```python
import streamlit as st
import os

app_name = st.secrets["app_name"]
API_ENDPOINT = os.getenv("API_ENDPOINT")
```

For actual secrets like API keys, passwords, and tokens, always use Snowflake’s built-in secrets management system
as described in the previous section.

### Calling a Cortex Agent in a container runtime

To call a Cortex Agent in a container-runtime app, read the session token from the
underlying Snowpark Container Services container and then use the `requests` library. This is the
recommended replacement for `_snowflake.send_snow_api_request()`.

```python
import requests
import json
import os

SNOWFLAKE_HOST = os.getenv("SNOWFLAKE_HOST")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
ANALYST_ENDPOINT = "/api/v2/cortex/analyst/message"
URL = "https://" + SNOWFLAKE_HOST + ANALYST_ENDPOINT

def get_token() -> str:
    """Read the oauth token embedded into SPCS container"""
    return open("/snowflake/session/token", "r").read()

def send_request(semantic_model_file, prompt):
    """Sends the prompt using the semantic model file """
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "Authorization": f"Bearer {get_token()}",
        "X-Snowflake-Authorization-Token-Type": "OAUTH"
    }
    request_body = {
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
        "semantic_model_file": semantic_model_file,
    }
    return requests.post(URL, headers=headers, data=json.dumps(request_body))
```

## Secrets in warehouse runtimes

In warehouse runtimes, you can use the `_snowflake` module to access secrets directly in your Streamlit app code.
Warehouse runtimes inherit access to the `_snowflake` module from stored procedures, which allows you to retrieve
secrets that are referenced in the Streamlit object.

To use secrets in a warehouse runtime:

1. Create a secret object in Snowflake. For more information, see [CREATE SECRET](../../../sql-reference/sql/create-secret.md).

   ```sqlexample
   CREATE OR REPLACE SECRET my_secret
     TYPE = GENERIC_STRING
     SECRET_STRING = 'my_secret_value';
   ```

2. Create an external access integration and assign the secret to it.

   ```sqlexample
   CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION my_eai
     ALLOWED_AUTHENTICATION_SECRETS = (my_secret)
     ENABLED = TRUE;
   ```

3. Reference the secret in your Streamlit object using the SECRETS parameter:

   ```sqlexample
   ALTER STREAMLIT my_warehouse_app
     SET EXTERNAL_ACCESS_INTEGRATIONS = (my_eai)
     SECRETS = ('my_secret_key' = my_secret);
   ```

   You must assign both the external access integration and the secret to the Streamlit object. You can’t assign a
   secret to a Streamlit object by itself.
4. In your Streamlit app code, import the `_snowflake` module and retrieve the secret:

   ```python
   import streamlit as st
   import _snowflake

   # Retrieve an API key from a generic string secret
   my_secret = _snowflake.get_generic_secret_string('my_secret_key')
   ```

For more information about accessing secrets with the `_snowflake` module, see [Python API for Secret Access](../../external-network-access/secret-api-reference.md).

## Streamlit configuration

Streamlit apps can include a configuration file (`.streamlit/config.toml`). This file allows
you to customize various aspects of your app, such as the theme, layout, and behavior. The configuration
file is written in TOML format. For more information about available configuration options, see the
Streamlit documentation on [`config.toml`](https://docs.streamlit.io/develop/api-reference/configuration/config.toml).

Support for configuration options varies by runtime environment. Container runtimes generally provide
broader support for configuration options than warehouse runtimes, particularly for static serving.
The following table shows which configuration sections are supported in warehouse and container runtimes:

| Configuration section | Warehouse runtime | Container runtime |
| --- | --- | --- |
| `[global]` | Not supported | Limited support (`disableWidgetStateDuplicationWarning`) |
| `[logger]` | Not supported | Not supported |
| `[client]` | Not supported | Limited support (`showErrorDetails`, `showSidebarNavigation`) |
| `[runner]` | Not supported | Supported |
| `[server]` | Not supported | Not supported |
| `[browser]` | Not supported | Not supported |
| `[mapbox]` | Not supported | Supported (deprecated, use environment variables instead) |
| `[theme]` | Supported | Supported |
| `[theme.sidebar]` | Supported | Supported |
| `[secrets]` | Not supported | Supported (but only recommended for non-secret environment variables) |
| `[snowflake.sleep]` | Supported | Not applicable |

For information about using the `[snowflake.sleep]` section to configure sleep timers in warehouse runtimes, see
[Custom sleep timer for a Streamlit app](../features/sleep-timer.md).

The following directory structure shows an example of a Streamlit app with a configuration file:

```none
source_directory/
├── .streamlit/
│   └── config.toml
├── pyproject.toml
├── streamlit_app.py
└── uv.lock
```
