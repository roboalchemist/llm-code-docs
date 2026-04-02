Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/TeamPreferencesListResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / TeamPreferencesListResponse

# Type Alias: TeamPreferencesListResponse

```typescript
type TeamPreferencesListResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/TeamPreferencesListResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/TeamPreferencesListResponse.ts#L11)

## Type Declaration {#type-declaration}

### allow_message_deletion? {#allow_message_deletion}

```typescript
optional allow_message_deletion: boolean;
```

### disable_file_uploads? {#disable_file_uploads}

```typescript
optional disable_file_uploads: string;
```

### display_real_names? {#display_real_names}

```typescript
optional display_real_names: boolean;
```

### error? {#error}

```typescript
optional error: string;
```

### msg_edit_window_mins? {#msg_edit_window_mins}

```typescript
optional msg_edit_window_mins: number;
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

### who_can_post_general? {#who_can_post_general}

```typescript
optional who_can_post_general: string;
```
