Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowsStepCompletedArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowsStepCompletedArguments

# Interface: WorkflowsStepCompletedArguments

Defined in: [packages/web-api/src/types/request/workflows.ts:55](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L55)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### outputs? {#outputs}

```text
optional outputs: Record<string, unknown>;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L57)

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

Defined in: [packages/web-api/src/types/request/workflows.ts:56](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L56)
