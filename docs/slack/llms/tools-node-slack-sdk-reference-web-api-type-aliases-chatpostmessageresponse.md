Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChatPostMessageResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChatPostMessageResponse

# Type Alias: ChatPostMessageResponse

```typescript
type ChatPostMessageResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ChatPostMessageResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ChatPostMessageResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel? {#channel}

```typescript
optional channel: string;
```

### deprecated_argument? {#deprecated_argument}

```typescript
optional deprecated_argument: string;
```

### error? {#error}

```typescript
optional error: string;
```

### errors? {#errors}

```typescript
optional errors: string[];
```

### message? {#message}

```typescript
optional message: ChatPostMessageResponseMessage;
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

### ts? {#ts}

```typescript
optional ts: string;
```
