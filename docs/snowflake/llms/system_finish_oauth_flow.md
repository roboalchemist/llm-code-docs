# Source: https://docs.snowflake.com/en/sql-reference/functions/system_finish_oauth_flow.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$FINISH_OAUTH_FLOW

Sets the OAUTH_REFRESH_TOKEN parameter value of the secret passed as an argument in the [SYSTEM$START_OAUTH_FLOW](system_start_oauth_flow.md)
call that began the OAuth flow.

This function completes the OAuth client flow begun with SYSTEM$START_OAUTH_FLOW.

## Syntax

```sqlsyntax
SYSTEM$FINISH_OAUTH_FLOW( '<query_string>' )
```

## Arguments

`'query_string'`
:   Query string from the URL in the browser after completing user authentication and providing OAuth consent.

## Usage notes

Use this function to set the refresh token of an OAuth2 secret you’re using to authenticate with a service provider. This function finishes an
OAuth flow that must begin with your call to [SYSTEM$START_OAUTH_FLOW](system_start_oauth_flow.md).

You must execute this function immediately after – and in the same session as – SYSTEM$START_OAUTH_FLOW. This ensures that the user who is
finishing the flow is the same as the user who started it.

## Examples

```sqlexample
SELECT SYSTEM$FINISH_OAUTH_FLOW('state=252462476&authz_code=54264262');
```
