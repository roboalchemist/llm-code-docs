# Source: https://docs.snowflake.com/en/sql-reference/functions/system_start_oauth_flow.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$START_OAUTH_FLOW

Initiates the OAUTH client flow, returning a URL you use in a browser to complete the OAuth consent process.

## Syntax

```sqlsyntax
SYSTEM$START_OAUTH_FLOW( '<database_name.schema_name.secret_name>' )
```

## Arguments

`'database_name.schema_name.secret_name'`
:   The name of the OAuth2 secret specifying authentication information for the API to access with OAuth.

## Usage notes

Use this function to begin a flow that results in an OAuth refresh token added to the secret you pass to this function as an argument.

As an intermediate step, this function returns an authorization URL you can in a browser to complete the OAuth consent process.

After executing this function and using the URL it returns, immediately execute [SYSTEM$FINISH_OAUTH_FLOW](system_finish_oauth_flow.md)
in the same session to have Snowflake add a refresh token to the secret you specified.

The [secret](../sql/create-secret.md) in this function’s argument must include:

* A TYPE parameter specifying a value of `oauth2`.
* An API_AUTHENTICATION parameter specifying a [security integration](../sql/create-security-integration-api-auth.md)
  containing details (such as OAuth client ID, secret, authorization endpoint, and token endpoint) about the service provider for which
  access is being granted.
