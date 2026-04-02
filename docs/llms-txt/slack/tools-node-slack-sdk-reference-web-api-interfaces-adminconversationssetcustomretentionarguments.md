Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsSetCustomRetentionArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsSetCustomRetentionArguments

# Interface: AdminConversationsSetCustomRetentionArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:202](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L202)

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

### duration_days {#duration_days}

```
duration_days: number;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:204](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L204)

#### Description {#description-1}

The message retention duration in days to set for this conversation.

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
