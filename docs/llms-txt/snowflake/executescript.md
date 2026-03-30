# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/executescript.md

# ExecuteScript 2025.10.9.21

## Bundle

org.apache.nifi | nifi-scripting-nar

## Description

Experimental - Executes a script given the flow file and a process session. The script is responsible for handling the incoming flow file (transfer to SUCCESS or remove, e.g.) as well as any flow files created by the script. If the handling is incomplete or incorrect, the session will be rolled back. Experimental: Impact of sustained usage not yet verified.

## Tags

clojure, execute, groovy, script

## Input Requirement

ALLOWED

## Supports Sensitive Dynamic Properties

true

## Properties

| Property | Description |
| --- | --- |
| Module Directory | Comma-separated list of paths to files and/or directories which contain modules required by the script. |
| Script Body | Body of script to execute. Only one of Script File or Script Body may be used |
| Script Engine | Language Engine for executing scripts |
| Script File | Path to script file to execute. Only one of Script File or Script Body may be used |

## State management

| Scopes | Description |
| --- | --- |
| LOCAL | Scripts can store and retrieve state using the State Management APIs. Consult the State Manager section of the Developer’s Guide for more details. |
| CLUSTER | Scripts can store and retrieve state using the State Management APIs. Consult the State Manager section of the Developer’s Guide for more details. |

## Restrictions

| Required Permission | Explanation |
| --- | --- |
| execute code | Provides operator the ability to execute arbitrary code assuming all permissions that NiFi has. |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles that failed to be processed |
| success | FlowFiles that were successfully processed |

## See also

* [org.apache.nifi.processors.script.InvokeScriptedProcessor](invokescriptedprocessor.md)
