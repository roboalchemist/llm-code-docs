Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Placeholdable

[@slack/types](/tools/node-slack-sdk/reference/types/) / Placeholdable

# Interface: Placeholdable

Defined in: [block-kit/extensions.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L52)

## Extended by {#extended-by}

* [`Datepicker`](/tools/node-slack-sdk/reference/types/interfaces/Datepicker)
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
* [`Timepicker`](/tools/node-slack-sdk/reference/types/interfaces/Timepicker)
* [`URLInput`](/tools/node-slack-sdk/reference/types/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/types/interfaces/RichTextInput)

## Properties {#properties}

### placeholder? {#placeholder}

```
optional placeholder: PlainTextElement;
```

Defined in: [block-kit/extensions.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L57)

#### Description {#description}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.
