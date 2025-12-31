# Source: https://docs.apify.com/api/client/python/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/BuildClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/BuildClient.md

# BuildClient<!-- -->

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

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L35)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L27)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L37)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L23)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L39)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L29)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L31)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L25)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L33)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#abort)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L39)abort

* ****abort**(): Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- <https://docs.apify.com/api/v2#/reference/actor-builds/abort-build/abort-build>

  ***

  #### Returns Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L52)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/actor-builds/delete-build/delete-build>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L25)get

* ****get**(options): Promise\<undefined | [Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- <https://docs.apify.com/api/v2#/reference/actor-builds/build-object/get-build>

  ***

  #### Parameters

  * ##### options: [BuildClientGetOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildClientGetOptions.md) = <!-- -->{}

  #### Returns Promise\<undefined | [Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

### [**](#getOpenApiDefinition)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L59)getOpenApiDefinition

* ****getOpenApiDefinition**(): Promise<[OpenApiDefinition](https://docs.apify.com/api/client/js/api/client/js/reference/interface/OpenApiDefinition.md)>

- <https://docs.apify.com/api/v2/actor-build-openapi-json-get>

  ***

  #### Returns Promise<[OpenApiDefinition](https://docs.apify.com/api/client/js/api/client/js/reference/interface/OpenApiDefinition.md)>

### [**](#log)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L94)log

* ****log**(): [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-builds/build-log>

  ***

  #### Returns [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

### [**](#waitForFinish)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/build.ts#L80)waitForFinish

* ****waitForFinish**(options): Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- Returns a promise that resolves with the finished Build object when the provided actor build finishes or with the unfinished Build object when the `waitSecs` timeout lapses. The promise is NOT rejected based on run status. You can inspect the `status` property of the Build object to find out its status.

  The difference between this function and the `waitForFinish` parameter of the `get` method is the fact that this function can wait indefinitely. Its use is preferable to the `waitForFinish` parameter alone, which it uses internally.

  This is useful when you need to immediately start a run after a build finishes.

  ***

  #### Parameters

  * ##### options: [BuildClientWaitForFinishOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildClientWaitForFinishOptions.md) = <!-- -->{}

  #### Returns Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>
