Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/AdminUsersSessionGetSettingsResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSessionGetSettingsResponse

# Type Alias: AdminUsersSessionGetSettingsResponse

```typescript
type AdminUsersSessionGetSettingsResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/AdminUsersSessionGetSettingsResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/AdminUsersSessionGetSettingsResponse.ts#L11)

## Type Declaration {#type-declaration}

### error? {#error}

```typescript
optional error: string;
```

### needed? {#needed}

```typescript
optional needed: string;
```

### no_settings_applied? {#no_settings_applied}

```typescript
optional no_settings_applied: string[];
```

### ok? {#ok}

```typescript
optional ok: boolean;
```

### provided? {#provided}

```typescript
optional provided: string;
```

### session_settings? {#session_settings}

```typescript
optional session_settings: SessionSetting[];
```
