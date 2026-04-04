Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/TaskUpdateChunk

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TaskUpdateChunk

# Interface: TaskUpdateChunk

Defined in: packages/types/dist/chunk.d.ts:29

Used for displaying task progress in a timeline-style UI. [https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming)

## Extends {#extends}

* [`Chunk`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk)

## Properties {#properties}

### details? {#details}

```text
optional details: string;
```text

Defined in: packages/types/dist/chunk.d.ts:34

* * *

### id {#id}

```text
id: string;
```text

Defined in: packages/types/dist/chunk.d.ts:31

* * *

### output? {#output}

```text
optional output: string;
```text

Defined in: packages/types/dist/chunk.d.ts:35

* * *

### sources? {#sources}

```text
optional sources: URLSourceElement[];
```text

Defined in: packages/types/dist/chunk.d.ts:36

* * *

### status {#status}

```text
status: "pending" | "in_progress" | "complete" | "error";
```text

Defined in: packages/types/dist/chunk.d.ts:33

* * *

### title {#title}

```text
title: string;
```text

Defined in: packages/types/dist/chunk.d.ts:32

* * *

### type {#type}

```text
type: "task_update";
```text

Defined in: packages/types/dist/chunk.d.ts:30

#### Overrides {#overrides}

[`Chunk`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk#type)
