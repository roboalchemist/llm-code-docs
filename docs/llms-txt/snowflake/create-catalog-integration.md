# Source: https://docs.snowflake.com/en/sql-reference/sql/create-catalog-integration.md

# CREATE CATALOG INTEGRATION

Creates a new [catalog integration](../../user-guide/tables-iceberg.md) for [Apache Iceberg™ tables](../../user-guide/tables-iceberg.md)
in the account or replaces an existing catalog integration.

The syntax of the command depends on the type of external Iceberg catalog that you use. The following topics explain the syntax for
creating catalog integrations for different use cases:

* [CREATE CATALOG INTEGRATION (AWS Glue)](create-catalog-integration-glue.md)
* [CREATE CATALOG INTEGRATION (Object storage)](create-catalog-integration-object-storage.md)
* [CREATE CATALOG INTEGRATION (Snowflake Open Catalog)](create-catalog-integration-open-catalog.md)
* [CREATE CATALOG INTEGRATION (Apache Iceberg™ REST)](create-catalog-integration-rest.md)
* [CREATE CATALOG INTEGRATION (SAP® Business Data Cloud)](create-catalog-integration-sap.md)

See also:
:   [ALTER CATALOG INTEGRATION](alter-catalog-integration.md) , [DROP CATALOG INTEGRATION](drop-catalog-integration.md) , [SHOW CATALOG INTEGRATIONS](show-catalog-integrations.md), [DESCRIBE CATALOG INTEGRATION](desc-catalog-integration.md)
