Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/EmojiListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EmojiListResponse

# Type Alias: EmojiListResponse

```typescript
type EmojiListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/EmojiListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/EmojiListResponse.ts#L11)

## Type Declaration {#type-declaration}

### cache_ts? {#cache_ts}

```typescript
optional cache_ts: string;
```

### categories? {#categories}

```typescript
optional categories: Category[];
```

### categories_version? {#categories_version}

```typescript
optional categories_version: string;
```

### emoji? {#emoji}

```typescript
optional emoji: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: string
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
