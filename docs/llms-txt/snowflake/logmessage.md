# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/logmessage.md

# LogMessage 2025.10.9.21

## Bundle

org.apache.nifi | nifi-standard-nar

## Description

Emits a log message at the specified log level

## Tags

attributes, logging

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| log-level | The Log Level to use when logging the message: [trace, debug, info, warn, error] |
| log-message | The log message to emit |
| log-prefix | Log prefix appended to the log lines. It helps to distinguish the output of multiple LogMessage processors. |

## Relationships

| Name | Description |
| --- | --- |
| success | All FlowFiles are routed to this relationship |
