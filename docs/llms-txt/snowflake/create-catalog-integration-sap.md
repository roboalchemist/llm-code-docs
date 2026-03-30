# Source: https://docs.snowflake.com/en/sql-reference/sql/create-catalog-integration-sap.md

# CREATE CATALOG INTEGRATION (SAP® Business Data Cloud)

Creates a new catalog integration in the account or replaces an existing catalog integration for
SAP® Business Data Cloud to interact with SAP® Data Products managed in the SAP® Business Data Cloud object store.

See also:
:   [ALTER CATALOG INTEGRATION](alter-catalog-integration.md) , [DROP CATALOG INTEGRATION](drop-catalog-integration.md) , [SHOW CATALOG INTEGRATIONS](show-catalog-integrations.md), [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] CATALOG INTEGRATION [ IF NOT EXISTS ] <name>
  CATALOG_SOURCE = SAP_BDC
  TABLE_FORMAT = DELTA
  REST_CONFIG = (
    restConfigParams
  )
  ENABLED = { TRUE | FALSE }
  [ REFRESH_INTERVAL_SECONDS = <value> ]
  [ COMMENT = '<string_literal>' ]
```

Where:

```sqlsyntax
restConfigParams ::=

SAP_BDC_INVITATION_LINK = '<Invitation Link from SAP BDC>'
[ ACCESS_DELEGATION_MODE = { VENDED_CREDENTIALS } ]
```

## Parameters

`name`
:   String that specifies the identifier (name) for the catalog integration; must be unique in your account.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`CATALOG_SOURCE = SAP_BDC`
:   Specifies that the catalog source is SAP® Business Data Cloud.

`TABLE_FORMAT = DELTA`
:   Specifies DELTA as the table format supplied by the catalog.

`ENABLED = { TRUE | FALSE }`
:   Specifies whether the catalog integration is available to use for Iceberg tables.

    > * `TRUE` allows users to create new Iceberg tables that reference this integration.
    > * `FALSE` prevents users from creating new Iceberg tables that reference this integration.

    The value is case-insensitive.

    The default is `TRUE`.

`REFRESH_INTERVAL_SECONDS = <value>`
:   Specifies the number of seconds that Snowflake waits between attempts to poll SAP®
    Business Data Cloud catalog for metadata updates for automated refresh.

    Values: 30 to 86400, inclusive

    Default: 30 seconds

`COMMENT = 'string_literal'`
:   String (literal) that specifies a comment for the integration.

    Default: No value

### REST configuration parameters (restConfigParams)

`ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS`
:   Specifies the access delegation mode to use for accessing table files from SAP® Business Data Cloud.
    The only option supported is VENDED_CREDENTIALS.

`SAP_BDC_INVITATION_LINK = VENDED_CREDENTIALS`
:   Specifies the Invitation Link obtained from [SAP 4 Me](https://me.sap.com/) as documented in
    [Provisioning SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/administering-sap-business-data-cloud/provision-sap-business-data-cloud-connector-for-supported-external-systems)

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE INTEGRATION | Account | Only the ACCOUNTADMIN role has this privilege by default. The privilege can be granted to additional roles as needed. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following example creates a catalog integration and enrolls it with SAP® Business Data Cloud.

```sqlexample
CREATE OR REPLACE CATALOG INTEGRATION MY_SAP_BDC_CATALOG_INT
  CATALOG_SOURCE = SAP_BDC
  TABLE_FORMAT = DELTA
  REST_CONFIG = (
    SAP_BDC_INVITATION_LINK = '<Invitation URL from SAP BDC>'
    ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS
  )
  ENABLED = TRUE
  COMMENT = 'My SAP BDC catalog integration'
  ;
```
