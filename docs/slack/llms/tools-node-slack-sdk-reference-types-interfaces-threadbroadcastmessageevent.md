Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ThreadBroadcastMessageEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / ThreadBroadcastMessageEvent

# Interface: ThreadBroadcastMessageEvent

Defined in: [events/message.ts:273](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L273)

## Properties {#properties}

### attachments? {#attachments}

```
optional attachments: MessageAttachment[];
```

Defined in: [events/message.ts:278](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L278)

* * *

### blocks? {#blocks}

```
optional blocks: (Block | KnownBlock)[];
```

Defined in: [events/message.ts:279](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L279)

* * *

### channel {#channel}

```
channel: string;
```

Defined in: [events/message.ts:291](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L291)

* * *

### channel_type {#channel_type}

```
channel_type: ChannelTypes;
```

Defined in: [events/message.ts:292](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L292)

* * *

### client_msg_id {#client_msg_id}

```
client_msg_id: string;
```

Defined in: [events/message.ts:290](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L290)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/message.ts:276](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L276)

* * *

### root {#root}

```
root:   | GenericMessageEvent  | BotMessageEvent & object;
```

Defined in: [events/message.ts:283](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L283)

#### Type Declaration {#type-declaration}

##### latest_reply {#latest_reply}

```
latest_reply: string;
```

##### reply_count {#reply_count}

```
reply_count: number;
```

##### reply_users {#reply_users}

```
reply_users: string[];
```

##### reply_users_count {#reply_users_count}

```
reply_users_count: number;
```

##### thread_ts {#thread_ts}

```
thread_ts: string;
```

* * *

### subtype {#subtype}

```
subtype: "thread_broadcast";
```

Defined in: [events/message.ts:275](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L275)

* * *

### text {#text}

```
text: string;
```

Defined in: [events/message.ts:277](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L277)

* * *

### thread_ts? {#thread_ts-1}

```
optional thread_ts: string;
```

Defined in: [events/message.ts:282](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L282)

* * *

### ts {#ts}

```
ts: string;
```

Defined in: [events/message.ts:281](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L281)

* * *

### type {#type}

```
type: "message";
```

Defined in: [events/message.ts:274](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L274)

* * *

### user {#user}

```
user: string;
```

Defined in: [events/message.ts:280](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L280)
