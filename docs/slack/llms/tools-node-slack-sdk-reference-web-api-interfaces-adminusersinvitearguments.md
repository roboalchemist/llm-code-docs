Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersInviteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersInviteArguments

# Interface: AdminUsersInviteArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L63)

## Extends {#extends}

* `ChannelIDs`.`TeamID`.`IsRestricted`.`IsUltraRestricted`.`TokenOverridable`

## Properties {#properties}

### channel_ids {#channel_ids}

```text
channel_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L81)

#### Description {#description}

An array of channel IDs (must include at least one ID).

#### Inherited from {#inherited-from}

```text
ChannelIDs.channel_ids
```

* * *

### custom_message? {#custom_message}

```text
optional custom_message: string;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:72](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L72)

#### Description {#description-1}

An optional message to send to the user in the invite email.

* * *

### email {#email}

```text
email: string;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L70)

#### Description {#description-2}

The email address of the person to invite.

* * *

### email_password_policy_enabled? {#email_password_policy_enabled}

```text
optional email_password_policy_enabled: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:77](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L77)

#### Description {#description-3}

Allow invited user to sign in via email and password. Only available for Enterprise Grid teams via admin invite.

* * *

### guest_expiration_ts? {#guest_expiration_ts}

```text
optional guest_expiration_ts: string;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:82](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L82)

#### Description {#description-4}

Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.

* * *

### is_restricted? {#is_restricted}

```text
optional is_restricted: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L15)

#### Description {#description-5}

Set to `true` if user should be added to the workspace as a guest.

#### Inherited from {#inherited-from-1}

```text
IsRestricted.is_restricted
```

* * *

### is_ultra_restricted? {#is_ultra_restricted}

```text
optional is_ultra_restricted: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L20)

#### Description {#description-6}

Set to `true` if user should be added to the workspace as a guest.

#### Inherited from {#inherited-from-2}

```text
IsUltraRestricted.is_ultra_restricted
```

* * *

### real_name? {#real_name}

```text
optional real_name: string;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:84](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L84)

#### Description {#description-7}

Full name of the user.

* * *

### resend? {#resend}

```text
optional resend: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:89](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L89)

#### Description {#description-8}

Allow this invite to be resent in the future if a user has not signed up yet. Resending can only be done via the UI and has no expiration. Defaults to `false`.

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description-9}

The encoded team ID.

#### Inherited from {#inherited-from-3}

```text
TeamID.team_id
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-10}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

```text
TokenOverridable.token
```
