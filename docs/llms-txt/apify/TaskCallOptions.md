# Source: https://docs.apify.com/api/client/js/reference/interface/TaskCallOptions.md

# TaskCallOptions<!-- -->

### Hierarchy

* Omit<[TaskStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#TaskStartOptions), waitForFinish>
  * *TaskCallOptions*

## Index[**](#Index)

### Properties

* [**build](#build)
* [**maxItems](#maxItems)
* [**memory](#memory)
* [**restartOnError](#restartOnError)
* [**timeout](#timeout)
* [**waitSecs](#waitSecs)
* [**webhooks](#webhooks)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L368)optionalinheritedbuild

**build?

<!-- -->

: string

Inherited from Omit.build

Tag or number of the actor build to run (e.g. `beta` or `1.2.345`). If not provided, the run uses build tag or number from the default actor run configuration (typically `latest`).

### [**](#maxItems)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L411)optionalinheritedmaxItems

**maxItems?

<!-- -->

: number

Inherited from Omit.maxItems

Specifies maximum number of items that the actor run should return. This is used by pay per result actors to limit the maximum number of results that will be charged to customer. Value can be accessed in actor run using `ACTOR_MAX_PAID_DATASET_ITEMS` environment variable.

### [**](#memory)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L382)optionalinheritedmemory

**memory?

<!-- -->

: number

Inherited from Omit.memory

Memory in megabytes which will be allocated for the new actor run. If not provided, the run uses memory of the default actor run configuration.

### [**](#restartOnError)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L416)optionalinheritedrestartOnError

**restartOnError?

<!-- -->

: boolean

Inherited from Omit.restartOnError

Determines whether the run will be restarted if it fails.

### [**](#timeout)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L387)optionalinheritedtimeout

**timeout?

<!-- -->

: number

Inherited from Omit.timeout

Timeout for the actor run in seconds. Zero value means there is no timeout. If not provided, the run uses timeout of the default actor run configuration.

### [**](#waitSecs)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L242)optionalwaitSecs

**waitSecs?

<!-- -->

: number

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L404)optionalinheritedwebhooks

**webhooks?

<!-- -->

: readonly

<!-- -->

[WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)\[]

Inherited from Omit.webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed, see [ad hook webhooks documentation](https://docs.apify.com/webhooks/ad-hoc-webhooks) for detailed description.
