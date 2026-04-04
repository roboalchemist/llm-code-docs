Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/WorkflowDeletedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / WorkflowDeletedEvent

# Interface: WorkflowDeletedEvent

Defined in: [events/steps-from-apps.ts:1](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L1)

## Properties {#properties}

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/steps-from-apps.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L12)

* * *

### type {#type}

```
type: "workflow_deleted";
```

Defined in: [events/steps-from-apps.ts:2](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L2)

* * *

### workflow_draft_configuration {#workflow_draft_configuration}

```
workflow_draft_configuration: object;
```

Defined in: [events/steps-from-apps.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L4)

#### app_steps {#app_steps}

```
app_steps: object[];
```

#### version_id {#version_id}

```
version_id: string;
```

* * *

### workflow_id {#workflow_id}

```
workflow_id: string;
```

Defined in: [events/steps-from-apps.ts:3](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L3)
