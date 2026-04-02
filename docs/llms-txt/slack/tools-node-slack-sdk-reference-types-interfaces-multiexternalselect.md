Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MultiExternalSelect

[@slack/types](/tools/node-slack-sdk/reference/types/) / MultiExternalSelect

# Interface: MultiExternalSelect

Defined in: [block-kit/block-elements.ts:539](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L539)

## Description {#description}

This menu will load its options from an external data source, allowing for a dynamic list of options.

## See {#see}

* [Multi-select menu of external data source reference](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#external_multi_select).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`MaxItemsSelectable`](/tools/node-slack-sdk/reference/types/interfaces/MaxItemsSelectable).[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable)

## Properties {#properties}

### action_id? {#action_id}

```
optional action_id: string;
```

Defined in: [block-kit/extensions.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L15)

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```
optional confirm: ConfirmationDialog;
```

Defined in: [block-kit/extensions.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L25)

#### Description {#description-1}

A [Confirm](/tools/node-slack-sdk/reference/types/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable#confirm)

* * *

### focus_on_load? {#focus_on_load}

```
optional focus_on_load: boolean;
```

Defined in: [block-kit/extensions.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L42)

#### Description {#description-2}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.

#### Inherited from {#inherited-from-2}

[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`focus_on_load`](/tools/node-slack-sdk/reference/types/interfaces/Focusable#focus_on_load)

* * *

### initial_options? {#initial_options}

```
optional initial_options: PlainTextOption[];
```

Defined in: [block-kit/block-elements.ts:548](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L548)

#### Description {#description-3}

An array of options to be selected when the menu initially loads.

* * *

### max_selected_items? {#max_selected_items}

```
optional max_selected_items: number;
```

Defined in: [block-kit/extensions.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L49)

#### Description {#description-4}

Specifies the maximum number of items that can be selected. Minimum number is 1.

#### Inherited from {#inherited-from-3}

[`MaxItemsSelectable`](/tools/node-slack-sdk/reference/types/interfaces/MaxItemsSelectable).[`max_selected_items`](/tools/node-slack-sdk/reference/types/interfaces/MaxItemsSelectable#max_selected_items)

* * *

### min_query_length? {#min_query_length}

```
optional min_query_length: number;
```

Defined in: [block-kit/block-elements.ts:554](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L554)

#### Description {#description-5}

When the typeahead field is used, a request will be sent on every character change. If you prefer fewer requests or more fully ideated queries, use the `min_query_length` attribute to tell Slack the fewest number of typed characters required before dispatch. The default value is `3`.

* * *

### placeholder? {#placeholder}

```
optional placeholder: PlainTextElement;
```

Defined in: [block-kit/extensions.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L57)

#### Description {#description-6}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-4}

[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable#placeholder)

* * *

### type {#type}

```
type: "multi_external_select";
```

Defined in: [block-kit/block-elements.ts:543](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L543)

#### Description {#description-7}

The type of element. In this case `type` is always `multi_external_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
