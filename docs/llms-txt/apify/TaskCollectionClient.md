# Source: https://docs.apify.com/api/client/python/reference/class/TaskCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/TaskCollectionClient.md

# TaskCollectionClient<!-- -->

Client for managing the collection of Actor tasks in your account.

Tasks are pre-configured Actor runs with saved input and options. This client provides methods to list and create tasks.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const tasksClient = client.tasks();

  // List all tasks
  const { items } = await tasksClient.list();

  // Create a new task
  const newTask = await tasksClient.create({
    actId: 'my-actor-id',
    name: 'my-task',
    input: { url: 'https://example.com' }
  });
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running/tasks>

### Hierarchy

* ResourceCollectionClient
  * *TaskCollectionClient*

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

* [**create](#create)
* [**list](#list)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task_collection.ts#L83)create

* ****create**(task): Promise<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

- Creates a new task.

  * **@see**

    <https://docs.apify.com/api/v2/actor-tasks-post>

  ***

  #### Parameters

  * ##### task: [TaskCreateData](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskCreateData.md)

    The task data.

  #### Returns Promise<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

  The created task object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/task_collection.ts#L63)list

* ****list**(options): PaginatedIterator<[TaskList](https://docs.apify.com/api/client/js/api/client/js/reference.md#TaskList)>

- Lists all Tasks.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/actor-tasks-get>

  ***

  #### Parameters

  * ##### options: [TaskCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskCollectionListOptions.md) = <!-- -->{}

    Pagination and sorting options.

  #### Returns PaginatedIterator<[TaskList](https://docs.apify.com/api/client/js/api/client/js/reference.md#TaskList)>

  A paginated iterator of tasks.
