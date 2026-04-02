Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersProfileGetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersProfileGetArguments

# Interface: UsersProfileGetArguments

Defined in: [packages/web-api/src/types/request/users.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L66)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### include_labels? {#include_labels}

```text
optional include_labels: boolean;
```text

Defined in: [packages/web-api/src/types/request/users.ts:71](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L71)

#### Description {#description}

Include labels for each ID in custom profile fields. Using this parameter will heavily rate-limit your requests and is not recommended. Defaults to `false`.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text

* * *

### user? {#user}

```text
optional user: string;
```text

Defined in: [packages/web-api/src/types/request/users.ts:73](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L73)

#### Description {#description-2}

User to retrieve profile info for.
