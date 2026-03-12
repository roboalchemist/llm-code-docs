# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/consumeboxevents.md

# ConsumeBoxEvents 2025.10.9.21

## Bundle

org.apache.nifi | nifi-box-nar

## Description

Consumes all events from Box. This processor can be used to capture events such as uploads, modifications, deletions, etc. The content of the events is sent to the ‘success’ relationship as a JSON array. Events can be dropped in case of NiFi restart or if the queue capacity is exceeded. The last known position of the Box stream is stored in the processor state and is used to resume the stream from the last known position when the processor is restarted.

## Tags

box, storage

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Box Client Service | Controller Service used to obtain a Box API connection. |
| Queue Capacity | The maximum size of the internal queue used to buffer events being transferred from the underlying stream to the processor. Setting this value higher allows more messages to be buffered in memory during surges of incoming messages, but increases the total memory used by the processor during these surges. |

## State management

| Scopes | Description |
| --- | --- |
| CLUSTER | The last known position of the Box stream is stored in the processor state and is used to resume the stream from the last known position when the processor is restarted. |

## Relationships

| Name | Description |
| --- | --- |
| success | Events received successfully will be sent out this relationship. |

## See also

* [org.apache.nifi.processors.box.FetchBoxFile](fetchboxfile.md)
* [org.apache.nifi.processors.box.ListBoxFile](listboxfile.md)
* [org.apache.nifi.processors.box.PutBoxFile](putboxfile.md)
