Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/WorkflowStepView

[@slack/types](/tools/node-slack-sdk/reference/types/) / WorkflowStepView

# Interface: WorkflowStepView

Defined in: [views.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L67)

[modal](https://docs.slack.dev/legacy/legacy-steps-from-appsConfiguration) for [legacy Workflow Steps from Apps](https://docs.slack.dev/legacy/legacy-steps-from-apps).

## Deprecated {#deprecated}

Steps from Apps are deprecated and will no longer be executed starting September 12, 2024. For more information, see our [deprecation announcement](https://docs.slack.dev/changelog/2023-08-workflow-steps-from-apps-step-back).

## Extends {#extends}

* `BaseView`

## Properties {#properties}

### blocks {#blocks}

```
blocks: AnyBlock[];
```

Defined in: [views.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L6)

#### Description {#description}

An array of [AnyBlock](/tools/node-slack-sdk/reference/types/type-aliases/AnyBlock) that defines the content of the view. Max of 100 blocks.

#### Inherited from {#inherited-from}

```
BaseView.blocks
```

* * *

### callback_id? {#callback_id}

```
optional callback_id: string;
```

Defined in: [views.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L19)

#### Description {#description-1}

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Maximum length of 255 characters.

#### See {#see}

[Handling and responding to interactions](https://docs.slack.dev/surfaces/modals#interactions).

#### Inherited from {#inherited-from-1}

```
BaseView.callback_id
```

* * *

### external_id? {#external_id}

```
optional external_id: string;
```

Defined in: [views.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L21)

#### Description {#description-2}

A custom identifier that must be unique for all views on a per-team basis.

#### Inherited from {#inherited-from-2}

```
BaseView.external_id
```

* * *

### private_metadata? {#private_metadata}

```
optional private_metadata: string;
```

Defined in: [views.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L13)

#### Description {#description-3}

String that will be sent to your app in [\`view\_submission\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) and [\`block\_actions\`](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload) events. Maximum length of 3000 characters.

#### Inherited from {#inherited-from-3}

```
BaseView.private_metadata
```

* * *

### submit_disabled? {#submit_disabled}

```
optional submit_disabled: boolean;
```

Defined in: [views.ts:73](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L73)

#### Description {#description-4}

When set to `true`, disables the submit button until the user has completed one or more inputs. Defaults to `false`.

* * *

### type {#type}

```
type: "workflow_step";
```

Defined in: [views.ts:68](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L68)
