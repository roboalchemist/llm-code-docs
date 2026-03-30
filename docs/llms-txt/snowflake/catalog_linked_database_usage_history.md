# Source: https://docs.snowflake.com/en/sql-reference/account-usage/catalog_linked_database_usage_history.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md)

# CATALOG_LINKED_DATABASE_USAGE_HISTORY view

Use this Account Usage view to view the credit usage for your
[catalog-linked databases](../../user-guide/tables-iceberg-catalog-linked-database.md)
within the last 12 months.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the catalog-linked database operation took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the catalog-linked database operation took place. |
| DATABASE_ID | NUMBER | Internal identifier for the catalog-linked database that consumed credits. |
| DATABASE_NAME | VARCHAR | Name of the catalog-linked database that consumed credits. |
| CREDITS_USED_COMPUTE | NUMBER(38,9) | Number of credits used by the catalog-linked database for table creation operations between the START_TIME and END_TIME. The cost for this usage is described in Table 5 of the [Snowflake service consumption table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) on the Snowflake website. See the Snowflake-managed compute column for the Automated Refresh and Data Registration row. |
| CREDITS_USED_CLOUD_SERVICES | NUMBER(38,9) | Number of credits used by the catalog-linked database for automatic table discovery, schema creation or deletion, and table deletion between the START_TIME and END_TIME. Usage for cloud services is charged only if the daily consumption of cloud services exceeds 10% of the daily usage of virtual warehouses. For more information, see [Understanding billing for cloud services usage](../../user-guide/cost-understanding-compute.md). |
| CREDITS_USED | NUMBER(38,9) | Number of credits billed for this catalog-linked database between the START_TIME and END_TIME. |
|  |  |  |
