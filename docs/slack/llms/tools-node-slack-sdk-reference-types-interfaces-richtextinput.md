Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/RichTextInput

[@slack/types](/tools/node-slack-sdk/reference/types/) / RichTextInput

# Interface: RichTextInput

Defined in: [block-kit/block-elements.ts:1060](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1060)

## Description {#description}

A rich text input creates a composer/WYSIWYG editor for entering formatted text, offering nearly the same experience you have writing messages in Slack.

## See {#see}

* [Rich-text input element reference](https://docs.slack.dev/reference/block-kit/block-elements/rich-text-input-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Dispatchable`](/tools/node-slack-sdk/reference/types/interfaces/Dispatchable).[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable)

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

### dispatch_action_config? {#dispatch_action_config}

```
optional dispatch_action_config: DispatchActionConfig;
```

Defined in: [block-kit/extensions.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L33)

#### Description {#description-1}

A [DispatchActionConfig](/tools/node-slack-sdk/reference/types/interfaces/DispatchActionConfig) object that determines when during text input the element returns a [\`block\_actions\` payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload).

#### Inherited from {#inherited-from-1}

[`Dispatchable`](/tools/node-slack-sdk/reference/types/interfaces/Dispatchable).[`dispatch_action_config`](/tools/node-slack-sdk/reference/types/interfaces/Dispatchable#dispatch_action_config)

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

### initial_value? {#initial_value}

```
optional initial_value: RichTextBlock;
```

Defined in: [block-kit/block-elements.ts:1068](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1068)

#### Description {#description-3}

Initial contents of the input when it is loaded.

* * *

### placeholder? {#placeholder}

```
optional placeholder: PlainTextElement;
```

Defined in: [block-kit/extensions.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L57)

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-3}

[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable#placeholder)

* * *

### type {#type}

```
type: "rich_text_input";
```

Defined in: [block-kit/block-elements.ts:1064](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L1064)

#### Description {#description-5}

The type of element. In this case `type` is always `rich_text_input`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
