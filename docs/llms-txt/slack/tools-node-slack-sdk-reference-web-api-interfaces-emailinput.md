Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/EmailInput

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EmailInput

# Interface: EmailInput

Defined in: packages/types/dist/block-kit/block-elements.d.ts:106

## Description {#description}

Allows user to enter an email into a single-line field.

## See {#see}

* [Email input element reference](https://docs.slack.dev/reference/block-kit/block-elements/email-input-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Dispatchable`](/tools/node-slack-sdk/reference/web-api/interfaces/Dispatchable).[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable)

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

### dispatch_action_config? {#dispatch_action_config}

```text
optional dispatch_action_config: DispatchActionConfig;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:28

#### Description {#description-1}

A [DispatchActionConfig](/tools/node-slack-sdk/reference/web-api/interfaces/DispatchActionConfig) object that determines when during text input the element returns a [\`block\_actions\` payload](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload).

#### Inherited from {#inherited-from-1}

[`Dispatchable`](/tools/node-slack-sdk/reference/web-api/interfaces/Dispatchable).[`dispatch_action_config`](/tools/node-slack-sdk/reference/web-api/interfaces/Dispatchable#dispatch_action_config)

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

### initial_value? {#initial_value}

```text
optional initial_value: string;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:114

#### Description {#description-3}

The initial value in the email input when it is loaded.

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:49

#### Description {#description-4}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-3}

[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable#placeholder)

* * *

### type {#type}

```text
type: "email_text_input";
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:110

#### Description {#description-5}

The type of element. In this case `type` is always `email_text_input`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
