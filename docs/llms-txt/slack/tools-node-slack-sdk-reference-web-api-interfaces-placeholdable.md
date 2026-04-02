Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Placeholdable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Placeholdable

# Interface: Placeholdable

Defined in: packages/types/dist/block-kit/extensions.d.ts:44

## Extended by {#extended-by}

* [`Datepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/Datepicker)
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
* [`Timepicker`](/tools/node-slack-sdk/reference/web-api/interfaces/Timepicker)
* [`URLInput`](/tools/node-slack-sdk/reference/web-api/interfaces/URLInput)
* [`RichTextInput`](/tools/node-slack-sdk/reference/web-api/interfaces/RichTextInput)

## Properties {#properties}

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:49

#### Description {#description}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) object that defines the placeholder text shown on the element. Maximum length for the `text` field in this object is 150 characters.
