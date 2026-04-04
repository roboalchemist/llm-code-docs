Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MaxItemsSelectable

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MaxItemsSelectable

# Interface: MaxItemsSelectable

Defined in: packages/types/dist/block-kit/extensions.d.ts:38

## Extended by {#extended-by}

* [`MultiUsersSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiUsersSelect)
* [`MultiStaticSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiStaticSelect)
* [`MultiConversationsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiConversationsSelect)
* [`MultiChannelsSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiChannelsSelect)
* [`MultiExternalSelect`](/tools/node-slack-sdk/reference/web-api/interfaces/MultiExternalSelect)

## Properties {#properties}

### max_selected_items? {#max_selected_items}

```text
optional max_selected_items: number;
```text

Defined in: packages/types/dist/block-kit/extensions.d.ts:42

#### Description {#description}

Specifies the maximum number of items that can be selected. Minimum number is 1.
