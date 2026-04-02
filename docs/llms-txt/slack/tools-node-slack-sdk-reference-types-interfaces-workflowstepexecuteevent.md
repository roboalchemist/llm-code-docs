Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/WorkflowStepExecuteEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / WorkflowStepExecuteEvent

# Interface: WorkflowStepExecuteEvent

Defined in: [events/steps-from-apps.ts:65](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L65)

## Properties {#properties}

### callback_id {#callback_id}

```
callback_id: string;
```

Defined in: [events/steps-from-apps.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L67)

* * *

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/steps-from-apps.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L85)

* * *

### type {#type}

```
type: "workflow_step_execute";
```

Defined in: [events/steps-from-apps.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L66)

* * *

### workflow_step {#workflow_step}

```
workflow_step: object;
```

Defined in: [events/steps-from-apps.ts:68](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L68)

#### inputs {#inputs}

```
inputs: object;
```

##### Index Signature {#index-signature}

```
[key: string]: object
```

#### outputs {#outputs}

```
outputs: object[];
```

#### step_id {#step_id}

```
step_id: string;
```

#### workflow_id {#workflow_id}

```
workflow_id: string;
```

#### workflow_instance_id {#workflow_instance_id}

```
workflow_instance_id: string;
```

#### workflow_step_execute_id {#workflow_step_execute_id}

```
workflow_step_execute_id: string;
```
