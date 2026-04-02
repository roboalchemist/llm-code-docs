Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ExternalSelect

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ExternalSelect

# Interface: ExternalSelect

Defined in: packages/types/dist/block-kit/block-elements.d.ts:444

## Description {#description}

This select menu will load its options from an external data source, allowing for a dynamic list of options.

## See {#see}

* [Select menu of external data source reference](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#external_select).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#action_id)

* * *

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:21

#### Description {#description-1}

A [Confirm](/tools/node-slack-sdk/reference/web-api/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.

#### Inherited from {#inherited-from-1}

[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`confirm`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable#confirm)

* * *

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:36

#### Description {#description-2}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.

#### Inherited from {#inherited-from-2}

[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`focus_on_load`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable#focus_on_load)

* * *

### initial_option? {#initial_option}

```text
optional initial_option: PlainTextOption;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:452

#### Description {#description-3}

A single option to be selected when the menu initially loads.

* * *

### min_query_length? {#min_query_length}

```text
optional min_query_length: number;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:458

#### Description {#description-4}

When the typeahead field is used, a request will be sent on every character change. If you prefer fewer requests or more fully ideated queries, use the `min_query_length` attribute to tell Slack the fewest number of typed characters required before dispatch. The default value is `3`.

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:49

#### Description {#description-5}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-3}

[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable#placeholder)

* * *

### type {#type}

```text
type: "external_select";
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:448

#### Description {#description-6}

The type of element. In this case `type` is always `external_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
