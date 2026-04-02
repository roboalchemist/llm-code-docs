Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/TeamBillableInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamBillableInfoResponse

# Type Alias: TeamBillableInfoResponse

```typescript
type TeamBillableInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/TeamBillableInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/TeamBillableInfoResponse.ts#L11)

## Type Declaration {#type-declaration}

### billable_info? {#billable_info}

```typescript
optional billable_info: object;
```

#### Index Signature {#index-signature}

```typescript
[key: string]: BillableInfo
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
