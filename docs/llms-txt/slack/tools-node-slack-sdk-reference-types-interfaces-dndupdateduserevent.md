Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/DNDUpdatedUserEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / DNDUpdatedUserEvent

# Interface: DNDUpdatedUserEvent

Defined in: [events/dnd.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L15)

## Properties {#properties}

### dnd_status {#dnd_status}

```text
dnd_status: object;
```

Defined in: [events/dnd.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L18)

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

Defined in: [events/dnd.ts:23](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L23)

* * *

### type {#type}

```text
type: "dnd_updated_user";
```

Defined in: [events/dnd.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L16)

* * *

### user {#user}

```text
user: string;
```

Defined in: [events/dnd.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/dnd.ts#L17)
