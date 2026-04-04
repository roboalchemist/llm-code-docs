Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersGetPresenceArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersGetPresenceArguments

# Interface: UsersGetPresenceArguments

Defined in: [packages/web-api/src/types/request/users.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L30)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description}

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

Defined in: [packages/web-api/src/types/request/users.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L32)

#### Description {#description-1}

User to get presence info on. Defaults to the authed user.
