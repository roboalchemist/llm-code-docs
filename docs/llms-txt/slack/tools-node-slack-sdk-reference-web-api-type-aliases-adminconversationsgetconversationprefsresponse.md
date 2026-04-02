Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminConversationsGetConversationPrefsResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminConversationsGetConversationPrefsResponse

# Type Alias: AdminConversationsGetConversationPrefsResponse

```typescript
type AdminConversationsGetConversationPrefsResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminConversationsGetConversationPrefsResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminConversationsGetConversationPrefsResponse.ts#L11)

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

### prefs? {#prefs}

```typescript
optional prefs: Prefs;
```

### provided? {#provided}

```typescript
optional provided: string;
```
