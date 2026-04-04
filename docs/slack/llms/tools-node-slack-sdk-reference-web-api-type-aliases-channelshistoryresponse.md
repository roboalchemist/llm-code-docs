Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ChannelsHistoryResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ChannelsHistoryResponse

# Type Alias: ChannelsHistoryResponse

```typescript
type ChannelsHistoryResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/ChannelsHistoryResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/ChannelsHistoryResponse.ts#L11)

## Type Declaration {#type-declaration}

### channel_actions_count? {#channel_actions_count}

```typescript
optional channel_actions_count: number;
```

### channel_actions_ts? {#channel_actions_ts}

```typescript
optional channel_actions_ts: number;
```

### error? {#error}

```typescript
optional error: string;
```

### has_more? {#has_more}

```typescript
optional has_more: boolean;
```

### latest? {#latest}

```typescript
optional latest: string;
```

### messages? {#messages}

```typescript
optional messages: Message[];
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

### warning? {#warning}

```typescript
optional warning: string;
```
