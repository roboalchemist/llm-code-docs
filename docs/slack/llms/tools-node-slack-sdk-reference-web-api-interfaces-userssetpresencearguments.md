Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersSetPresenceArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersSetPresenceArguments

# Interface: UsersSetPresenceArguments

Defined in: [packages/web-api/src/types/request/users.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L61)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### presence {#presence}

```text
presence: "auto" | "away";
```text

Defined in: [packages/web-api/src/types/request/users.ts:63](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L63)

#### Description {#description}

Either `auto` or `away`.

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
