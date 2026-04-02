Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/UsersListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersListResponse

# Type Alias: UsersListResponse

```typescript
type UsersListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/UsersListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/UsersListResponse.ts#L11)

## Type Declaration {#type-declaration}

### arg? {#arg}

```typescript
optional arg: string;
```

### cache_ts? {#cache_ts}

```typescript
optional cache_ts: number;
```

### error? {#error}

```typescript
optional error: string;
```

### members? {#members}

```typescript
optional members: Member[];
```

### needed? {#needed}

```typescript
optional needed: string;
```

### offset? {#offset}

```typescript
optional offset: string;
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
