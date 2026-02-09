# Source: https://docs.apify.com/api/client/python/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RunClient.md

# RunClient<!-- -->

Client for managing a specific Actor run.

Provides methods to get run details, abort, metamorph, resurrect, wait for completion, and access the run's dataset, key-value store, request queue, and logs.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const runClient = client.run('my-run-id');

  // Get run details
  const run = await runClient.get();

  // Wait for the run to finish
  const finishedRun = await runClient.waitForFinish();

  // Access the run's dataset
  const { items } = await runClient.dataset().listItems();
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running/runs-and-builds>

### Hierarchy

* ResourceClient
  * *RunClient*

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

* [**abort](#abort)
* [**charge](#charge)
* [**dataset](#dataset)
* [**delete](#delete)
* [**get](#get)
* [**getStreamedLog](#getStreamedLog)
* [**keyValueStore](#keyValueStore)
* [**log](#log)
* [**metamorph](#metamorph)
* [**reboot](#reboot)
* [**requestQueue](#requestQueue)
* [**resurrect](#resurrect)
* [**update](#update)
* [**waitForFinish](#waitForFinish)

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

### [**](#abort)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L99)abort

* ****abort**(options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Aborts the Actor run.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-abort-post>

  * **@example**

    ```
    // Abort immediately
    await client.run('run-id').abort();

    // Abort gracefully (allows cleanup)
    await client.run('run-id').abort({ gracefully: true });
    ```

  ***

  #### Parameters

  * ##### options: [RunAbortOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunAbortOptions.md) = <!-- -->{}

    Abort options

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The updated ActorRun object with `ABORTING` or `ABORTED` status

### [**](#charge)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L293)charge

* ****charge**(options): Promise\<ApifyResponse\<Record\<string, never>>>

- Charges the Actor run for a specific event.

  * **@see**

    <https://docs.apify.com/api/v2/post-charge-run>

  ***

  #### Parameters

  * ##### options: [RunChargeOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunChargeOptions.md)

    Charge options including event name and count.

  #### Returns Promise\<ApifyResponse\<Record\<string, never>>>

  Empty response object.

### [**](#dataset)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L375)dataset

* ****dataset**(): [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Record\<string | number, unknown>>

- Returns a client for the default dataset of this Actor run.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-get>

  * **@example**

    ```
    // Access run's dataset
    const { items } = await client.run('run-id').dataset().listItems();
    ```

  ***

  #### Returns [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Record\<string | number, unknown>>

  A client for accessing the run's default dataset

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L121)delete

* ****delete**(): Promise\<void>

- Deletes the Actor run.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-delete>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L71)get

* ****get**(options): Promise\<undefined | [ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Gets the Actor run object from the Apify API.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-get>

  * **@example**

    ```
    // Get run status immediately
    const run = await client.run('run-id').get();
    console.log(`Status: ${run.status}`);

    // Wait up to 60 seconds for run to finish
    const run = await client.run('run-id').get({ waitForFinish: 60 });
    ```

  ***

  #### Parameters

  * ##### options: [RunGetOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunGetOptions.md) = <!-- -->{}

    Get options

  #### Returns Promise\<undefined | [ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The ActorRun object, or `undefined` if it does not exist

### [**](#getStreamedLog)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L447)getStreamedLog

* ****getStreamedLog**(options): Promise\<undefined | [StreamedLog](https://docs.apify.com/api/client/js/api/client/js/reference/class/StreamedLog.md)>

- Get StreamedLog for convenient streaming of the run log and their redirection.

  ***

  #### Parameters

  * ##### options: [GetStreamedLogOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/GetStreamedLogOptions.md) = <!-- -->{}

  #### Returns Promise\<undefined | [StreamedLog](https://docs.apify.com/api/client/js/api/client/js/reference/class/StreamedLog.md)>

### [**](#keyValueStore)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L395)keyValueStore

* ****keyValueStore**(): [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

- Returns a client for the default key-value store of this Actor run.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-get>

  * **@example**

    ```
    // Access run's key-value store
    const output = await client.run('run-id').keyValueStore().getRecord('OUTPUT');
    ```

  ***

  #### Returns [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

  A client for accessing the run's default key-value store

### [**](#log)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L436)log

* ****log**(): [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

- Returns a client for accessing the log of this Actor run.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-get>

  * **@example**

    ```
    // Get run log
    const log = await client.run('run-id').log().get();
    console.log(log);
    ```

  ***

  #### Returns [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

  A client for accessing the run's log

### [**](#metamorph)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L150)metamorph

* ****metamorph**(targetActorId, input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Transforms the Actor run into a run of another Actor (metamorph).

  This operation preserves the run ID, storages (dataset, key-value store, request queue), and resource allocation. The run effectively becomes a run of the target Actor with new input. This is useful for chaining Actor executions or implementing complex workflows.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-metamorph-post>

  * **@example**

    ```
    // Transform current run into another Actor
    const metamorphedRun = await client.run('original-run-id').metamorph(
      'target-actor-id',
      { url: 'https://example.com' }
    );
    console.log(`Run ${metamorphedRun.id} is now running ${metamorphedRun.actId}`);
    ```

  ***

  #### Parameters

  * ##### targetActorId: string

    ID or username/name of the target Actor

  * ##### input: unknown

    Input for the target Actor. Can be any JSON-serializable value.

  * ##### options: [RunMetamorphOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunMetamorphOptions.md) = <!-- -->{}

    Metamorph options

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The metamorphed ActorRun object (same ID, but now running the target Actor)

### [**](#reboot)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L205)reboot

* ****reboot**(): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Reboots the Actor run.

  Rebooting restarts the Actor's Docker container while preserving the run ID and storages. This can be useful to recover from certain errors or to force the Actor to restart with a fresh environment.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-reboot-post>

  * **@example**

    ```
    const run = await client.run('run-id').reboot();
    ```

  ***

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The updated ActorRun object

### [**](#requestQueue)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L415)requestQueue

* ****requestQueue**(): [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

- Returns a client for the default Request queue of this Actor run.

  * **@see**

    <https://docs.apify.com/api/v2/actor-run-get>

  * **@example**

    ```
    // Access run's Request queue
    const { items } = await client.run('run-id').requestQueue().listHead();
    ```

  ***

  #### Returns [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

  A client for accessing the run's default Request queue

### [**](#resurrect)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L261)resurrect

* ****resurrect**(options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Resurrects a finished Actor run, starting it again with the same settings.

  This creates a new run with the same configuration as the original run. The original run's storages (dataset, key-value store, request queue) are preserved and reused.

  * **@see**

    <https://docs.apify.com/api/v2/post-resurrect-run>

  * **@example**

    ```
    // Resurrect a failed run with more memory
    const newRun = await client.run('failed-run-id').resurrect({ memory: 2048 });
    console.log(`New run started: ${newRun.id}`);
    ```

  ***

  #### Parameters

  * ##### options: [RunResurrectOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunResurrectOptions.md) = <!-- -->{}

    Resurrection options (override original run settings)

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The new (resurrected) ActorRun object

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L232)update

* ****update**(newFields): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Updates the Actor run with specified fields.

  * **@example**

    ```
    // Set a status message
    await client.run('run-id').update({
      statusMessage: 'Processing items: 50/100'
    });
    ```

  ***

  #### Parameters

  * ##### newFields: [RunUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunUpdateOptions.md)

    Fields to update

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The updated ActorRun object

### [**](#waitForFinish)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L352)waitForFinish

* ****waitForFinish**(options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Waits for the Actor run to finish and returns the finished Run object.

  The promise resolves when the run reaches a terminal state (`SUCCEEDED`, `FAILED`, `ABORTED`, or `TIMED-OUT`). If `waitSecs` is provided and the timeout is reached, the promise resolves with the unfinished Run object (status will be `RUNNING` or `READY`). The promise is NOT rejected based on run status.

  Unlike the `waitForFinish` parameter in get, this method can wait indefinitely by polling the run status. It uses the `waitForFinish` parameter internally (max 60s per call) and continuously polls until the run finishes or the timeout is reached.

  * **@example**

    ```
    // Wait indefinitely for run to finish
    const run = await client.run('run-id').waitForFinish();
    console.log(`Run finished with status: ${run.status}`);

    // Wait up to 5 minutes
    const run = await client.run('run-id').waitForFinish({ waitSecs: 300 });
    if (run.status === 'SUCCEEDED') {
      console.log('Run succeeded!');
    }
    ```

  ***

  #### Parameters

  * ##### options: [RunWaitForFinishOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunWaitForFinishOptions.md) = <!-- -->{}

    Wait options

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The ActorRun object (finished or still running if timeout was reached)
