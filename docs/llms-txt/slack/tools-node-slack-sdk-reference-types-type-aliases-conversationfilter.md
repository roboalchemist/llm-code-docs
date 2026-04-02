Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/type-aliases/ConversationFilter

[@slack/types](/tools/node-slack-sdk/reference/types/) / ConversationFilter

# Type Alias: ConversationFilter

```
type ConversationFilter =   | BaseConversationFilter & Required<Pick<BaseConversationFilter, "include">>  | BaseConversationFilter & Required<Pick<BaseConversationFilter, "exclude_bot_users">>| BaseConversationFilter & Required<Pick<BaseConversationFilter, "exclude_external_shared_channels">>;
```

Defined in: [block-kit/composition-objects.ts:214](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L214)

## Description {#description}

Defines a filter for the list of options in a conversation selector menu. The menu can be either a conversations select menu or a conversations multi-select menu.

## See {#see}

[Conversation filter object reference](https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object).
