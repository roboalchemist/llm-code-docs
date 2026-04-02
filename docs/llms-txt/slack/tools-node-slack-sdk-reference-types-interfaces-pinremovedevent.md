Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/PinRemovedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / PinRemovedEvent

# Interface: PinRemovedEvent

Defined in: [events/pin.ts:46](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L46)

## Properties {#properties}

### channel_id {#channel_id}

```
channel_id: string;
```

Defined in: [events/pin.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L49)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/pin.ts:59](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L59)

* * *

### has_pins {#has_pins}

```
has_pins: boolean;
```

Defined in: [events/pin.ts:58](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L58)

* * *

### item {#item}

```
item: PinnedItem;
```

Defined in: [events/pin.ts:50](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L50)

* * *

### item_user {#item_user}

```
item_user: string;
```

Defined in: [events/pin.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L51)

* * *

### pin_count {#pin_count}

```
pin_count: string;
```

Defined in: [events/pin.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L52)

* * *

### pinned_info {#pinned_info}

```
pinned_info: object;
```

Defined in: [events/pin.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L53)

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
type: "pin_removed";
```

Defined in: [events/pin.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L47)

* * *

### user {#user}

```
user: string;
```

Defined in: [events/pin.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/pin.ts#L48)
