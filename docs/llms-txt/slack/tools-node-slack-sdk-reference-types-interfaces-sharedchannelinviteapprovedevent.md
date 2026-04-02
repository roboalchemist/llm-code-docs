Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/SharedChannelInviteApprovedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / SharedChannelInviteApprovedEvent

# Interface: SharedChannelInviteApprovedEvent

Defined in: [events/shared-channel.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L61)

## Properties {#properties}

### approving_team_id {#approving_team_id}

```
approving_team_id: string;
```

Defined in: [events/shared-channel.ts:65](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L65)

* * *

### approving_user {#approving_user}

```
approving_user: SharedChannelUserItem;
```

Defined in: [events/shared-channel.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L67)

* * *

### channel {#channel}

```
channel: SharedChannelItem;
```

Defined in: [events/shared-channel.ts:64](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L64)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/shared-channel.ts:68](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L68)

* * *

### invite {#invite}

```
invite: SharedChannelInviteItem;
```

Defined in: [events/shared-channel.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L63)

* * *

### teams_in_channel {#teams_in_channel}

```
teams_in_channel: SharedChannelTeamItem[];
```

Defined in: [events/shared-channel.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L66)

* * *

### type {#type}

```
type: "shared_channel_invite_approved";
```

Defined in: [events/shared-channel.ts:62](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L62)
