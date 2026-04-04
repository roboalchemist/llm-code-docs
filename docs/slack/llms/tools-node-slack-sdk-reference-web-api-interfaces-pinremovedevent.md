Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PinRemovedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PinRemovedEvent

# Interface: PinRemovedEvent

Defined in: packages/types/dist/events/pin.d.ts:44

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:47

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:57

* * *

### has_pins {#has_pins}

```text
has_pins: boolean;
```text

Defined in: packages/types/dist/events/pin.d.ts:56

* * *

### item {#item}

```text
item: PinnedItem;
```text

Defined in: packages/types/dist/events/pin.d.ts:48

* * *

### item_user {#item_user}

```text
item_user: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:49

* * *

### pin_count {#pin_count}

```text
pin_count: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:50

* * *

### pinned_info {#pinned_info}

```text
pinned_info: object;
```text

Defined in: packages/types/dist/events/pin.d.ts:51

#### channel {#channel}

```text
channel: string;
```text

#### pinned_by {#pinned_by}

```text
pinned_by: string;
```text

#### pinned_ts {#pinned_ts}

```text
pinned_ts: number;
```text

* * *

### type {#type}

```text
type: "pin_removed";
```text

Defined in: packages/types/dist/events/pin.d.ts:45

* * *

### user {#user}

```text
user: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:46
