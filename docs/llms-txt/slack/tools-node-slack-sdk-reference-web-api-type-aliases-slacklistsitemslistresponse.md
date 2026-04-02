Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/SlackListsItemsListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackListsItemsListResponse

# Type Alias: SlackListsItemsListResponse

```typescript
type SlackListsItemsListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/SlackListsItemsListResponse.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/SlackListsItemsListResponse.ts#L4)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### items? {#items}

```typescript
optional items: SlackListsItem[];
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
optional response_metadata: object;
```

#### response_metadata.next_cursor? {#response_metadatanext_cursor}

```typescript
optional next_cursor: string;
```
