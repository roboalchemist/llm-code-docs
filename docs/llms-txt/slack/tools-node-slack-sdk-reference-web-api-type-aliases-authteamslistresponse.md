Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AuthTeamsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AuthTeamsListResponse

# Type Alias: AuthTeamsListResponse

```typescript
type AuthTeamsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AuthTeamsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AuthTeamsListResponse.ts#L11)

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

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### teams? {#teams}

```typescript
optional teams: Team[];
```
