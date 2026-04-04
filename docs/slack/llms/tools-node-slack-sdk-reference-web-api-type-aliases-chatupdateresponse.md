Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatUpdateResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatUpdateResponse

# Type Alias: ChatUpdateResponse

```typescript
type ChatUpdateResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ChatUpdateResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ChatUpdateResponse.ts#L11)

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

### provided? {#provided}

```typescript
optional provided: string;
```

### response_metadata? {#response_metadata}

```typescript
optional response_metadata: ResponseMetadata;
```

### text? {#text}

```typescript
optional text: string;
```

### ts? {#ts}

```typescript
optional ts: string;
```
