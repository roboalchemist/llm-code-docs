Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsRestrictAccessAddGroupArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsRestrictAccessAddGroupArguments

# Interface: AdminConversationsRestrictAccessAddGroupArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:142](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L142)

## Extends {#extends}

* `ChannelID`.`GroupID`.`RestrictAccessTeamID`.`TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L85)

#### Description {#description}

Encoded channel ID.

#### Inherited from {#inherited-from}

```
ChannelID.channel_id
```

* * *

### group_id {#group_id}

```
group_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:29](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L29)

#### Description {#description-1}

The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID.

#### Inherited from {#inherited-from-1}

```
GroupID.group_id
```

* * *

### team_id? {#team_id}

```
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L38)

#### Description {#description-2}

The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.

#### Inherited from {#inherited-from-2}

```
RestrictAccessTeamID.team_id
```

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```
TokenOverridable.token
```
