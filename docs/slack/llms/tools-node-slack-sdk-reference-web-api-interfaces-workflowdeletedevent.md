Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowDeletedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowDeletedEvent

# Interface: WorkflowDeletedEvent

Defined in: packages/types/dist/events/steps-from-apps.d.ts:1

## Properties {#properties}

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:12

* * *

### type {#type}

```text
type: "workflow_deleted";
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:2

* * *

### workflow_draft_configuration {#workflow_draft_configuration}

```text
workflow_draft_configuration: object;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:4

#### app_steps {#app_steps}

```text
app_steps: object[];
```text

#### version_id {#version_id}

```text
version_id: string;
```text

* * *

### workflow_id {#workflow_id}

```text
workflow_id: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:3
