Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/OAuthV2ExchangeArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OAuthV2ExchangeArguments

# Interface: OAuthV2ExchangeArguments

Defined in: [packages/web-api/src/types/request/oauth.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/oauth.ts#L11)

## Extends {#extends}

* `Pick`<`OAuthCredentials`, `"client_id"` | `"client_secret"`\>

## Properties {#properties}

### client_id {#client_id}

```text
client_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:138](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L138)

#### Description {#description}

Issued when you created your application.

#### Inherited from {#inherited-from}

[`OAuthAccessArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments).[`client_id`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments#client_id)

* * *

### client_secret {#client_secret}

```text
client_secret: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:140](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L140)

#### Description {#description-1}

Issued when you created your application.

#### Inherited from {#inherited-from-1}

[`OAuthAccessArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments).[`client_secret`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments#client_secret)

* * *

### token {#token}

```text
token: string;
```text

Defined in: [packages/web-api/src/types/request/oauth.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/oauth.ts#L13)

#### Description {#description-2}

The legacy xoxb or xoxp token being migrated.
