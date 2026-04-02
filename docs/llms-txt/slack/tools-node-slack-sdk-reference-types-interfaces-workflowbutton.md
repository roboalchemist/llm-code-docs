Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/WorkflowButton

[@slack/types](/tools/node-slack-sdk/reference/types/) / WorkflowButton

# Interface: WorkflowButton

Defined in: [block-kit/block-elements.ts:731](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L731)

## Description {#description}

Allows users to run a [link trigger](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-link-triggers/#workflow_buttons) with customizable inputs.

## See {#see}

[Workflow button element reference](https://docs.slack.dev/reference/block-kit/block-elements/workflow-button-element).

## Extends {#extends}

* [`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable)

## Properties {#properties}

### accessibility_label? {#accessibility_label}

```
optional accessibility_label: string;
```

Defined in: [block-kit/block-elements.ts:785](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L785)

#### Description {#description-1}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

* * *

### confirm? {#confirm}

```
optional confirm: ConfirmationDialog;
```

Defined in: [block-kit/extensions.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L25)

#### Description {#description-2}

A [Confirm](/tools/node-slack-sdk/reference/types/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from}

[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable#confirm)

* * *

### style? {#style}

```
optional style: ColorScheme;
```

Defined in: [block-kit/block-elements.ts:780](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L780)

#### Description {#description-3}

Decorates buttons with alternative visual color schemes. Use this option with restraint. `primary` gives buttons a green outline and text, ideal for affirmation or confirmation actions. `primary` should only be used for one button within a set. `danger` gives buttons a red outline and text, and should be used when the action is destructive. Use `danger` even more sparingly than primary. If you don't include this field, the default button style will be used.

* * *

### text {#text}

```
text: PlainTextElement;
```

Defined in: [block-kit/block-elements.ts:740](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L740)

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) that defines the button's text. `text` may truncate with ~30 characters. Maximum length for the `text` in this field is 75 characters.

* * *

### type {#type}

```
type: "workflow_button";
```

Defined in: [block-kit/block-elements.ts:735](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L735)

#### Description {#description-5}

The type of element. In this case `type` is always `workflow_button`.

* * *

### workflow {#workflow}

```
workflow: object;
```

Defined in: [block-kit/block-elements.ts:744](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L744)

#### trigger {#trigger}

```
trigger: object;
```

##### Description {#description-6}

Properties of the [link trigger](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-link-triggers/#workflow_buttons) that will be invoked via this button.

##### trigger.customizable_input_parameters? {#triggercustomizable_input_parameters}

```
optional customizable_input_parameters: object[];
```

###### Description {#description-7}

List of customizable input parameters and their values. Should match input parameters specified on the provided trigger.

##### trigger.url {#triggerurl}

```
url: string;
```

###### Description {#description-8}

The trigger URL of the [link trigger](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-link-triggers/#workflow_buttons)

#### Description {#description-9}

A workflow object that contains details about the workflow that will run when the button is clicked.
