# Source: https://docs.apify.com/api/client/python/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetCollectionClient.md

# DatasetCollectionClient<!-- -->

### Hierarchy

* ResourceCollectionClient
  * *DatasetCollectionClient*

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

* [**getOrCreate](#getOrCreate)
* [**list](#list)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L35)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L27)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L37)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L23)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L39)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L29)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L31)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L25)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L33)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#getOrCreate)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset_collection.ts#L39)getOrCreate

* ****getOrCreate**(name, options): Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

- <https://docs.apify.com/api/v2#/reference/datasets/dataset-collection/create-dataset>

  ***

  #### Parameters

  * ##### optionalname: string
  * ##### optionaloptions: [DatasetCollectionClientGetOrCreateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetCollectionClientGetOrCreateOptions.md)

  #### Returns Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset_collection.ts#L22)list

* ****list**(options): Promise<[DatasetCollectionClientListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#DatasetCollectionClientListResult)>

- <https://docs.apify.com/api/v2#/reference/datasets/dataset-collection/get-list-of-datasets>

  ***

  #### Parameters

  * ##### options: [DatasetCollectionClientListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetCollectionClientListOptions.md) = <!-- -->{}

  #### Returns Promise<[DatasetCollectionClientListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#DatasetCollectionClientListResult)>
