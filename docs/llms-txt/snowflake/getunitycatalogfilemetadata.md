# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getunitycatalogfilemetadata.md

# GetUnityCatalogFileMetadata 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

Checks for Unity Catalog file metadata.

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
| not.found | The original FlowFile is transferred to this relationship if no Unity Catalog can be found at the specified path |
| success | Databricks success relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | The content type of the checked file. |
| uc.size | The size of the Unity Catalog file. |
| uc.lastModifiedTime | The last modified time of the Unity Catalog file in milliseconds since epoch in UTC time. |
| error.code | The error code for the SQL statement if an error occurred. |
| error.message | The error message for the SQL statement if an error occurred. |
