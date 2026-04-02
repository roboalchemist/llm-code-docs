Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/DateTimepicker

[@slack/types](/tools/node-slack-sdk/reference/types/) / DateTimepicker

# Interface: DateTimepicker

Defined in: [block-kit/block-elements.ts:112](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L112)

## Description {#description}

Allows users to select both a date and a time of day, formatted as a Unix timestamp. On desktop clients, this time picker will take the form of a dropdown list and the date picker will take the form of a dropdown calendar. Both options will have free-text entry for precise choices. On mobile clients, the time picker and date picker will use native UIs.

## See {#see}

* [Datetime picker element reference](https://docs.slack.dev/reference/block-kit/block-elements/datetime-picker-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable)

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

### initial_date_time? {#initial_date_time}

```text
optional initial_date_time: number;
```

Defined in: [block-kit/block-elements.ts:122](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L122)

#### Description {#description-3}

The initial date and time that is selected when the element is loaded, represented as a UNIX timestamp in seconds. This should be in the format of 10 digits, for example `1628633820` represents the date and time August 10th, 2021 at 03:17pm PST.

* * *

### type {#type}

```text
type: "datetimepicker";
```

Defined in: [block-kit/block-elements.ts:116](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L116)

#### Description {#description-4}

The type of element. In this case `type` is always `datetimepicker`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
