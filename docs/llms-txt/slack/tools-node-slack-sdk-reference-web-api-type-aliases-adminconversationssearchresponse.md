Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminConversationsSearchResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsSearchResponse

# Type Alias: AdminConversationsSearchResponse

```typescript
type AdminConversationsSearchResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminConversationsSearchResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminConversationsSearchResponse.ts#L11)

## Type Declaration {#type-declaration}

### conversations? {#conversations}

```typescript
optional conversations: Conversation[];
```

### error? {#error}

```typescript
optional error: string;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### next_cursor? {#next_cursor}

```typescript
optional next_cursor: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### total_count? {#total_count}

```typescript
optional total_count: number;
```
