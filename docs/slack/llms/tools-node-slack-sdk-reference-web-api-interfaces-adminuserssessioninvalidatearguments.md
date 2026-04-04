Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersSessionInvalidateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSessionInvalidateArguments

# Interface: AdminUsersSessionInvalidateArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L115)

## Extends {#extends}

* `TeamID`.`TokenOverridable`

## Properties {#properties}

### session_id {#session_id}

```text
session_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:117](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L117)

#### Description {#description}

ID of the session to invalidate.

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L61)

#### Description {#description-1}

The encoded team ID.

#### Inherited from {#inherited-from}

```text
TeamID.team_id
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
