Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/SharedChannelInviteAcceptedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / SharedChannelInviteAcceptedEvent

# Interface: SharedChannelInviteAcceptedEvent

Defined in: [events/shared-channel.ts:46](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L46)

## Properties {#properties}

### accepting_user {#accepting_user}

```
accepting_user: SharedChannelUserItem;
```

Defined in: [events/shared-channel.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L52)

* * *

### approval_required {#approval_required}

```
approval_required: boolean;
```

Defined in: [events/shared-channel.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L48)

* * *

### channel {#channel}

```
channel: SharedChannelItem;
```

Defined in: [events/shared-channel.ts:50](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L50)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/shared-channel.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L53)

* * *

### invite {#invite}

```
invite: SharedChannelInviteItem;
```

Defined in: [events/shared-channel.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L49)

* * *

### teams_in_channel {#teams_in_channel}

```
teams_in_channel: SharedChannelTeamItem[];
```

Defined in: [events/shared-channel.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L51)

* * *

### type {#type}

```
type: "shared_channel_invite_accepted";
```

Defined in: [events/shared-channel.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L47)
