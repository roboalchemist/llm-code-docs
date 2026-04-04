# Source: https://docs.apify.com/api/client/python/reference/class/ActorClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorClient.md

# ActorClient<!-- -->

Client for managing a specific Actor.

Provides methods to start, call, build, update, and delete an Actor, as well as manage its versions, builds, runs, and webhooks.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const actorClient = client.actor('my-actor-id');

  // Start an Actor
  const run = await actorClient.start(input, { memory: 256 });

  // Call an Actor and wait for it to finish
  const finishedRun = await actorClient.call({ url: 'https://example.com' });
  ```

* **@see**

  <https://docs.apify.com/platform/actors>

### Hierarchy

* ResourceClient
  * *ActorClient*

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

* [**build](#build)
* [**builds](#builds)
* [**call](#call)
* [**defaultBuild](#defaultBuild)
* [**delete](#delete)
* [**get](#get)
* [**lastRun](#lastRun)
* [**runs](#runs)
* [**start](#start)
* [**update](#update)
* [**version](#version)
* [**versions](#versions)
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

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L287)build

* ****build**(versionNumber, options): Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- Builds the Actor.

  Creates a new build of the specified Actor version. The build compiles the Actor's source code, installs dependencies, and prepares it for execution.

  * **@see**

    <https://docs.apify.com/api/v2/act-builds-post>

  * **@example**

    ```
    // Start a build and return immediately
    const build = await client.actor('my-actor').build('0.1');
    console.log(`Build ${build.id} started with status: ${build.status}`);

    // Build and wait up to 120 seconds for it to finish
    const build = await client.actor('my-actor').build('0.1', {
      waitForFinish: 120,
      tag: 'latest',
      useCache: true
    });
    ```

  ***

  #### Parameters

  * ##### versionNumber: string

    Version number or tag to build (e.g., `'0.1'`, `'0.2'`, `'latest'`)

  * ##### options: [ActorBuildOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorBuildOptions.md) = <!-- -->{}

    Build configuration options

  #### Returns Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

  The Build object with status and build details

### [**](#builds)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L377)builds

* ****builds**(): [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

- Returns a client for managing builds of this Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-builds-get>

  ***

  #### Returns [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

  A client for the Actor's build collection

### [**](#call)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L220)call

* ****call**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts the Actor and waits for it to finish before returning the Run object.

  This is a convenience method that starts the Actor run and waits for its completion by polling the run status. It optionally streams logs to the console or a custom Log instance. By default, it waits indefinitely unless the `waitSecs` option is provided.

  * **@see**

    <https://docs.apify.com/api/v2/act-runs-post>

  * **@example**

    ```
    // Run an Actor and wait for it to finish
    const run = await client.actor('my-actor').call({ url: 'https://example.com' });
    console.log(`Run finished with status: ${run.status}`);
    console.log(`Dataset ID: ${run.defaultDatasetId}`);

    // Run with a timeout and log streaming to console
    const run = await client.actor('my-actor').call(
      { url: 'https://example.com' },
      { waitSecs: 300, log: 'default' }
    );

    // Run with custom log instance
    import { Log } from '@apify/log';
    const log = new Log({ prefix: 'My Actor' });
    const run = await client.actor('my-actor').call({ url: 'https://example.com' }, { log });
    ```

  ***

  #### Parameters

  * ##### optionalinput: unknown

    Input for the Actor. Can be any JSON-serializable value (object, array, string, number). If `contentType` is specified in options, input should be a string or Buffer.

  * ##### options: [ActorCallOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCallOptions.md) = <!-- -->{}

    Run configuration options (extends all options from start)

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The finished Actor run object with final status (`SUCCEEDED`, `FAILED`, `ABORTED`, or `TIMED-OUT`)

### [**](#defaultBuild)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L318)defaultBuild

* ****defaultBuild**(options): Promise<[BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)>

- Retrieves the default build of the Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-build-default-get>

  ***

  #### Parameters

  * ##### options: [BuildClientGetOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildClientGetOptions.md) = <!-- -->{}

    Options for getting the build.

  #### Returns Promise<[BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)>

  A client for the default build.

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L81)delete

* ****delete**(): Promise\<void>

- Deletes the Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-delete>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L59)get

* ****get**(): Promise\<undefined | [Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

- Gets the Actor object from the Apify API.

  * **@see**

    <https://docs.apify.com/api/v2/act-get>

  ***

  #### Returns Promise\<undefined | [Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

  The Actor object, or `undefined` if it does not exist

### [**](#lastRun)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L353)lastRun

* ****lastRun**(options): [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

- Returns a client for the last run of this Actor.

  Provides access to the most recent Actor run, optionally filtered by status or origin.

  * **@see**

    <https://docs.apify.com/api/v2/act-runs-last-get>

  * **@example**

    ```
    // Get the last successful run
    const lastRun = await client.actor('my-actor').lastRun({ status: 'SUCCEEDED' }).get();
    ```

  ***

  #### Parameters

  * ##### options: [ActorLastRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorLastRunOptions.md) = <!-- -->{}

    Options to filter the last run

  #### Returns [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

  A client for the last run

### [**](#runs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L391)runs

* ****runs**(): [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

- Returns a client for managing runs of this Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-runs-get>

  ***

  #### Returns [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

  A client for the Actor's run collection

### [**](#start)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L119)start

* ****start**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts the Actor and immediately returns the Run object.

  The Actor run can be configured with optional input and various options. The run starts asynchronously and this method returns immediately without waiting for completion. Use the call method if you want to wait for the Actor to finish.

  * **@see**

    <https://docs.apify.com/api/v2/act-runs-post>

  * **@example**

    ```
    // Start Actor with simple input
    const run = await client.actor('my-actor').start({ url: 'https://example.com' });
    console.log(`Run started with ID: ${run.id}, status: ${run.status}`);

    // Start Actor with specific build and memory
    const run = await client.actor('my-actor').start(
      { url: 'https://example.com' },
      { build: '0.1.2', memory: 512, timeout: 300 }
    );
    ```

  ***

  #### Parameters

  * ##### optionalinput: unknown

    Input for the Actor. Can be any JSON-serializable value (object, array, string, number). If `contentType` is specified in options, input should be a string or Buffer.

  * ##### options: [ActorStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStartOptions.md) = <!-- -->{}

    Run configuration options

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

  The Actor run object with status, usage, and storage IDs

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L70)update

* ****update**(newFields): Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

- Updates the Actor with specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/act-put>

  ***

  #### Parameters

  * ##### newFields: Partial\<Pick<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md), name | description | isPublic | isDeprecated | seoTitle | seoDescription | title | restartOnError | versions | categories | defaultRunOptions | actorStandby | actorPermissionLevel | taggedBuilds>>

    Fields to update in the Actor

  #### Returns Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

  The updated Actor object

### [**](#version)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L406)version

* ****version**(versionNumber): [ActorVersionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionClient.md)

- Returns a client for a specific version of this Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-version-get>

  ***

  #### Parameters

  * ##### versionNumber: string

    Version number (e.g., '0.1', '1.2.3')

  #### Returns [ActorVersionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionClient.md)

  A client for the specified Actor version

### [**](#versions)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L421)versions

* ****versions**(): [ActorVersionCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionCollectionClient.md)

- Returns a client for managing versions of this Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-versions-get>

  ***

  #### Returns [ActorVersionCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionCollectionClient.md)

  A client for the Actor's version collection

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L431)webhooks

* ****webhooks**(): [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

- Returns a client for managing webhooks associated with this Actor.

  * **@see**

    <https://docs.apify.com/api/v2/act-webhooks-get>

  ***

  #### Returns [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

  A client for the Actor's webhook collection
