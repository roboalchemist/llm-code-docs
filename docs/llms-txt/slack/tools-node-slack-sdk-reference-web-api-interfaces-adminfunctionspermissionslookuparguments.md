Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminFunctionsPermissionsLookupArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminFunctionsPermissionsLookupArguments

# Interface: AdminFunctionsPermissionsLookupArguments

Defined in: [packages/web-api/src/types/request/admin/functions.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/functions.ts#L12)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### function_ids {#function_ids}

```text
function_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/admin/functions.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/functions.ts#L14)

#### Description {#description}

An array of function IDs to get permissions for.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```
