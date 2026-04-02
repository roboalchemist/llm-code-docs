Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SharedChannelInviteApprovedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SharedChannelInviteApprovedEvent

# Interface: SharedChannelInviteApprovedEvent

Defined in: packages/types/dist/events/shared-channel.d.ts:58

## Properties {#properties}

### approving_team_id {#approving_team_id}

```text
approving_team_id: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:62

* * *

### approving_user {#approving_user}

```text
approving_user: SharedChannelUserItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:64

* * *

### channel {#channel}

```text
channel: SharedChannelItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:61

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:65

* * *

### invite {#invite}

```text
invite: SharedChannelInviteItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:60

* * *

### teams_in_channel {#teams_in_channel}

```text
teams_in_channel: SharedChannelTeamItem[];
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:63

* * *

### type {#type}

```text
type: "shared_channel_invite_approved";
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:59
