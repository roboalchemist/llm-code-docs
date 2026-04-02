Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ImOpenResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ImOpenResponse

# Type Alias: ImOpenResponse

```typescript
type ImOpenResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ImOpenResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ImOpenResponse.ts#L11)

## Type Declaration {#type-declaration}

### already_open? {#already_open}

```typescript
optional already_open: boolean;
```

### channel? {#channel}

```typescript
optional channel: Channel;
```

### error? {#error}

```typescript
optional error: string;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### no_op? {#no_op}

```typescript
optional no_op: boolean;
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
