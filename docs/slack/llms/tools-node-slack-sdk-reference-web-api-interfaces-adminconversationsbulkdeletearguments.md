Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsBulkDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsBulkDeleteArguments

# Interface: AdminConversationsBulkDeleteArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L48)

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
