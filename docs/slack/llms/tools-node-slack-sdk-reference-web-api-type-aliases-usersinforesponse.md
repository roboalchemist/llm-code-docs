Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/UsersInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersInfoResponse

# Type Alias: UsersInfoResponse

```typescript
type UsersInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/UsersInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/UsersInfoResponse.ts#L11)

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

### user? {#user}

```typescript
optional user: User;
```
