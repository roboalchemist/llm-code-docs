# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getdbfsfile.md

# GetDBFSFile 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

Read a DBFS file.

## Tags

databricks, dbfs, openflow

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| DBFS File Path | DBFS file path e.g. /directory/file.txt |
| Databricks Client | Databricks Client Service. |

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
