Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/BotMessageEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / BotMessageEvent

# Interface: BotMessageEvent

Defined in: [events/message.ts:65](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L65)

## Properties {#properties}

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```

Defined in: [events/message.ts:83](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L83)

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```

Defined in: [events/message.ts:84](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L84)

* * *

### bot_id {#bot_id}

```text
bot_id: string;
```

Defined in: [events/message.ts:74](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L74)

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: [events/message.ts:69](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L69)

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```

Defined in: [events/message.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L70)

* * *

### edited? {#edited}

```text
optional edited: object;
```

Defined in: [events/message.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L85)

#### ts {#ts}

```text
ts: string;
```

#### user {#user}

```text
user: string;
```

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: [events/message.ts:68](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L68)

* * *

### icons? {#icons}

```text
optional icons: object;
```

Defined in: [events/message.ts:76](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L76)

#### Index Signature {#index-signature}

```text
[size: string]: string
```

* * *

### streaming_state? {#streaming_state}

```text
optional streaming_state: "in_progress" | "completed" | "errored";
```

Defined in: [events/message.ts:71](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L71)

* * *

### subtype {#subtype}

```text
subtype: "bot_message";
```

Defined in: [events/message.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L67)

* * *

### text {#text}

```text
text: string;
```

Defined in: [events/message.ts:73](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L73)

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```

Defined in: [events/message.ts:89](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L89)

* * *

### ts {#ts-1}

```text
ts: string;
```

Defined in: [events/message.ts:72](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L72)

* * *

### type {#type}

```text
type: "message";
```

Defined in: [events/message.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L66)

* * *

### user? {#user-1}

```text
optional user: string;
```

Defined in: [events/message.ts:82](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L82)

* * *

### username? {#username}

```text
optional username: string;
```

Defined in: [events/message.ts:75](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L75)
