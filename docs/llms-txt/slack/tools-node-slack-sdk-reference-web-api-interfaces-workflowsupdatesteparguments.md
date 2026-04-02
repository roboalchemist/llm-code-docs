Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowsUpdateStepArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowsUpdateStepArguments

# Interface: WorkflowsUpdateStepArguments

Defined in: [packages/web-api/src/types/request/workflows.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L67)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### inputs? {#inputs}

```text
optional inputs: object;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:71](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L71)

#### Index Signature {#index-signature}

```text
[name: string]: object
```text

* * *

### outputs? {#outputs}

```text
optional outputs: object[];
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:82](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L82)

#### label {#label}

```text
label: string;
```text

#### name {#name}

```text
name: string;
```text

#### type {#type}

```text
type: string;
```text

* * *

### step_image_url? {#step_image_url}

```text
optional step_image_url: string;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:69](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L69)

* * *

### step_name? {#step_name}

```text
optional step_name: string;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:70](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L70)

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

### workflow_step_edit_id {#workflow_step_edit_id}

```text
workflow_step_edit_id: string;
```text

Defined in: [packages/web-api/src/types/request/workflows.ts:68](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/workflows.ts#L68)
