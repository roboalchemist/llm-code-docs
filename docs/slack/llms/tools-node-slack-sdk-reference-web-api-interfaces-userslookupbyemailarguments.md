Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersLookupByEmailArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersLookupByEmailArguments

# Interface: UsersLookupByEmailArguments

Defined in: [packages/web-api/src/types/request/users.ts:48](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L48)

## Extends {#extends}

* `Email`.`TokenOverridable`

## Properties {#properties}

### email {#email}

```text
email: string;
```text

Defined in: [packages/web-api/src/types/request/users.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L7)

#### Description {#description}

An email address belonging to a user in the workspace

#### Inherited from {#inherited-from}

```text
Email.email
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
