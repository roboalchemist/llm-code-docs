Source: https://docs.slack.dev/tools/node-slack-sdk/reference/oauth/interfaces/OAuthV2Response

[@slack/oauth](/tools/node-slack-sdk/reference/oauth/) / OAuthV2Response

# Interface: OAuthV2Response

Defined in: [packages/oauth/src/install-provider.ts:764](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L764)

## Extends {#extends}

* `WebAPICallResult`

## Properties {#properties}

### access_token? {#access_token}

```text
optional access_token: string;
```

Defined in: [packages/oauth/src/install-provider.ts:776](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L776)

* * *

### app_id {#app_id}

```text
app_id: string;
```

Defined in: [packages/oauth/src/install-provider.ts:765](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L765)

* * *

### authed_user {#authed_user}

```text
authed_user: object;
```

Defined in: [packages/oauth/src/install-provider.ts:766](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L766)

#### access_token? {#access_token-1}

```text
optional access_token: string;
```

#### expires_in? {#expires_in}

```text
optional expires_in: number;
```

#### id {#id}

```text
id: string;
```

#### refresh_token? {#refresh_token}

```text
optional refresh_token: string;
```

#### scope? {#scope}

```text
optional scope: string;
```

#### token_type? {#token_type}

```text
optional token_type: string;
```

* * *

### bot_user_id? {#bot_user_id}

```text
optional bot_user_id: string;
```

Defined in: [packages/oauth/src/install-provider.ts:779](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L779)

* * *

### enterprise {#enterprise}

```text
enterprise:   | {  id: string;  name: string;}  | null;
```

Defined in: [packages/oauth/src/install-provider.ts:781](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L781)

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

### expires_in? {#expires_in-1}

```text
optional expires_in: number;
```

Defined in: [packages/oauth/src/install-provider.ts:778](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L778)

* * *

### incoming_webhook? {#incoming_webhook}

```text
optional incoming_webhook: object;
```

Defined in: [packages/oauth/src/install-provider.ts:783](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L783)

#### channel {#channel}

```text
channel: string;
```

#### channel_id {#channel_id}

```text
channel_id: string;
```

#### configuration_url {#configuration_url}

```text
configuration_url: string;
```

#### url {#url}

```text
url: string;
```

* * *

### is_enterprise_install {#is_enterprise_install}

```text
is_enterprise_install: boolean;
```

Defined in: [packages/oauth/src/install-provider.ts:782](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L782)

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

### refresh_token? {#refresh_token-1}

```text
optional refresh_token: string;
```

Defined in: [packages/oauth/src/install-provider.ts:777](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L777)

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

### scope? {#scope-1}

```text
optional scope: string;
```

Defined in: [packages/oauth/src/install-provider.ts:774](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L774)

* * *

### team {#team}

```text
team:   | {  id: string;  name: string;}  | null;
```

Defined in: [packages/oauth/src/install-provider.ts:780](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L780)

* * *

### token_type? {#token_type-1}

```text
optional token_type: "bot";
```

Defined in: [packages/oauth/src/install-provider.ts:775](https://github.com/slackapi/node-slack-sdk/blob/main/packages/oauth/src/install-provider.ts#L775)
