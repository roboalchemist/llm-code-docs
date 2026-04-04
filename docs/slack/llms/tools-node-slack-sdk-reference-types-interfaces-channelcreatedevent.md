Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ChannelCreatedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / ChannelCreatedEvent

# Interface: ChannelCreatedEvent

Defined in: [events/channel.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L9)

## Properties {#properties}

### channel {#channel}

```text
channel: object;
```

Defined in: [events/channel.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L12)

#### context_team_id {#context_team_id}

```text
context_team_id: string;
```

#### created {#created}

```text
created: number;
```

#### creator {#creator}

```text
creator: string;
```

#### id {#id}

```text
id: string;
```

#### is_archived {#is_archived}

```text
is_archived: boolean;
```

#### is_channel {#is_channel}

```text
is_channel: boolean;
```

#### is_ext_shared {#is_ext_shared}

```text
is_ext_shared: boolean;
```

#### is_frozen {#is_frozen}

```text
is_frozen: boolean;
```

#### is_general {#is_general}

```text
is_general: boolean;
```

#### is_group {#is_group}

```text
is_group: boolean;
```

#### is_im {#is_im}

```text
is_im: boolean;
```

#### is_mpim {#is_mpim}

```text
is_mpim: boolean;
```

#### is_org_shared {#is_org_shared}

```text
is_org_shared: boolean;
```

#### is_pending_ext_shared {#is_pending_ext_shared}

```text
is_pending_ext_shared: boolean;
```

#### is_private {#is_private}

```text
is_private: boolean;
```

#### is_shared {#is_shared}

```text
is_shared: boolean;
```

#### name {#name}

```text
name: string;
```

#### name_normalized {#name_normalized}

```text
name_normalized: string;
```

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: [events/channel.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L11)

* * *

### type {#type}

```text
type: "channel_created";
```

Defined in: [events/channel.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L10)
