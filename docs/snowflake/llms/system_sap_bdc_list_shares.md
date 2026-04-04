# Source: https://docs.snowflake.com/en/sql-reference/functions/system_sap_bdc_list_shares.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$SAP_BDC_LIST_SHARES

Lists Data Products shared by SAP® Business Data Cloud with the enrolled catalog integration.

See also:
:   [CREATE CATALOG INTEGRATION (SAP® Business Data Cloud)](../sql/create-catalog-integration-sap.md)

## Syntax

```sqlsyntax
SYSTEM$SAP_BDC_LIST_SHARES( '<catalog_integration_name>' )
```

## Arguments

`catalog_integration_name`
:   Identifier for the catalog integration for [Iceberg REST](../sql/create-catalog-integration-rest.md) or
    [Snowflake Open Catalog](../../user-guide/tables-iceberg-configure-catalog-integration-open-catalog.md).

## Returns

Returns a JSON-formatted array of strings that lists the Data Products shared by SAP® Business Data Cloud with the enrolled catalog integration.

The JSON-formatted string has the following structure:

```json
[
  "usid:[guid]:ns:[namespace]:r:[dataproduct1]:v:[version]",
  "usid:[guid]:ns:[namespace]:r:[dataproduct2]:v:[version]",
]
```

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Integration (catalog) |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

List the Data Products that currently shared from SAP® BDC to Snowflake with an enrolled catalog integration. Note that when new Data Products are shared, they are automatically available in the return value. When previously shared Data Products are unshared, they are automatically removed from the return value.

```sqlexample
SELECT SYSTEM$LIST_ICEBERG_TABLES_FROM_CATALOG('myCatalogIntegration');
SELECT SYSTEM$SAP_BDC_LIST_SHARES('my-sap-bdc-catalog-int');
```

Which should produce results similar to:

```output
["usid:0c7785a5-951f-4f3c-9f9f-9df3a5524d84:ns:sap.s4com:r:cashflow:v:1",
 "usid:0c7785a5-951f-4f3c-9f9f-9df3a5524d84:ns:sap.s4com:r:generalledgeraccount:v:1",
 "usid:0c7785a5-951f-4f3c-9f9f-9df3a5524d84:ns:sap.s4com:r:salesorder:v:1",
 "usid:0c7785a5-951f-4f3c-9f9f-9df3a5524d84:ns:sap.s4com:r:profitcenter:v:1"]
```

Where `cashflow`, `generalledgeraccount`, `salesorder`, and `profitcenter`
are the Data Products shared from SAP® BDC to Snowflake with the enrolled catalog integration `my-sap-bdc-catalog-int`.
