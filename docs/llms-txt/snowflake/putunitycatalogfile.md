# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/putunitycatalogfile.md

# PutUnityCatalogFile 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

Write FlowFile content with max size of 5 GiB to Unity Catalog.

## Tags

databricks, openflow, unity catalog

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Databricks Client | Databricks Client Service. |
| Unity Catalog File Path | Unity Catalog file path e.g. /Volumes/catalog/schema/volume_name/file.txt |

## Relationships

| Name | Description |
| --- | --- |
| failure | Databricks failure relationship |
| success | Databricks success relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| error.code | The error code for the SQL statement if an error occurred. |
| error.message | The error message for the SQL statement if an error occurred. |
