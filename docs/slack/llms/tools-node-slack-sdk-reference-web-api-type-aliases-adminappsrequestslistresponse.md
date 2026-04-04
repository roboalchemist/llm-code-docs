Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminAppsRequestsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminAppsRequestsListResponse

# Type Alias: AdminAppsRequestsListResponse

```typescript
type AdminAppsRequestsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminAppsRequestsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminAppsRequestsListResponse.ts#L11)

## Type Declaration {#type-declaration}

### app_requests? {#app_requests}

```typescript
optional app_requests: AppRequest[];
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

### warning? {#warning}

```typescript
optional warning: string;
```
