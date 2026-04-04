# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/abortqueryjob.md

# AbortQueryJob 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-salesforce-processors-nar

## Description

Aborts a Query Job in Salesforce using the Bulk API 2.0.

## Tags

abort, bulk, job, preview, query, salesforce

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Job ID | The ID of the job for which the status is checked. |
| Salesforce Client | Salesforce Client to interact with the APIs |

## Relationships

| Name | Description |
| --- | --- |
| comms.failure | A FlowFile is routed to this relationship if the Query Job could not be aborted but the operation might be retried |
| failure | A FlowFile is routed to this relationship if the Query Job could not be aborted |
| success | If the Query Job has been successfully aborted, the FlowFile is routed to this relationship |

## See also

* [com.snowflake.openflow.runtime.processors.salesforce.DeleteQueryJob](deletequeryjob.md)
* [com.snowflake.openflow.runtime.processors.salesforce.GetQueryJobResult](getqueryjobresult.md)
* [com.snowflake.openflow.runtime.processors.salesforce.GetQueryJobStatus](getqueryjobstatus.md)
* [com.snowflake.openflow.runtime.processors.salesforce.SubmitQueryJob](submitqueryjob.md)
