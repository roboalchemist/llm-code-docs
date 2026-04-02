Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsLookupArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsLookupArguments

# Interface: AdminConversationsLookupArguments

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:122](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L122)

## Extends {#extends}

* `TeamIDs`.`TokenOverridable`.`CursorPaginationEnabled`

## Properties {#properties}

### cursor? {#cursor}

```
optional cursor: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L16)

#### Description {#description}

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.

#### See {#see}

[pagination](https://docs.slack.dev/apis/web-api/pagination) for more detail.

#### Inherited from {#inherited-from}

```
CursorPaginationEnabled.cursor
```

* * *

### last_message_activity_before {#last_message_activity_before}

```
last_message_activity_before: number;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:127](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L127)

#### Description {#description-1}

UNIX timestamp to filter by public channels where the most recent message was sent before this parameter.

* * *

### limit? {#limit}

```
optional limit: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L9)

#### Description {#description-2}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-1}

```
CursorPaginationEnabled.limit
```

* * *

### max_member_count? {#max_member_count}

```
optional max_member_count: number;
```

Defined in: [packages/web-api/src/types/request/admin/conversations.ts:129](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/conversations.ts#L129)

#### Description {#description-3}

Filter by public channels with member count equal to or less than the specified number.

* * *

### team_ids {#team_ids}

```
team_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:65](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L65)

#### Description {#description-4}

A list of team IDs (must include at least one ID).

#### Inherited from {#inherited-from-2}

```
TeamIDs.team_ids
```

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-5}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```
TokenOverridable.token
```
