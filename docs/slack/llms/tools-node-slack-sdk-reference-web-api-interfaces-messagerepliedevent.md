Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MessageRepliedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MessageRepliedEvent

# Interface: MessageRepliedEvent

Defined in: packages/types/dist/events/message.d.ts:211

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```text

Defined in: packages/types/dist/events/message.d.ts:216

* * *

### channel_type {#channel_type}

```text
channel_type: ChannelTypes;
```text

Defined in: packages/types/dist/events/message.d.ts:217

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:214

* * *

### hidden {#hidden}

```text
hidden: true;
```text

Defined in: packages/types/dist/events/message.d.ts:215

* * *

### message {#message}

```text
message: AllMessageEvents & object;
```text

Defined in: packages/types/dist/events/message.d.ts:219

#### Type Declaration {#type-declaration}

##### replies {#replies}

```text
replies: AllMessageEvents[];
```text

##### reply_count {#reply_count}

```text
reply_count: number;
```text

##### thread_ts {#thread_ts}

```text
thread_ts: string;
```text

* * *

### subtype {#subtype}

```text
subtype: "message_replied";
```text

Defined in: packages/types/dist/events/message.d.ts:213

* * *

### ts {#ts}

```text
ts: string;
```text

Defined in: packages/types/dist/events/message.d.ts:218

* * *

### type {#type}

```text
type: "message";
```text

Defined in: packages/types/dist/events/message.d.ts:212
