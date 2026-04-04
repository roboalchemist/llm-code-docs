Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminBarriersUpdateArguments

# Interface: AdminBarriersUpdateArguments

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:30](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L30)

## Extends {#extends}

* [`AdminBarriersCreateArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments).`BarrierID`

## Properties {#properties}

### barrier_id {#barrier_id}

```
barrier_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L7)

#### Description {#description}

The ID of the barrier.

#### Inherited from {#inherited-from}

```
BarrierID.barrier_id
```

* * *

### barriered_from_usergroup_ids {#barriered_from_usergroup_ids}

```
barriered_from_usergroup_ids: string[];
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L13)

#### Description {#description-1}

A list of [IDP Groups](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) IDs ti associate with the barrier.

#### Inherited from {#inherited-from-1}

[`AdminBarriersCreateArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments).[`barriered_from_usergroup_ids`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments#barriered_from_usergroup_ids)

* * *

### primary_usergroup_id {#primary_usergroup_id}

```
primary_usergroup_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L15)

#### Description {#description-2}

The ID of the primary [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org).

#### Inherited from {#inherited-from-2}

[`AdminBarriersCreateArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments).[`primary_usergroup_id`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments#primary_usergroup_id)

* * *

### restricted_subjects {#restricted_subjects}

```
restricted_subjects: ["im", "mpim", "call"];
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L20)

#### Description {#description-3}

What kind of interactions are blocked by this barrier? Currently you must provide all three: `im`, `mpim`, `call`.

#### Inherited from {#inherited-from-3}

[`AdminBarriersCreateArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments).[`restricted_subjects`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments#restricted_subjects)

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

[`AdminBarriersCreateArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments).[`token`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments#token)
