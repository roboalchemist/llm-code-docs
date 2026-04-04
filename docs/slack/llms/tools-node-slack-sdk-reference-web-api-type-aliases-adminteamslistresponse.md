Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminTeamsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminTeamsListResponse

# Type Alias: AdminTeamsListResponse

```typescript
type AdminTeamsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminTeamsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminTeamsListResponse.ts#L11)

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

### teams? {#teams}

```typescript
optional teams: Team[];
```
