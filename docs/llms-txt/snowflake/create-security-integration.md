# Source: https://docs.snowflake.com/en/connectors/microsoft/powerapps/create-security-integration.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/create-security-integration.md

# CREATE SECURITY INTEGRATION

Creates a new security integration in the account or replaces an existing integration. An integration is a Snowflake object that provides
an interface between Snowflake and a third-party service.

See also:
:   [ALTER SECURITY INTEGRATION](alter-security-integration.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SECURITY INTEGRATION [ IF NOT EXISTS ]
  <name>
  TYPE = { API_AUTHENTICATION | EXTERNAL_OAUTH | OAUTH | SAML2 | SCIM }
  ...
```

The syntax varies considerably among security environments (i.e. types of security integrations). For specific syntax, usage notes, and
examples, see:

* [CREATE SECURITY INTEGRATION (AWS IAM Authentication)](create-security-integration-aws-iam.md)
* [CREATE SECURITY INTEGRATION (External API Authentication)](create-security-integration-api-auth.md)
* [CREATE SECURITY INTEGRATION (External OAuth)](create-security-integration-oauth-external.md)
* [CREATE SECURITY INTEGRATION (Snowflake OAuth)](create-security-integration-oauth-snowflake.md)
* [CREATE SECURITY INTEGRATION (SAML2)](create-security-integration-saml2.md)
* [CREATE SECURITY INTEGRATION (SCIM)](create-security-integration-scim.md)
