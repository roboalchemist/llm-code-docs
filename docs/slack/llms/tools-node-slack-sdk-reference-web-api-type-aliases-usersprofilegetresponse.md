Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/UsersProfileGetResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersProfileGetResponse

# Type Alias: UsersProfileGetResponse

```typescript
type UsersProfileGetResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/UsersProfileGetResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/UsersProfileGetResponse.ts#L11)

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

### profile? {#profile}

```typescript
optional profile: Profile;
```

### provided? {#provided}

```typescript
optional provided: string;
```
