Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowPublishedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowPublishedEvent

# Interface: WorkflowPublishedEvent

Defined in: packages/types/dist/events/steps-from-apps.d.ts:14

## Properties {#properties}

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:25

* * *

### type {#type}

```text
type: "workflow_published";
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:15

* * *

### workflow_id {#workflow_id}

```text
workflow_id: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:16

* * *

### workflow_published_configuration {#workflow_published_configuration}

```text
workflow_published_configuration: object;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:17

#### app_steps {#app_steps}

```text
app_steps: object[];
```text

#### version_id {#version_id}

```text
version_id: string;
```text
