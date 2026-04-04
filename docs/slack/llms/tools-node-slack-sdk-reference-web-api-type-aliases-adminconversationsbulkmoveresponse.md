Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminConversationsBulkMoveResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsBulkMoveResponse

# Type Alias: AdminConversationsBulkMoveResponse

```typescript
type AdminConversationsBulkMoveResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminConversationsBulkMoveResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminConversationsBulkMoveResponse.ts#L11)

## Type Declaration {#type-declaration}

### bulk_action_id? {#bulk_action_id}

```typescript
optional bulk_action_id: string;
```

### error? {#error}

```typescript
optional error: string;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### not_added? {#not_added}

```typescript
optional not_added: NotAdded[];
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
