Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/RadioButtons

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RadioButtons

# Interface: RadioButtons

Defined in: packages/types/dist/block-kit/block-elements.d.ts:564

## Description {#description}

Allows users to choose one item from a list of possible options.

## See {#see}

* [Radio button group element reference](https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:21

#### Description {#description-1}

A [Confirm](/tools/node-slack-sdk/reference/web-api/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable#confirm)

* * *

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:36

#### Description {#description-2}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.

#### Inherited from {#inherited-from-2}

[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`focus_on_load`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable#focus_on_load)

* * *

### initial_option? {#initial_option}

```text
optional initial_option: Option;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:573

#### Description {#description-3}

An [Option](/tools/node-slack-sdk/reference/web-api/type-aliases/Option) object that exactly matches one of the options within `options`. This option will be selected when the radio button group initially loads.

* * *

### options {#options}

```text
options: Option[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:577

#### Description {#description-4}

An array of [Option](/tools/node-slack-sdk/reference/web-api/type-aliases/Option) objects. A maximum of 10 options are allowed.

* * *

### type {#type}

```text
type: "radio_buttons";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:568

#### Description {#description-5}

The type of element. In this case `type` is always `radio_buttons`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
