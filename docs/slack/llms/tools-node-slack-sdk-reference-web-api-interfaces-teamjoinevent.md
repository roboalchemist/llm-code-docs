Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/TeamJoinEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamJoinEvent

# Interface: TeamJoinEvent

Defined in: packages/types/dist/events/team.d.ts:17

## Properties {#properties}

### cache_ts {#cache_ts}

```text
cache_ts: number;
```text

Defined in: packages/types/dist/events/team.d.ts:92

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/team.d.ts:93

* * *

### type {#type}

```text
type: "team_join";
```text

Defined in: packages/types/dist/events/team.d.ts:18

* * *

### user {#user}

```text
user: object;
```text

Defined in: packages/types/dist/events/team.d.ts:19

#### color {#color}

```text
color: string;
```text

#### deleted {#deleted}

```text
deleted: boolean;
```text

#### enterprise_user? {#enterprise_user}

```text
optional enterprise_user: object;
```text

##### enterprise_user.enterprise_id {#enterprise_userenterprise_id}

```text
enterprise_id: string;
```text

##### enterprise_user.enterprise_name {#enterprise_userenterprise_name}

```text
enterprise_name: string;
```text

##### enterprise_user.id {#enterprise_userid}

```text
id: string;
```text

##### enterprise_user.is_admin {#enterprise_useris_admin}

```text
is_admin: boolean;
```text

##### enterprise_user.is_owner {#enterprise_useris_owner}

```text
is_owner: boolean;
```text

##### enterprise_user.teams {#enterprise_userteams}

```text
teams: string[];
```text

#### has_2fa? {#has_2fa}

```text
optional has_2fa: boolean;
```text

#### has_files? {#has_files}

```text
optional has_files: boolean;
```text

#### id {#id}

```text
id: string;
```text

#### is_admin {#is_admin}

```text
is_admin: boolean;
```text

#### is_app_user {#is_app_user}

```text
is_app_user: boolean;
```text

#### is_bot {#is_bot}

```text
is_bot: boolean;
```text

#### is_email_confirmed {#is_email_confirmed}

```text
is_email_confirmed: boolean;
```text

#### is_invited_user? {#is_invited_user}

```text
optional is_invited_user: boolean;
```text

#### is_owner {#is_owner}

```text
is_owner: boolean;
```text

#### is_primary_owner {#is_primary_owner}

```text
is_primary_owner: boolean;
```text

#### is_restricted {#is_restricted}

```text
is_restricted: boolean;
```text

#### is_stranger? {#is_stranger}

```text
optional is_stranger: boolean;
```text

#### is_ultra_restricted {#is_ultra_restricted}

```text
is_ultra_restricted: boolean;
```text

#### is_workflow_bot? {#is_workflow_bot}

```text
optional is_workflow_bot: boolean;
```text

#### locale {#locale}

```text
locale: string;
```text

#### name {#name}

```text
name: string;
```text

#### presence? {#presence}

```text
optional presence: string;
```text

#### profile {#profile}

```text
profile: object;
```text

##### profile.avatar_hash {#profileavatar_hash}

```text
avatar_hash: string;
```text

##### profile.display_name {#profiledisplay_name}

```text
display_name: string;
```text

##### profile.display_name_normalized {#profiledisplay_name_normalized}

```text
display_name_normalized: string;
```text

##### profile.email? {#profileemail}

```text
optional email: string;
```text

##### profile.fields {#profilefields}

```text
fields:   | {[key: string]: object;}  | []  | null;
```text

##### profile.first_name {#profilefirst_name}

```text
first_name: string;
```text

##### profile.huddle_state? {#profilehuddle_state}

```text
optional huddle_state: string;
```text

##### profile.huddle_state_expiration_ts? {#profilehuddle_state_expiration_ts}

```text
optional huddle_state_expiration_ts: number;
```text

##### profile.image_1024? {#profileimage_1024}

```text
optional image_1024: string;
```text

##### profile.image_192 {#profileimage_192}

```text
image_192: string;
```text

##### profile.image_24 {#profileimage_24}

```text
image_24: string;
```text

##### profile.image_32 {#profileimage_32}

```text
image_32: string;
```text

##### profile.image_48 {#profileimage_48}

```text
image_48: string;
```text

##### profile.image_512 {#profileimage_512}

```text
image_512: string;
```text

##### profile.image_72 {#profileimage_72}

```text
image_72: string;
```text

##### profile.image_original? {#profileimage_original}

```text
optional image_original: string;
```text

##### profile.is_custom_image? {#profileis_custom_image}

```text
optional is_custom_image: boolean;
```text

##### profile.last_name {#profilelast_name}

```text
last_name: string;
```text

##### profile.phone {#profilephone}

```text
phone: string;
```text

##### profile.real_name {#profilereal_name}

```text
real_name: string;
```text

##### profile.real_name_normalized {#profilereal_name_normalized}

```text
real_name_normalized: string;
```text

##### profile.skype {#profileskype}

```text
skype: string;
```text

##### profile.status_emoji {#profilestatus_emoji}

```text
status_emoji: string;
```text

##### profile.status_emoji_display_info {#profilestatus_emoji_display_info}

```text
status_emoji_display_info: StatusEmojiDisplayInfo[];
```text

##### profile.status_expiration {#profilestatus_expiration}

```text
status_expiration: number;
```text

##### profile.status_text {#profilestatus_text}

```text
status_text: string;
```text

##### profile.status_text_canonical {#profilestatus_text_canonical}

```text
status_text_canonical: string;
```text

##### profile.team {#profileteam}

```text
team: string;
```text

##### profile.title {#profiletitle}

```text
title: string;
```text

#### real_name {#real_name}

```text
real_name: string;
```text

#### team_id {#team_id}

```text
team_id: string;
```text

#### two_factor_type? {#two_factor_type}

```text
optional two_factor_type: string;
```text

#### tz {#tz}

```text
tz: string;
```text

#### tz_label {#tz_label}

```text
tz_label: string;
```text

#### tz_offset {#tz_offset}

```text
tz_offset: number;
```text

#### updated {#updated}

```text
updated: number;
```text

#### who_can_share_contact_card {#who_can_share_contact_card}

```text
who_can_share_contact_card: string;
```text
