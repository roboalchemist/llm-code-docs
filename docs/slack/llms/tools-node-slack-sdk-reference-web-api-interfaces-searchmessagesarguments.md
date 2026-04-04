Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/SearchMessagesArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SearchMessagesArguments

# Interface: SearchMessagesArguments

Defined in: [packages/web-api/src/types/request/search.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/search.ts#L30)

## Extends {#extends}

* `TokenOverridable`.`TraditionalPagingEnabled`.`Searchable`.`SearchMessagesCursorPagination`

## Properties {#properties}

### count? {#count}

```text
optional count: number;
```text

Defined in: [packages/web-api/src/types/request/common.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L33)

#### Description {#description}

Number of items to return per page. Defaults to `20`

#### Inherited from {#inherited-from}

```text
TraditionalPagingEnabled.count
```text

* * *

### cursor? {#cursor}

```text
optional cursor: string;
```text

Defined in: [packages/web-api/src/types/request/search.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/search.ts#L22)

#### Description {#description-1}

Paginate through collections of data by setting the `cursor` parameter to `*` for the first "page" or a `next_cursor` attribute returned by a previous request's `response_metadata`. Use the `count` parameter to set the number of items to return per page rather than `limit`.

#### See {#see}

[pagination](https://docs.slack.dev/apis/web-api/pagination) for more detail.

#### Inherited from {#inherited-from-1}

```text
SearchMessagesCursorPagination.cursor
```text

* * *

### highlight? {#highlight}

```text
optional highlight: boolean;
```text

Defined in: [packages/web-api/src/types/request/search.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/search.ts#L10)

#### Description {#description-2}

Set to `true` to enable query highlight markers. Defaults to `false`.

#### See {#see-1}

[\`search.messages\` Usage info](https://docs.slack.dev/reference/methods/search.messages) for details.

#### Inherited from {#inherited-from-2}

```text
Searchable.highlight
```text

* * *

### page? {#page}

```text
optional page: number;
```text

Defined in: [packages/web-api/src/types/request/common.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L35)

#### Description {#description-3}

Page number of results to return. Defaults to `1`.

#### Inherited from {#inherited-from-3}

```text
TraditionalPagingEnabled.page
```text

* * *

### query {#query}

```text
query: string;
```text

Defined in: [packages/web-api/src/types/request/search.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/search.ts#L5)

#### Description {#description-4}

Search query.

#### Inherited from {#inherited-from-4}

```text
Searchable.query
```text

* * *

### sort? {#sort}

```text
optional sort: "score" | "timestamp";
```text

Defined in: [packages/web-api/src/types/request/search.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/search.ts#L12)

#### Description {#description-5}

Return matches sorted by either `score` or `timestamp`. Defaults to `score`.

#### Inherited from {#inherited-from-5}

```text
Searchable.sort
```text

* * *

### sort_dir? {#sort_dir}

```text
optional sort_dir: "asc" | "desc";
```text

Defined in: [packages/web-api/src/types/request/common.ts:130](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L130)

#### Description {#description-6}

Change sort direction to ascending (`asc`) or descending (`desc`). Defaults to `desc`.

#### Inherited from {#inherited-from-6}

```text
Searchable.sort_dir
```text

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-7}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-7}

```text
Searchable.team_id
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-8}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-8}

```text
TokenOverridable.token
```text
