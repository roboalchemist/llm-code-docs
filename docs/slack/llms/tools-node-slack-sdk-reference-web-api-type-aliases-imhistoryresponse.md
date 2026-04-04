Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ImHistoryResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ImHistoryResponse

# Type Alias: ImHistoryResponse

```typescript
type ImHistoryResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ImHistoryResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ImHistoryResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel_actions_count? {#channel_actions_count}

```typescript
optional channel_actions_count: number;
```

### error? {#error}

```typescript
optional error: string;
```

### has_more? {#has_more}

```typescript
optional has_more: boolean;
```

### messages? {#messages}

```typescript
optional messages: Message[];
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

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### warning? {#warning}

```typescript
optional warning: string;
```
