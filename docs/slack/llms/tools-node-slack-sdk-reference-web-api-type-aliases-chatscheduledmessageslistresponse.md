Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatScheduledMessagesListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatScheduledMessagesListResponse

# Type Alias: ChatScheduledMessagesListResponse

```typescript
type ChatScheduledMessagesListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ChatScheduledMessagesListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ChatScheduledMessagesListResponse.ts#L11)

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

### scheduled_messages? {#scheduled_messages}

```typescript
optional scheduled_messages: ScheduledMessage[];
```
