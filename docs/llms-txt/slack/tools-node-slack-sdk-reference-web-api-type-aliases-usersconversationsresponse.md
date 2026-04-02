Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/UsersConversationsResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersConversationsResponse

# Type Alias: UsersConversationsResponse

```typescript
type UsersConversationsResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/UsersConversationsResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/UsersConversationsResponse.ts#L11)

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
