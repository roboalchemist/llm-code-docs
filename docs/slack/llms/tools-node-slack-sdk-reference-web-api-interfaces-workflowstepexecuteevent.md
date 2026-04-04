Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowStepExecuteEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowStepExecuteEvent

# Interface: WorkflowStepExecuteEvent

Defined in: packages/types/dist/events/steps-from-apps.d.ts:61

## Properties {#properties}

### callback_id {#callback_id}

```text
callback_id: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:63

* * *

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:80

* * *

### type {#type}

```text
type: "workflow_step_execute";
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:62

* * *

### workflow_step {#workflow_step}

```text
workflow_step: object;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:64

#### inputs {#inputs}

```text
inputs: object;
```text

##### Index Signature {#index-signature}

```text
[key: string]: object
```text

#### outputs {#outputs}

```text
outputs: object[];
```text

#### step_id {#step_id}

```text
step_id: string;
```text

#### workflow_id {#workflow_id}

```text
workflow_id: string;
```text

#### workflow_instance_id {#workflow_instance_id}

```text
workflow_instance_id: string;
```text

#### workflow_step_execute_id {#workflow_step_execute_id}

```text
workflow_step_execute_id: string;
```text
