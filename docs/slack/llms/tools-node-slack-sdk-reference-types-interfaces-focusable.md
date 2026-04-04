Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Focusable

[@slack/types](/tools/node-slack-sdk/reference/types/) / Focusable

# Interface: Focusable

Defined in: [block-kit/extensions.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L36)

## Extended by {#extended-by}

* [`Checkboxes`](/tools/node-slack-sdk/reference/types/interfaces/Checkboxes)
* [`Datepicker`](/tools/node-slack-sdk/reference/types/interfaces/Datepicker)
* [`DateTimepicker`](/tools/node-slack-sdk/reference/types/interfaces/DateTimepicker)
* [`EmailInput`](/tools/node-slack-sdk/reference/types/interfaces/EmailInput)
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
* [`PlainTextInput`](/tools/node-slack-sdk/reference/types/interfaces/PlainTextInput)
* [`RadioButtons`](/tools/node-slack-sdk/reference/types/interfaces/RadioButtons)
* [`Timepicker`](/tools/node-slack-sdk/reference/types/interfaces/Timepicker)
* [`URLInput`](/tools/node-slack-sdk/reference/types/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/types/interfaces/RichTextInput)

## Properties {#properties}

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```

Defined in: [block-kit/extensions.ts:42](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L42)

#### Description {#description}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.
