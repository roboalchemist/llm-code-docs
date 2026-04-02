Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/GroupsInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / GroupsInfoResponse

# Type Alias: GroupsInfoResponse

```typescript
type GroupsInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/GroupsInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/GroupsInfoResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### group? {#group}

```typescript
optional group: Group;
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

### warning? {#warning}

```typescript
optional warning: string;
```
