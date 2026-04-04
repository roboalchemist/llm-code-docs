Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminConversationsInviteResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsInviteResponse

# Type Alias: AdminConversationsInviteResponse

```typescript
type AdminConversationsInviteResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminConversationsInviteResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminConversationsInviteResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### failed_user_ids? {#failed_user_ids}

```typescript
optional failed_user_ids: FailedUserids;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### provided? {#provided}

```typescript
optional provided: string;
```
