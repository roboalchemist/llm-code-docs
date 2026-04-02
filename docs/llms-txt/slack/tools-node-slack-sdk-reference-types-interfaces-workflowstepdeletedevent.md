Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/WorkflowStepDeletedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / WorkflowStepDeletedEvent

# Interface: WorkflowStepDeletedEvent

Defined in: [events/steps-from-apps.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L43)

## Properties {#properties}

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/steps-from-apps.ts:62](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L62)

* * *

### type {#type}

```
type: "workflow_step_deleted";
```

Defined in: [events/steps-from-apps.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L44)

* * *

### workflow_draft_configuration {#workflow_draft_configuration}

```
workflow_draft_configuration: object;
```

Defined in: [events/steps-from-apps.ts:46](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L46)

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

Defined in: [events/steps-from-apps.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L45)

* * *

### workflow_published_configuration? {#workflow_published_configuration}

```
optional workflow_published_configuration: object;
```

Defined in: [events/steps-from-apps.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L54)

#### app_steps {#app_steps-1}

```
app_steps: object[];
```

#### version_id {#version_id-1}

```
version_id: string;
```
