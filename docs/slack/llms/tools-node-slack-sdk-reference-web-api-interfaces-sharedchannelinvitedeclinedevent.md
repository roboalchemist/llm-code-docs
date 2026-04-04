Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SharedChannelInviteDeclinedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SharedChannelInviteDeclinedEvent

# Interface: SharedChannelInviteDeclinedEvent

Defined in: packages/types/dist/events/shared-channel.d.ts:71

## Properties {#properties}

### channel {#channel}

```text
channel: SharedChannelItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:74

* * *

### declining_team_id {#declining_team_id}

```text
declining_team_id: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:75

* * *

### declining_user {#declining_user}

```text
declining_user: SharedChannelUserItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:77

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:78

* * *

### invite {#invite}

```text
invite: SharedChannelInviteItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:73

* * *

### teams_in_channel {#teams_in_channel}

```text
teams_in_channel: SharedChannelTeamItem[];
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:76

* * *

### type {#type}

```text
type: "shared_channel_invite_declined";
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:72
