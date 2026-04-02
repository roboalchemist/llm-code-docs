Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AppMentionEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AppMentionEvent

# Interface: AppMentionEvent

Defined in: packages/types/dist/events/app.d.ts:102

## Properties {#properties}

### attachments? {#attachments}

```text
optional attachments: MessageAttachment[];
```

Defined in: packages/types/dist/events/app.d.ts:124

* * *

### blocks? {#blocks}

```text
optional blocks: (Block | KnownBlock)[];
```

Defined in: packages/types/dist/events/app.d.ts:125

* * *

### bot_id? {#bot_id}

```text
optional bot_id: string;
```

Defined in: packages/types/dist/events/app.d.ts:105

* * *

### bot_profile? {#bot_profile}

```text
optional bot_profile: BotProfile;
```

Defined in: packages/types/dist/events/app.d.ts:106

* * *

### channel {#channel}

```text
channel: string;
```

Defined in: packages/types/dist/events/app.d.ts:189

* * *

### client_msg_id? {#client_msg_id}

```text
optional client_msg_id: string;
```

Defined in: packages/types/dist/events/app.d.ts:192

* * *

### display_as_bot? {#display_as_bot}

```text
optional display_as_bot: boolean;
```

Defined in: packages/types/dist/events/app.d.ts:183

* * *

### edited? {#edited}

```text
optional edited: object;
```

Defined in: packages/types/dist/events/app.d.ts:184

#### ts {#ts}

```text
ts: string;
```

#### user {#user}

