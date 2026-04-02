Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/UserHuddleChangedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / UserHuddleChangedEvent

# Interface: UserHuddleChangedEvent

Defined in: [events/user.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/user.ts#L85)

## Properties {#properties}

### cache_ts {#cache_ts}

```
cache_ts: number;
```

Defined in: [events/user.ts:164](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/user.ts#L164)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/user.ts:165](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/user.ts#L165)

* * *

### type {#type}

```
type: "user_huddle_changed";
```

Defined in: [events/user.ts:86](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/user.ts#L86)

* * *

### user {#user}

```
user: object;
```

Defined in: [events/user.ts:87](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/user.ts#L87)

#### color {#color}

```
color: string;
```

#### deleted {#deleted}

```
deleted: boolean;
```

#### enterprise_user? {#enterprise_user}

```
optional enterprise_user: object;
```

##### enterprise_user.enterprise_id {#enterprise_userenterprise_id}

```
enterprise_id: string;
```

##### enterprise_user.enterprise_name {#enterprise_userenterprise_name}

```
enterprise_name: string;
```

##### enterprise_user.id {#enterprise_userid}

```
id: string;
```

##### enterprise_user.is_admin {#enterprise_useris_admin}

```
is_admin: boolean;
```

##### enterprise_user.is_owner {#enterprise_useris_owner}

```
is_owner: boolean;
```

##### enterprise_user.teams {#enterprise_userteams}

```
teams: string[];
```

#### has_2fa? {#has_2fa}

```
optional has_2fa: boolean;
```

#### has_files? {#has_files}

```
optional has_files: boolean;
```

#### id {#id}

```
id: string;
```

#### is_admin {#is_admin}

```
is_admin: boolean;
```

#### is_app_user {#is_app_user}

```
is_app_user: boolean;
```

#### is_bot {#is_bot}

```
is_bot: boolean;
```

#### is_email_confirmed {#is_email_confirmed}

```
is_email_confirmed: boolean;
```

#### is_invited_user? {#is_invited_user}

```
optional is_invited_user: boolean;
```

#### is_owner {#is_owner}

```
is_owner: boolean;
```

#### is_primary_owner {#is_primary_owner}

```
is_primary_owner: boolean;
```

#### is_restricted {#is_restricted}

```
is_restricted: boolean;
```

#### is_stranger? {#is_stranger}

```
optional is_stranger: boolean;
```

#### is_ultra_restricted {#is_ultra_restricted}

```
is_ultra_restricted: boolean;
```

#### is_workflow_bot? {#is_workflow_bot}

```
optional is_workflow_bot: boolean;
```

#### locale {#locale}

```
locale: string;
```

#### name {#name}

```
name: string;
```

#### presence? {#presence}

```
optional presence: string;
```

#### profile {#profile}

```
profile: object;
```

##### profile.avatar_hash {#profileavatar_hash}

```
avatar_hash: string;
```

##### profile.display_name {#profiledisplay_name}

```
display_name: string;
```

##### profile.display_name_normalized {#profiledisplay_name_normalized}

```
display_name_normalized: string;
```

##### profile.email? {#profileemail}

```
optional email: string;
```

##### profile.fields {#profilefields}

```
fields:   | []  | {[key: string]: object;}  | null;
```

##### profile.first_name {#profilefirst_name}

```
first_name: string;
```

##### profile.huddle_state {#profilehuddle_state}

```
huddle_state: string;
```

##### profile.huddle_state_call_id? {#profilehuddle_state_call_id}

```
optional huddle_state_call_id: string;
```

##### profile.huddle_state_expiration_ts {#profilehuddle_state_expiration_ts}

```
huddle_state_expiration_ts: number;
```

##### profile.image_1024? {#profileimage_1024}

```
optional image_1024: string;
```

##### profile.image_192 {#profileimage_192}

```
image_192: string;
```

##### profile.image_24 {#profileimage_24}

```
image_24: string;
```

##### profile.image_32 {#profileimage_32}

```
image_32: string;
```

##### profile.image_48 {#profileimage_48}

```
image_48: string;
```

##### profile.image_512 {#profileimage_512}

```
image_512: string;
```

##### profile.image_72 {#profileimage_72}

```
image_72: string;
```

##### profile.image_original? {#profileimage_original}

```
optional image_original: string;
```

##### profile.is_custom_image? {#profileis_custom_image}

```
optional is_custom_image: boolean;
```

##### profile.last_name {#profilelast_name}

```
last_name: string;
```

##### profile.phone {#profilephone}

```
phone: string;
```

##### profile.real_name {#profilereal_name}

```
real_name: string;
```

##### profile.real_name_normalized {#profilereal_name_normalized}

```
real_name_normalized: string;
```

##### profile.skype {#profileskype}

```
skype: string;
```

##### profile.status_emoji {#profilestatus_emoji}

```
status_emoji: string;
```

##### profile.status_emoji_display_info {#profilestatus_emoji_display_info}

```
status_emoji_display_info: StatusEmojiDisplayInfo[];
```

##### profile.status_expiration {#profilestatus_expiration}

```
status_expiration: number;
```

##### profile.status_text {#profilestatus_text}

```
status_text: string;
```

##### profile.status_text_canonical {#profilestatus_text_canonical}

```
status_text_canonical: string;
```

##### profile.team {#profileteam}

```
team: string;
```

##### profile.title {#profiletitle}

```
title: string;
```

#### real_name {#real_name}

```
real_name: string;
```

#### team_id {#team_id}

```
team_id: string;
```

#### two_factor_type? {#two_factor_type}

```
optional two_factor_type: string;
```

#### tz {#tz}

```
tz: string;
```

#### tz_label {#tz_label}

```
tz_label: string;
```

#### tz_offset {#tz_offset}

```
tz_offset: number;
```

#### updated {#updated}

```
updated: number;
```

#### who_can_share_contact_card {#who_can_share_contact_card}

```
who_can_share_contact_card: string;
```
