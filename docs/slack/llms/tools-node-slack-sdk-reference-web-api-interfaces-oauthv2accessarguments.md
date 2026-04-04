Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/OAuthV2AccessArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OAuthV2AccessArguments

# Interface: OAuthV2AccessArguments

Defined in: [packages/web-api/src/types/request/oauth.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/oauth.ts#L9)

## Extends {#extends}

* `OAuthCredentials`.`OAuthGrantRefresh`

## Properties {#properties}

### client_id {#client_id}

```text
client_id: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:138](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L138)

#### Description {#description}

Issued when you created your application.

#### Inherited from {#inherited-from}

```text
OAuthCredentials.client_id
```text

* * *

### client_secret {#client_secret}

```text
client_secret: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:140](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L140)

#### Description {#description-1}

Issued when you created your application.

#### Inherited from {#inherited-from-1}

```text
OAuthCredentials.client_secret
```text

* * *

### code? {#code}

```text
optional code: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:142](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L142)

#### Description {#description-2}

The `code` parameter returned via the OAuth callback.

#### Inherited from {#inherited-from-2}

```text
OAuthCredentials.code
```text

* * *

### grant_type? {#grant_type}

```text
optional grant_type: "authorization_code" | "refresh_token";
```text

Defined in: [packages/web-api/src/types/request/common.ts:152](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L152)

#### Description {#description-3}

The `grant_type` param as described in the OAuth spec.

#### Inherited from {#inherited-from-3}

```text
OAuthGrantRefresh.grant_type
```text

* * *

### redirect_uri? {#redirect_uri}

```text
optional redirect_uri: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:147](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L147)

#### Description {#description-4}

While optional, it is _required_ if your app passed it as a parameter to the OpenID/OAuth flow's first step and must match the originally submitted URI.

#### Inherited from {#inherited-from-4}

```text
OAuthCredentials.redirect_uri
```text

* * *

### refresh_token? {#refresh_token}

```text
optional refresh_token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:154](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L154)

#### Description {#description-5}

The `refresh_token` param as described in the OAuth spec.

#### Inherited from {#inherited-from-5}

```text
OAuthGrantRefresh.refresh_token
```text
