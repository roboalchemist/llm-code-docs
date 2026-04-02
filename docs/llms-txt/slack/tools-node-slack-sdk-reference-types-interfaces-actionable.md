Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Actionable

[@slack/types](/tools/node-slack-sdk/reference/types/) / Actionable

# Interface: Actionable

Defined in: [block-kit/extensions.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L18)

## Deprecated {#deprecated}

[Action](/tools/node-slack-sdk/reference/types/interfaces/Action) aliased to Actionable in order to name the mixins in this file consistently.

## Extends {#extends}

* [`Action`](/tools/node-slack-sdk/reference/types/interfaces/Action)

## Extended by {#extended-by}

* [`Button`](/tools/node-slack-sdk/reference/types/interfaces/Button)
* [`Checkboxes`](/tools/node-slack-sdk/reference/types/interfaces/Checkboxes)
* [`Datepicker`](/tools/node-slack-sdk/reference/types/interfaces/Datepicker)
* [`DateTimepicker`](/tools/node-slack-sdk/reference/types/interfaces/DateTimepicker)
* [`EmailInput`](/tools/node-slack-sdk/reference/types/interfaces/EmailInput)
* [`FeedbackButtons`](/tools/node-slack-sdk/reference/types/interfaces/FeedbackButtons)
* [`FileInput`](/tools/node-slack-sdk/reference/types/interfaces/FileInput)
* [`IconButton`](/tools/node-slack-sdk/reference/types/interfaces/IconButton)
* [`UsersSelect`](/tools/node-slack-sdk/reference/types/interfaces/UsersSelect)
* [`MultiUsersSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiUsersSelect)
* [`StaticSelect`](/tools/node-slack-sdk/reference/types/interfaces/StaticSelect)
* [`MultiStaticSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiStaticSelect)
* [`ConversationsSelect`](/tools/node-slack-sdk/reference/types/interfaces/ConversationsSelect)
* [`MultiConversationsSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiConversationsSelect)
* [`ChannelsSelect`](/tools/node-slack-sdk/reference/types/interfaces/ChannelsSelect)
* [`MultiChannelsSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiChannelsSelect)
* [`ExternalSelect`](/tools/node-slack-sdk/reference/types/interfaces/ExternalSelect)
* [`MultiExternalSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiExternalSelect)
* [`NumberInput`](/tools/node-slack-sdk/reference/types/interfaces/NumberInput)
* [`Overflow`](/tools/node-slack-sdk/reference/types/interfaces/Overflow)
* [`PlainTextInput`](/tools/node-slack-sdk/reference/types/interfaces/PlainTextInput)
* [`RadioButtons`](/tools/node-slack-sdk/reference/types/interfaces/RadioButtons)
* [`Timepicker`](/tools/node-slack-sdk/reference/types/interfaces/Timepicker)
* [`URLInput`](/tools/node-slack-sdk/reference/types/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/types/interfaces/RichTextInput)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: [block-kit/extensions.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L15)

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Action`](/tools/node-slack-sdk/reference/types/interfaces/Action).[`action_id`](/tools/node-slack-sdk/reference/types/interfaces/Action#action_id)

* * *

### type {#type}

```text
type: string;
```

Defined in: [block-kit/extensions.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L9)

#### Inherited from {#inherited-from-1}

[`Action`](/tools/node-slack-sdk/reference/types/interfaces/Action).[`type`](/tools/node-slack-sdk/reference/types/interfaces/Action#type)
