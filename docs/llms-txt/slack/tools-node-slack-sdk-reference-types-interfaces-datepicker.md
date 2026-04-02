Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Datepicker

[@slack/types](/tools/node-slack-sdk/reference/types/) / Datepicker

# Interface: Datepicker

Defined in: [block-kit/block-elements.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L92)

## Description {#description}

Allows users to select a date from a calendar style UI.

## See {#see}

* [Date picker element reference](https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: [block-kit/extensions.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L15)

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```

Defined in: [block-kit/extensions.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L25)

#### Description {#description-1}

A [Confirm](/tools/node-slack-sdk/reference/types/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable#confirm)

* * *

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```

Defined in: [block-kit/extensions.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L42)

#### Description {#description-2}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.

#### Inherited from {#inherited-from-2}

[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`focus_on_load`](/tools/node-slack-sdk/reference/types/interfaces/Focusable#focus_on_load)

* * *

### initial_date? {#initial_date}

```text
optional initial_date: string;
```

Defined in: [block-kit/block-elements.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L101)

#### Description {#description-3}

The initial date that is selected when the element is loaded. This should be in the format `YYYY-MM-DD`.

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```

Defined in: [block-kit/extensions.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L57)

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-3}

[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable#placeholder)

* * *

### type {#type}

```text
type: "datepicker";
```

Defined in: [block-kit/block-elements.ts:96](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L96)

#### Description {#description-5}

The type of element. In this case `type` is always `datepicker`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
