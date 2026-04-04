Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/SearchMessagesResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SearchMessagesResponse

# Type Alias: SearchMessagesResponse

```typescript
type SearchMessagesResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/SearchMessagesResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/SearchMessagesResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### messages? {#messages}

```typescript
optional messages: Messages;
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

### query? {#query}

```typescript
optional query: string;
```
