Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/RemindersInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RemindersInfoResponse

# Type Alias: RemindersInfoResponse

```typescript
type RemindersInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/RemindersInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/RemindersInfoResponse.ts#L11)

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

### reminder? {#reminder}

```typescript
optional reminder: Reminder;
```
