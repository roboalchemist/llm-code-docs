Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminAppsRestrictedListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminAppsRestrictedListResponse

# Type Alias: AdminAppsRestrictedListResponse

```typescript
type AdminAppsRestrictedListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminAppsRestrictedListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminAppsRestrictedListResponse.ts#L11)

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

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### restricted_apps? {#restricted_apps}

```typescript
optional restricted_apps: RestrictedApp[];
```

### warning? {#warning}

```typescript
optional warning: string;
```
