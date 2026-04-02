Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/OauthV2AccessResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OauthV2AccessResponse

# Type Alias: OauthV2AccessResponse

```typescript
type OauthV2AccessResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/OauthV2AccessResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/OauthV2AccessResponse.ts#L11)

## Type Declaration {#type-declaration}

### access_token? {#access_token}

```typescript
optional access_token: string;
```

### app_id? {#app_id}

```typescript
optional app_id: string;
```

### authed_user? {#authed_user}

```typescript
optional authed_user: AuthedUser;
```

### bot_user_id? {#bot_user_id}

```typescript
optional bot_user_id: string;
```

### enterprise? {#enterprise}

```typescript
optional enterprise: Enterprise;
```

### error? {#error}

```typescript
optional error: string;
```

### expires_in? {#expires_in}

```typescript
optional expires_in: number;
```

### incoming_webhook? {#incoming_webhook}

```typescript
optional incoming_webhook: IncomingWebhook;
```

### is_enterprise_install? {#is_enterprise_install}

```typescript
optional is_enterprise_install: boolean;
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

### refresh_token? {#refresh_token}

```typescript
optional refresh_token: string;
```

### scope? {#scope}

```typescript
optional scope: string;
```

### team? {#team}

```typescript
optional team: Enterprise;
```

### token_type? {#token_type}

```typescript
optional token_type: string;
```

### warning? {#warning}

```typescript
optional warning: string;
```
