Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersCreateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminBarriersCreateArguments

# Interface: AdminBarriersCreateArguments

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:11](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L11)

## Extends {#extends}

* `TokenOverridable`

## Extended by {#extended-by}

* [`AdminBarriersUpdateArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersUpdateArguments)

## Properties {#properties}

### barriered_from_usergroup_ids {#barriered_from_usergroup_ids}

```
barriered_from_usergroup_ids: string[];
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L13)

#### Description {#description}

A list of [IDP Groups](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) IDs ti associate with the barrier.

* * *

### primary_usergroup_id {#primary_usergroup_id}

```
primary_usergroup_id: string;
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L15)

#### Description {#description-1}

The ID of the primary [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org).

* * *

### restricted_subjects {#restricted_subjects}

```
restricted_subjects: ["im", "mpim", "call"];
```

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:20](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L20)

#### Description {#description-2}

What kind of interactions are blocked by this barrier? Currently you must provide all three: `im`, `mpim`, `call`.

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```
TokenOverridable.token
```
