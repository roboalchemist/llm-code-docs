Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/RemindersListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RemindersListResponse

# Type Alias: RemindersListResponse

```typescript
type RemindersListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/RemindersListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/RemindersListResponse.ts#L11)

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

### reminders? {#reminders}

```typescript
optional reminders: Reminder[];
```
