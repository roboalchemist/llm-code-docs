# Source: https://docs.apify.com/api/client/js/reference/interface/ActorStartOptions.md

# ActorStartOptions<!-- -->

## Index[**](#Index)

### Properties

* [**build](#build)
* [**contentType](#contentType)
* [**forcePermissionLevel](#forcePermissionLevel)
* [**maxItems](#maxItems)
* [**memory](#memory)
* [**restartOnError](#restartOnError)
* [**timeout](#timeout)
* [**waitForFinish](#waitForFinish)
* [**webhooks](#webhooks)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L368)optionalbuild

**build?

<!-- -->

: string

Tag or number of the actor build to run (e.g. `beta` or `1.2.345`). If not provided, the run uses build tag or number from the default actor run configuration (typically `latest`).

### [**](#contentType)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L376)optionalcontentType

**contentType?

<!-- -->

: string

Content type for the `input`. If not specified, `input` is expected to be an object that will be stringified to JSON and content type set to `application/json; charset=utf-8`. If `options.contentType` is specified, then `input` must be a `String` or `Buffer`.

### [**](#forcePermissionLevel)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L424)optionalforcePermissionLevel

**forcePermissionLevel?

<!-- -->

: string

Override the Actor's permissions for this run. If not set, the Actor will run with permissions configured in the Actor settings.

### [**](#maxItems)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L411)optionalmaxItems

**maxItems?

<!-- -->

: number

Specifies maximum number of items that the actor run should return. This is used by pay per result actors to limit the maximum number of results that will be charged to customer. Value can be accessed in actor run using `ACTOR_MAX_PAID_DATASET_ITEMS` environment variable.

### [**](#memory)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L382)optionalmemory

**memory?

<!-- -->

: number

Memory in megabytes which will be allocated for the new actor run. If not provided, the run uses memory of the default actor run configuration.

### [**](#restartOnError)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L416)optionalrestartOnError

**restartOnError?

<!-- -->

: boolean

Determines whether the run will be restarted if it fails.

### [**](#timeout)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L387)optionaltimeout

**timeout?

<!-- -->

: number

Timeout for the actor run in seconds. Zero value means there is no timeout. If not provided, the run uses timeout of the default actor run configuration.

### [**](#waitForFinish)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L397)optionalwaitForFinish

**waitForFinish?

<!-- -->

: number

Maximum time to wait for the actor run to finish, in seconds. If the limit is reached, the returned promise is resolved to a run object that will have status `READY` or `RUNNING` and it will not contain the actor run output. By default (or when `waitForFinish` is set to `0`), the function resolves immediately without waiting. The wait is limited to 60s and happens on the API directly, as opposed to the `call` method and its `waitSecs` option, which is implemented via polling on the client side instead (and has no limit like that).

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L404)optionalwebhooks

**webhooks?

<!-- -->

: readonly

<!-- -->

[WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)\[]

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed, see [ad hook webhooks documentation](https://docs.apify.com/webhooks/ad-hoc-webhooks) for detailed description.
