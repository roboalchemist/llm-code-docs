# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getunitycatalogfile.md

# GetUnityCatalogFile 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

Read a Unity Catalog file up to 5 GiB.

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
