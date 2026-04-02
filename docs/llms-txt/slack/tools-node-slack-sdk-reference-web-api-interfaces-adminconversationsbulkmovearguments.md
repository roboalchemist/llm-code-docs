Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkMoveArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsBulkMoveArguments

# Interface: AdminConversationsBulkMoveArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L51)

## Extends {#extends}

* `ChannelIDs`.`TokenOverridable`

## Properties {#properties}

### channel_ids {#channel_ids}

```
channel_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:81](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L81)

#### Description {#description}

An array of channel IDs (must include at least one ID).

#### Inherited from {#inherited-from}

```
ChannelIDs.channel_ids
```

* * *

### target_team_id {#target_team_id}

```
target_team_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:53](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L53)

#### Description {#description-1}

Target team ID to move channels to.

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```
TokenOverridable.token
```
