Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/WebAPICallResult

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / WebAPICallResult

# Interface: WebAPICallResult

Defined in: [packages/web-api/src/WebClient.ts:136](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L136)

## Properties {#properties}

### error? {#error}

```text
optional error: string;
```text

Defined in: [packages/web-api/src/WebClient.ts:138](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L138)

* * *

### ok {#ok}

```text
ok: boolean;
```text

Defined in: [packages/web-api/src/WebClient.ts:137](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L137)

* * *

### response_metadata? {#response_metadata}

```text
optional response_metadata: object;
```text

Defined in: [packages/web-api/src/WebClient.ts:139](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/WebClient.ts#L139)

#### acceptedScopes? {#acceptedscopes}

```text
optional acceptedScopes: string[];
```text

#### messages? {#messages}

```text
optional messages: string[];
```text

#### next_cursor? {#next_cursor}

```text
optional next_cursor: string;
```text

#### retryAfter? {#retryafter}

```text
optional retryAfter: number;
```text

#### scopes? {#scopes}

```text
optional scopes: string[];
```text

#### warnings? {#warnings}

```text
optional warnings: string[];
```text
