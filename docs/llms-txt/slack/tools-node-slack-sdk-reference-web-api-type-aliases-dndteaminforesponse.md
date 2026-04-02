Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/DndTeamInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DndTeamInfoResponse

# Type Alias: DndTeamInfoResponse

```typescript
type DndTeamInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/DndTeamInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/DndTeamInfoResponse.ts#L11)

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

### users? {#users}

```typescript
optional users: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: User
```
