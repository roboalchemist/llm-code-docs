Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatStopStreamArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatStopStreamArguments

# Type Alias: ChatStopStreamArguments

```typescript
type ChatStopStreamArguments = TokenOverridable & ChannelAndTS & Partial<MarkdownText> & Partial<Metadata> & object;
```

Defined in: [packages/web-api/src/types/request/chat.ts:265](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L265)

## Type Declaration {#type-declaration}

### blocks? {#blocks}

```typescript
optional blocks: (KnownBlock | Block)[];
```

Block formatted elements will be appended to the end of the message.

### chunks? {#chunks}

```typescript
optional chunks: AnyChunk[];
```

#### Description {#description}

An array of [chunk objects](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming) to finish the stream with.
