Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/FilesCompleteUploadExternalResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesCompleteUploadExternalResponse

# Type Alias: FilesCompleteUploadExternalResponse

```typescript
type FilesCompleteUploadExternalResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/FilesCompleteUploadExternalResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/FilesCompleteUploadExternalResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### files? {#files}

```typescript
optional files: File[];
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
