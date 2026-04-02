Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/SharedChannelInviteDeclinedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / SharedChannelInviteDeclinedEvent

# Interface: SharedChannelInviteDeclinedEvent

Defined in: [events/shared-channel.ts:76](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L76)

## Properties {#properties}

### channel {#channel}

```
channel: SharedChannelItem;
```

Defined in: [events/shared-channel.ts:79](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L79)

* * *

### declining_team_id {#declining_team_id}

```
declining_team_id: string;
```

Defined in: [events/shared-channel.ts:80](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L80)

* * *

### declining_user {#declining_user}

```
declining_user: SharedChannelUserItem;
```

Defined in: [events/shared-channel.ts:82](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L82)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/shared-channel.ts:83](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L83)

* * *

### invite {#invite}

```
invite: SharedChannelInviteItem;
```

Defined in: [events/shared-channel.ts:78](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L78)

* * *

### teams_in_channel {#teams_in_channel}

```
teams_in_channel: SharedChannelTeamItem[];
```

Defined in: [events/shared-channel.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L81)

* * *

### type {#type}

```
type: "shared_channel_invite_declined";
```

Defined in: [events/shared-channel.ts:77](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L77)
