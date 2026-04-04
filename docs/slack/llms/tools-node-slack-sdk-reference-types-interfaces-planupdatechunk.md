Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/PlanUpdateChunk

[@slack/types](/tools/node-slack-sdk/reference/types/) / PlanUpdateChunk

# Interface: PlanUpdateChunk

Defined in: [chunk.ts:23](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L23)

Used for displaying an updated title of a plan. [https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming)

## Extends {#extends}

* [`Chunk`](/tools/node-slack-sdk/reference/types/interfaces/Chunk)

## Properties {#properties}

### title {#title}

```
title: string;
```

Defined in: [chunk.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L25)

* * *

### type {#type}

```
type: "plan_update";
```

Defined in: [chunk.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L24)

#### Overrides {#overrides}

[`Chunk`](/tools/node-slack-sdk/reference/types/interfaces/Chunk).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Chunk#type)
