Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DNDUpdatedUserEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DNDUpdatedUserEvent

# Interface: DNDUpdatedUserEvent

Defined in: packages/types/dist/events/dnd.d.ts:14

## Properties {#properties}

### dnd_status {#dnd_status}

```text
dnd_status: object;
```

Defined in: packages/types/dist/events/dnd.d.ts:17

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

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: packages/types/dist/events/dnd.d.ts:22

* * *

### type {#type}

```text
type: "dnd_updated_user";
```

Defined in: packages/types/dist/events/dnd.d.ts:15

* * *

### user {#user}

```text
user: string;
```

Defined in: packages/types/dist/events/dnd.d.ts:16
