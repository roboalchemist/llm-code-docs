Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminEmojiListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminEmojiListResponse

# Type Alias: AdminEmojiListResponse

```typescript
type AdminEmojiListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminEmojiListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminEmojiListResponse.ts#L11)

## Type Declaration {#type-declaration}

### emoji? {#emoji}

```typescript
optional emoji: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: Emoji
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
