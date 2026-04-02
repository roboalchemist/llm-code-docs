Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatScheduleMessageResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatScheduleMessageResponse

# Type Alias: ChatScheduleMessageResponse

```typescript
type ChatScheduleMessageResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ChatScheduleMessageResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ChatScheduleMessageResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel? {#channel}

```typescript
optional channel: string;
```

### error? {#error}

```typescript
optional error: string;
```

### message? {#message}

```typescript
optional message: Message;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### post_at? {#post_at}

```typescript
optional post_at: number;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### scheduled_message_id? {#scheduled_message_id}

```typescript
optional scheduled_message_id: string;
```
