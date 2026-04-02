Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FilesListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesListArguments

# Interface: FilesListArguments

Defined in: [packages/web-api/src/types/request/files.ts:104](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L104)

## Extends {#extends}

* `TokenOverridable`.`TraditionalPagingEnabled`.`OptionalTeamAssignable`

## Properties {#properties}

### channel? {#channel}

```text
optional channel: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:106](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L106)

#### Description {#description}

Filter files appearing in a specific channel, indicated by its ID.

* * *

### count? {#count}

```text
optional count: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L33)

#### Description {#description-1}

Number of items to return per page. Defaults to `20`

#### Inherited from {#inherited-from}

```text
TraditionalPagingEnabled.count
```

* * *

### page? {#page}

```text
optional page: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:35](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L35)

#### Description {#description-2}

Page number of results to return. Defaults to `1`.

#### Inherited from {#inherited-from-1}

```text
TraditionalPagingEnabled.page
```

* * *

### show_files_hidden_by_limit? {#show_files_hidden_by_limit}

```text
optional show_files_hidden_by_limit: boolean;
```

Defined in: [packages/web-api/src/types/request/files.ts:111](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L111)

#### Description {#description-3}

Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-4}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-2}

```text
OptionalTeamAssignable.team_id
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-5}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```text
TokenOverridable.token
```

* * *

### ts_from? {#ts_from}

```text
optional ts_from: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:113](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L113)

#### Description {#description-6}

Filter files created after this timestamp (inclusive).

* * *

### ts_to? {#ts_to}

```text
optional ts_to: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L115)

#### Description {#description-7}

Filter files created before this timestamp (inclusive).

* * *

### types? {#types}

```text
optional types: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:121](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L121)

#### Description {#description-8}

Filter files by type. Pass multiple values for `types` argument by comma-seperating the values. The default value is `all`, which does not filter the list. Available types are `all`, `spaces`, `snippets`, `images`, `gdocs`, `zips` and `pdfs`.

* * *

### user? {#user}

```text
optional user: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:123](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L123)

#### Description {#description-9}

Filter files created by a single user.
