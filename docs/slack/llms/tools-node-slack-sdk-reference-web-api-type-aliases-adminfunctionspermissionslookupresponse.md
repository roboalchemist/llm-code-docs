Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminFunctionsPermissionsLookupResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminFunctionsPermissionsLookupResponse

# Type Alias: AdminFunctionsPermissionsLookupResponse

```typescript
type AdminFunctionsPermissionsLookupResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminFunctionsPermissionsLookupResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminFunctionsPermissionsLookupResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### errors? {#errors}

```typescript
optional errors: Errors;
```

### metadata? {#metadata}

```typescript
optional metadata: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: Errors
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### permissions? {#permissions}

```typescript
optional permissions: object;
```

#### Index Signature {#index-signature-1}

```typescript
[key: string]: Permission
```

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```
