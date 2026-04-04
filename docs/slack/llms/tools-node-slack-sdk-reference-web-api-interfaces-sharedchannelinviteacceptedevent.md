Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SharedChannelInviteAcceptedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SharedChannelInviteAcceptedEvent

# Interface: SharedChannelInviteAcceptedEvent

Defined in: packages/types/dist/events/shared-channel.d.ts:45

## Properties {#properties}

### accepting_user {#accepting_user}

```text
accepting_user: SharedChannelUserItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:51

* * *

### approval_required {#approval_required}

```text
approval_required: boolean;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:47

* * *

### channel {#channel}

```text
channel: SharedChannelItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:49

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:52

* * *

### invite {#invite}

```text
invite: SharedChannelInviteItem;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:48

* * *

### teams_in_channel {#teams_in_channel}

```text
teams_in_channel: SharedChannelTeamItem[];
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:50

* * *

### type {#type}

```text
type: "shared_channel_invite_accepted";
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:46
