# Source: https://docs.snowflake.com/en/sql-reference/functions/system_set_application_restricted_feature_access.md

Categories:
:   [System functions](../functions-system.md) (Control)

# SYSTEM$SET_APPLICATION_RESTRICTED_FEATURE_ACCESS

Enables a restricted feature for a Snowflake Native App. Currently, only external and Apache Iceberg™ tables are
supported.

## Syntax

```sqlsyntax
SYSTEM$SET_APPLICATION_RESTRICTED_FEATURE_ACCESS(
  '<app_name>',
  '<type>',
  '<parameters>'
)
```

## Arguments

`app_name`
:   Name of the Snowflake Native App.

`type`
:   The type of restricted feature. Currently only `EXTERNAL_DATA` is supported.

`parameters`
:   A JSON object that contains configuration parameters for the restricted feature. Currently,
    only JSON objects of the following format are supported:

    ```json
    {"allowed_cloud_providers" : "all"}
    ```

    The supported values for `allowed_cloud_providers` are `all` and `none`.

## Returns

A JSON object containing a list of external features whose value the consumer has set. The JSON
object has the following structure:

```sqljson
"{""external_data"":{""allowed_cloud_providers"":""all""}}"
```

## Examples

To call the function:

```sqlexample
SELECT SYSTEM$SET_APPLICATION_RESTRICTED_FEATURE_ACCESS('hello_snowflake_app', 'external_data', '{"allowed_cloud_providers" : "none"}');
```

Sample output:

```output
"SYSTEM$SET_APPLICATION_RESTRICTED_FEATURE_ACCESS('EXTERNAL_DATA_DEMO_APP', 'EXTERNAL_DATA', '{""ALLOWED_CLOUD_PROVIDERS"" : ""NONE""}')"
"{""external_data"":{""allowed_cloud_providers"":""none""}}"
```
