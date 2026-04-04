Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/GenericMessageEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / GenericMessageEvent

# Interface: GenericMessageEvent

Defined in: [events/message.ts:29](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L29)

## Properties {#properties}

### assistant_thread? {#assistant_thread}

```
optional assistant_thread: Record<string, unknown>;
```

Defined in: [events/message.ts:62](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L62)

* * *

### attachments? {#attachments}

```
optional attachments: MessageAttachment[];
```

Defined in: [events/message.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L42)

* * *

### blocks? {#blocks}

```
optional blocks: (Block | KnownBlock)[];
```

Defined in: [events/message.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L43)

* * *

### bot_id? {#bot_id}

```
optional bot_id: string;
```

Defined in: [events/message.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L36)

* * *

### bot_profile? {#bot_profile}

```
optional bot_profile: BotProfile;
```

Defined in: [events/message.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L37)

* * *

### channel {#channel}

```
channel: string;
```

Defined in: [events/message.ts:34](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L34)

* * *

### channel_type {#channel_type}

```
channel_type: ChannelTypes;
```

Defined in: [events/message.ts:41](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L41)

* * *

### client_msg_id? {#client_msg_id}

```
optional client_msg_id: string;
```

Defined in: [events/message.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L49)

* * *

### edited? {#edited}

```
optional edited: object;
```

Defined in: [events/message.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L45)

#### ts {#ts}

```
ts: string;
```

#### user {#user}

```
user: string;
```

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/message.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L32)

* * *

### files? {#files}

```
optional files: File[];
```

Defined in: [events/message.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L44)

* * *

### is_starred? {#is_starred}

```
optional is_starred: boolean;
```

Defined in: [events/message.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L53)

* * *

### parent_user_id? {#parent_user_id}

```
optional parent_user_id: string;
```

Defined in: [events/message.ts:50](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L50)

* * *

### pinned_to? {#pinned_to}

```
optional pinned_to: string[];
```

Defined in: [events/message.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L54)

* * *

### reactions? {#reactions}

```
optional reactions: object[];
```

Defined in: [events/message.ts:55](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L55)

#### count {#count}

```
count: number;
```

#### name {#name}

```
name: string;
```

#### users {#users}

```
users: string[];
```

* * *

### subtype {#subtype}

```
subtype: undefined;
```

Defined in: [events/message.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L31)

* * *

### team? {#team}

```
optional team: string;
```

Defined in: [events/message.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L33)

* * *

### text? {#text}

```
optional text: string;
```

Defined in: [events/message.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L38)

* * *

### thread_ts? {#thread_ts}

```
optional thread_ts: string;
```

Defined in: [events/message.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L40)

* * *

### ts {#ts-1}

```
ts: string;
```

Defined in: [events/message.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L39)

* * *

### type {#type}

```
type: "message";
```

Defined in: [events/message.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L30)

* * *

### user {#user-1}

```
user: string;
```

Defined in: [events/message.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L35)
