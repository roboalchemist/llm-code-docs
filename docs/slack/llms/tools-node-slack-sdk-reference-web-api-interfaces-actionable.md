Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Actionable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Actionable

# Interface: Actionable

Defined in: packages/types/dist/block-kit/extensions.d.ts:14

## Deprecated {#deprecated}

[Action](/tools/node-slack-sdk/reference/web-api/interfaces/Action) aliased to Actionable in order to name the mixins in this file consistently.

## Extends {#extends}

* [`Action`](/tools/node-slack-sdk/reference/web-api/interfaces/Action)

## Extended by {#extended-by}

* [`Button`](/tools/node-slack-sdk/reference/web-api/interfaces/Button)
* [`Checkboxes`](/tools/node-slack-sdk/reference/web-api/interfaces/Checkboxes)
* [`Datepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/Datepicker)
* [`DateTimepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/DateTimepicker)
* [`EmailInput`](/tools/node-slack-sdk/reference/web-api/interfaces/EmailInput)
* [`FeedbackButtons`](/tools/node-slack-sdk/reference/web-api/interfaces/FeedbackButtons)
* [`FileInput`](/tools/node-slack-sdk/reference/web-api/interfaces/FileInput)
* [`IconButton`](/tools/node-slack-sdk/reference/web-api/interfaces/IconButton)
* [`UsersSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/UsersSelect)
* [`MultiUsersSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiUsersSelect)
* [`StaticSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/StaticSelect)
* [`MultiStaticSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiStaticSelect)
* [`ConversationsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsSelect)
* [`MultiConversationsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiConversationsSelect)
* [`ChannelsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/ChannelsSelect)
* [`MultiChannelsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiChannelsSelect)
* [`ExternalSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/ExternalSelect)
* [`MultiExternalSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiExternalSelect)
* [`NumberInput`](/tools/node-slack-sdk/reference/web-api/interfaces/NumberInput)
* [`Overflow`](/tools/node-slack-sdk/reference/web-api/interfaces/Overflow)
* [`PlainTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextInput)
* [`RadioButtons`](/tools/node-slack-sdk/reference/web-api/interfaces/RadioButtons)
* [`Timepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/Timepicker)
* [`URLInput`](/tools/node-slack-sdk/reference/web-api/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextInput)

## Properties {#properties}

### action_id? {#action_id}

```
optional action_id: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Action`](/tools/node-slack-sdk/reference/web-api/interfaces/Action).[`action_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Action#action_id)

* * *

### type {#type}

```
type: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:6

#### Inherited from {#inherited-from-1}

[`Action`](/tools/node-slack-sdk/reference/web-api/interfaces/Action).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Action#type)
