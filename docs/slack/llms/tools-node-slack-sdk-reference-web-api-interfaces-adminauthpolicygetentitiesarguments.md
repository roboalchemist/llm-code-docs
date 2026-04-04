Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminAuthPolicyGetEntitiesArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminAuthPolicyGetEntitiesArguments

# Interface: AdminAuthPolicyGetEntitiesArguments

Defined in: [packages/web-api/src/types/request/admin/auth.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L20)

## Extends {#extends}

* `Partial`<`EntityType`\>.`PolicyName`.`TokenOverridable`.`CursorPaginationEnabled`

## Properties {#properties}

### cursor? {#cursor}

```
optional cursor: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:16](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L16)

#### Description {#description}

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.

#### See {#see}

[pagination](https://docs.slack.dev/apis/web-api/pagination) for more detail.

#### Inherited from {#inherited-from}

```
CursorPaginationEnabled.cursor
```

* * *

### entity_type? {#entity_type}

```
optional entity_type: "USER";
```

Defined in: [packages/web-api/src/types/request/admin/auth.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L9)

#### Description {#description-1}

The type of entity interacting with the policy.

#### Inherited from {#inherited-from-1}

[`AdminAuthPolicyAssignEntitiesArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminAuthPolicyAssignEntitiesArguments).[`entity_type`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminAuthPolicyAssignEntitiesArguments#entity_type)

* * *

### limit? {#limit}

```
optional limit: number;
```

Defined in: [packages/web-api/src/types/request/common.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L9)

#### Description {#description-2}

The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer with a max value of `999`. Default is `100`.

#### Inherited from {#inherited-from-2}

```
CursorPaginationEnabled.limit
```

* * *

### policy_name {#policy_name}

```
policy_name: "email_password";
```

Defined in: [packages/web-api/src/types/request/admin/auth.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L13)

#### Description {#description-3}

The name of the policy.

#### Inherited from {#inherited-from-3}

```
PolicyName.policy_name
```

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

```
TokenOverridable.token
```
