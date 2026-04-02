Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Overflow

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Overflow

# Interface: Overflow

Defined in: packages/types/dist/block-kit/block-elements.d.ts:519

## Description {#description}

Allows users to press a button to view a list of options. Unlike the select menu, there is no typeahead field, and the button always appears with an ellipsis ('…') rather than customizable text. As such, it is usually used if you want a more compact layout than a select menu, or to supply a list of less visually important actions after a row of buttons. You can also specify simple URL links as overflow menu options, instead of actions.

## See {#see}

* [Overflow menu element reference](https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable)

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

### options {#options}

```text
options: PlainTextOption[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:527

#### Description {#description-2}

An array of up to 5 [PlainTextOption](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextOption) to display in the menu.

* * *

### type {#type}

```text
type: "overflow";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:523

#### Description {#description-3}

The type of element. In this case `type` is always `number_input`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
