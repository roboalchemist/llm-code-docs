Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsHistoryArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsHistoryArguments

# Interface: ConversationsHistoryArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:93](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L93)

## Extends {#extends}

* `Channel`.`IncludeAllMetadata`.`TokenOverridable`.`CursorPaginationEnabled`.`TimelinePaginationEnabled`

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L15)

#### Description {#description}

ID of conversation.

#### Inherited from {#inherited-from}

```text
Channel.channel
```

* * *

### cursor? {#cursor}

```text
optional cursor: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L16)

#### Description {#description-1}

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.

#### See {#see}

[pagination](https://docs.slack.dev/apis/web-api/pagination) for more detail.

#### Inherited from {#inherited-from-1}

```text
CursorPaginationEnabled.cursor
```

* * *

### include_all_metadata? {#include_all_metadata}

```text
optional include_all_metadata: boolean;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L24)

#### Description {#description-2}

Return all metadata associated with messages. Defaults to `false`.

#### Inherited from {#inherited-from-2}

```text
IncludeAllMetadata.include_all_metadata
```

* * *

### inclusive? {#inclusive}

```text
optional inclusive: boolean;
```

Defined in: [packages/web-api/src/types/request/common.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L28)

#### Description {#description-3}

Include messages with `oldest` or `latest` timestamps in results. Ignored unless either timestamp is specified. Defaults to `false`.

#### Inherited from {#inherited-from-3}

```text
TimelinePaginationEnabled.inclusive
```

* * *

### latest? {#latest}

```text
optional latest: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:23](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L23)

#### Description {#description-4}

Only messages before this Unix timestamp will be included in results.

#### Inherited from {#inherited-from-4}

```text
TimelinePaginationEnabled.latest
```

* * *

### limit? {#limit}

```text
optional limit: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L9)

#### Description {#description-5}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-5}

```text
CursorPaginationEnabled.limit
```

* * *

### oldest? {#oldest}

```text
optional oldest: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L21)

#### Description {#description-6}

Only messages after this Unix timestamp will be included in results.

#### Inherited from {#inherited-from-6}

```text
TimelinePaginationEnabled.oldest
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-7}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-7}

```text
TokenOverridable.token
```
