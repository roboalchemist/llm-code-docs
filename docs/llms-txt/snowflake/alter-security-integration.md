# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-security-integration.md

# ALTER SECURITY INTEGRATION

Modifies the properties for an existing security integration.

See also:
:   [CREATE SECURITY INTEGRATION](create-security-integration.md) , [DROP INTEGRATION](drop-integration.md) , [SHOW INTEGRATIONS](show-integrations.md) , [DESCRIBE INTEGRATION](desc-integration.md)

## Syntax

```sqlsyntax
ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name> SET <parameters>

ALTER [ SECURITY ] INTEGRATION [ IF EXISTS ] <name>  UNSET <parameter>

ALTER [ SECURITY ] INTEGRATION <name> SET TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' ... ]

ALTER [ SECURITY ] INTEGRATION <name> UNSET TAG <tag_name> [ , <tag_name> ... ]
```

The syntax varies considerably among security environments (i.e. types of security integrations). For specific syntax, usage notes, and
examples, see:

* [ALTER SECURITY INTEGRATION (AWS IAM Authentication)](alter-security-integration-aws-iam.md)
* [ALTER SECURITY INTEGRATION (External API Authentication)](alter-security-integration-api-auth.md)
* [ALTER SECURITY INTEGRATION (External OAuth)](alter-security-integration-oauth-external.md)
* [ALTER SECURITY INTEGRATION (Snowflake OAuth)](alter-security-integration-oauth-snowflake.md)
* [ALTER SECURITY INTEGRATION (SAML2)](alter-security-integration-saml2.md)
* [ALTER SECURITY INTEGRATION (SCIM)](alter-security-integration-scim.md)
