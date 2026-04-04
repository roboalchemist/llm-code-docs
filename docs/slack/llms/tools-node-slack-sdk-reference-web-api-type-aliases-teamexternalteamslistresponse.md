Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/TeamExternalTeamsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamExternalTeamsListResponse

# Type Alias: TeamExternalTeamsListResponse

```typescript
type TeamExternalTeamsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/TeamExternalTeamsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/TeamExternalTeamsListResponse.ts#L11)

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

### organizations? {#organizations}

```typescript
optional organizations: Organization[];
```

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### total_count? {#total_count}

```typescript
optional total_count: number;
```
