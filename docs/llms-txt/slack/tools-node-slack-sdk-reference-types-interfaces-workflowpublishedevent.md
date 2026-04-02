Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/WorkflowPublishedEvent

[@slack/types](/tools/node-slack-sdk/reference/types/) / WorkflowPublishedEvent

# Interface: WorkflowPublishedEvent

Defined in: [events/steps-from-apps.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L15)

## Properties {#properties}

### event_ts {#event_ts}

```
event_ts: string;
```

Defined in: [events/steps-from-apps.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L26)

* * *

### type {#type}

```
type: "workflow_published";
```

Defined in: [events/steps-from-apps.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L16)

* * *

### workflow_id {#workflow_id}

```
workflow_id: string;
```

Defined in: [events/steps-from-apps.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L17)

* * *

### workflow_published_configuration {#workflow_published_configuration}

```
workflow_published_configuration: object;
```

Defined in: [events/steps-from-apps.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/events/steps-from-apps.ts#L18)

#### app_steps {#app_steps}

```
app_steps: object[];
```

#### version_id {#version_id}

```
version_id: string;
```
