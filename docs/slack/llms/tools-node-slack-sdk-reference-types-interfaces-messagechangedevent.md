Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MessageChangedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / MessageChangedEvent

# Interface: MessageChangedEvent

Defined in: [events/message.ts:231](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L231)

## Properties {#properties}

### channel {#channel}

```
channel: string;
```

Defined in: [events/message.ts:236](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L236)

* * *

### channel_type {#channel_type}

```
channel_type: ChannelTypes;
```

Defined in: [events/message.ts:237](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L237)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/message.ts:234](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L234)

* * *

### hidden {#hidden}

```
hidden: true;
```

Defined in: [events/message.ts:235](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L235)

* * *

### message {#message}

```
message: AllMessageEvents;
```

Defined in: [events/message.ts:239](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L239)

* * *

### previous_message {#previous_message}

```
previous_message: AllMessageEvents;
```

Defined in: [events/message.ts:240](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L240)

* * *

### subtype {#subtype}

```
subtype: "message_changed";
```

Defined in: [events/message.ts:233](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L233)

* * *

### ts {#ts}

```
ts: string;
```

Defined in: [events/message.ts:238](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L238)

* * *

### type {#type}

```
type: "message";
```

Defined in: [events/message.ts:232](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/message.ts#L232)
