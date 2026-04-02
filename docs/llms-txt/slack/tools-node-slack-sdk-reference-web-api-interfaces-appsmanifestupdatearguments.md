Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AppsManifestUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AppsManifestUpdateArguments

# Interface: AppsManifestUpdateArguments

Defined in: [packages/web-api/src/types/request/apps.ts:26](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L26)

## Extends {#extends}

* `AppID`.`TokenOverridable`

## Properties {#properties}

### app_id {#app_id}

```text
app_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L101)

#### Description {#description}

The ID of the app.

#### Inherited from {#inherited-from}

```text
AppID.app_id
```

* * *

### manifest {#manifest}

```text
manifest: Manifest;
```

Defined in: [packages/web-api/src/types/request/apps.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L27)

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
