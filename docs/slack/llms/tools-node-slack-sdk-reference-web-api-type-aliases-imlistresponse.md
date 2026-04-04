Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ImListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ImListResponse

# Type Alias: ImListResponse

```typescript
type ImListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ImListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ImListResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### ims? {#ims}

```typescript
optional ims: Im[];
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
