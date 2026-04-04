Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/GroupRenameEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / GroupRenameEvent

# Interface: GroupRenameEvent

Defined in: [events/group.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/group.ts#L43)

## Properties {#properties}

### channel {#channel}

```
channel: object;
```

Defined in: [events/group.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/group.ts#L45)

#### created {#created}

```
created: number;
```

#### id {#id}

```
id: string;
```

#### is_channel {#is_channel}

```
is_channel: boolean;
```

#### is_mpim {#is_mpim}

```
is_mpim: boolean;
```

#### name {#name}

```
name: string;
```

#### name_normalized {#name_normalized}

```
name_normalized: string;
```

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/group.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/group.ts#L53)

* * *

### type {#type}

```
type: "group_rename";
```

Defined in: [events/group.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/group.ts#L44)
