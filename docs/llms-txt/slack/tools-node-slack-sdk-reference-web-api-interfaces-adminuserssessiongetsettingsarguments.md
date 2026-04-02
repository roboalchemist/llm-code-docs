Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersSessionGetSettingsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSessionGetSettingsArguments

# Interface: AdminUsersSessionGetSettingsArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:112](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L112)

## Extends {#extends}

* `UserIDs`.`TokenOverridable`

## Properties {#properties}

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```

* * *

### user_ids {#user_ids}

```text
user_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L92)

#### Description {#description-1}

List of encoded user IDs.

#### Inherited from {#inherited-from-1}

```text
UserIDs.user_ids
```
