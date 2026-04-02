Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminUsersSessionListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSessionListResponse

# Type Alias: AdminUsersSessionListResponse

```typescript
type AdminUsersSessionListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminUsersSessionListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminUsersSessionListResponse.ts#L11)

## Type Declaration {#type-declaration}

### active_sessions? {#active_sessions}

```typescript
optional active_sessions: ActiveSession[];
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
