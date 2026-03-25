# Source: https://docs.snowflake.com/en/sql-reference/functions/system_generate_scim_access_token.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GENERATE_SCIM_ACCESS_TOKEN

Returns a new SCIM access token that is valid for six months.

## Syntax

```sqlsyntax
SYSTEM$GENERATE_SCIM_ACCESS_TOKEN('<integration_name>')
```

## Arguments

`<integration_name>`
:   Name of the security integration where `TYPE = SCIM`. Note that the integration name is case-sensitive, must be uppercase, and be enclosed in single quotes.

    For more information, see [CREATE SECURITY INTEGRATION](../sql/create-security-integration-scim.md).

## Usage notes

* Generating a new SCIM access token does not invalidate an existing token. To invalidate an access token,
  you must delete the entire SCIM security integration using the [DROP INTEGRATION](../sql/drop-integration.md) command. At that point, you can
  recreate the security integration using the [CREATE SECURITY INTEGRATION](../sql/create-security-integration-scim.md) command, and then use this
  function to generate a new token.
* There is no limit to the number of SCIM access tokens that you can generate.

## Output

The function returns the SCIM access token as a string.

## Examples

The following example retrieves the SCIM access token for the specified integration:

> ```sqlexample
> SELECT SYSTEM$GENERATE_SCIM_ACCESS_TOKEN('OKTA_PROVISIONING');
> ```
