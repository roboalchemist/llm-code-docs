Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsRemoveCustomRetentionArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsRemoveCustomRetentionArguments

# Interface: AdminConversationsRemoveCustomRetentionArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:133](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L133)

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

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```
TokenOverridable.token
```
