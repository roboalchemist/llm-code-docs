Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MarkdownTextChunk

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MarkdownTextChunk

# Interface: MarkdownTextChunk

Defined in: packages/types/dist/chunk.d.ts:13

Used for streaming text content with markdown formatting support. [https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming)

## Extends {#extends}

* [`Chunk`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk)

## Properties {#properties}

### text {#text}

```text
text: string;
```text

Defined in: packages/types/dist/chunk.d.ts:15

* * *

### type {#type}

```text
type: "markdown_text";
```text

Defined in: packages/types/dist/chunk.d.ts:14

#### Overrides {#overrides}

[`Chunk`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Chunk#type)
