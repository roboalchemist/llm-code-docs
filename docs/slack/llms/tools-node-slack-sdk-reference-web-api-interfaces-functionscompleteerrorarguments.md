Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FunctionsCompleteErrorArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FunctionsCompleteErrorArguments

# Interface: FunctionsCompleteErrorArguments

Defined in: [packages/web-api/src/types/request/functions.ts:8](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/functions.ts#L8)

## Extends {#extends}

* `ExecutionID`.`TokenOverridable`

## Properties {#properties}

### error {#error}

```text
error: string;
```text

Defined in: [packages/web-api/src/types/request/functions.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/functions.ts#L9)

* * *

### function_execution_id {#function_execution_id}

```text
function_execution_id: string;
```text

Defined in: [packages/web-api/src/types/request/functions.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/functions.ts#L4)

#### Inherited from {#inherited-from}

```text
ExecutionID.function_execution_id
```text

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```text
