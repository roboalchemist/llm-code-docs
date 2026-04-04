Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/SearchFilesResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SearchFilesResponse

# Type Alias: SearchFilesResponse

```typescript
type SearchFilesResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/SearchFilesResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/SearchFilesResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### files? {#files}

```typescript
optional files: Files;
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

### query? {#query}

```typescript
optional query: string;
```
