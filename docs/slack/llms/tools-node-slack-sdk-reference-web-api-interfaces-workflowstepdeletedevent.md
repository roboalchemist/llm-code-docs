Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowStepDeletedEvent

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowStepDeletedEvent

# Interface: WorkflowStepDeletedEvent

Defined in: packages/types/dist/events/steps-from-apps.d.ts:40

## Properties {#properties}

### event_ts {#event_ts}

```text
event_ts: string;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:59

* * *

### type {#type}

```text
type: "workflow_step_deleted";
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:41

* * *

### workflow_draft_configuration {#workflow_draft_configuration}

```text
workflow_draft_configuration: object;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:43

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

Defined in: packages/types/dist/events/steps-from-apps.d.ts:42

* * *

### workflow_published_configuration? {#workflow_published_configuration}

```text
optional workflow_published_configuration: object;
```text

Defined in: packages/types/dist/events/steps-from-apps.d.ts:51

#### app_steps {#app_steps-1}

```text
app_steps: object[];
```text

#### version_id {#version_id-1}

```text
version_id: string;
```text
