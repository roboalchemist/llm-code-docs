# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/listsfdcobjects.md

# ListSFDCObjects 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-salesforce-processors-nar

## Description

List the available objects in the organization that are available to the identified user.

## Tags

list, objects, preview, salesforce, sfdc

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Salesforce Client | Salesforce Client to interact with the APIs |

## Relationships

| Name | Description |
| --- | --- |
| success | FlowFile containing the list of available objects will be routed to this relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| nbObjects | The number of objects listed in the organization that are available to the identified user. |

## See also

* [com.snowflake.openflow.runtime.processors.salesforce.DeleteQueryJob](deletequeryjob.md)
* [com.snowflake.openflow.runtime.processors.salesforce.DescribeSFDCObject](describesfdcobject.md)
* [com.snowflake.openflow.runtime.processors.salesforce.GetQueryJobResult](getqueryjobresult.md)
* [com.snowflake.openflow.runtime.processors.salesforce.SubmitQueryJob](submitqueryjob.md)
