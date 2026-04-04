Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsListChannelsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsergroupsListChannelsArguments

# Interface: AdminUsergroupsListChannelsArguments

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L35)

## Extends {#extends}

* `UsergroupID`.`OptionalTeamAssignable`.`TokenOverridable`

## Properties {#properties}

### include_num_members? {#include_num_members}

```text
optional include_num_members: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L37)

#### Description {#description}

Flag to include or exclude the count of members per channel.

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

### usergroup_id {#usergroup_id}

```text
usergroup_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L10)

#### Description {#description-3}

ID of the IDP group to list/manage channels for.

#### Inherited from {#inherited-from-2}

```text
UsergroupID.usergroup_id
```
