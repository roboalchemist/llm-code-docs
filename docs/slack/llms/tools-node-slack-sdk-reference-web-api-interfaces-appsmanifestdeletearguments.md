Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AppsManifestDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AppsManifestDeleteArguments

# Interface: AppsManifestDeleteArguments

Defined in: [packages/web-api/src/types/request/apps.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L20)

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
