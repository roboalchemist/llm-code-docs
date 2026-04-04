Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminAuthPolicyAssignEntitiesArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminAuthPolicyAssignEntitiesArguments

# Interface: AdminAuthPolicyAssignEntitiesArguments

Defined in: [packages/web-api/src/types/request/admin/auth.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L17)

## Extends {#extends}

* `EntityIDs`.`EntityType`.`PolicyName`.`TokenOverridable`

## Properties {#properties}

### entity_ids {#entity_ids}

```
entity_ids: string[];
```

Defined in: [packages/web-api/src/types/request/admin/auth.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L5)

#### Description {#description}

Encoded IDs of the entities interacting with.

#### Inherited from {#inherited-from}

```
EntityIDs.entity_ids
```

* * *

### entity_type {#entity_type}

```
entity_type: "USER";
```

Defined in: [packages/web-api/src/types/request/admin/auth.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L9)

#### Description {#description-1}

The type of entity interacting with the policy.

#### Inherited from {#inherited-from-1}

```
EntityType.entity_type
```

* * *

### policy_name {#policy_name}

```
policy_name: "email_password";
```

Defined in: [packages/web-api/src/types/request/admin/auth.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/auth.ts#L13)

#### Description {#description-2}

The name of the policy.

#### Inherited from {#inherited-from-2}

```
PolicyName.policy_name
```

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-3}

```
TokenOverridable.token
```
