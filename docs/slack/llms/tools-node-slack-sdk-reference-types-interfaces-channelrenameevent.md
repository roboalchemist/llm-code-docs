Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ChannelRenameEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / ChannelRenameEvent

# Interface: ChannelRenameEvent

Defined in: [events/channel.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L60)

## Properties {#properties}

### channel {#channel}

```text
channel: object;
```

Defined in: [events/channel.ts:62](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L62)

#### created {#created}

```text
created: number;
```

#### id {#id}

```text
id: string;
```

#### is_channel {#is_channel}

```text
is_channel: boolean;
```

#### is_mpim {#is_mpim}

```text
is_mpim: boolean;
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

Defined in: [events/channel.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L70)

* * *

### type {#type}

```text
type: "channel_rename";
```

Defined in: [events/channel.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/channel.ts#L61)
