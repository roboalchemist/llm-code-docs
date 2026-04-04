# Source: https://docs.apify.com/sdk/js/reference/class/ApifyClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ApifyClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ApifyClient.md

# ApifyClient<!-- -->

The official JavaScript client for the Apify API.

Provides programmatic access to all Apify platform resources including Actors, runs, datasets, key-value stores, request queues, and more. Works in both Node.js and browser environments.

* **@example**

  ```
  import { ApifyClient } from 'apify-client';

  const client = new ApifyClient({ token: 'my-token' });

  // Start an Actor and wait for it to finish
  const run = await client.actor('my-actor-id').call();

  // Fetch dataset items
  const { items } = await client.dataset(run.defaultDatasetId).listItems();
  ```

* **@see**

  <https://docs.apify.com/api/v2>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**baseUrl](#baseUrl)
* [**httpClient](#httpClient)
* [**logger](#logger)
* [**publicBaseUrl](#publicBaseUrl)
* [**stats](#stats)
* [**token](#token)

### Methods

* [**actor](#actor)
* [**actors](#actors)
* [**build](#build)
* [**builds](#builds)
* [**dataset](#dataset)
* [**datasets](#datasets)
* [**keyValueStore](#keyValueStore)
* [**keyValueStores](#keyValueStores)
* [**log](#log)
* [**requestQueue](#requestQueue)
* [**requestQueues](#requestQueues)
* [**run](#run)
* [**runs](#runs)
* [**schedule](#schedule)
* [**schedules](#schedules)
* [**setStatusMessage](#setStatusMessage)
* [**store](#store)
* [**task](#task)
* [**tasks](#tasks)
* [**user](#user)
* [**webhook](#webhook)
* [**webhookDispatch](#webhookDispatch)
* [**webhookDispatches](#webhookDispatches)
* [**webhooks](#webhooks)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L72)constructor

* ****new ApifyClient**(options): [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

- #### Parameters

  * ##### options: [ApifyClientOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ApifyClientOptions.md) = <!-- -->{}

  #### Returns [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

## Properties<!-- -->[**](#Properties)

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L60)baseUrl

**baseUrl: string

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L70)httpClient

**httpClient: HttpClient

### [**](#logger)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L68)logger

**logger: Log

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L62)publicBaseUrl

**publicBaseUrl: string

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L66)stats

**stats: Statistics

### [**](#token)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L64)optionaltoken

**token?

<!-- -->

: string

## Methods<!-- -->[**](#Methods)

### [**](#actor)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L155)actor

* ****actor**(id): [ActorClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorClient.md)

- Returns a client for a specific Actor.

  Use this to get, update, delete, start, or call an Actor, as well as manage its builds, runs, versions, and webhooks.

  * **@see**

    <https://docs.apify.com/api/v2/act-get>

  * **@example**

    ```
    // Call an Actor and wait for it to finish
    const run = await client.actor('apify/web-scraper').call({ url: 'https://example.com' });
    ```

  ***

  #### Parameters

  * ##### id: string

    Actor ID or username/name

  #### Returns [ActorClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorClient.md)

  A client for the specific Actor

### [**](#actors)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L135)actors

* ****actors**(): [ActorCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorCollectionClient.md)

- Returns a client for managing Actors in your account.

  Provides access to the Actor collection, allowing you to list, create, and search for Actors.

  * **@see**

    <https://docs.apify.com/api/v2/acts-get>

  ***

  #### Returns [ActorCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorCollectionClient.md)

  A client for the Actors collection

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L185)build

* ****build**(id): [BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)

- Returns a client for a specific Actor build.

  Use this to get details about a build, wait for it to finish, or access its logs.

  * **@see**

    <https://docs.apify.com/api/v2/actor-build-get>

  ***

  #### Parameters

  * ##### id: string

    Build ID

  #### Returns [BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)

  A client for the specified build

### [**](#builds)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L172)builds

* ****builds**(): [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

- Returns a client for managing Actor builds in your account.

  Lists all builds across all of your Actors.

  * **@see**

    <https://docs.apify.com/api/v2/actor-builds-get>

  ***

  #### Returns [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

  A client for Actor builds collection

### [**](#dataset)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L229)dataset

* ****dataset**\<Data>(id): [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Data>

- Returns a client for a specific dataset.

  Use this to read, write, and manage items in the dataset. Datasets contain structured data stored as individual items (records).

  * **@see**

    <https://docs.apify.com/api/v2/dataset-get>

  * **@example**

    ```
    // Push items to a dataset
    await client.dataset('my-dataset').pushItems([
      { url: 'https://example.com', title: 'Example' },
      { url: 'https://test.com', title: 'Test' }
    ]);

    // Retrieve items
    const { items } = await client.dataset('my-dataset').listItems();
    ```

  ***

  #### Parameters

  * ##### id: string

    Dataset ID or name

  #### Returns [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Data>

  A client for the specific Dataset

### [**](#datasets)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L202)datasets

* ****datasets**(): [DatasetCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetCollectionClient.md)

- Returns a client for managing datasets in your account.

  Datasets store structured data results from Actor runs. Use this to list or create datasets.

  * **@see**

    <https://docs.apify.com/api/v2/datasets-get>

  ***

  #### Returns [DatasetCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetCollectionClient.md)

  A client for the Datasets collection

### [**](#keyValueStore)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L271)keyValueStore

* ****keyValueStore**(id): [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

- Returns a client for a specific key-value store.

  Use this to read, write, and delete records in the store. Key-value stores can hold any type of data including text, JSON, images, and other files.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-get>

  * **@example**

    ```
    // Save a record
    await client.keyValueStore('my-store').setRecord({ key: 'OUTPUT', value: { foo: 'bar' } });

    // Get a record
    const record = await client.keyValueStore('my-store').getRecord('OUTPUT');
    ```

  ***

  #### Parameters

  * ##### id: string

    Key-value store ID or name

  #### Returns [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

  A client for the specific key-value store

### [**](#keyValueStores)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L248)keyValueStores

* ****keyValueStores**(): [KeyValueStoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreCollectionClient.md)

- Returns a client for managing key-value stores in your account.

  Key-value stores are used to store arbitrary data records or files.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-stores-get>

  ***

  #### Returns [KeyValueStoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreCollectionClient.md)

  A client for the Key-value stores collection

### [**](#log)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L287)log

* ****log**(buildOrRunId): [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

- Returns a client for accessing logs of an Actor build or run.

  * **@see**

    <https://docs.apify.com/api/v2/log-get>

  ***

  #### Parameters

  * ##### buildOrRunId: string

    Build ID or run ID

  #### Returns [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

  A client for accessing logs

### [**](#requestQueue)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L329)requestQueue

* ****requestQueue**(id, options): [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

- Returns a client for a specific request queue.

  Use this to add, retrieve, and manage requests in the queue. Request queues are used by web crawlers to manage URLs that need to be visited.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-get>

  * **@example**

    ```
    // Add requests to a queue
    const queue = client.requestQueue('my-queue');
    await queue.addRequest({ url: 'https://example.com', uniqueKey: 'example' });

    // Get and lock the next request
    const { items } = await queue.listAndLockHead({ lockSecs: 60 });
    ```

  ***

  #### Parameters

  * ##### id: string

    Request queue ID or name

  * ##### options: [RequestQueueUserOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueUserOptions.md) = <!-- -->{}

    Configuration options for the request queue client

  #### Returns [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

  A client for the specific Request queue

### [**](#requestQueues)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L304)requestQueues

* ****requestQueues**(): [RequestQueueCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueCollectionClient.md)

- Returns a client for managing request queues in your account.

  Request queues store URLs to be crawled, along with their metadata.

  * **@see**

    <https://docs.apify.com/api/v2/request-queues-get>

  ***

  #### Returns [RequestQueueCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueCollectionClient.md)

  A client for the Request queues collection

### [**](#run)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L380)run

* ****run**(id): [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

- Returns a client for a specific Actor run.

  Use this to get details about a run, wait for it to finish, abort it, or access its dataset, key-value store, and request queue.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-get>

  * **@example**

    ```
    // Wait for a run to finish
    const run = await client.run('run-id').waitForFinish();

    // Access run's dataset
    const { items } = await client.run('run-id').dataset().listItems();
    ```

  ***

  #### Parameters

  * ##### id: string

    Run ID

  #### Returns [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

  A client for the specified run

### [**](#runs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L354)runs

* ****runs**(): [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

- Returns a client for managing Actor runs in your account.

  Lists all runs across all of your Actors.

  * **@see**

    <https://docs.apify.com/api/v2/actor-runs-get>

  ***

  #### Returns [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

  A client for the run collection

### [**](#schedule)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L446)schedule

* ****schedule**(id): [ScheduleClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleClient.md)

- Returns a client for a specific schedule.

  Use this to get, update, or delete a schedule.

  * **@see**

    <https://docs.apify.com/api/v2/schedule-get>

  ***

  #### Parameters

  * ##### id: string

    Schedule ID

  #### Returns [ScheduleClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleClient.md)

  A client for the specific Schedule

### [**](#schedules)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L433)schedules

* ****schedules**(): [ScheduleCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleCollectionClient.md)

- Returns a client for managing schedules in your account.

  Schedules automatically start Actor or task runs at specified times.

  * **@see**

    <https://docs.apify.com/api/v2/schedules-get>

  ***

  #### Returns [ScheduleCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleCollectionClient.md)

  A client for the Schedules collection

### [**](#setStatusMessage)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L553)setStatusMessage

* ****setStatusMessage**(message, options): Promise\<void>

- Sets a status message for the current Actor run.

  This is a convenience method that updates the status message of the run specified by the `ACTOR_RUN_ID` environment variable. Only works when called from within an Actor run.

  * **@throws**

    If `ACTOR_RUN_ID` environment variable is not set

  ***

  #### Parameters

  * ##### message: string

    The status message to set

  * ##### optionaloptions: SetStatusMessageOptions

    Additional options for the status message

  #### Returns Promise\<void>

### [**](#store)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L539)store

* ****store**(): [StoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/StoreCollectionClient.md)

- Returns a client for browsing Actors in Apify Store.

  Use this to search and retrieve information about public Actors.

  * **@see**

    <https://docs.apify.com/api/v2/store-actors-get>

  ***

  #### Returns [StoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/StoreCollectionClient.md)

  A client for the Apify Store

### [**](#task)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L416)task

* ****task**(id): [TaskClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskClient.md)

- Returns a client for a specific Actor task.

  Use this to get, update, delete, or run a task with pre-configured input.

  * **@see**

    <https://docs.apify.com/api/v2/actor-task-get>

  * **@example**

    ```
    // Run a task and wait for it to finish
    const run = await client.task('my-task').call();
    ```

  ***

  #### Parameters

  * ##### id: string

    Task ID or username/task-name

  #### Returns [TaskClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskClient.md)

  A client for the specified task

### [**](#tasks)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L397)tasks

* ****tasks**(): [TaskCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskCollectionClient.md)

- Returns a client for managing Actor tasks in your account.

  Tasks are pre-configured Actor runs with stored input that can be executed repeatedly.

  * **@see**

    <https://docs.apify.com/api/v2/actor-tasks-get>

  ***

  #### Returns [TaskCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskCollectionClient.md)

  A client for the task collection

### [**](#user)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L464)user

* ****user**(id): [UserClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/UserClient.md)

- Returns a client for accessing user data.

  By default, returns information about the current user (determined by the API token).

  * **@see**

    <https://docs.apify.com/api/v2/user-get>

  ***

  #### Parameters

  * ##### id: string = <!-- -->ME\_USER\_NAME\_PLACEHOLDER

    User ID or username. Defaults to 'me' (current user)

  #### Returns [UserClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/UserClient.md)

  A client for the user

### [**](#webhook)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L494)webhook

* ****webhook**(id): [WebhookClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookClient.md)

- Returns a client for a specific webhook.

  Use this to get, update, delete, or test a webhook.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-get>

  ***

  #### Parameters

  * ##### id: string

    Webhook ID

  #### Returns [WebhookClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookClient.md)

  A client for the specific webhook

### [**](#webhookDispatch)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L522)webhookDispatch

* ****webhookDispatch**(id): [WebhookDispatchClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchClient.md)

- Returns a client for a specific webhook dispatch.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-dispatch-get>

  ***

  #### Parameters

  * ##### id: string

    Webhook dispatch ID

  #### Returns [WebhookDispatchClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchClient.md)

  A client for the specific webhook dispatch

### [**](#webhookDispatches)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L511)webhookDispatches

* ****webhookDispatches**(): [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

- Returns a client for viewing webhook dispatches in your account.

  Webhook dispatches represent individual invocations of webhooks.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-dispatches-get>

  ***

  #### Returns [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

  A client for the webhook dispatches collection

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/apify_client.ts#L481)webhooks

* ****webhooks**(): [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

- Returns a client for managing webhooks in your account.

  Webhooks notify external services when specific events occur (e.g., Actor run finishes).

  * **@see**

    <https://docs.apify.com/api/v2/webhooks-get>

  ***

  #### Returns [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

  A client for the Webhooks collection
