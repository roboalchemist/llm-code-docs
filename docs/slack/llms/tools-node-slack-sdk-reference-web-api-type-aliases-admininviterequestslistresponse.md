Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminInviteRequestsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminInviteRequestsListResponse

# Type Alias: AdminInviteRequestsListResponse

```typescript
type AdminInviteRequestsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminInviteRequestsListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminInviteRequestsListResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### invite_requests? {#invite_requests}

```typescript
optional invite_requests: InviteRequest[];
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
