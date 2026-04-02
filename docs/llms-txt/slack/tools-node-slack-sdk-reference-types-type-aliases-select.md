Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/type-aliases/Select

[@slack/types](/tools/node-slack-sdk/reference/types/) / Select

# Type Alias: Select

```
type Select =   | UsersSelect  | StaticSelect  | ConversationsSelect  | ChannelsSelect  | ExternalSelect;
```

Defined in: [block-kit/block-elements.ts:276](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L276)

## Description {#description}

Allows users to choose an option from a drop down menu. The select menu also includes type-ahead functionality, where a user can type a part or all of an option string to filter the list. There are different types of select menu elements that depend on different data sources for their lists of options: [StaticSelect](/tools/node-slack-sdk/reference/types/interfaces/StaticSelect), [ExternalSelect](/tools/node-slack-sdk/reference/types/interfaces/ExternalSelect), [UsersSelect](/tools/node-slack-sdk/reference/types/interfaces/UsersSelect), [ConversationsSelect](/tools/node-slack-sdk/reference/types/interfaces/ConversationsSelect), [ChannelsSelect](/tools/node-slack-sdk/reference/types/interfaces/ChannelsSelect).

## See {#see}

* [Select menu element reference](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element).
* [This is an interactive component - see our guide to enabling interactivity](https://docs.slack.dev/interactivity/handling-user-interaction).
