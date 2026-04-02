Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/TeamInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamInfoResponse

# Type Alias: TeamInfoResponse

```typescript
type TeamInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/TeamInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/TeamInfoResponse.ts#L11)

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

### team? {#team}

```typescript
optional team: Team;
```
