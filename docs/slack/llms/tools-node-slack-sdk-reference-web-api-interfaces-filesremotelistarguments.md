Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FilesRemoteListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesRemoteListArguments

# Interface: FilesRemoteListArguments

Defined in: [packages/web-api/src/types/request/files.ts:221](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L221)

## Extends {#extends}

* `TokenOverridable`.`CursorPaginationEnabled`

## Properties {#properties}

### channel? {#channel}

```text
optional channel: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:223](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L223)

#### Description {#description}

Filter files appearing in a specific channel, indicated by its ID.

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

#### Inherited from {#inherited-from}

```text
CursorPaginationEnabled.cursor
```

* * *

### limit? {#limit}

```text
optional limit: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L9)

#### Description {#description-2}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-1}

```text
CursorPaginationEnabled.limit
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```

* * *

### ts_from? {#ts_from}

```text
optional ts_from: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:225](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L225)

#### Description {#description-4}

Filter files created after this timestamp (inclusive).

* * *

### ts_to? {#ts_to}

```text
optional ts_to: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:227](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L227)

#### Description {#description-5}

Filter files created before this timestamp (inclusive).
