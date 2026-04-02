Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/OpenIDConnectTokenResponse

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OpenIDConnectTokenResponse

# Type Alias: OpenIDConnectTokenResponse

```typescript
type OpenIDConnectTokenResponse = WebAPICallResult & object;
```

Defined in: [packages/web-api/src/types/response/OpenIDConnectTokenResponse.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/response/OpenIDConnectTokenResponse.ts#L11)

## Type Declaration {#type-declaration}

### access_token? {#access_token}

```typescript
optional access_token: string;
```

### error? {#error}

```typescript
optional error: string;
```

### expires_in? {#expires_in}

```typescript
optional expires_in: number;
```

### id_token? {#id_token}

```typescript
optional id_token: string;
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

### token_type? {#token_type}

```typescript
optional token_type: string;
```

### warning? {#warning}

```typescript
optional warning: string;
```
