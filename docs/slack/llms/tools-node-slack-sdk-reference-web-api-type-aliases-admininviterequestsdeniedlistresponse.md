Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminInviteRequestsDeniedListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminInviteRequestsDeniedListResponse

# Type Alias: AdminInviteRequestsDeniedListResponse

```typescript
type AdminInviteRequestsDeniedListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminInviteRequestsDeniedListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminInviteRequestsDeniedListResponse.ts#L11)

## Type Declaration {#type-declaration}

### denied_requests? {#denied_requests}

```typescript
optional denied_requests: DeniedRequest[];
```

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
