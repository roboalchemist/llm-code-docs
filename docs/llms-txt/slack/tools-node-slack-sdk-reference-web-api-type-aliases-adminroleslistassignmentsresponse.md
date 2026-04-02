Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminRolesListAssignmentsResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminRolesListAssignmentsResponse

# Type Alias: AdminRolesListAssignmentsResponse

```typescript
type AdminRolesListAssignmentsResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminRolesListAssignmentsResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminRolesListAssignmentsResponse.ts#L11)

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

### role_assignments? {#role_assignments}

```typescript
optional role_assignments: RoleAssignment[];
```
