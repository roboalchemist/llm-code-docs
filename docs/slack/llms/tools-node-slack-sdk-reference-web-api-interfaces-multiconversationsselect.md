Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MultiConversationsSelect

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MultiConversationsSelect

# Interface: MultiConversationsSelect

Defined in: packages/types/dist/block-kit/block-elements.d.ts:382

## Description {#description}

This multi-select menu will populate its options with a list of public and private channels, DMs, and MPIMs visible to the current user in the active workspace.

## See {#see}

* [Multi-select menu of conversations reference](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element#conversation_multi_select).
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

### default_to_current_conversation? {#default_to_current_conversation}

```text
optional default_to_current_conversation: boolean;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:396

#### Description {#description-2}

Pre-populates the select menu with the conversation that the user was viewing when they opened the modal, if available. Default is `false`.

* * *

### filter? {#filter}

```text
optional filter: object;
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:400

#### exclude_bot_users? {#exclude_bot_users}

```text
optional exclude_bot_users: boolean;
```text

#### exclude_external_shared_channels? {#exclude_external_shared_channels}

```text
optional exclude_external_shared_channels: boolean;
```text

#### include? {#include}

```text
optional include: ("im" | "mpim" | "private" | "public")[];
```text

#### Description {#description-3}

A filter object that reduces the list of available conversations using the specified criteria.

* * *

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:36

#### Description {#description-4}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.

#### Inherited from {#inherited-from-2}

[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`focus_on_load`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable#focus_on_load)

* * *

### initial_conversations? {#initial_conversations}

```text
optional initial_conversations: string[];
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:391

#### Description {#description-5}

An array of one or more IDs of any valid conversations to be pre-selected when the menu loads. If `default_to_current_conversation` is also supplied, `initial_conversation` will be ignored.

* * *

### max_selected_items? {#max_selected_items}

```text
optional max_selected_items: number;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:42

#### Description {#description-6}

Specifies the maximum number of items that can be selected. Minimum number is 1.

#### Inherited from {#inherited-from-3}

[`MaxItemsSelectable`](/tools/node-slack-sdk/reference/web-api/interfaces/MaxItemsSelectable).[`max_selected_items`](/tools/node-slack-sdk/reference/web-api/interfaces/MaxItemsSelectable#max_selected_items)

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
type: "multi_conversations_select";
```text

Defined in: packages/types/dist/block-kit/block-elements.d.ts:386

#### Description {#description-8}

The type of element. In this case `type` is always `conversations_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
