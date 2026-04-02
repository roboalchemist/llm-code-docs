Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersInfoArguments

# Interface: UsersInfoArguments

Defined in: [packages/web-api/src/types/request/users.ts:37](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L37)

## Extends {#extends}

* `TokenOverridable`.`LocaleAware`

## Properties {#properties}

### include_locale? {#include_locale}

```text
optional include_locale: boolean;
```text

Defined in: [packages/web-api/src/types/request/common.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L51)

#### Description {#description}

Set this to `true` to receive the locale with the response.

#### Inherited from {#inherited-from}

```text
LocaleAware.include_locale
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```text

* * *

### user {#user}

```text
user: string;
```text

Defined in: [packages/web-api/src/types/request/users.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L39)

#### Description {#description-2}

User to get info on.
