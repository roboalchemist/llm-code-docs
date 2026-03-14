# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/getfileresource.md

# GetFileResource 2025.10.9.21

## Bundle

org.apache.nifi | nifi-standard-nar

## Description

This processor creates FlowFiles with the content of the configured File Resource. GetFileResource is useful for load testing, configuration, and simulation.

## Tags

file, generate, load, test

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| File Resource | Location of the File Resource (Local File or URL). This file will be used as content of the generated FlowFiles. |
| MIME Type | Specifies the value to set for the [mime.type] attribute. |

## Restrictions

| Required Permission | Explanation |
| --- | --- |
| read filesystem | Provides operator the ability to read from any file that NiFi has access to. |
| reference remote resources | File Resource can reference resources over HTTP/HTTPS |

## Relationships

| Name | Description |
| --- | --- |
| success |  |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | Sets the MIME type of the output if the ‘MIME Type’ property is set |
| Dynamic property key | Value for the corresponding dynamic property, if any is set |
