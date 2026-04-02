Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/UsersSelect

[@slack/types](/tools/node-slack-sdk/reference/types/) / UsersSelect

# Interface: UsersSelect

Defined in: [block-kit/block-elements.ts:301](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L301)

## Description {#description}

This select menu will populate its options with a list of Slack users visible to the current user in the active workspace.

## See {#see}

* [Select menu of users reference](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#users_select).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/types/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/types/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/types/interfaces/Placeholdable)

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

### initial_user? {#initial_user}

```
optional initial_user: string;
```

Defined in: [block-kit/block-elements.ts:309](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L309)

#### Description {#description-3}

The user ID of any valid user to be pre-selected when the menu loads.

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
type: "users_select";
```

Defined in: [block-kit/block-elements.ts:305](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L305)

#### Description {#description-5}

The type of element. In this case `type` is always `users_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/types/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Actionable#type)
