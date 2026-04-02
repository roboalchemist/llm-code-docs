Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksEditArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / BookmarksEditArguments

# Interface: BookmarksEditArguments

Defined in: [packages/web-api/src/types/request/bookmarks.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L25)

## Extends {#extends}

* `ChannelID`.`ID`.`Partial`<`BookmarkFields`\>.`TokenOverridable`

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

### emoji? {#emoji}

```text
optional emoji: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L12)

#### Description {#description-1}

Emoji tag to apply to the bookmark.

#### Inherited from {#inherited-from-2}

[`BookmarksAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments).[`emoji`](/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments#emoji)

* * *

### link? {#link}

```text
optional link: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L10)

#### Description {#description-2}

Link to bookmark.

#### Inherited from {#inherited-from-3}

[`BookmarksAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments).[`link`](/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments#link)

* * *

### title? {#title}

```text
optional title: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L8)

#### Description {#description-3}

Title for the bookmark.

#### Inherited from {#inherited-from-4}

[`BookmarksAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments).[`title`](/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments#title)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-5}

```text
TokenOverridable.token
```
