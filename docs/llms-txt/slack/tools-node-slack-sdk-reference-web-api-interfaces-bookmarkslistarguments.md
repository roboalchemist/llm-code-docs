Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / BookmarksListArguments

# Interface: BookmarksListArguments

Defined in: [packages/web-api/src/types/request/bookmarks.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L28)

## Extends {#extends}

* `ChannelID`.`TokenOverridable`

## Properties {#properties}

### channel_id {#channel_id}

```text
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L85)

#### Description {#description}

Encoded channel ID.

#### Inherited from {#inherited-from}

```text
ChannelID.channel_id
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
