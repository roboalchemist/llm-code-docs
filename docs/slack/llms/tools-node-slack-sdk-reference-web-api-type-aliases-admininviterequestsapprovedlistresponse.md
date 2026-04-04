Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminInviteRequestsApprovedListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminInviteRequestsApprovedListResponse

# Type Alias: AdminInviteRequestsApprovedListResponse

```typescript
type AdminInviteRequestsApprovedListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminInviteRequestsApprovedListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminInviteRequestsApprovedListResponse.ts#L11)

## Type Declaration {#type-declaration}

### approved_requests? {#approved_requests}

```typescript
optional approved_requests: ApprovedRequest[];
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
