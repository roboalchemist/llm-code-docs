Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsRestrictAccessListGroupsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsRestrictAccessListGroupsArguments

# Interface: AdminConversationsRestrictAccessListGroupsArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:149](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L149)

## Extends {#extends}

* `ChannelID`.`RestrictAccessTeamID`.`TokenOverridable`

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

### team_id? {#team_id}

```
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L38)

#### Description {#description-1}

The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.

#### Inherited from {#inherited-from-1}

```
RestrictAccessTeamID.team_id
```

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```
TokenOverridable.token
```
