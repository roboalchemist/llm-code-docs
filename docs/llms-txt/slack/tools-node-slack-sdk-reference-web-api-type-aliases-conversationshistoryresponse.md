Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsHistoryResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsHistoryResponse

# Type Alias: ConversationsHistoryResponse

```typescript
type ConversationsHistoryResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ConversationsHistoryResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ConversationsHistoryResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel_actions_count? {#channel_actions_count}

```typescript
optional channel_actions_count: number;
```

### channel_actions_ts? {#channel_actions_ts}

```typescript
optional channel_actions_ts: number;
```

### error? {#error}

```typescript
optional error: string;
```

### has_more? {#has_more}

```typescript
optional has_more: boolean;
```

### latest? {#latest}

```typescript
optional latest: string;
```

### messages? {#messages}

```typescript
optional messages: MessageElement[];
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### oldest? {#oldest}

```typescript
optional oldest: string;
```

### pin_count? {#pin_count}

```typescript
optional pin_count: number;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```
