Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/PinAddedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / PinAddedEvent

# Interface: PinAddedEvent

Defined in: [events/pin.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L32)

## Properties {#properties}

### channel_id {#channel_id}

```
channel_id: string;
```

Defined in: [events/pin.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L35)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/pin.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L44)

* * *

### item {#item}

```
item: PinnedItem;
```

Defined in: [events/pin.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L36)

* * *

### item_user {#item_user}

```
item_user: string;
```

Defined in: [events/pin.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L37)

* * *

### pin_count {#pin_count}

```
pin_count: string;
```

Defined in: [events/pin.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L38)

* * *

### pinned_info {#pinned_info}

```
pinned_info: object;
```

Defined in: [events/pin.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L39)

#### channel {#channel}

```
channel: string;
```

#### pinned_by {#pinned_by}

```
pinned_by: string;
```

#### pinned_ts {#pinned_ts}

```
pinned_ts: number;
```

* * *

### type {#type}

```
type: "pin_added";
```

Defined in: [events/pin.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L33)

* * *

### user {#user}

```
user: string;
```

Defined in: [events/pin.ts:34](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L34)
