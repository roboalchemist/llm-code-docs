Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminRolesRemoveAssignmentsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminRolesRemoveAssignmentsArguments

# Interface: AdminRolesRemoveAssignmentsArguments

Defined in: [packages/web-api/src/types/request/admin/roles.ts:39](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/roles.ts#L39)

## Extends {#extends}

* `EntityIDs`.`RoleID`.`UserIDs`.`TokenOverridable`

## Properties {#properties}

### entity_ids {#entity_ids}

```text
entity_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/admin/roles.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/roles.ts#L10)

#### Description {#description}

List of the entity IDs for which roles will be assigned/listed/removed. These can be Org IDs (E12345), Team IDs (T12345) or Channel IDs (C12345).

#### Inherited from {#inherited-from}

```text
EntityIDs.entity_ids
```

* * *

### role_id {#role_id}

```text
role_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/roles.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/roles.ts#L18)

#### Description {#description-1}

ID of the role to which users will be assigned/removed.

#### See {#see}

[Admin Roles under Usage info](https://docs.slack.dev/reference/methods/admin.roles.addAssignments).

#### Inherited from {#inherited-from-1}

```text
RoleID.role_id
```

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

* * *

### user_ids {#user_ids}

```text
user_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L92)

#### Description {#description-3}

List of encoded user IDs.

#### Inherited from {#inherited-from-3}

```text
UserIDs.user_ids
```
