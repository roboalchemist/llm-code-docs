Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsAddTeamsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsergroupsAddTeamsArguments

# Interface: AdminUsergroupsAddTeamsArguments

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L21)

## Extends {#extends}

* `UsergroupID`.`TokenOverridable`

## Properties {#properties}

### auto_provision? {#auto_provision}

```text
optional auto_provision: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L31)

#### Description {#description}

When `true`, this method automatically creates new workspace accounts for the IDP group members. Defaults to `false`.

* * *

### team_ids {#team_ids}

```text
team_ids: string | string[];
```

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L26)

#### Description {#description-1}

One or more encoded team (workspace) IDs. Each workspace MUST belong to the organization associated with the token.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```

* * *

### usergroup_id {#usergroup_id}

```text
usergroup_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L10)

#### Description {#description-3}

ID of the IDP group to list/manage channels for.

#### Inherited from {#inherited-from-1}

```text
UsergroupID.usergroup_id
```
