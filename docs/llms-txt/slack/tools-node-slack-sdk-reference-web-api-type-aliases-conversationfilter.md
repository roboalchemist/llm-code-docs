Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationFilter

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationFilter

# Type Alias: ConversationFilter

```typescript
type ConversationFilter =   | BaseConversationFilter & Required<Pick<BaseConversationFilter, "include">>  | BaseConversationFilter & Required<Pick<BaseConversationFilter, "exclude_bot_users">>| BaseConversationFilter & Required<Pick<BaseConversationFilter, "exclude_external_shared_channels">>;
```

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:197

## Description {#description}

Defines a filter for the list of options in a conversation selector menu. The menu can be either a conversations select menu or a conversations multi-select menu.

## See {#see}

[Conversation filter object reference](https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object).
