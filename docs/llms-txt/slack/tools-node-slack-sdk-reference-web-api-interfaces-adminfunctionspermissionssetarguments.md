Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminFunctionsPermissionsSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminFunctionsPermissionsSetArguments

# Interface: AdminFunctionsPermissionsSetArguments

Defined in: [packages/web-api/src/types/request/admin/functions.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/functions.ts#L18)

## Extends {#extends}

* `TokenOverridable`.`Partial`<`UserIDs`\>

## Properties {#properties}

### function_id {#function_id}

```text
function_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/functions.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/functions.ts#L20)

#### Description {#description}

The function ID to set permissions for.

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

* * *

### user_ids? {#user_ids}

```text
optional user_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L92)

#### Description {#description-2}

List of encoded user IDs.

#### Inherited from {#inherited-from-1}

[`AdminConversationsInviteArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsInviteArguments).[`user_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminConversationsInviteArguments#user_ids)

* * *

### visibility {#visibility}

```text
visibility: "everyone" | "app_collaborators" | "named_entities" | "no_one";
```

Defined in: [packages/web-api/src/types/request/admin/functions.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/functions.ts#L22)

#### Description {#description-3}

The function visibility.
