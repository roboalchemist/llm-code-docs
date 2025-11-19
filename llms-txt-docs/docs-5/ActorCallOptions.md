# Source: https://docs.apify.com/api/client/js/reference/interface/ActorCallOptions.md

# ActorCallOptions<!-- -->

### Hierarchy

* Omit<[ActorStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStartOptions.md), waitForFinish>
  * *ActorCallOptions*

## Index[**](#Index)

### Properties

* [**build](#build)
* [**contentType](#contentType)
* [**forcePermissionLevel](#forcePermissionLevel)
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

### [**](#contentType)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L376)optionalinheritedcontentType

**contentType?

<!-- -->

: string

Inherited from Omit.contentType

Content type for the `input`. If not specified, `input` is expected to be an object that will be stringified to JSON and content type set to `application/json; charset=utf-8`. If `options.contentType` is specified, then `input` must be a `String` or `Buffer`.

### [**](#forcePermissionLevel)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L424)optionalinheritedforcePermissionLevel

**forcePermissionLevel?

<!-- -->

: string

Inherited from Omit.forcePermissionLevel

Override the Actor's permissions for this run. If not set, the Actor will run with permissions configured in the Actor settings.

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

### [**](#waitSecs)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L428)optionalwaitSecs

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
