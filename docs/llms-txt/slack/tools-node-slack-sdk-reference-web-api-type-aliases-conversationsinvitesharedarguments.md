Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsInviteSharedArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsInviteSharedArguments

# Type Alias: ConversationsInviteSharedArguments

```typescript
type ConversationsInviteSharedArguments = Channel & TokenOverridable & Emails | UserIDs & object;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:118](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L118)

## Type Declaration {#type-declaration}

### external_limited? {#external_limited}

```typescript
optional external_limited: boolean;
```

#### Description {#description}

Whether invite is to an external limited member. Defaults to `true`.
