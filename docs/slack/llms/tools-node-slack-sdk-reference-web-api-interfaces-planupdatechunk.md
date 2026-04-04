Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PlanUpdateChunk

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PlanUpdateChunk

# Interface: PlanUpdateChunk

Defined in: packages/types/dist/chunk.d.ts:21

Used for displaying an updated title of a plan. [https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming)

## Extends {#extends}

* [`Chunk`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk)

## Properties {#properties}

### title {#title}

```text
title: string;
```text

Defined in: packages/types/dist/chunk.d.ts:23

* * *

### type {#type}

```text
type: "plan_update";
```text

Defined in: packages/types/dist/chunk.d.ts:22

#### Overrides {#overrides}

[`Chunk`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk#type)
