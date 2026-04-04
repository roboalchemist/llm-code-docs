Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MaxItemsSelectable

[@slack/types](/tools/node-slack-sdk/reference/types/) / MaxItemsSelectable

# Interface: MaxItemsSelectable

Defined in: [block-kit/extensions.ts:45](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L45)

## Extended by {#extended-by}

* [`MultiUsersSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiUsersSelect)
* [`MultiStaticSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiStaticSelect)
* [`MultiConversationsSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiConversationsSelect)
* [`MultiChannelsSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiChannelsSelect)
* [`MultiExternalSelect`](/tools/node-slack-sdk/reference/types/interfaces/MultiExternalSelect)

## Properties {#properties}

### max_selected_items? {#max_selected_items}

```
optional max_selected_items: number;
```

Defined in: [block-kit/extensions.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/extensions.ts#L49)

#### Description {#description}

Specifies the maximum number of items that can be selected. Minimum number is 1.
