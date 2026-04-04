Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ThreadBroadcastMessageEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ThreadBroadcastMessageEvent

# Interface: ThreadBroadcastMessageEvent

Defined in: packages/types/dist/events/message.d.ts:225

## Properties {#properties}

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```text

Defined in: packages/types/dist/events/message.d.ts:230

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```text

Defined in: packages/types/dist/events/message.d.ts:231

* * *

### channel {#channel}

```text
channel: string;
```text

Defined in: packages/types/dist/events/message.d.ts:243

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```text

Defined in: packages/types/dist/events/message.d.ts:244

* * *

### client_msg_id {#client_msg_id}

```text
client_msg_id: string;
```text

Defined in: packages/types/dist/events/message.d.ts:242

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:228

* * *

### root {#root}

```text
root:   | GenericMessageEvent  | BotMessageEvent & object;
```text

Defined in: packages/types/dist/events/message.d.ts:235

#### Type Declaration {#type-declaration}

##### latest_reply {#latest_reply}

```text
latest_reply: string;
```text

##### reply_count {#reply_count}

```text
reply_count: number;
```text

##### reply_users {#reply_users}

```text
reply_users: string[];
```text

##### reply_users_count {#reply_users_count}

```text
reply_users_count: number;
```text

##### thread_ts {#thread_ts}

```text
thread_ts: string;
```text

* * *

### subtype {#subtype}

```text
subtype: "thread_broadcast";
```text

Defined in: packages/types/dist/events/message.d.ts:227

* * *

### text {#text}

```text
text: string;
```text

Defined in: packages/types/dist/events/message.d.ts:229

* * *

### thread_ts? {#thread_ts-1}

```text
optional thread_ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:234

* * *

### ts {#ts}

```text
ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:233

* * *

### type {#type}

```text
type: "message";
```text

Defined in: packages/types/dist/events/message.d.ts:226

* * *

### user {#user}

```text
user: string;
```text

Defined in: packages/types/dist/events/message.d.ts:232
