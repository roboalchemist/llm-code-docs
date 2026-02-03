# Source: https://docs.apify.com/api/client/js/reference/interface/Task.md

# Task<!-- -->

Represents an Actor task.

Tasks are saved Actor configurations with input and settings that can be executed repeatedly without having to specify the full input each time.

## Index[**](#Index)

### Properties

* [**actId](#actId)
* [**actorStandby](#actorStandby)
* [**createdAt](#createdAt)
* [**description](#description)
* [**id](#id)
* [**input](#input)
* [**modifiedAt](#modifiedAt)
* [**name](#name)
* [**options](#options)
* [**stats](#stats)
* [**title](#title)
* [**userId](#userId)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L285)actId

**actId: string

### [**](#actorStandby)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L295)optionalactorStandby

**actorStandby?

<!-- -->

: Partial<[ActorStandby](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStandby.md)>

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L290)createdAt

**createdAt: Date

### [**](#description)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L288)optionaldescription

**description?

<!-- -->

: string

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L283)id

**id: string

### [**](#input)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L294)optionalinput

**input?

<!-- -->

: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]

### [**](#modifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L291)modifiedAt

**modifiedAt: Date

### [**](#name)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L286)name

**name: string

### [**](#options)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L293)optionaloptions

**options?

<!-- -->

: [TaskOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskOptions.md)

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L292)stats

**stats: [TaskStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskStats.md)

### [**](#title)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L287)optionaltitle

**title?

<!-- -->

: string

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L284)userId

**userId: string

### [**](#username)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L289)optionalusername

**username?

<!-- -->

: string
