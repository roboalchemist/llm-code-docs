Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/SharedChannelInviteRequestedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / SharedChannelInviteRequestedEvent

# Interface: SharedChannelInviteRequestedEvent

Defined in: [events/shared-channel.ts:103](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L103)

## Properties {#properties}

### actor {#actor}

```
actor: object;
```

Defined in: [events/shared-channel.ts:105](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L105)

#### display_name {#display_name}

```
display_name: string;
```

#### id {#id}

```
id: string;
```

#### is_bot {#is_bot}

```
is_bot: boolean;
```

#### name {#name}

```
name: string;
```

#### real_name {#real_name}

```
real_name: string;
```

#### team_id {#team_id}

```
team_id: string;
```

#### timezone {#timezone}

```
timezone: string;
```

* * *

### channel_date_created {#channel_date_created}

```
channel_date_created: number;
```

Defined in: [events/shared-channel.ts:132](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L132)

* * *

### channel_id {#channel_id}

```
channel_id: string;
```

Defined in: [events/shared-channel.ts:114](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L114)

* * *

### channel_message_latest_counted_timestamp {#channel_message_latest_counted_timestamp}

```
channel_message_latest_counted_timestamp: number;
```

Defined in: [events/shared-channel.ts:133](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L133)

* * *

### channel_name {#channel_name}

```
channel_name: string;
```

Defined in: [events/shared-channel.ts:116](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L116)

* * *

### channel_type {#channel_type}

```
channel_type: "private" | "public";
```

Defined in: [events/shared-channel.ts:117](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L117)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/shared-channel.ts:134](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L134)

* * *

### event_type {#event_type}

```
event_type: "slack#/events/shared_channel_invite_requested";
```

Defined in: [events/shared-channel.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L115)

* * *

### is_external_limited {#is_external_limited}

```
is_external_limited: boolean;
```

Defined in: [events/shared-channel.ts:131](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L131)

* * *

### target_users {#target_users}

```
target_users: [{  email: string;  invite_id: string;}];
```

Defined in: [events/shared-channel.ts:118](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L118)

* * *

### teams_in_channel {#teams_in_channel}

```
teams_in_channel: [{  avatar_base_url: string;  date_created: number;  domain: string;  icon: {     image_34: string;     image_default: boolean;  };  id: string;  is_verified: boolean;  name: string;  requires_sponsorship: boolean;}];
```

Defined in: [events/shared-channel.ts:119](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L119)

* * *

### type {#type}

```
type: "shared_channel_invite_requested";
```

Defined in: [events/shared-channel.ts:104](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/shared-channel.ts#L104)
