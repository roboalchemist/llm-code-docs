Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/BookmarksListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / BookmarksListResponse

# Type Alias: BookmarksListResponse

```typescript
type BookmarksListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/BookmarksListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/BookmarksListResponse.ts#L11)

## Type Declaration {#type-declaration}

### bookmarks? {#bookmarks}

```typescript
optional bookmarks: Bookmark[];
```

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
