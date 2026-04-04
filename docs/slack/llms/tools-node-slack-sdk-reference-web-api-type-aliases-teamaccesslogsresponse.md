Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/TeamAccessLogsResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamAccessLogsResponse

# Type Alias: TeamAccessLogsResponse

```typescript
type TeamAccessLogsResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/TeamAccessLogsResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/TeamAccessLogsResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### logins? {#logins}

```typescript
optional logins: Login[];
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

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```
