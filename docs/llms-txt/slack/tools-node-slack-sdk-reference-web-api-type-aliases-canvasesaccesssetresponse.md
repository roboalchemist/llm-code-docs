Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/CanvasesAccessSetResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CanvasesAccessSetResponse

# Type Alias: CanvasesAccessSetResponse

```typescript
type CanvasesAccessSetResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/CanvasesAccessSetResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/CanvasesAccessSetResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### failed_to_update_channel_ids? {#failed_to_update_channel_ids}

```typescript
optional failed_to_update_channel_ids: string[];
```

### failed_to_update_user_ids? {#failed_to_update_user_ids}

```typescript
optional failed_to_update_user_ids: string[];
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
