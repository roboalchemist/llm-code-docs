Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MultiStaticSelect

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MultiStaticSelect

# Interface: MultiStaticSelect

Defined in: packages/types/dist/block-kit/block-elements.d.ts:322

## Description {#description}

This is the simplest form of select menu, with a static list of options passed in when defining the element.

## See {#see}

* [Multi-select menu of static options reference](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#static_multi_select).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`MaxItemsSelectable`](/tools/node-slack-sdk/reference/web-api/interfaces/MaxItemsSelectable).[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable)

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

### initial_options? {#initial_options}

```text
optional initial_options: PlainTextOption[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:331

#### Description {#description-3}

An array of option objects that exactly match one or more of the options within `options` or `option_groups`. These options will be selected when the menu initially loads.

* * *

### max_selected_items? {#max_selected_items}

```text
optional max_selected_items: number;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:42

#### Description {#description-4}

Specifies the maximum number of items that can be selected. Minimum number is 1.

#### Inherited from {#inherited-from-3}

[`MaxItemsSelectable`](/tools/node-slack-sdk/reference/web-api/interfaces/MaxItemsSelectable).[`max_selected_items`](/tools/node-slack-sdk/reference/web-api/interfaces/MaxItemsSelectable#max_selected_items)

* * *

### option_groups? {#option_groups}

```text
optional option_groups: object[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:341

#### label {#label}

```text
label: PlainTextElement;
```text

#### options {#options}

```text
options: PlainTextOption[];
```text

#### Description {#description-5}

An array of option group objects. Maximum number of option groups is 100. If `options` is specified, this field should not be.

* * *

### options? {#options-1}

```text
optional options: PlainTextOption[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:336

#### Description {#description-6}

An array of [PlainTextOption](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextOption). Maximum number of options is 100. If `option_groups` is specified, this field should not be.

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:49

#### Description {#description-7}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-4}

[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable#placeholder)

* * *

### type {#type}

```text
type: "multi_static_select";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:326

#### Description {#description-8}

The type of element. In this case `type` is always `multi_static_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
