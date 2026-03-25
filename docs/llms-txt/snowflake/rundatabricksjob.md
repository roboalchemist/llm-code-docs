# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/rundatabricksjob.md

# RunDatabricksJob 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-databricks-processors-nar

## Description

Triggers a pre-defined Databricks job to run with custom parameters. Job parameters can be set using dynamic properties

## Tags

databricks, jobs, openflow

## Input Requirement

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Databricks Client | Databricks Client Service. |
| Job ID | Databricks Job ID |
| Job Name | Databricks Job Name |
| Wait for Job Completion | Wait for the Databricks job to complete before transferring the FlowFile to success |

## Relationships

| Name | Description |
| --- | --- |
| failure | Databricks failure relationship |
| success | Databricks success relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| job.run.id | The run id assigned to the invoked job |
| job.result.state | The result state for the invoked job |
| error.code | The error code for the SQL statement if an error occurred. |
| error.message | The error message for the SQL statement if an error occurred. |
