Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/TeamIntegrationLogsResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamIntegrationLogsResponse

# Type Alias: TeamIntegrationLogsResponse

```typescript
type TeamIntegrationLogsResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/TeamIntegrationLogsResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/TeamIntegrationLogsResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### logs? {#logs}

```typescript
optional logs: Log[];
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### paging? {#paging}

```typescript
optional paging: Paging;
```

### provided? {#provided}

```typescript
optional provided: string;
```
