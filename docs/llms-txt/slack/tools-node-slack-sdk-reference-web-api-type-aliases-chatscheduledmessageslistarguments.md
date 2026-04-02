Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatScheduledMessagesListArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatScheduledMessagesListArguments

# Type Alias: ChatScheduledMessagesListArguments

```typescript
type ChatScheduledMessagesListArguments = OptionalArgument<TokenOverridable & CursorPaginationEnabled & OptionalTeamAssignable & Pick<TimelinePaginationEnabled, "latest" | "oldest"> & Partial<Channel>>;
```

Defined in: [packages/web-api/src/types/request/chat.ts:234](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/chat.ts#L234)
