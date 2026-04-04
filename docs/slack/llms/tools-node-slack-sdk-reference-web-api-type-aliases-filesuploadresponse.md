Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/FilesUploadResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesUploadResponse

# Type Alias: FilesUploadResponse

```typescript
type FilesUploadResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/FilesUploadResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/FilesUploadResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### file? {#file}

```typescript
optional file: File;
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
