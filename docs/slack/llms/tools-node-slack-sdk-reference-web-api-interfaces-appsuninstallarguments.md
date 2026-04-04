Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AppsUninstallArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AppsUninstallArguments

# Interface: AppsUninstallArguments

Defined in: [packages/web-api/src/types/request/apps.ts:44](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L44)

## Extends {#extends}

* `Pick`<`OAuthCredentials`, `"client_id"` | `"client_secret"`\>.`TokenOverridable`

## Properties {#properties}

### client_id {#client_id}

```text
client_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:138](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L138)

#### Description {#description}

Issued when you created your application.

#### Inherited from {#inherited-from}

[`OAuthAccessArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments).[`client_id`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments#client_id)

* * *

### client_secret {#client_secret}

```text
client_secret: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:140](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L140)

#### Description {#description-1}

Issued when you created your application.

#### Inherited from {#inherited-from-1}

[`OAuthAccessArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments).[`client_secret`](/tools/node-slack-sdk/reference/web-api/interfaces/OAuthAccessArguments#client_secret)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```
