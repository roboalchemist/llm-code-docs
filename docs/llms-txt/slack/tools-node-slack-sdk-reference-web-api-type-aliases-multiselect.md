Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/MultiSelect

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MultiSelect

# Type Alias: MultiSelect

```typescript
type MultiSelect =   | MultiUsersSelect  | MultiStaticSelect  | MultiConversationsSelect  | MultiChannelsSelect  | MultiExternalSelect;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:253

## Description {#description}

Allows users to select multiple items from a list of options. Just like regular [Select](/tools/node-slack-sdk/reference/web-api/type-aliases/Select), multi-select menus also include type-ahead functionality, where a user can type a part or all of an option string to filter the list. There are different types of multi-select menu that depend on different data sources for their lists of options: [MultiStaticSelect](/tools/node-slack-sdk/reference/web-api/interfaces/MultiStaticSelect), [MultiExternalSelect](/tools/node-slack-sdk/reference/web-api/interfaces/MultiExternalSelect), [MultiUsersSelect](/tools/node-slack-sdk/reference/web-api/interfaces/MultiUsersSelect), [MultiConversationsSelect](/tools/node-slack-sdk/reference/web-api/interfaces/MultiConversationsSelect), [MultiChannelsSelect](/tools/node-slack-sdk/reference/web-api/interfaces/MultiChannelsSelect).

## See {#see}

* [Multi-select menu element reference](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menus-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).
