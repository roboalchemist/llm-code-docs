Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsListResponse

# Type Alias: ConversationsListResponse

```typescript
type ConversationsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ConversationsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ConversationsListResponse.ts#L11)

## Type Declaration {#type-declaration}

### channels? {#channels}

```typescript
optional channels: Channel[];
```

### error? {#error}

```typescript
optional error: string;
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
