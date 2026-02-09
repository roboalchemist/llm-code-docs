# Source: https://docs.apify.com/api/client/js/reference/interface/ActorStartOptions.md

# ActorStartOptions<!-- -->

## Index[**](#Index)

### Properties

* [**build](#build)
* [**contentType](#contentType)
* [**forcePermissionLevel](#forcePermissionLevel)
* [**maxItems](#maxItems)
* [**maxTotalChargeUsd](#maxTotalChargeUsd)
* [**memory](#memory)
* [**restartOnError](#restartOnError)
* [**timeout](#timeout)
* [**waitForFinish](#waitForFinish)
* [**webhooks](#webhooks)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L594)optionalbuild

**build?

<!-- -->

: string

Tag or number of the Actor build to run (e.g. `beta` or `1.2.345`). If not provided, the run uses build tag or number from the default Actor run configuration (typically `latest`).

### [**](#contentType)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L602)optionalcontentType

**contentType?

<!-- -->

: string

Content type for the `input`. If not specified, `input` is expected to be an object that will be stringified to JSON and content type set to `application/json; charset=utf-8`. If `options.contentType` is specified, then `input` must be a `String` or `Buffer`.

### [**](#forcePermissionLevel)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L660)optionalforcePermissionLevel

**forcePermissionLevel?

<!-- -->

: ACTOR\_PERMISSION\_LEVEL

Override the Actor's permissions for this run. If not set, the Actor will run with permissions configured in the Actor settings.

### [**](#maxItems)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L639)optionalmaxItems

**maxItems?

<!-- -->

: number

Specifies the maximum number of dataset items that will be charged for pay-per-result Actors. This does NOT guarantee that the Actor will return only this many items. It only ensures you won't be charged for more than this number of items. Only works for pay-per-result Actors. Value can be accessed in the Actor run using `ACTOR_MAX_PAID_DATASET_ITEMS` environment variable.

### [**](#maxTotalChargeUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L647)optionalmaxTotalChargeUsd

**maxTotalChargeUsd?

<!-- -->

: number

Specifies the maximum cost of the Actor run. This parameter is used only for pay-per-event Actors. It allows you to limit the amount charged to your subscription. You can access the maximum cost in your Actor by using the `ACTOR_MAX_TOTAL_CHARGE_USD` environment variable.

### [**](#memory)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L608)optionalmemory

**memory?

<!-- -->

: number

Memory in megabytes which will be allocated for the new Actor run. If not provided, the run uses memory of the default Actor run configuration.

### [**](#restartOnError)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L652)optionalrestartOnError

**restartOnError?

<!-- -->

: boolean

Determines whether the run will be restarted if it fails.

### [**](#timeout)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L613)optionaltimeout

**timeout?

<!-- -->

: number

Timeout for the Actor run in seconds. Zero value means there is no timeout. If not provided, the run uses timeout of the default Actor run configuration.

### [**](#waitForFinish)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L623)optionalwaitForFinish

**waitForFinish?

<!-- -->

: number

Maximum time to wait for the Actor run to finish, in seconds. If the limit is reached, the returned promise is resolved to a run object that will have status `READY` or `RUNNING` and it will not contain the Actor run output. By default (or when `waitForFinish` is set to `0`), the function resolves immediately without waiting. The wait is limited to 60s and happens on the API directly, as opposed to the `call` method and its `waitSecs` option, which is implemented via polling on the client side instead (and has no limit like that).

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L630)optionalwebhooks

**webhooks?

<!-- -->

: readonly

<!-- -->

[WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)\[]

Specifies optional webhooks associated with the Actor run, which can be used to receive a notification e.g. when the Actor finished or failed, see [ad hook webhooks documentation](https://docs.apify.com/webhooks/ad-hoc-webhooks) for detailed description.
