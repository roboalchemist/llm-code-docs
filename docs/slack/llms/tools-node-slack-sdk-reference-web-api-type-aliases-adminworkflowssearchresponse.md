Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminWorkflowsSearchResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminWorkflowsSearchResponse

# Type Alias: AdminWorkflowsSearchResponse

```typescript
type AdminWorkflowsSearchResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminWorkflowsSearchResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminWorkflowsSearchResponse.ts#L11)

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

### total_found? {#total_found}

```typescript
optional total_found: number;
```

### workflows? {#workflows}

```typescript
optional workflows: Workflow[];
```
