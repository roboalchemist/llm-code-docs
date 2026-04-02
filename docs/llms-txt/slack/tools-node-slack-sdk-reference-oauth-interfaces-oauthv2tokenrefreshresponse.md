Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/OAuthV2TokenRefreshResponse

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / OAuthV2TokenRefreshResponse

# Interface: OAuthV2TokenRefreshResponse

Defined in: [packages/oauth/src/install-provider.ts:791](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L791)

## Extends {#extends}

* `WebAPICallResult`

## Properties {#properties}

### access_token {#access_token}

```text
access_token: string;
```

Defined in: [packages/oauth/src/install-provider.ts:795](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L795)

* * *

### app_id {#app_id}

```text
app_id: string;
```

Defined in: [packages/oauth/src/install-provider.ts:792](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L792)

* * *

### bot_user_id? {#bot_user_id}

```text
optional bot_user_id: string;
```

Defined in: [packages/oauth/src/install-provider.ts:798](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L798)

* * *

### enterprise {#enterprise}

```text
enterprise:   | {  id: string;  name: string;}  | null;
```

Defined in: [packages/oauth/src/install-provider.ts:800](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L800)

* * *

### error? {#error}

```text
optional error: string;
```

Defined in: packages/web-api/dist/WebClient.d.ts:66

#### Inherited from {#inherited-from}

```text
WebAPICallResult.error
```

* * *

### expires_in {#expires_in}

```text
expires_in: number;
```

Defined in: [packages/oauth/src/install-provider.ts:797](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L797)

* * *

### is_enterprise_install {#is_enterprise_install}

```text
is_enterprise_install: boolean;
```

Defined in: [packages/oauth/src/install-provider.ts:801](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L801)

* * *

### ok {#ok}

```text
ok: boolean;
```

Defined in: packages/web-api/dist/WebClient.d.ts:65

#### Inherited from {#inherited-from-1}

```text
WebAPICallResult.ok
```

* * *

### refresh_token {#refresh_token}

```text
refresh_token: string;
```

Defined in: [packages/oauth/src/install-provider.ts:796](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L796)

* * *

### response_metadata? {#response_metadata}

```text
optional response_metadata: object;
```

Defined in: packages/web-api/dist/WebClient.d.ts:67

#### acceptedScopes? {#acceptedscopes}

```text
optional acceptedScopes: string[];
```

#### messages? {#messages}

```text
optional messages: string[];
```

#### next_cursor? {#next_cursor}

```text
optional next_cursor: string;
```

#### retryAfter? {#retryafter}

```text
optional retryAfter: number;
```

#### scopes? {#scopes}

```text
optional scopes: string[];
```

#### warnings? {#warnings}

```text
optional warnings: string[];
```

#### Inherited from {#inherited-from-2}

```text
WebAPICallResult.response_metadata
```

* * *

### scope {#scope}

```text
scope: string;
```

Defined in: [packages/oauth/src/install-provider.ts:793](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L793)

* * *

### team {#team}

```text
team: object;
```

Defined in: [packages/oauth/src/install-provider.ts:799](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L799)

#### id {#id}

```text
id: string;
```

#### name {#name}

```text
name: string;
```

* * *

### token_type {#token_type}

```text
token_type: "bot" | "user";
```

Defined in: [packages/oauth/src/install-provider.ts:794](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L794)
