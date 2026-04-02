Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsSetTeamsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsSetTeamsArguments

# Interface: AdminConversationsSetTeamsArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:208](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L208)

## Extends {#extends}

* `ChannelID`.`TokenOverridable`

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

### org_channel? {#org_channel}

```
optional org_channel: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:210](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L210)

#### Description {#description-1}

Set to `true` if channel has to be converted to an org channel. Defaults to `false`.

* * *

### target_team_ids? {#target_team_ids}

```
optional target_team_ids: string[];
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:215](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L215)

#### Description {#description-2}

A list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.

* * *

### team_id? {#team_id}

```
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:220](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L220)

#### Description {#description-3}

The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```
TokenOverridable.token
```
