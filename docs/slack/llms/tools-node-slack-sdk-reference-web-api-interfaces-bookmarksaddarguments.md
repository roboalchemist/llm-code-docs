Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/BookmarksAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / BookmarksAddArguments

# Interface: BookmarksAddArguments

Defined in: [packages/web-api/src/types/request/bookmarks.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L16)

## Extends {#extends}

* `ChannelID`.`BookmarkFields`.`TokenOverridable`

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

### emoji? {#emoji}

```text
optional emoji: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L12)

#### Description {#description-1}

Emoji tag to apply to the bookmark.

#### Inherited from {#inherited-from-1}

```text
BookmarkFields.emoji
```

* * *

### entity_id? {#entity_id}

```text
optional entity_id: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L20)

#### Description {#description-2}

ID of the entity being bookmarked. Only applies to message and file types.

* * *

### link {#link}

```text
link: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L10)

#### Description {#description-3}

Link to bookmark.

#### Inherited from {#inherited-from-2}

```text
BookmarkFields.link
```

* * *

### parent_id? {#parent_id}

```text
optional parent_id: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L22)

#### Description {#description-4}

ID of this bookmark's parent.

* * *

### title {#title}

```text
title: string;
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L8)

#### Description {#description-5}

Title for the bookmark.

#### Inherited from {#inherited-from-3}

```text
BookmarkFields.title
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-6}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

```text
TokenOverridable.token
```

* * *

### type {#type}

```text
type: "link";
```

Defined in: [packages/web-api/src/types/request/bookmarks.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/bookmarks.ts#L18)

#### Description {#description-7}

Type of the bookmark. Only `link` is supported at the moment.
