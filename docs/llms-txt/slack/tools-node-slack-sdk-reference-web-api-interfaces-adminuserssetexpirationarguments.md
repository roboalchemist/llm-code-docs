Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersSetExpirationArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSetExpirationArguments

# Interface: AdminUsersSetExpirationArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:146](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L146)

## Extends {#extends}

* `UserID`.`TokenOverridable`.`OptionalTeamAssignable`

## Properties {#properties}

### expiration_ts {#expiration_ts}

```text
expiration_ts: number;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:148](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L148)

#### Description {#description}

Epoch timestamp in seconds when guest account should be disabled.

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-1}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from}

```text
OptionalTeamAssignable.team_id
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```

* * *

### user_id {#user_id}

```text
user_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:96](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L96)

#### Description {#description-3}

Encoded user ID.

#### Inherited from {#inherited-from-2}

```text
UserID.user_id
```
