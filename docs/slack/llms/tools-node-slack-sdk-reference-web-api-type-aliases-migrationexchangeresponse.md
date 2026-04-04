Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/MigrationExchangeResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MigrationExchangeResponse

# Type Alias: MigrationExchangeResponse

```typescript
type MigrationExchangeResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/MigrationExchangeResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/MigrationExchangeResponse.ts#L11)

## Type Declaration {#type-declaration}

### enterprise_id? {#enterprise_id}

```typescript
optional enterprise_id: string;
```

### error? {#error}

```typescript
optional error: string;
```

### invalid_user_ids? {#invalid_user_ids}

```typescript
optional invalid_user_ids: string[];
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

### team_id? {#team_id}

```typescript
optional team_id: string;
```

### user_id_map? {#user_id_map}

```typescript
optional user_id_map: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: string
```

### warning? {#warning}

```typescript
optional warning: string;
```
