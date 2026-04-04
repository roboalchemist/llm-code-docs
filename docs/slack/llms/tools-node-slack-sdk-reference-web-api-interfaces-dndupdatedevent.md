Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DNDUpdatedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DNDUpdatedEvent

# Interface: DNDUpdatedEvent

Defined in: packages/types/dist/events/dnd.d.ts:1

## Properties {#properties}

### dnd_status {#dnd_status}

```text
dnd_status: object;
```

Defined in: packages/types/dist/events/dnd.d.ts:4

#### dnd_enabled {#dnd_enabled}

```text
dnd_enabled: boolean;
```

#### next_dnd_end_ts {#next_dnd_end_ts}

```text
next_dnd_end_ts: number;
```

#### next_dnd_start_ts {#next_dnd_start_ts}

```text
next_dnd_start_ts: number;
```

#### snooze_enabled {#snooze_enabled}

```text
snooze_enabled: boolean;
```

#### snooze_endtime {#snooze_endtime}

```text
snooze_endtime: number;
```

#### snooze_remaining {#snooze_remaining}

```text
snooze_remaining: number;
```

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: packages/types/dist/events/dnd.d.ts:12

* * *

### type {#type}

```text
type: "dnd_updated";
```

Defined in: packages/types/dist/events/dnd.d.ts:2

* * *

### user {#user}

```text
user: string;
```

Defined in: packages/types/dist/events/dnd.d.ts:3
