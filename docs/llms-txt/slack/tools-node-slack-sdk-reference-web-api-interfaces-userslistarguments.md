Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersListArguments

# Interface: UsersListArguments

Defined in: [packages/web-api/src/types/request/users.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L42)

## Extends {#extends}

* `TokenOverridable`.`CursorPaginationEnabled`.`LocaleAware`.`OptionalTeamAssignable`

## Properties {#properties}

### cursor? {#cursor}

```text
optional cursor: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L16)

#### Description {#description}

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.

#### See {#see}

[pagination](https://docs.slack.dev/apis/web-api/pagination) for more detail.

#### Inherited from {#inherited-from}

```text
CursorPaginationEnabled.cursor
```text

* * *

### include_locale? {#include_locale}

```text
optional include_locale: boolean;
```text

Defined in: [packages/web-api/src/types/request/common.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L51)

#### Description {#description-1}

Set this to `true` to receive the locale with the response.

#### Inherited from {#inherited-from-1}

```text
LocaleAware.include_locale
```text

* * *

### limit? {#limit}

```text
optional limit: number;
```text

Defined in: [packages/web-api/src/types/request/common.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L9)

#### Description {#description-2}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-2}

```text
CursorPaginationEnabled.limit
```text

* * *

### team_id? {#team_id}

```text
optional team_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L70)

#### Description {#description-3}

If using an org token, `team_id` is required.

#### Inherited from {#inherited-from-3}

```text
OptionalTeamAssignable.team_id
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

```text
TokenOverridable.token
```text
