Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/FileShareMessageEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / FileShareMessageEvent

# Interface: FileShareMessageEvent

Defined in: [events/message.ts:201](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L201)

## Properties {#properties}

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```

Defined in: [events/message.ts:205](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L205)

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```

Defined in: [events/message.ts:206](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L206)

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: [events/message.ts:215](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L215)

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```

Defined in: [events/message.ts:216](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L216)

* * *

### display_as_bot? {#display_as_bot}

```text
optional display_as_bot: boolean;
```

Defined in: [events/message.ts:209](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L209)

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: [events/message.ts:217](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L217)

* * *

### files? {#files}

```text
optional files: File[];
```

Defined in: [events/message.ts:207](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L207)

* * *

### parent_user_id? {#parent_user_id}

```text
optional parent_user_id: string;
```

Defined in: [events/message.ts:212](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L212)

* * *

### subtype {#subtype}

```text
subtype: "file_share";
```

Defined in: [events/message.ts:203](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L203)

* * *

### text {#text}

```text
text: string;
```

Defined in: [events/message.ts:204](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L204)

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```

Defined in: [events/message.ts:214](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L214)

* * *

### ts {#ts}

```text
ts: string;
```

Defined in: [events/message.ts:213](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L213)

* * *

### type {#type}

```text
type: "message";
```

Defined in: [events/message.ts:202](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L202)

* * *

### upload? {#upload}

```text
optional upload: boolean;
```

Defined in: [events/message.ts:208](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L208)

* * *

### user {#user}

```text
user: string;
```

Defined in: [events/message.ts:211](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L211)

* * *

### x_files? {#x_files}

```text
optional x_files: string[];
```

Defined in: [events/message.ts:210](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L210)
