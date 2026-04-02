Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminBarriersDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminBarriersDeleteArguments

# Interface: AdminBarriersDeleteArguments

Defined in: [packages/web-api/src/types/request/admin/barriers.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/barriers.ts#L24)

## Extends {#extends}

* `BarrierID`.`TokenOverridable`

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

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```
TokenOverridable.token
```
