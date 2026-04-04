Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChannelCreatedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChannelCreatedEvent

# Interface: ChannelCreatedEvent

Defined in: packages/types/dist/events/channel.d.ts:8

## Properties {#properties}

### channel {#channel}

```text
channel: object;
```

Defined in: packages/types/dist/events/channel.d.ts:11

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

Defined in: packages/types/dist/events/channel.d.ts:10

* * *

### type {#type}

```text
type: "channel_created";
```

Defined in: packages/types/dist/events/channel.d.ts:9
