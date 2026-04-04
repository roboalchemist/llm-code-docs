Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CallsAddArguments

# Interface: CallsAddArguments

Defined in: [packages/web-api/src/types/request/calls.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L28)

## Extends {#extends}

* `Partial`<`Users`\>.`CallDetails`.`TokenOverridable`

## Properties {#properties}

### created_by? {#created_by}

```text
optional created_by: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L37)

#### Description {#description}

ID of the user who created this Call. When this method is called with a user token, this field is optional and defaults to the authed user of the token. Otherwise, the field is required.

* * *

### date_start? {#date_start}

```text
optional date_start: number;
```

Defined in: [packages/web-api/src/types/request/calls.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L39)

#### Description {#description-1}

Unix timestamp of the call start time.

* * *

### desktop_app_join_url? {#desktop_app_join_url}

```text
optional desktop_app_join_url: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L22)

#### Description {#description-2}

When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.

#### Inherited from {#inherited-from}

```text
CallDetails.desktop_app_join_url
```

* * *

### external_display_id? {#external_display_id}

```text
optional external_display_id: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L44)

#### Description {#description-3}

An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.

* * *

### external_unique_id {#external_unique_id}

```text
external_unique_id: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L32)

#### Description {#description-4}

An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.

* * *

### join_url {#join_url}

```text
join_url: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L17)

#### Description {#description-5}

The URL required for a client to join the Call.

#### Inherited from {#inherited-from-1}

```text
CallDetails.join_url
```

* * *

### title? {#title}

```text
optional title: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L24)

#### Description {#description-6}

The name of the Call.

#### Inherited from {#inherited-from-2}

```text
CallDetails.title
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-7}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```text
TokenOverridable.token
```

* * *

### users? {#users}

```text
optional users: CallUser[];
```

Defined in: [packages/web-api/src/types/request/calls.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L13)

#### Description {#description-8}

The list of users to add/remove to/from the Call.

#### See {#see}

[Using the Calls API: a note on Users](https://docs.slack.dev/apis/web-api/using-the-calls-api).

#### Inherited from {#inherited-from-4}

[`CallsParticipantsAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsParticipantsAddArguments).[`users`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsParticipantsAddArguments#users)
