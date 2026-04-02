Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChatStreamerOptions

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatStreamerOptions

# Interface: ChatStreamerOptions

Defined in: [packages/web-api/src/chat-stream.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/chat-stream.ts#L7)

## Properties {#properties}

### buffer_size? {#buffer_size}

```text
optional buffer_size: number;
```

Defined in: [packages/web-api/src/chat-stream.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/chat-stream.ts#L12)

#### Description {#description}

The length of markdown\_text to buffer in-memory before calling a method. Increasing this value decreases the number of method calls made for the same amount of text, which is useful to avoid rate limits.

#### Default {#default}

```text
256
```
