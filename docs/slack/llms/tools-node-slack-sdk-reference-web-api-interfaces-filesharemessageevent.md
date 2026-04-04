Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FileShareMessageEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FileShareMessageEvent

# Interface: FileShareMessageEvent

Defined in: packages/types/dist/events/message.d.ts:161

## Properties {#properties}

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```

Defined in: packages/types/dist/events/message.d.ts:165

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```

Defined in: packages/types/dist/events/message.d.ts:166

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: packages/types/dist/events/message.d.ts:175

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```

Defined in: packages/types/dist/events/message.d.ts:176

* * *

### display_as_bot? {#display_as_bot}

```text
optional display_as_bot: boolean;
```

Defined in: packages/types/dist/events/message.d.ts:169

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: packages/types/dist/events/message.d.ts:177

* * *

### files? {#files}

```text
optional files: File[];
```

Defined in: packages/types/dist/events/message.d.ts:167

* * *

### parent_user_id? {#parent_user_id}

```text
optional parent_user_id: string;
```

Defined in: packages/types/dist/events/message.d.ts:172

* * *

### subtype {#subtype}

```text
subtype: "file_share";
```

Defined in: packages/types/dist/events/message.d.ts:163

* * *

### text {#text}

```text
text: string;
```

Defined in: packages/types/dist/events/message.d.ts:164

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```

Defined in: packages/types/dist/events/message.d.ts:174

* * *

### ts {#ts}

```text
ts: string;
```

Defined in: packages/types/dist/events/message.d.ts:173

* * *

### type {#type}

```text
type: "message";
```

Defined in: packages/types/dist/events/message.d.ts:162

* * *

### upload? {#upload}

```text
optional upload: boolean;
```

Defined in: packages/types/dist/events/message.d.ts:168

* * *

### user {#user}

```text
user: string;
```

Defined in: packages/types/dist/events/message.d.ts:171

* * *

### x_files? {#x_files}

```text
optional x_files: string[];
```

Defined in: packages/types/dist/events/message.d.ts:170
