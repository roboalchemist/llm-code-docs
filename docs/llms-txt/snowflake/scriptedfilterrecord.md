# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/scriptedfilterrecord.md

# ScriptedFilterRecord 2025.10.9.21

## Bundle

org.apache.nifi | nifi-scripting-nar

## Description

This processor provides the ability to filter records out from FlowFiles using the user-provided script. Every record will be evaluated by the script which must return with a boolean value. Records with “true” result will be routed to the “matching” relationship in a batch. Other records will be filtered out.

## Tags

filter, groovy, record, script

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Module Directory | Comma-separated list of paths to files and/or directories which contain modules required by the script. |
| Record Reader | The Record Reader to use parsing the incoming FlowFile into Records |
| Record Writer | The Record Writer to use for serializing Records after they have been transformed |
| Script Body | Body of script to execute. Only one of Script File or Script Body may be used |
| Script Engine | The Language to use for the script |
| Script File | Path to script file to execute. Only one of Script File or Script Body may be used |

## Restrictions

| Required Permission | Explanation |
| --- | --- |
| execute code | Provides operator the ability to execute arbitrary code assuming all permissions that NiFi has. |

## Relationships

| Name | Description |
| --- | --- |
| failure | In case of any issue during processing the incoming FlowFile, the incoming FlowFile will be routed to this relationship. |
| original | After successful procession, the incoming FlowFile will be transferred to this relationship. This happens regardless the number of filtered or remaining records. |
| success | Matching records of the original FlowFile will be routed to this relationship. If there are no matching records, no FlowFile will be routed here. |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | Sets the mime.type attribute to the MIME Type specified by the Record Writer |
| record.count | The number of records within the flow file. |
| record.error.message | This attribute provides on failure the error message encountered by the Reader or Writer. |

## See also

* [org.apache.nifi.processors.script.ScriptedPartitionRecord](scriptedpartitionrecord.md)
* [org.apache.nifi.processors.script.ScriptedTransformRecord](scriptedtransformrecord.md)
* [org.apache.nifi.processors.script.ScriptedValidateRecord](scriptedvalidaterecord.md)
