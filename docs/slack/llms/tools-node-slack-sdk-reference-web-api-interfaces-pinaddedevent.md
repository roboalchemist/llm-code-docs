Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PinAddedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PinAddedEvent

# Interface: PinAddedEvent

Defined in: packages/types/dist/events/pin.d.ts:30

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:33

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:42

* * *

### item {#item}

```text
item: PinnedItem;
```text

Defined in: packages/types/dist/events/pin.d.ts:34

* * *

### item_user {#item_user}

```text
item_user: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:35

* * *

### pin_count {#pin_count}

```text
pin_count: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:36

* * *

### pinned_info {#pinned_info}

```text
pinned_info: object;
```text

Defined in: packages/types/dist/events/pin.d.ts:37

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
type: "pin_added";
```text

Defined in: packages/types/dist/events/pin.d.ts:31

* * *

### user {#user}

```text
user: string;
```text

Defined in: packages/types/dist/events/pin.d.ts:32
