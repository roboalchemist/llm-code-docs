Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Focusable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Focusable

# Interface: Focusable

Defined in: packages/types/dist/block-kit/extensions.d.ts:30

## Extended by {#extended-by}

* [`Checkboxes`](/tools/node-slack-sdk/reference/web-api/interfaces/Checkboxes)
* [`Datepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/Datepicker)
* [`DateTimepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/DateTimepicker)
* [`EmailInput`](/tools/node-slack-sdk/reference/web-api/interfaces/EmailInput)
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
* [`PlainTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextInput)
* [`RadioButtons`](/tools/node-slack-sdk/reference/web-api/interfaces/RadioButtons)
* [`Timepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/Timepicker)
* [`URLInput`](/tools/node-slack-sdk/reference/web-api/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextInput)

## Properties {#properties}

### focus_on_load? {#focus_on_load}

```text
optional focus_on_load: boolean;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:36

#### Description {#description}

Indicates whether the element will be set to auto focus within the [\`view\` object](https://docs.slack.dev/surfaces/modals). Only one element can be set to `true`. Defaults to `false`.
