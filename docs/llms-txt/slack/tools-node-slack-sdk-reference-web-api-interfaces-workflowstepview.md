Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowStepView

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowStepView

# Interface: WorkflowStepView

Defined in: packages/types/dist/views.d.ts:61

[modal](https://docs.slack.dev/legacy/legacy-steps-from-appsConfiguration) for [legacy Workflow Steps from Apps](https://docs.slack.dev/legacy/legacy-steps-from-apps).

## Deprecated {#deprecated}

Steps from Apps are deprecated and will no longer be executed starting September 12, 2024. For more information, see our [deprecation announcement](https://docs.slack.dev/changelog/2023-08-workflow-steps-from-apps-step-back).

## Extends {#extends}

* `BaseView`

## Properties {#properties}

### blocks {#blocks}

```text
blocks: AnyBlock[];
```text

Defined in: packages/types/dist/views.d.ts:5

#### Description {#description}

An array of [AnyBlock](/tools/node-slack-sdk/reference/web-api/type-aliases/AnyBlock) that defines the content of the view. Max of 100 blocks.

#### Inherited from {#inherited-from}

```text
BaseView.blocks
```text

* * *

### callback_id? {#callback_id}

```text
optional callback_id: string;
```text

Defined in: packages/types/dist/views.d.ts:18

#### Description {#description-1}

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Maximum length of 255 characters.

#### See {#see}

[Handling and responding to interactions](https://docs.slack.dev/surfaces/modals#interactions).

#### Inherited from {#inherited-from-1}

```text
BaseView.callback_id
```text

* * *

### external_id? {#external_id}

```text
optional external_id: string;
```text

Defined in: packages/types/dist/views.d.ts:20

#### Description {#description-2}

A custom identifier that must be unique for all views on a per-team basis.

#### Inherited from {#inherited-from-2}

```text
BaseView.external_id
```text

* * *

### private_metadata? {#private_metadata}

```text
optional private_metadata: string;
```text

Defined in: packages/types/dist/views.d.ts:12

#### Description {#description-3}

String that will be sent to your app in [\`view\_submission\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) and [\`block\_actions\`](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload) events. Maximum length of 3000 characters.

#### Inherited from {#inherited-from-3}

```text
BaseView.private_metadata
```text

* * *

### submit_disabled? {#submit_disabled}

```text
optional submit_disabled: boolean;
```text

Defined in: packages/types/dist/views.d.ts:67

#### Description {#description-4}

When set to `true`, disables the submit button until the user has completed one or more inputs. Defaults to `false`.

* * *

### type {#type}

```text
type: "workflow_step";
```text

Defined in: packages/types/dist/views.d.ts:62
