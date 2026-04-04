Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/Confirmable

[@slack/types](/tools/node-slack-sdk/reference/types/) / Confirmable

# Interface: Confirmable

Defined in: [block-kit/extensions.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L20)

## Extended by {#extended-by}

* [`Button`](/tools/node-slack-sdk/reference/types/interfaces/Button)
* [`Checkboxes`](/tools/node-slack-sdk/reference/types/interfaces/Checkboxes)
* [`Datepicker`](/tools/node-slack-sdk/reference/types/interfaces/Datepicker)
* [`DateTimepicker`](/tools/node-slack-sdk/reference/types/interfaces/DateTimepicker)
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
* [`Overflow`](/tools/node-slack-sdk/reference/types/interfaces/Overflow)
* [`RadioButtons`](/tools/node-slack-sdk/reference/types/interfaces/RadioButtons)
* [`Timepicker`](/tools/node-slack-sdk/reference/types/interfaces/Timepicker)
* [`WorkflowButton`](/tools/node-slack-sdk/reference/types/interfaces/WorkflowButton)

## Properties {#properties}

### confirm? {#confirm}

```text
optional confirm: ConfirmationDialog;
```

Defined in: [block-kit/extensions.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L25)

#### Description {#description}

A [Confirm](/tools/node-slack-sdk/reference/types/interfaces/Confirm) object that defines an optional confirmation dialog after the element is interacted with.
