Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsDisconnectSharedArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsDisconnectSharedArguments

# Interface: AdminConversationsDisconnectSharedArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:99](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L99)

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

### leaving_team_ids? {#leaving_team_ids}

```
optional leaving_team_ids: string[];
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L101)

#### Description {#description-1}

Team IDs getting removed from the channel, optional if there are only two teams in the channel.

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
