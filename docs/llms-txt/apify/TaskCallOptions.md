# Source: https://docs.apify.com/api/client/js/reference/interface/TaskCallOptions.md

# TaskCallOptions<!-- -->

Options for calling a Task and waiting for it to finish.

### Hierarchy

* Omit<[TaskStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#TaskStartOptions), waitForFinish>
  * *TaskCallOptions*

## Index[**](#Index)

### Properties

* [**build](#build)
* [**maxItems](#maxItems)
* [**maxTotalChargeUsd](#maxTotalChargeUsd)
* [**memory](#memory)
* [**restartOnError](#restartOnError)
* [**timeout](#timeout)
* [**waitSecs](#waitSecs)
* [**webhooks](#webhooks)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L594)optionalinheritedbuild

**build?

<!-- -->

: string

Inherited from Omit.build

Tag or number of the Actor build to run (e.g. `beta` or `1.2.345`). If not provided, the run uses build tag or number from the default Actor run configuration (typically `latest`).

### [**](#maxItems)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L639)optionalinheritedmaxItems

**maxItems?

<!-- -->

: number

Inherited from Omit.maxItems

Specifies the maximum number of dataset items that will be charged for pay-per-result Actors. This does NOT guarantee that the Actor will return only this many items. It only ensures you won't be charged for more than this number of items. Only works for pay-per-result Actors. Value can be accessed in the Actor run using `ACTOR_MAX_PAID_DATASET_ITEMS` environment variable.

### [**](#maxTotalChargeUsd)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L647)optionalinheritedmaxTotalChargeUsd

**maxTotalChargeUsd?

<!-- -->

: number

Inherited from Omit.maxTotalChargeUsd

Specifies the maximum cost of the Actor run. This parameter is used only for pay-per-event Actors. It allows you to limit the amount charged to your subscription. You can access the maximum cost in your Actor by using the `ACTOR_MAX_TOTAL_CHARGE_USD` environment variable.

### [**](#memory)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L608)optionalinheritedmemory

**memory?

<!-- -->

: number

Inherited from Omit.memory

Memory in megabytes which will be allocated for the new Actor run. If not provided, the run uses memory of the default Actor run configuration.

### [**](#restartOnError)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L652)optionalinheritedrestartOnError

**restartOnError?

<!-- -->

: boolean

Inherited from Omit.restartOnError

Determines whether the run will be restarted if it fails.

### [**](#timeout)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L613)optionalinheritedtimeout

**timeout?

<!-- -->

: number

Inherited from Omit.timeout

Timeout for the Actor run in seconds. Zero value means there is no timeout. If not provided, the run uses timeout of the default Actor run configuration.

### [**](#waitSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L341)optionalwaitSecs

**waitSecs?

<!-- -->

: number

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L630)optionalinheritedwebhooks

**webhooks?

<!-- -->

: readonly

<!-- -->

[WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)\[]

Inherited from Omit.webhooks

Specifies optional webhooks associated with the Actor run, which can be used to receive a notification e.g. when the Actor finished or failed, see [ad hook webhooks documentation](https://docs.apify.com/webhooks/ad-hoc-webhooks) for detailed description.
