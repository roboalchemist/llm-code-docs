Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/DNDUpdatedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / DNDUpdatedEvent

# Interface: DNDUpdatedEvent

Defined in: [events/dnd.ts:1](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L1)

## Properties {#properties}

### dnd_status {#dnd_status}

```text
dnd_status: object;
```

Defined in: [events/dnd.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L4)

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

Defined in: [events/dnd.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L12)

* * *

### type {#type}

```text
type: "dnd_updated";
```

Defined in: [events/dnd.ts:2](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L2)

* * *

### user {#user}

```text
user: string;
```

Defined in: [events/dnd.ts:3](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L3)
