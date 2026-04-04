Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksRemoveArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / BookmarksRemoveArguments

# Interface: BookmarksRemoveArguments

Defined in: [packages/web-api/src/types/request/bookmarks.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L31)

## Extends {#extends}

* `ChannelID`.`ID`.`TokenOverridable`

## Properties {#properties}

### bookmark_id {#bookmark_id}

```text
bookmark_id: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L4)

#### Inherited from {#inherited-from}

```text
ID.bookmark_id
```

* * *

### channel_id {#channel_id}

```text
channel_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L85)

#### Description {#description}

Encoded channel ID.

#### Inherited from {#inherited-from-1}

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

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```
