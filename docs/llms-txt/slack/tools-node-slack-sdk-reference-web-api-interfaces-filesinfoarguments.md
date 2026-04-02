Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FilesInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesInfoArguments

# Interface: FilesInfoArguments

Defined in: [packages/web-api/src/types/request/files.ts:98](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L98)

## Extends {#extends}

* `FileArgument`.`TokenOverridable`.`CursorPaginationEnabled`.`TraditionalPagingEnabled`

## Properties {#properties}

### count? {#count}

```text
optional count: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L33)

#### Description {#description}

Number of items to return per page. Defaults to `20`

#### Inherited from {#inherited-from}

```text
TraditionalPagingEnabled.count
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

### file {#file}

```text
file: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L14)

#### Description {#description-2}

Encoded file ID.

#### Inherited from {#inherited-from-2}

```text
FileArgument.file
```

* * *

### limit? {#limit}

```text
optional limit: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L9)

#### Description {#description-3}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-3}

```text
CursorPaginationEnabled.limit
```

* * *

### page? {#page}

```text
optional page: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L35)

#### Description {#description-4}

Page number of results to return. Defaults to `1`.

#### Inherited from {#inherited-from-4}

```text
TraditionalPagingEnabled.page
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-5}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-5}

```text
TokenOverridable.token
```
