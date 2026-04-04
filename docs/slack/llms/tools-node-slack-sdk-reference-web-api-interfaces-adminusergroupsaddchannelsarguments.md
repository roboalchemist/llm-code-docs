Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsAddChannelsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsergroupsAddChannelsArguments

# Interface: AdminUsergroupsAddChannelsArguments

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L14)

## Extends {#extends}

* `ChannelIDs`.`UsergroupID`.`OptionalTeamAssignable`.`TokenOverridable`

## Properties {#properties}

### channel_ids {#channel_ids}

```text
channel_ids: string | string[];
```

Defined in: [packages/web-api/src/types/request/admin/usergroups.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/usergroups.ts#L5)

#### Description {#description}

One or more encoded channel IDs.

#### Inherited from {#inherited-from}

```text
ChannelIDs.channel_ids
```

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-1}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-1}

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

#### Inherited from {#inherited-from-2}

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

#### Inherited from {#inherited-from-3}

```text
UsergroupID.usergroup_id
```
