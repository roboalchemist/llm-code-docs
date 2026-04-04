# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listunitycatalogdirectory.md

# ListUnityCatalogDirectory 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

List file names in a Unity Catalog directory and output a new FlowFile with the filename.

## Tags

databricks, openflow, unity catalog

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Databricks Client | Databricks Client Service. |
| Include Directories | Include directories in FlowFiles produced. |
| Recursive Directory Listing | Recursively list files in sub directories. |
| Unity Catalog Directory Path | Unity Catalog directory path e.g. /Volumes/catalog/schema/volume_name/directory |

## Relationships

| Name | Description |
| --- | --- |
| failure | Databricks failure relationship |
| original | The original FlowFile is routed to this relationship when processing is successful. |
| success | Databricks success relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| filename | Base filename of the Unity Catalog file or directory. |
| path | Path to parent directory containing the Unity Catalog file or directory. |
| absolute.path | Full path to the Unity Catalog file or directory. |
| uc.resourceType | The type of resource, ‘file’ or ‘directory’ of the Unity Catalog resource. |
| uc.size | The size of the Unity Catalog file. |
| uc.lastModifiedTime | The last modified time of the Unity Catalog file in milliseconds since epoch in UTC time. |
| error.code | The error code for the SQL statement if an error occurred. |
| error.message | The error message for the SQL statement if an error occurred. |
