# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/scriptedtransformrecord.md

# ScriptedTransformRecord 2025.10.9.21

## Bundle

org.apache.nifi | nifi-scripting-nar

## Description

Provides the ability to evaluate a simple script against each record in an incoming FlowFile. The script may transform the record in some way, filter the record, or fork additional records. See Processor’s Additional Details for more information.

## Tags

filter, groovy, modify, record, script, transform, update

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
| failure | Any FlowFile that cannot be transformed will be routed to this Relationship |
| success | Each FlowFile that were successfully transformed will be routed to this Relationship |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | Sets the mime.type attribute to the MIME Type specified by the Record Writer |
| record.count | The number of records in the FlowFile |
| record.error.message | This attribute provides on failure the error message encountered by the Reader or Writer. |

## See also

* [org.apache.nifi.processors.jolt.JoltTransformRecord](jolttransformrecord.md)
* [org.apache.nifi.processors.script.ExecuteScript](executescript.md)
* [org.apache.nifi.processors.standard.LookupRecord](lookuprecord.md)
* [org.apache.nifi.processors.standard.QueryRecord](queryrecord.md)
* [org.apache.nifi.processors.standard.UpdateRecord](updaterecord.md)
