Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowsStepFailedArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowsStepFailedArguments

# Interface: WorkflowsStepFailedArguments

Defined in: [packages/web-api/src/types/request/workflows.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L60)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### error {#error}

```text
error: object;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:62](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L62)

#### message {#message}

```text
message: string;
```text

* * *

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

### workflow_step_execute_id {#workflow_step_execute_id}

```text
workflow_step_execute_id: string;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:61](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L61)
