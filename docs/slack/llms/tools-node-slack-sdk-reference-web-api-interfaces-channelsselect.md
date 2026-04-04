Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ChannelsSelect

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChannelsSelect

# Interface: ChannelsSelect

Defined in: packages/types/dist/block-kit/block-elements.d.ts:412

## Description {#description}

This select menu will populate its options with a list of public channels visible to the current user in the active workspace.

## See {#see}

* [Select menu of public channels reference](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element#channels_select).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`Confirmable`](/tools/node-slack-sdk/reference/web-api/interfaces/Confirmable).[`Focusable`](/tools/node-slack-sdk/reference/web-api/interfaces/Focusable).[`Placeholdable`](/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable).[`URLRespondable`](/tools/node-slack-sdk/reference/web-api/interfaces/URLRespondable)

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

### initial_channel? {#initial_channel}

```text
optional initial_channel: string;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:420

#### Description {#description-3}

The ID of any valid public channel to be pre-selected when the menu loads.

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

### response_url_enabled? {#response_url_enabled}

```text
optional response_url_enabled: boolean;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:58

#### Description {#description-5}

When set to `true`, the [\`view\_submission\` payload](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) from the menu's parent view will contain a `response_url`. This `response_url` can be used for [message responses](https://docs.slack.dev/interactivity/handling-user-interaction#message_responses). The target conversation for the message will be determined by the value of this select menu.

#### Inherited from {#inherited-from-4}

[`URLRespondable`](/tools/node-slack-sdk/reference/web-api/interfaces/URLRespondable).[`response_url_enabled`](/tools/node-slack-sdk/reference/web-api/interfaces/URLRespondable#response_url_enabled)

* * *

### type {#type}

```text
type: "channels_select";
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:416

#### Description {#description-6}

The type of element. In this case `type` is always `channels_select`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
