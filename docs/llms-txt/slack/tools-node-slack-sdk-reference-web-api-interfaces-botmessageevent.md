Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/BotMessageEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / BotMessageEvent

# Interface: BotMessageEvent

Defined in: packages/types/dist/events/message.d.ts:38

## Properties {#properties}

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```

Defined in: packages/types/dist/events/message.d.ts:53

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```

Defined in: packages/types/dist/events/message.d.ts:54

* * *

### bot_id {#bot_id}

```text
bot_id: string;
```

Defined in: packages/types/dist/events/message.d.ts:47

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: packages/types/dist/events/message.d.ts:42

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```

Defined in: packages/types/dist/events/message.d.ts:43

* * *

### edited? {#edited}

```text
optional edited: object;
```

Defined in: packages/types/dist/events/message.d.ts:55

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

Defined in: packages/types/dist/events/message.d.ts:41

* * *

### icons? {#icons}

```text
optional icons: object;
```

Defined in: packages/types/dist/events/message.d.ts:49

#### Index Signature {#index-signature}

```text
[size: string]: string
```

* * *

### streaming_state? {#streaming_state}

```text
optional streaming_state: "in_progress" | "completed" | "errored";
```

Defined in: packages/types/dist/events/message.d.ts:44

* * *

### subtype {#subtype}

```text
subtype: "bot_message";
```

Defined in: packages/types/dist/events/message.d.ts:40

* * *

### text {#text}

```text
text: string;
```

Defined in: packages/types/dist/events/message.d.ts:46

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```

Defined in: packages/types/dist/events/message.d.ts:59

* * *

### ts {#ts-1}

```text
ts: string;
```

Defined in: packages/types/dist/events/message.d.ts:45

* * *

### type {#type}

```text
type: "message";
```

Defined in: packages/types/dist/events/message.d.ts:39

* * *

### user? {#user-1}

```text
optional user: string;
```

Defined in: packages/types/dist/events/message.d.ts:52

* * *

### username? {#username}

```text
optional username: string;
```

Defined in: packages/types/dist/events/message.d.ts:48
