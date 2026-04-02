Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminInviteRequestsListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminInviteRequestsListArguments

# Interface: AdminInviteRequestsListArguments

Defined in: [packages/web-api/src/types/request/admin/inviteRequests.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/inviteRequests.ts#L33)

## Extends {#extends}

* `Required`<`OptionalTeamAssignable`\>.`TokenOverridable`.`CursorPaginationEnabled`

## Properties {#properties}

### cursor? {#cursor}

```text
optional cursor: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L16)

#### Description {#description}

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

#### Description {#description-1}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-1}

```text
CursorPaginationEnabled.limit
```

* * *

### team_id {#team_id}

```text
team_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-2}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-2}

[`AdminUsergroupsAddChannelsArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsAddChannelsArguments).[`team_id`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsergroupsAddChannelsArguments#team_id)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```text
TokenOverridable.token
```
