# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-integration.md

# DESCRIBE INTEGRATION

Describes the properties of an integration.

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE INTEGRATION](create-integration.md) , [DROP INTEGRATION](drop-integration.md) , [ALTER INTEGRATION](alter-integration.md) , [SHOW INTEGRATIONS](show-integrations.md)

API integrations:
:   [ALTER API INTEGRATION](alter-api-integration.md) , [CREATE API INTEGRATION](create-api-integration.md)

Catalog integrations:
:   [ALTER CATALOG INTEGRATION](alter-catalog-integration.md) , [CREATE CATALOG INTEGRATION](create-catalog-integration.md)

External access integrations:
:   [ALTER EXTERNAL ACCESS INTEGRATION](alter-external-access-integration.md) , [CREATE EXTERNAL ACCESS INTEGRATION](create-external-access-integration.md)

Notification integrations:
:   [ALTER NOTIFICATION INTEGRATION](alter-notification-integration.md) , [CREATE NOTIFICATION INTEGRATION](create-notification-integration.md)

Security integrations:
:   [ALTER SECURITY INTEGRATION](alter-security-integration.md) , [CREATE SECURITY INTEGRATION](create-security-integration.md)

Storage integrations:
:   [ALTER STORAGE INTEGRATION](alter-storage-integration.md) , [CREATE STORAGE INTEGRATION](create-storage-integration.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } [ { API | CATALOG | EXTERNAL ACCESS | NOTIFICATION | SECURITY | STORAGE } ] INTEGRATION <name>
```

## Parameters

`{ API | CATALOG | EXTERNAL ACCESS | NOTIFICATION | SECURITY | STORAGE }`
:   Describes an integration of the specified type.

    For more information about some of these types, see the following topics:

    * [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md)
    * [DESCRIBE NOTIFICATION INTEGRATION](desc-notification-integration.md)

`name`
:   Specifies the identifier for the integration to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

* If the integration is an API integration, then the output includes the API_KEY column. The API_KEY displays a masked value if an
  [API key](../external-functions-security.md) was entered. (This does not display either the original unencrypted key or the
  encrypted version of the key.)
* If the security integration has the `TYPE` property set to `OAUTH` (i.e. Snowflake OAuth), Snowflake returns two additional security
  integration properties in the query result that cannot be set with either a CREATE SECURITY INTEGRATION or an ALTER SECURITY INTEGRATION
  command:

  `OAUTH_ALLOWED_AUTHORIZATION_ENDPOINTS`
  :   A list of all supported endpoints for a client application to receive an authorization code from Snowflake.

  `OAUTH_ALLOWED_TOKEN_ENDPOINTS`
  :   A list of all supported endpoints for a client application to exchange an authorization code for an access token or to obtain a refresh
      token.

## Examples

Describe the properties of an integration named `my_int`:

```sqlexample
DESC INTEGRATION my_int;
```
