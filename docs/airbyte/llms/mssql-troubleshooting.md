# Source: https://docs.airbyte.com/integrations/sources/mssql/mssql-troubleshooting.md

![](https://connectors.airbyte.com/files/metadata/airbyte/source-mssql/latest/icon.svg)

# Troubleshooting Microsoft SQL Server (MSSQL) Sources

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Airbyte](/integrations/connector-support-levels.md)

* Connector Version

  [4.3.5](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-mssql)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/source-mssql)(last updated 16 days ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `b5ea17b1-f170-46dc-bc31-cc744ca984c1`

## Connector Limitations[​](#connector-limitations "Direct link to Connector Limitations")

### Adding columns to existing tables with CDC[​](#adding-columns-to-existing-tables-with-cdc "Direct link to Adding columns to existing tables with CDC")

When using SQL Server (MSSQL) in CDC mode, adding new columns to existing tables using `ALTER TABLE <table> ADD <column>` will **not** automatically be captured by the CDC stream. As a result, the column will be excluded from CDC tracking (while it might appear in the Schema section, it will return zero records). To ensure the column is tracked, we recommend disabling and re-enabling CDC on the table. This will create a new capture instance that reflects the updated structure and includes the new column:

1. Disabling CDC on the table:

```
EXEC sys.sp_cdc_disable_table
    @source_schema = N'<schema>',
    @source_name   = N'<table>',
    @capture_instance = N'<capture instance (typically schema_table)>'
```

2. Enabling CDC on the table:

```
EXEC sys.sp_cdc_enable_table
    @source_schema = N'<schema>',
    @source_name   = N'<table>',
    @role_name     = NULL
```

Note: You may want to set a `@role_name` or any other arguments similarly to how they were set when CDC was enabled in the first place.

3. (Optional) Validate that all columns are being captured:

```
EXEC sys.sp_cdc_get_captured_columns 
    @capture_instance = N'<capture instance (typically schema_table)>';
```
