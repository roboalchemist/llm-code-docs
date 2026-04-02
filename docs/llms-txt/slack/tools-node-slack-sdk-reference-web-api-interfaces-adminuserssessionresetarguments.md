Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersSessionResetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSessionResetArguments

# Interface: AdminUsersSessionResetArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:126](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L126)

## Extends {#extends}

* `UserID`.`SessionExpirationTarget`.`TokenOverridable`

## Properties {#properties}

### mobile_only? {#mobile_only}

```text
optional mobile_only: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L25)

#### Description {#description}

Only expire mobile sessions. Defaults to `false`.

#### Inherited from {#inherited-from}

```text
SessionExpirationTarget.mobile_only
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

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

#### Description {#description-2}

Encoded user ID.

#### Inherited from {#inherited-from-2}

```text
UserID.user_id
```

* * *

### web_only? {#web_only}

```text
optional web_only: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L27)

#### Description {#description-3}

Only expire web sessions. Defaults to `false`.

#### Inherited from {#inherited-from-3}

```text
SessionExpirationTarget.web_only
```
