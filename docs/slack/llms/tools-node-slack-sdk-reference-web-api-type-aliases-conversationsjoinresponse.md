Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsJoinResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsJoinResponse

# Type Alias: ConversationsJoinResponse

```typescript
type ConversationsJoinResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ConversationsJoinResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ConversationsJoinResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel? {#channel}

```typescript
optional channel: Channel;
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

### warning? {#warning}

```typescript
optional warning: string;
```
