Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/TaskUpdateChunk

[@slack/types](/tools/node-slack-sdk/reference/types/) / TaskUpdateChunk

# Interface: TaskUpdateChunk

Defined in: [chunk.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L32)

Used for displaying task progress in a timeline-style UI. [https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming)

## Extends {#extends}

* [`Chunk`](/tools/node-slack-sdk/reference/types/interfaces/Chunk)

## Properties {#properties}

### details? {#details}

```
optional details: string;
```

Defined in: [chunk.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L37)

* * *

### id {#id}

```
id: string;
```

Defined in: [chunk.ts:34](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L34)

* * *

### output? {#output}

```
optional output: string;
```

Defined in: [chunk.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L38)

* * *

### sources? {#sources}

```
optional sources: URLSourceElement[];
```

Defined in: [chunk.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L39)

* * *

### status {#status}

```
status: "pending" | "in_progress" | "complete" | "error";
```

Defined in: [chunk.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L36)

* * *

### title {#title}

```
title: string;
```

Defined in: [chunk.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L35)

* * *

### type {#type}

```
type: "task_update";
```

Defined in: [chunk.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L33)

#### Overrides {#overrides}

[`Chunk`](/tools/node-slack-sdk/reference/types/interfaces/Chunk).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Chunk#type)
