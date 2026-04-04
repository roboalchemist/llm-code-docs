Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsInviteResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsInviteResponse

# Type Alias: ConversationsInviteResponse

```typescript
type ConversationsInviteResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ConversationsInviteResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ConversationsInviteResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel? {#channel}

```typescript
optional channel: Channel;
```

### error? {#error}

```typescript
optional error: string;
```

### errors? {#errors}

```typescript
optional errors: Error[];
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
