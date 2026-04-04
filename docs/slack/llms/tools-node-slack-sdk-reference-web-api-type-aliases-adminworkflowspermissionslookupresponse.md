Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminWorkflowsPermissionsLookupResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminWorkflowsPermissionsLookupResponse

# Type Alias: AdminWorkflowsPermissionsLookupResponse

```typescript
type AdminWorkflowsPermissionsLookupResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminWorkflowsPermissionsLookupResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminWorkflowsPermissionsLookupResponse.ts#L11)

## Type Declaration {#type-declaration}

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

### permissions? {#permissions}

```typescript
optional permissions: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: Permission
```

### provided? {#provided}

```typescript
optional provided: string;
```