```text
user: string;
```

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```

Defined in: packages/types/dist/events/app.d.ts:190

* * *

### files? {#files}

```text
optional files: object[];
```

Defined in: packages/types/dist/events/app.d.ts:126

#### created {#created}

```text
created: number;
```

#### display_as_bot {#display_as_bot-1}

```text
display_as_bot: boolean;
```

#### editable {#editable}

```text
editable: boolean;
```

#### external_type {#external_type}

```text
external_type: string;
```

#### file_access {#file_access}

```text
file_access: string;
```

#### filetype {#filetype}

```text
filetype: string;
```

#### has_rich_preview {#has_rich_preview}

```text
has_rich_preview: boolean;
```

#### id {#id}

```text
id: string;
```

#### is_external {#is_external}

```text
is_external: boolean;
```

#### is_public {#is_public}

```text
is_public: boolean;
```

#### is_starred {#is_starred}

```text
is_starred: boolean;
```

#### media_display_type {#media_display_type}

```text
media_display_type: string;
```

#### mimetype {#mimetype}

```text
mimetype: string;
```

#### mode {#mode}

```text
mode: string;
```

#### name {#name}

```text
name: string;
```

#### original_h? {#original_h}

```text
optional original_h: number;
```

#### original_w? {#original_w}

```text
optional original_w: number;
```

#### permalink {#permalink}

```text
permalink: string;
```

#### permalink_public {#permalink_public}

```text
permalink_public: string;
```

#### pretty_type {#pretty_type}

```text
pretty_type: string;
```

#### public_url_shared {#public_url_shared}

```text
public_url_shared: boolean;
```

#### size {#size}

```text
size: number;
```

#### thumb_1024? {#thumb_1024}

```text
optional thumb_1024: string;
```

#### thumb_1024_h? {#thumb_1024_h}

```text
optional thumb_1024_h: number;
```

#### thumb_1024_w? {#thumb_1024_w}

```text
optional thumb_1024_w: number;
```

#### thumb_160? {#thumb_160}

```text
optional thumb_160: string;
```

#### thumb_360? {#thumb_360}

```text
optional thumb_360: string;
```

#### thumb_360_h? {#thumb_360_h}

```text
optional thumb_360_h: number;
```

#### thumb_360_w? {#thumb_360_w}

```text
optional thumb_360_w: number;
```

#### thumb_480? {#thumb_480}

```text
optional thumb_480: string;
```

#### thumb_480_h? {#thumb_480_h}

```text
optional thumb_480_h: number;
```

#### thumb_480_w? {#thumb_480_w}

```text
optional thumb_480_w: number;
```

#### thumb_64? {#thumb_64}

```text
optional thumb_64: string;
```

#### thumb_720? {#thumb_720}

```text
optional thumb_720: string;
```

#### thumb_720_h? {#thumb_720_h}

```text
optional thumb_720_h: number;
```

#### thumb_720_w? {#thumb_720_w}

```text
optional thumb_720_w: number;
```

#### thumb_80? {#thumb_80}

```text
optional thumb_80: string;
```

#### thumb_800? {#thumb_800}

```text
optional thumb_800: string;
```

#### thumb_800_h? {#thumb_800_h}

```text
optional thumb_800_h: number;
```

#### thumb_800_w? {#thumb_800_w}

```text
optional thumb_800_w: number;
```

#### thumb_960? {#thumb_960}

```text
optional thumb_960: string;
```

#### thumb_960_h? {#thumb_960_h}

```text
optional thumb_960_h: number;
```

#### thumb_960_w? {#thumb_960_w}

```text
optional thumb_960_w: number;
```

#### thumb_pdf? {#thumb_pdf}

```text
optional thumb_pdf: string;
```

#### thumb_pdf_h? {#thumb_pdf_h}

```text
optional thumb_pdf_h: number;
```

#### thumb_pdf_w? {#thumb_pdf_w}

```text
optional thumb_pdf_w: number;
```

#### thumb_tiny? {#thumb_tiny}

```text
optional thumb_tiny: string;
```

#### timestamp {#timestamp}

```text
timestamp: number;
```

#### title {#title}

```text
title: string;
```

#### url_private {#url_private}

```text
url_private: string;
```

#### url_private_download {#url_private_download}

```text
url_private_download: string;
```

#### user {#user-1}

```text
user: string;
```

#### user_team {#user_team}

```text
user_team: string;
```

#### username {#username}

```text
username: string;
```

* * *

### source_team? {#source_team}

```text
optional source_team: string;
```

Defined in: packages/types/dist/events/app.d.ts:110

* * *

### subtype? {#subtype}

```text
optional subtype: string;
```

Defined in: packages/types/dist/events/app.d.ts:104

* * *

### team? {#team}

```text
optional team: string;
```

Defined in: packages/types/dist/events/app.d.ts:108

* * *

### text {#text}

```text
text: string;
```

Defined in: packages/types/dist/events/app.d.ts:123

* * *

### thread_ts? {#thread_ts}

```text
optional thread_ts: string;
```

Defined in: packages/types/dist/events/app.d.ts:191

* * *

### ts {#ts-1}

```text
ts: string;
```

Defined in: packages/types/dist/events/app.d.ts:188

* * *

### type {#type}

```text
type: "app_mention";
```

Defined in: packages/types/dist/events/app.d.ts:103

* * *

### upload? {#upload}

```text
optional upload: boolean;
```

Defined in: packages/types/dist/events/app.d.ts:182

* * *

### user? {#user-2}

```text
optional user: string;
```

Defined in: packages/types/dist/events/app.d.ts:122

* * *

### user_profile? {#user_profile}

```text
optional user_profile: object;
```

Defined in: packages/types/dist/events/app.d.ts:111

#### avatar_hash? {#avatar_hash}

```text
optional avatar_hash: string;
```

#### display_name {#display_name}

```text
display_name: string;
```

#### first_name {#first_name}

```text
first_name: string;
```

#### image_72? {#image_72}

```text
optional image_72: string;
```

#### is_restricted? {#is_restricted}

```text
optional is_restricted: boolean;
```

#### is_ultra_restricted? {#is_ultra_restricted}

```text
optional is_ultra_restricted: boolean;
```

#### name {#name-1}

```text
name: string;
```

#### real_name {#real_name}

```text
real_name: string;
```

#### team {#team-1}

```text
team: string;
```

* * *

### user_team? {#user_team-1}

```text
optional user_team: string;
```

Defined in: packages/types/dist/events/app.d.ts:109

* * *

### username? {#username-1}

```text
optional username: string;
```

Defined in: packages/types/dist/events/app.d.ts:107
