Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/RemindersAddResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / RemindersAddResponse

# Type Alias: RemindersAddResponse

```typescript
type RemindersAddResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/RemindersAddResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/RemindersAddResponse.ts#L11)

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

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```
