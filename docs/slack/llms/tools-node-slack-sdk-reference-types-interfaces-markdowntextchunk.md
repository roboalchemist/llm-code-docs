Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MarkdownTextChunk

[@slack/types](/tools/node-slack-sdk/reference/types/) / MarkdownTextChunk

# Interface: MarkdownTextChunk

Defined in: [chunk.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L14)

Used for streaming text content with markdown formatting support. [https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming)

## Extends {#extends}

* [`Chunk`](/tools/node-slack-sdk/reference/types/interfaces/Chunk)

## Properties {#properties}

### text {#text}

```
text: string;
```

Defined in: [chunk.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L16)

* * *

### type {#type}

```
type: "markdown_text";
```

Defined in: [chunk.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/chunk.ts#L15)

#### Overrides {#overrides}

[`Chunk`](/tools/node-slack-sdk/reference/types/interfaces/Chunk).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Chunk#type)
