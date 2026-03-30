# Source: https://docs.snowflake.com/en/sql-reference/functions/system_show_oauth_client_secrets.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$SHOW_OAUTH_CLIENT_SECRETS

Returns the client secrets in a string. The client ID and a client secret must be included in the authorization header to the OAuth token endpoint.

## Syntax

```sqlsyntax
SYSTEM$SHOW_OAUTH_CLIENT_SECRETS( '<integration_name>' )
```

## Arguments

`integration_name`
:   Name of the integration. Note that the integration name is case-sensitive and must be uppercase and enclosed in single quotes.

## Output

The function returns the following elements in a JSON object:

| Column Name | Data Type | Description |
| --- | --- | --- |
| oauth_client_secret_2 | BASE64 | Secondary client secret for the specified integration. Snowflake supports two client secrets to allow for uninterrupted rotation. |
| oauth_client_secret | BASE64 | Client secret for the specified integration |
| oauth_client_id | STRING | Client ID in Snowflake |

## Examples

The following example retrieves the client secret for the specified integration:

> ```sqlexample
> select system$show_oauth_client_secrets('MYINT');
> ```
