Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/AppRequestedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / AppRequestedEvent

# Interface: AppRequestedEvent

Defined in: [events/app.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L6)

## Properties {#properties}

### app_request {#app_request}

```text
app_request: object;
```

Defined in: [events/app.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L8)

#### app {#app}

```text
app: object;
```

##### app.additional_info {#appadditional_info}

```text
additional_info: string;
```

##### app.app_directory_url {#appapp_directory_url}

```text
app_directory_url: string;
```

##### app.app_homepage_url {#appapp_homepage_url}

```text
app_homepage_url: string;
```

##### app.description {#appdescription}

```text
description: string;
```

##### app.help_url {#apphelp_url}

```text
help_url: string;
```

##### app.icons? {#appicons}

```text
optional icons: object;
```

##### app.icons.image_1024? {#appiconsimage_1024}

```text
optional image_1024: string;
```

##### app.icons.image_128? {#appiconsimage_128}

```text
optional image_128: string;
```

##### app.icons.image_192? {#appiconsimage_192}

```text
optional image_192: string;
```

##### app.icons.image_32? {#appiconsimage_32}

```text
optional image_32: string;
```

##### app.icons.image_36? {#appiconsimage_36}

```text
optional image_36: string;
```

##### app.icons.image_48? {#appiconsimage_48}

```text
optional image_48: string;
```

##### app.icons.image_512? {#appiconsimage_512}

```text
optional image_512: string;
```

##### app.icons.image_64? {#appiconsimage_64}

```text
optional image_64: string;
```

##### app.icons.image_72? {#appiconsimage_72}

```text
optional image_72: string;
```

##### app.icons.image_96? {#appiconsimage_96}

```text
optional image_96: string;
```

##### app.icons.image_original? {#appiconsimage_original}

```text
optional image_original: string;
```

##### app.id {#appid}

```text
id: string;
```

##### app.is_app_directory_approved {#appis_app_directory_approved}

```text
is_app_directory_approved: boolean;
```

##### app.is_granular_bot_app {#appis_granular_bot_app}

```text
is_granular_bot_app: boolean;
```

##### app.is_internal {#appis_internal}

```text
is_internal: boolean;
```

##### app.name {#appname}

```text
name: string;
```

##### app.privacy_policy_url {#appprivacy_policy_url}

```text
privacy_policy_url: string;
```

#### id {#id}

```text
id: string;
```

* * *

### date_created {#date_created}

```text
date_created: number;
```

Defined in: [events/app.ts:64](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L64)

* * *

### is_user_app_collaborator {#is_user_app_collaborator}

```text
is_user_app_collaborator: boolean;
```

Defined in: [events/app.ts:46](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L46)

* * *

### message {#message}

```text
message: string;
```

Defined in: [events/app.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L63)

* * *

### previous_resolution {#previous_resolution}

```text
previous_resolution:   | {  scopes: {     description: string;     is_dangerous: boolean;     name: string;     token_type: "user" | "bot" | "app" | null;  };  status: "approved" | "restricted";}  | null;
```

Defined in: [events/app.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L37)

* * *

### scopes {#scopes}

```text
scopes: object;
```

Defined in: [events/app.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L57)

#### description {#description}

```text
description: string;
```

#### is_dangerous {#is_dangerous}

```text
is_dangerous: boolean;
```

#### name {#name}

```text
name: string;
```

#### token_type {#token_type}

```text
token_type: "user" | "bot" | "app" | null;
```

* * *

### team {#team}

```text
team: object;
```

Defined in: [events/app.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L52)

#### domain {#domain}

```text
domain: string;
```

#### id {#id-1}

```text
id: string;
```

#### name {#name-1}

```text
name: string;
```

* * *

### type {#type}

```text
type: "app_requested";
```

Defined in: [events/app.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L7)

* * *

### user {#user}

```text
user: object;
```

Defined in: [events/app.ts:47](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/app.ts#L47)

#### email {#email}

```text
email: string;
```

#### id {#id-2}

```text
id: string;
```

#### name {#name-2}

```text
name: string;
```
