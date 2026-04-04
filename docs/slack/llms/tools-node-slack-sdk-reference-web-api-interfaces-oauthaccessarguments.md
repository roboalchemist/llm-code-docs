Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OAuthAccessArguments

# Interface: OAuthAccessArguments

Defined in: [packages/web-api/src/types/request/oauth.ts:4](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/oauth.ts#L4)

## Extends {#extends}

* `OAuthCredentials`

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

### redirect_uri? {#redirect_uri}

```text
optional redirect_uri: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:147](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L147)

#### Description {#description-3}

While optional, it is _required_ if your app passed it as a parameter to the OpenID/OAuth flow's first step and must match the originally submitted URI.

#### Inherited from {#inherited-from-3}

```text
OAuthCredentials.redirect_uri
```text

* * *

### single_channel? {#single_channel}

```text
optional single_channel: boolean;
```text

Defined in: [packages/web-api/src/types/request/oauth.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/oauth.ts#L6)

#### Description {#description-4}

Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://docs.slack.dev/legacy/legacy-steps-from-apps). Defaults to `false`.
