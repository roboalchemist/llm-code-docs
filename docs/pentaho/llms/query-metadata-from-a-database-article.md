# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/query-metadata-from-a-database-article.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/query-metadata-from-a-database-article.md

# Query metadata from a database

You can use the **Query metadata from a database** step to retrieve metadata from six different JDBC metadata discovery types. This is most useful with metadata injection.

| JDBC Metadata Discovery Types | Description                                                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Catalog                       | Gets a list of catalogs from the database servers. For databases that do not support catalogs, this step type will output no rows. |
| Schemas                       | Gets a list of schemas from the database servers. For databases that do not support schemas, this step type will output no rows.   |
| Tables                        | Gets a list of tables from the database.                                                                                           |
| Columns                       | Gets a list of columns from the database.                                                                                          |
| Primary keys                  | Gets a list of primary keys from the database.                                                                                     |
| Foreign keys                  | Gets a list of foreign keys from the database.                                                                                     |

**Note:** This step makes use of the standard JDBC API to collect metadata. Some database JDBC drivers do not fully implement the JDBC API. For databases that do not fully implement the JDBC API, it is possible that these steps may return unexpected results including no data or partial results. If this occurs, include a **%** in additional fields and/or upgrade the installed JDBC driver. If upgrading the driver does not resolve the issue, you may have to contact your database vendor.
