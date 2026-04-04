Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ConversationsMembersResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsMembersResponse

# Type Alias: ConversationsMembersResponse

```typescript
type ConversationsMembersResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ConversationsMembersResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ConversationsMembersResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### members? {#members}

```typescript
optional members: string[];
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
