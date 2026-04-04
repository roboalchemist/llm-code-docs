# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/deleteunitycatalogresource.md

# DeleteUnityCatalogResource 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

Delete a Unity Catalog file or directory.

## Tags

databricks, openflow, unity catalog

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Databricks Client | Databricks Client Service. |
| Missing Resource Policy | What to action to take if the resource is not found. |
| Unity Catalog Resource Path | Unity Catalog resource path e.g. /Volumes/catalog/schema/volume_name/path |

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
