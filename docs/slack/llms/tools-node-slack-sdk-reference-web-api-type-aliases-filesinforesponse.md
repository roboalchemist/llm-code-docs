Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/FilesInfoResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesInfoResponse

# Type Alias: FilesInfoResponse

```typescript
type FilesInfoResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/FilesInfoResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/FilesInfoResponse.ts#L11)

## Type Declaration {#type-declaration}

### comments? {#comments}

```typescript
optional comments: Comment[];
```

### content? {#content}

```typescript
optional content: string;
```

### content_highlight_css? {#content_highlight_css}

```typescript
optional content_highlight_css: string;
```

### content_highlight_html? {#content_highlight_html}

```typescript
optional content_highlight_html: string;
```

### content_highlight_html_truncated? {#content_highlight_html_truncated}

```typescript
optional content_highlight_html_truncated: boolean;
```

### error? {#error}

```typescript
optional error: string;
```

### file? {#file}

```typescript
optional file: File;
```

### is_truncated? {#is_truncated}

```typescript
optional is_truncated: boolean;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### paging? {#paging}

```typescript
optional paging: Paging;
```

### provided? {#provided}

```typescript
optional provided: string;
```
