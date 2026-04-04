Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChatStartStreamArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatStartStreamArguments

# Interface: ChatStartStreamArguments

Defined in: [packages/web-api/src/types/request/chat.ts:242](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L242)

## Extends {#extends}

* `TokenOverridable`.`Channel`.`Partial`<`MarkdownText`\>.`ThreadTS`

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
Channel.channel
```

* * *

### chunks? {#chunks}

```text
optional chunks: AnyChunk[];
```

Defined in: [packages/web-api/src/types/request/chat.ts:247](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L247)

#### Description {#description-1}

An array of [chunk objects](https://docs.slack.dev/messaging/sending-and-scheduling-messages#text-streaming) to start the stream with. Either `markdown_text` or `chunks` is required.

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

### recipient_team_id? {#recipient_team_id}

```text
optional recipient_team_id: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:252](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L252)

#### Description {#description-3}

The ID of the team that is associated with `recipient_user_id`. This is required when starting a streaming conversation outside of a DM.

* * *

### recipient_user_id? {#recipient_user_id}

```text
optional recipient_user_id: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:257](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L257)

#### Description {#description-4}

The ID of the user to receive the streaming conversation messages. This is required when starting a streaming conversation outside of a DM.

* * *

### task_display_mode? {#task_display_mode}

```text
optional task_display_mode: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:262](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L262)

#### Description {#description-5}

Specifies how tasks are displayed in the message. A "timeline" displays individual tasks with text and "plan" displays all tasks together.

* * *

### thread_ts {#thread_ts}

```text
thread_ts: string;
```

Defined in: [packages/web-api/src/types/request/chat.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L92)

#### Description {#description-6}

Provide another message's `ts` value to post this message in a thread. Avoid using a reply's `ts` value; use its parent's value instead.

#### Inherited from {#inherited-from-2}

```text
ThreadTS.thread_ts
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-7}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```text
TokenOverridable.token
```
