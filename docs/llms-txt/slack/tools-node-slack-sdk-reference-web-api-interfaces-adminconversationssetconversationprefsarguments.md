Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsSetConversationPrefsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsSetConversationPrefsArguments

# Interface: AdminConversationsSetConversationPrefsArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:196](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L196)

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

### prefs {#prefs}

```
prefs: Record<string, unknown>;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:198](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L198)

#### Description {#description-1}

The prefs for this channel.

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
