# Source: https://docs.apify.com/api/client/python/reference/class/TaskClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/TaskClient.md

# TaskClient<!-- -->

Client for managing a specific Actor task.

Tasks are pre-configured Actor runs with saved input and options. This client provides methods to start, call, update, and delete tasks, as well as manage their runs and webhooks.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const taskClient = client.task('my-task-id');

  // Start a task
  const run = await taskClient.start();

  // Call a task and wait for it to finish
  const finishedRun = await taskClient.call();
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running/tasks>

### Hierarchy

* ResourceClient
  * *TaskClient*

## Index[**](#Index)

### Properties

* [**apifyClient](#apifyClient)
* [**baseUrl](#baseUrl)
* [**httpClient](#httpClient)
* [**id](#id)
* [**params](#params)
* [**publicBaseUrl](#publicBaseUrl)
* [**resourcePath](#resourcePath)
* [**safeId](#safeId)
* [**url](#url)

### Methods

* [**call](#call)
* [**delete](#delete)
* [**get](#get)
* [**getInput](#getInput)
* [**lastRun](#lastRun)
* [**runs](#runs)
* [**start](#start)
* [**update](#update)
* [**updateInput](#updateInput)
* [**webhooks](#webhooks)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#call)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L158)call

* ****call**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts a task and waits for it to finish before returning the Run object. It waits indefinitely, unless the `waitSecs` option is provided.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-runs-post>

  ***

  #### Parameters

  * ##### optionalinput: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)

    Input overrides for the task. If not provided, the task's saved input is used.

  * ##### options: [TaskCallOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskCallOptions.md) = <!-- -->{}

    Run and wait options.

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The Actor run object.

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L75)delete

* ****delete**(): Promise\<void>

- Deletes the Task.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-delete>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L53)get

* ****get**(): Promise\<undefined | [Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

- Retrieves the Actor task.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-get>

  ***

  #### Returns Promise\<undefined | [Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

  The task object, or `undefined` if it does not exist.

### [**](#getInput)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L190)getInput

* ****getInput**(): Promise\<undefined | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

- Retrieves the Actor task's input object.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-input-get>

  ***

  #### Returns Promise\<undefined | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

  The Task's input, or `undefined` if it does not exist.

### [**](#lastRun)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L233)lastRun

* ****lastRun**(options): [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

- Returns a client for the last run of this task.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-runs-last-get>

  ***

  #### Parameters

  * ##### options: [TaskLastRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskLastRunOptions.md) = <!-- -->{}

    Filter options for the last run.

  #### Returns [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

  A client for the last run.

### [**](#runs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L257)runs

* ****runs**(): [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

- Returns a client for the Runs of this Task.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-runs-get>

  ***

  #### Returns [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

  A client for the task's runs.

### [**](#start)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L95)start

* ****start**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts an Actor task and immediately returns the Run object.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-runs-post>

  ***

  #### Parameters

  * ##### optionalinput: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)

    Input overrides for the task. If not provided, the task's saved input is used.

  * ##### options: [TaskStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#TaskStartOptions) = <!-- -->{}

    Run options.

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The Actor Run object.

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L64)update

* ****update**(newFields): Promise<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

- Updates the task with the specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-put>

  ***

  #### Parameters

  * ##### newFields: Partial\<Pick<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md), name | description | title | actorStandby | input | options>>

    Fields to update.

  #### Returns Promise<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

  The updated task object.

### [**](#updateInput)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L213)updateInput

* ****updateInput**(newFields): Promise<[Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

- Updates the Actor task's input object.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-input-put>

  ***

  #### Parameters

  * ##### newFields: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]

    New input data for the task.

  #### Returns Promise<[Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

  The updated task input.

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task.ts#L271)webhooks

* ****webhooks**(): [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

- Returns a client for the Webhooks of this Task.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-webhooks-get>

  ***

  #### Returns [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

  A client for the task's webhooks.
