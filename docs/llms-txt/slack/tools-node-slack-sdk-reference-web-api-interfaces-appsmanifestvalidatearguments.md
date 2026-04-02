Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AppsManifestValidateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AppsManifestValidateArguments

# Interface: AppsManifestValidateArguments

Defined in: [packages/web-api/src/types/request/apps.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L31)

## Extends {#extends}

* `Partial`<`AppID`\>.`TokenOverridable`

## Properties {#properties}

### app_id? {#app_id}

```text
optional app_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L101)

#### Description {#description}

The ID of the app.

#### Inherited from {#inherited-from}

[`AdminAppsConfigSetArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminAppsConfigSetArguments).[`app_id`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminAppsConfigSetArguments#app_id)

* * *

### manifest {#manifest}

```text
manifest: Manifest;
```

Defined in: [packages/web-api/src/types/request/apps.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L32)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
