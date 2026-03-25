# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getqueryjobresult.md

# GetQueryJobResult 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-salesforce-processors-nar

## Description

Gets the results of a Query Job in Salesforce using the Bulk API 2.0. The output is CSV and GZIP compression is used.

## Tags

bulk, job, preview, query, salesforce

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
| comms.failure | A FlowFile is routed to this relationship if the Query Job result could not be retrieved but the operation might be retried |
| failure | A FlowFile is routed to this relationship if the Query Job Results could not be retrieved |
| success | If Query Job Results have been successfully retrieved, the FlowFile is routed to this relationship |

## See also

* [com.snowflake.openflow.runtime.processors.salesforce.AbortQueryJob](abortqueryjob.md)
* [com.snowflake.openflow.runtime.processors.salesforce.DeleteQueryJob](deletequeryjob.md)
* [com.snowflake.openflow.runtime.processors.salesforce.GetQueryJobStatus](getqueryjobstatus.md)
* [com.snowflake.openflow.runtime.processors.salesforce.SubmitQueryJob](submitqueryjob.md)
