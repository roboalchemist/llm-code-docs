# Source: https://docs.apify.com/api/client/python/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/DatasetClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetClient.md

# DatasetClient<!-- --> \<Data>

### Hierarchy

* ResourceClient
  * *DatasetClient*

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

* [**createItemsPublicUrl](#createItemsPublicUrl)
* [**delete](#delete)
* [**downloadItems](#downloadItems)
* [**get](#get)
* [**getStatistics](#getStatistics)
* [**listItems](#listItems)
* [**pushItems](#pushItems)
* [**update](#update)

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

### [**](#createItemsPublicUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L181)createItemsPublicUrl

* ****createItemsPublicUrl**(options): Promise\<string>

- Generates a URL that can be used to access dataset items.

  If the client has permission to access the dataset's URL signing key, the URL will include a signature which will allow the link to work even without authentication.

  You can optionally control how long the signed URL should be valid using the `expiresInSecs` option. This value sets the expiration duration in seconds from the time the URL is generated. If not provided, the URL will not expire.

  Any other options (like `limit` or `prefix`) will be included as query parameters in the URL.

  ***

  #### Parameters

  * ##### options: [DatasetClientCreateItemsUrlOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientCreateItemsUrlOptions.md) = <!-- -->{}

  #### Returns Promise\<string>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L50)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/datasets/dataset/delete-dataset>

  ***

  #### Returns Promise\<void>

### [**](#downloadItems)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L91)downloadItems

* ****downloadItems**(format, options): Promise\<Buffer>

- Unlike `listItems` which returns a PaginationList with an array of individual dataset items, `downloadItems` returns the items serialized to the provided format. <https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items>

  ***

  #### Parameters

  * ##### format: [DownloadItemsFormat](https://docs.apify.com/api/client/js/api/client/js/reference/enum/DownloadItemsFormat.md)
  * ##### options: [DatasetClientDownloadItemsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientDownloadItemsOptions.md) = <!-- -->{}

  #### Returns Promise\<Buffer>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L34)get

* ****get**(): Promise\<undefined | [Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

- <https://docs.apify.com/api/v2#/reference/datasets/dataset/get-dataset>

  ***

  #### Returns Promise\<undefined | [Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

### [**](#getStatistics)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L153)getStatistics

* ****getStatistics**(): Promise\<undefined | [DatasetStatistics](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetStatistics.md)>

- <https://docs.apify.com/api/v2#tag/DatasetsStatistics/operation/dataset_statistics_get>

  ***

  #### Returns Promise\<undefined | [DatasetStatistics](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetStatistics.md)>

### [**](#listItems)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L57)listItems

* ****listItems**(options): Promise<[PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md)\<Data>>

- <https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items>

  ***

  #### Parameters

  * ##### options: [DatasetClientListItemOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientListItemOptions.md) = <!-- -->{}

  #### Returns Promise<[PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md)\<Data>>

### [**](#pushItems)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L134)pushItems

* ****pushItems**(items): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/datasets/item-collection/put-items>

  ***

  #### Parameters

  * ##### items: string | Data | string\[] | Data\[]

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/dataset.ts#L41)update

* ****update**(newFields): Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

- <https://docs.apify.com/api/v2#/reference/datasets/dataset/update-dataset>

  ***

  #### Parameters

  * ##### newFields: [DatasetClientUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientUpdateOptions.md)

  #### Returns Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>
