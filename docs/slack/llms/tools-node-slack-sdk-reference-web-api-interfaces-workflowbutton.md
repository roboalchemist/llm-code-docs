Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WorkflowButton

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WorkflowButton

# Interface: WorkflowButton

Defined in: packages/types/dist/block-kit/block-elements.d.ts:640

## Description {#description}

Allows users to run a [link trigger](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-link-triggers/#workflow_buttons) with customizable inputs.

## See {#see}

[Workflow button element reference](https://docs.slack.dev/reference/block-kit/block-elements/workflow-button-element).

## Extends {#extends}

* [`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable)

## Properties {#properties}

### accessibility_label? {#accessibility_label}

```text
optional accessibility_label: string;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:694

#### Description {#description-1}

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button `text` object. Maximum length for this field is 75 characters.

* * *

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:21

#### Description {#description-2}

A [Confirm](/tools/node-slack-sdk/reference/web-api/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from}

[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable#confirm)

* * *

### style? {#style}

```text
optional style: ColorScheme;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:689

#### Description {#description-3}

Decorates buttons with alternative visual color schemes. Use this option with restraint. `primary` gives buttons a green outline and text, ideal for affirmation or confirmation actions. `primary` should only be used for one button within a set. `danger` gives buttons a red outline and text, and should be used when the action is destructive. Use `danger` even more sparingly than primary. If you don't include this field, the default button style will be used.

* * *

### text {#text}

```text
text: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:649

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) that defines the button's text. `text` may truncate with ~30 characters. Maximum length for the `text` in this field is 75 characters.

* * *

### type {#type}

```text
type: "workflow_button";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:644

#### Description {#description-5}

The type of element. In this case `type` is always `workflow_button`.

* * *

### workflow {#workflow}

```text
workflow: object;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:653

#### trigger {#trigger}

```text
trigger: object;
```text

##### Description {#description-6}

Properties of the [link trigger](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-link-triggers/#workflow_buttons) that will be invoked via this button.

##### trigger.customizable_input_parameters? {#triggercustomizable_input_parameters}

```text
optional customizable_input_parameters: object[];
```text

###### Description {#description-7}

List of customizable input parameters and their values. Should match input parameters specified on the provided trigger.

##### trigger.url {#triggerurl}

```text
url: string;
```text

###### Description {#description-8}

The trigger URL of the [link trigger](https://docs.slack.dev/tools/deno-slack-sdk/guides/creating-link-triggers/#workflow_buttons)

#### Description {#description-9}

A workflow object that contains details about the workflow that will run when the button is clicked.
