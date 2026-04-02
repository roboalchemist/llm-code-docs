Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SharedChannelInviteRequestedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SharedChannelInviteRequestedEvent

# Interface: SharedChannelInviteRequestedEvent

Defined in: packages/types/dist/events/shared-channel.d.ts:94

## Properties {#properties}

### actor {#actor}

```text
actor: object;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:96

#### display_name {#display_name}

```text
display_name: string;
```text

#### id {#id}

```text
id: string;
```text

#### is_bot {#is_bot}

```text
is_bot: boolean;
```text

#### name {#name}

```text
name: string;
```text

#### real_name {#real_name}

```text
real_name: string;
```text

#### team_id {#team_id}

```text
team_id: string;
```text

#### timezone {#timezone}

```text
timezone: string;
```text

* * *

### channel_date_created {#channel_date_created}

```text
channel_date_created: number;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:129

* * *

### channel_id {#channel_id}

```text
channel_id: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:105

* * *

### channel_message_latest_counted_timestamp {#channel_message_latest_counted_timestamp}

```text
channel_message_latest_counted_timestamp: number;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:130

* * *

### channel_name {#channel_name}

```text
channel_name: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:107

* * *

### channel_type {#channel_type}

```text
channel_type: "private" | "public";
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:108

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:131

* * *

### event_type {#event_type}

```text
event_type: "slack#/events/shared_channel_invite_requested";
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:106

* * *

### is_external_limited {#is_external_limited}

```text
is_external_limited: boolean;
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:128

* * *

### target_users {#target_users}

```text
target_users: [{  email: string;  invite_id: string;}];
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:109

* * *

### teams_in_channel {#teams_in_channel}

```text
teams_in_channel: [{  avatar_base_url: string;  date_created: number;  domain: string;  icon: {     image_34: string;     image_default: boolean;  };  id: string;  is_verified: boolean;  name: string;  requires_sponsorship: boolean;}];
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:113

* * *

### type {#type}

```text
type: "shared_channel_invite_requested";
```text

Defined in: packages/types/dist/events/shared-channel.d.ts:95
