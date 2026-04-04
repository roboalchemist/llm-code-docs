Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChatAppendStreamArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatAppendStreamArguments

# Interface: ChatAppendStreamArguments

Defined in: [packages/web-api/src/types/request/chat.ts:172](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L172)

## Extends {#extends}

* `TokenOverridable`.`ChannelAndTS`.`Partial`<`MarkdownText`\>

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L22)

#### Description {#description}

Channel ID for the message.

#### Inherited from {#inherited-from}

```text
ChannelAndTS.channel
```

* * *

### chunks? {#chunks}

```text
optional chunks: AnyChunk[];
```

Defined in: [packages/web-api/src/types/request/chat.ts:177](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L177)

#### Description {#description-1}

An array of [chunk objects](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming) to append to the stream. Either `markdown_text` or `chunks` is required.

* * *

### markdown_text? {#markdown_text}

```text
optional markdown_text: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L63)

#### Description {#description-2}

Accepts message text formatted in markdown. This argument should not be used in conjunction with `blocks` or `text`. Limit this field to 12,000 characters.

#### Example {#example}

```text
**This is bold text**
```

#### Inherited from {#inherited-from-1}

```text
Partial.markdown_text
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```

* * *

### ts {#ts}

```text
ts: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L26)

#### Description {#description-4}

Timestamp of the message.

#### Inherited from {#inherited-from-3}

```text
ChannelAndTS.ts
```
