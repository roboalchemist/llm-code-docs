# Source: https://docs.apify.com/api/client/python/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/BuildClient.md

# BuildClient<!-- -->

Client for managing a specific Actor build.

Builds are created when an Actor is built from source code. This client provides methods to get build details, wait for the build to finish, abort it, and access its logs.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const buildClient = client.build('my-build-id');

  // Get build details
  const build = await buildClient.get();

  // Wait for the build to finish
  const finishedBuild = await buildClient.waitForFinish();

  // Access build logs
  const log = await buildClient.log().get();
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running/runs-and-builds#builds>

### Hierarchy

* ResourceClient
  * *BuildClient*

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
* [**delete](#delete)
* [**get](#get)
* [**getOpenApiDefinition](#getOpenApiDefinition)
* [**log](#log)
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

### [**](#abort)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L87)abort

* ****abort**(): Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- Aborts the Actor build.

  Stops the build process immediately. The build will have an `ABORTED` status.

  * **@see**

    <https://docs.apify.com/api/v2/actor-build-abort-post>

  * **@example**

    ```
    await client.build('build-id').abort();
    ```

  ***

  #### Returns Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

  The updated Build object with `ABORTED` status

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L102)delete

* ****delete**(): Promise\<void>

- Deletes the Actor build.

  * **@see**

    <https://docs.apify.com/api/v2/actor-build-delete>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L63)get

* ****get**(options): Promise\<undefined | [Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- Gets the Actor build object from the Apify API.

  * **@see**

    <https://docs.apify.com/api/v2/actor-build-get>

  * **@example**

    ```
    // Get build status immediately
    const build = await client.build('build-id').get();
    console.log(`Status: ${build.status}`);

    // Wait up to 60 seconds for build to finish
    const build = await client.build('build-id').get({ waitForFinish: 60 });
    ```

  ***

  #### Parameters

  * ##### options: [BuildClientGetOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildClientGetOptions.md) = <!-- -->{}

    Get options

  #### Returns Promise\<undefined | [Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

  The Build object, or `undefined` if it does not exist

### [**](#getOpenApiDefinition)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L112)getOpenApiDefinition

* ****getOpenApiDefinition**(): Promise<[OpenApiDefinition](https://docs.apify.com/api/client/js/api/client/js/reference/interface/OpenApiDefinition.md)>

- Retrieves the OpenAPI definition for the Actor build.

  * **@see**

    <https://docs.apify.com/api/v2/actor-build-openapi-json-get>

  ***

  #### Returns Promise<[OpenApiDefinition](https://docs.apify.com/api/client/js/api/client/js/reference/interface/OpenApiDefinition.md)>

  The OpenAPI definition object.

### [**](#log)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L176)log

* ****log**(): [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

- Returns a client for accessing the log of this Actor build.

  * **@see**

    <https://docs.apify.com/api/v2/actor-build-log-get>

  * **@example**

    ```
    // Get build log
    const log = await client.build('build-id').log().get();
    console.log(log);
    ```

  ***

  #### Returns [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

  A client for accessing the build's log

### [**](#waitForFinish)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build.ts#L152)waitForFinish

* ****waitForFinish**(options): Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- Waits for the Actor build to finish and returns the finished Build object.

  The promise resolves when the build reaches a terminal state (`SUCCEEDED`, `FAILED`, `ABORTED`, or `TIMED-OUT`). If `waitSecs` is provided and the timeout is reached, the promise resolves with the unfinished Build object (status will be `RUNNING` or `READY`). The promise is NOT rejected based on build status.

  Unlike the `waitForFinish` parameter in get, this method can wait indefinitely by polling the build status. It uses the `waitForFinish` parameter internally (max 60s per call) and continuously polls until the build finishes or the timeout is reached.

  This is useful when you need to immediately start a run after a build finishes.

  * **@example**

    ```
    // Wait indefinitely for build to finish
    const build = await client.build('build-id').waitForFinish();
    console.log(`Build finished with status: ${build.status}`);

    // Start a run immediately after build succeeds
    const build = await client.build('build-id').waitForFinish();
    if (build.status === 'SUCCEEDED') {
      const run = await client.actor('my-actor').start();
    }
    ```

  ***

  #### Parameters

  * ##### options: [BuildClientWaitForFinishOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildClientWaitForFinishOptions.md) = <!-- -->{}

    Wait options

  #### Returns Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

  The Build object (finished or still building if timeout was reached)
