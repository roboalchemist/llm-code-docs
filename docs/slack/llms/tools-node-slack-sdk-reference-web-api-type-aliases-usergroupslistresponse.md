Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/UsergroupsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsergroupsListResponse

# Type Alias: UsergroupsListResponse

```typescript
type UsergroupsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/UsergroupsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/UsergroupsListResponse.ts#L11)

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

### usergroups? {#usergroups}

```typescript
optional usergroups: Usergroup[];
```
