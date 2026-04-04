Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MessageRepliedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / MessageRepliedEvent

# Interface: MessageRepliedEvent

Defined in: [events/message.ts:255](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L255)

## Properties {#properties}

### channel {#channel}

```
channel: string;
```

Defined in: [events/message.ts:260](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L260)

* * *

### channel_type {#channel_type}

```
channel_type: ChannelTypes;
```

Defined in: [events/message.ts:261](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L261)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/message.ts:258](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L258)

* * *

### hidden {#hidden}

```
hidden: true;
```

Defined in: [events/message.ts:259](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L259)

* * *

### message {#message}

```
message: AllMessageEvents & object;
```

Defined in: [events/message.ts:263](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L263)

#### Type Declaration {#type-declaration}

##### replies {#replies}

```
replies: AllMessageEvents[];
```

##### reply_count {#reply_count}

```
reply_count: number;
```

##### thread_ts {#thread_ts}

```
thread_ts: string;
```

* * *

### subtype {#subtype}

```
subtype: "message_replied";
```

Defined in: [events/message.ts:257](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L257)

* * *

### ts {#ts}

```
ts: string;
```

Defined in: [events/message.ts:262](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L262)

* * *

### type {#type}

```
type: "message";
```

Defined in: [events/message.ts:256](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L256)
