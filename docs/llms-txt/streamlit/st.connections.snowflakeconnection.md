# st.connections.SnowflakeConnection

A connection to Snowflake using the Snowflake Connector for Python.

Initialize this connection object using `st.connection("snowflake")` or `st.connection("<name>", type="snowflake")`. Connection parameters for a SnowflakeConnection can be specified using `secrets.toml` and/or `**kwargs`. Connection parameters are passed to `snowflake.connector.connect()`.

When an app is running in Streamlit in Snowflake, `st.connection("snowflake")` connects automatically using the app owner's role without further configuration. `**kwargs` will be ignored in this case. Use `secrets.toml` and `**kwargs` to configure your connection for local development.

SnowflakeConnection includes several convenience methods. For example, you can directly execute a SQL query with `.query()` or access the underlying Snowflake Connector object with `.raw_connection`.

## Example

### Example 1: Configuration with Streamlit secrets

You can configure your Snowflake connection using Streamlit's [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management). For example, if you have MFA enabled on your account, you can connect using [key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth).

`streamlit/secrets.toml`:

```toml
[connections.snowflake]
account = "xxx-xxx"
user = "xxx"
private_key_file = "/xxx/xxx/xxx.p8"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 2: Configuration with keyword arguments and external authentication

You can configure your Snowflake connection with keyword arguments. The keyword arguments are merged with (and take precedence over) the values in `secrets.toml`. However, if you name your connection `snowflake` and don't have a `[connections.snowflake]` dictionary in your `secrets.toml` file, Streamlit will ignore any keyword arguments and use the default Snowflake connection as described in Example 5 and Example 6. To configure your connection using only keyword arguments, declare a name for the connection other than `snowflake`.

For example, if your Snowflake account supports SSO, you can set up a quick local connection for development using [browser-based SSO](https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use#how-browser-based-sso-works). Because there is nothing configured in `secrets.toml`, the name is an empty string and the type is set to `snowflake`. This prevents Streamlit from ignoring the keyword arguments and using a default Snowflake connection.

```python
import streamlit as st
conn = st.connection(
    "<name>",
    type="snowflake",
    account="xxx-xxx",
    user="xxx",
    authenticator="externalbrowser",
)
df = conn.query("SELECT * FROM my_table").collect()
```

### Example 3: Named connection with Snowflake's connection configuration file

Snowflake's Python Connector supports a connection configuration file, which is well integrated with Streamlit's SnowflakeConnection. If you already have one or more connections configured, all you need to do is pass the name of the connection to use.

`~/.snowflake/connections.toml`:

```toml
[my_connection]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
```

Your app code:

```python
import streamlit as st
conn = st.connection("my_connection", type="snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 4: Named connection with Streamlit secrets and Snowflake's connection configuration file

If you have a Snowflake configuration file with a connection named `my_connection` as in Example 3, you can pass the connection name through `secrets.toml`.

`streamlit/secrets.toml`:

```toml
[connections.snowflake]
connection_name = "my_connection"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 5: Default connection with an environment variable

If you don't have a `[connections.snowflake]` dictionary in your `secrets.toml` file and use `st.connection("snowflake")`, Streamlit will use the default connection for the [Snowflake Python Connector](https://docs.snowflake.cn/en/developer-guide/python-connector/python-connector-connect#setting-a-default-connection).

If you have a Snowflake configuration file with a connection named `my_connection` as in Example 3, you can set an environment variable to declare it as the default Snowflake connection.

```python
SNOWFLAKE_DEFAULT_CONNECTION_NAME = "my_connection"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 6: Default connection in Snowflake's connection configuration file

If you have a Snowflake configuration file that defines your `default` connection, Streamlit will automatically use it if no other connection is declared.

`~/.snowflake/connections.toml`:

```toml
[default]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

## Methods

### cursor

Create a new cursor object from this connection.

Snowflake Connector cursors implement the Python Database API v2.0 specification (PEP-249). For more information, see the [Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#object-cursor).

### query

Run a read-only SQL query.

This method implements query result caching and simple error handling/retries. The caching behavior is identical to that of using `st.cache_data`.

Queries that are run without a specified `ttl` are cached indefinitely.

### reset

Reset this connection so that it gets reinitialized the next time it's used.

This method can be useful when a connection has become stale, an auth token has expired, or in similar scenarios where a broken connection might be fixed by reinitializing it. Note that some connection methods may already use `reset()` in their error handling code.

### session

Create a new Snowpark session from this connection.

For information on how to use Snowpark sessions, see the [Snowpark developer guide](https://docs.snowflake.com/en/developer-guide/snowpark/python/working-with-dataframes) and [Snowpark API Reference](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/snowpark/session).

### write_pandas

Write a `pandas.DataFrame` to a table in a Snowflake database.

This convenience method is a thin wrapper around `snowflake.connector.pandas_tools.write_pandas()` using the underlying connection. The `conn` parameter is passed automatically. For more information and additional keyword arguments, see the [Snowflake Connector for Python documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#write_pandas).

## Examples

### Example 1: Configuration with Streamlit secrets

You can configure your Snowflake connection using Streamlit's [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management). For example, if you have MFA enabled on your account, you can connect using [key-pair authentication](https://docs.snowflake.com/en/user-guide/key-pair-auth).

`streamlit/secrets.toml`:

```toml
[connections.snowflake]
account = "xxx-xxx"
user = "xxx"
private_key_file = "/xxx/xxx/xxx.p8"
role = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 2: Configuration with keyword arguments and external authentication

You can configure your Snowflake connection with keyword arguments. The keyword arguments are merged with (and take precedence over) the values in `secrets.toml`. However, if you name your connection `snowflake` and don't have a `[connections.snowflake]` dictionary in your `secrets.toml` file, Streamlit will ignore any keyword arguments and use the default Snowflake connection as described in Example 5 and Example 6. To configure your connection using only keyword arguments, declare a name for the connection other than `snowflake`.

For example, if your Snowflake account supports SSO, you can set up a quick local connection for development using [browser-based SSO](https://docs.snowflake.com/en/user-guide/admin-security-fed-auth-use#how-browser-based-sso-works). Because there is nothing configured in `secrets.toml`, the name is an empty string and the type is set to `snowflake`. This prevents Streamlit from ignoring the keyword arguments and using a default Snowflake connection.

```python
import streamlit as st
conn = st.connection(
    "<name>",
    type="snowflake",
    account="xxx-xxx",
    user="xxx",
    authenticator="externalbrowser",
)
df = conn.query("SELECT * FROM my_table").collect()
```

### Example 3: Named connection with Snowflake's connection configuration file

Snowflake's Python Connector supports a connection configuration file, which is well integrated with Streamlit's SnowflakeConnection. If you already have one or more connections configured, all you need to do is pass the name of the connection to use.

`~/.snowflake/connections.toml`:

```toml
[my_connection]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
```

Your app code:

```python
import streamlit as st
conn = st.connection("my_connection", type="snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 4: Named connection with Streamlit secrets and Snowflake's connection configuration file

If you have a Snowflake configuration file with a connection named `my_connection` as in Example 3, you can pass the connection name through `secrets.toml`.

`streamlit/secrets.toml`:

```toml
[connections.snowflake]
connection_name = "my_connection"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 5: Default connection with an environment variable

If you don't have a `[connections.snowflake]` dictionary in your `secrets.toml` file and use `st.connection("snowflake")`, Streamlit will use the default connection for the [Snowflake Python Connector](https://docs.snowflake.cn/en/developer-guide/python-connector/python-connector-connect#setting-a-default-connection).

If you have a Snowflake configuration file with a connection named `my_connection` as in Example 3, you can set an environment variable to declare it as the default Snowflake connection.

```python
SNOWFLAKE_DEFAULT_CONNECTION_NAME = "my_connection"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```

### Example 6: Default connection in Snowflake's connection configuration file

If you have a Snowflake configuration file that defines your `default` connection, Streamlit will automatically use it if no other connection is declared.

`~/.snowflake/connections.toml`:

```toml
[default]
account = "xxx-xxx"
user = "xxx"
password = "xxx"
warehouse = "xxx"
database = "xxx"
schema = "xxx"
```

Your app code:

```python
import streamlit as st
conn = st.connection("snowflake")
df = conn.query("SELECT * FROM my_table")
```