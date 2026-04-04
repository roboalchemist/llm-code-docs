Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/MpimRepliesResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MpimRepliesResponse

# Type Alias: MpimRepliesResponse

```typescript
type MpimRepliesResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/MpimRepliesResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/MpimRepliesResponse.ts#L11)

## Type Declaration {#type-declaration}

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
