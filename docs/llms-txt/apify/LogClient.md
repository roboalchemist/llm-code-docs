# Source: https://docs.apify.com/api/client/python/reference/class/LogClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/LogClient.md

# LogClient<!-- -->

Client for accessing Actor run or build logs.

Provides methods to retrieve logs as text or stream them in real-time. Logs can be accessed for both running and finished Actor runs and builds.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const runClient = client.run('my-run-id');

  // Get the log content
  const log = await runClient.log().get();
  console.log(log);

  // Stream the log in real-time
  const stream = await runClient.log().stream();
  stream.on('line', (line) => console.log(line));
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running/runs-and-builds#logging>

### Hierarchy

* ResourceClient
  * *LogClient*

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

* [**get](#get)
* [**stream](#stream)

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

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L56)get

* ****get**(options): Promise\<undefined | string>

- Retrieves the log as a string.

  * **@see**

    <https://docs.apify.com/api/v2/log-get>

  ***

  #### Parameters

  * ##### options: [LogOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/LogOptions.md) = <!-- -->{}

    Log retrieval options.

  #### Returns Promise\<undefined | string>

  The log content as a string, or `undefined` if it does not exist.

### [**](#stream)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/log.ts#L81)stream

* ****stream**(options): Promise\<undefined | Readable>

- Retrieves the log as a Readable stream. Only works in Node.js.

  * **@see**

    <https://docs.apify.com/api/v2/log-get>

  ***

  #### Parameters

  * ##### options: [LogOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/LogOptions.md) = <!-- -->{}

    Log retrieval options.

  #### Returns Promise\<undefined | Readable>

  The log content as a Readable stream, or `undefined` if it does not exist.
