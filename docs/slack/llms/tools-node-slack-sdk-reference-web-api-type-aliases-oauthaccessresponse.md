Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/OauthAccessResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OauthAccessResponse

# Type Alias: OauthAccessResponse

```typescript
type OauthAccessResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/OauthAccessResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/OauthAccessResponse.ts#L11)

## Type Declaration {#type-declaration}

### access_token? {#access_token}

```typescript
optional access_token: string;
```

### authorizing_user? {#authorizing_user}

```typescript
optional authorizing_user: User;
```

### bot? {#bot}

```typescript
optional bot: Bot;
```

### enterprise_id? {#enterprise_id}

```typescript
optional enterprise_id: string;
```

### error? {#error}

```typescript
optional error: string;
```

### incoming_webhook? {#incoming_webhook}

```typescript
optional incoming_webhook: IncomingWebhook;
```

### installer_user? {#installer_user}

```typescript
optional installer_user: User;
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

### scope? {#scope}

```typescript
optional scope: string;
```

### scopes? {#scopes}

```typescript
optional scopes: Scopes;
```

### team_id? {#team_id}

```typescript
optional team_id: string;
```

### team_name? {#team_name}

```typescript
optional team_name: string;
```

### token_type? {#token_type}

```typescript
optional token_type: string;
```

### user_id? {#user_id}

```typescript
optional user_id: string;
```

### warning? {#warning}

```typescript
optional warning: string;
```
