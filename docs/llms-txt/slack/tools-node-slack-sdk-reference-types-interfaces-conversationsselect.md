Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ConversationsSelect

[@slack/types](/tools/node-slack-sdk/reference/types/) / ConversationsSelect

# Interface: ConversationsSelect

Defined in: [block-kit/block-elements.ts:409](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L409)

## Description {#description}

This select menu will populate its options with a list of public and private channels, DMs, and MPIMs visible to the current user in the active workspace.

## See {#see}

* [Select menu of conversations reference](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#conversations_select).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable).[`URLRespondable`](/tools/node-slack-sdk/reference/types/interfaces/URLRespondable)

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

### default_to_current_conversation? {#default_to_current_conversation}

```text
optional default_to_current_conversation: boolean;
```

Defined in: [block-kit/block-elements.ts:423](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L423)

#### Description {#description-2}

Pre-populates the select menu with the conversation that the user was viewing when they opened the modal, if available. Default is `false`.

* * *

### filter? {#filter}

```text
optional filter: object;
```

Defined in: [block-kit/block-elements.ts:427](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L427)

#### exclude_bot_users? {#exclude_bot_users}

```text
optional exclude_bot_users: boolean;
```

#### exclude_external_shared_channels? {#exclude_external_shared_channels}

```text
optional exclude_external_shared_channels: boolean;
```

#### include? {#include}

```text
optional include: ("im" | "mpim" | "private" | "public")[];
```

#### Description {#description-3}

A filter object that reduces the list of available conversations using the specified criteria.

* * *

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```

Defined in: [block-kit/extensions.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L42)

#### Description {#description-4}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.

#### Inherited from {#inherited-from-2}

[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`focus_on_load`](/tools/node-slack-sdk/reference/types/interfaces/Focusable#focus_on_load)

* * *

### initial_conversation? {#initial_conversation}

```text
optional initial_conversation: string;
```

Defined in: [block-kit/block-elements.ts:418](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L418)

#### Description {#description-5}

The ID of any valid conversation to be pre-selected when the menu loads. If `default_to_current_conversation` is also supplied, `initial_conversation` will take precedence.

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```

Defined in: [block-kit/extensions.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L57)

#### Description {#description-6}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.

#### Inherited from {#inherited-from-3}

[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable).[`placeholder`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable#placeholder)

* * *

### response_url_enabled? {#response_url_enabled}

```text
optional response_url_enabled: boolean;
```

Defined in: [block-kit/extensions.ts:67](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L67)

#### Description {#description-7}

When set to `true`, the [\`view\_submission\` payload](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) from the menu's parent view will contain a `response_url`. This `response_url` can be used for [message responses](https://docs.slack.dev/interactivity/handling-user-interaction#message_responses). The target conversation for the message will be determined by the value of this select menu.

#### Inherited from {#inherited-from-4}

[`URLRespondable`](/tools/node-slack-sdk/reference/types/interfaces/URLRespondable).[`response_url_enabled`](/tools/node-slack-sdk/reference/types/interfaces/URLRespondable#response_url_enabled)

* * *

### type {#type}

```text
type: "conversations_select";
```

Defined in: [block-kit/block-elements.ts:413](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L413)

#### Description {#description-8}

The type of element. In this case `type` is always `conversations_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
