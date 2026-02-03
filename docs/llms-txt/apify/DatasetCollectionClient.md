# Source: https://docs.apify.com/api/client/python/reference/class/DatasetCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/DatasetCollectionClient.md

# DatasetCollectionClient<!-- -->

Client for managing the collection of datasets in your account.

Datasets store structured data results from Actor runs. This client provides methods to list, create, or get datasets by name.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const datasetsClient = client.datasets();

  // List all datasets
  const { items } = await datasetsClient.list();

  // Get or create a dataset by name
  const dataset = await datasetsClient.getOrCreate('my-dataset');
  ```

* **@see**

  <https://docs.apify.com/platform/storage/dataset>

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

### [**](#getOrCreate)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset_collection.ts#L83)getOrCreate

* ****getOrCreate**(name, options): Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

- Gets or creates a dataset with the specified name.

  * **@see**

    <https://docs.apify.com/api/v2/datasets-post>

  ***

  #### Parameters

  * ##### optionalname: string

    Name of the dataset. If not provided, a default dataset is used.

  * ##### optionaloptions: [DatasetCollectionClientGetOrCreateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetCollectionClientGetOrCreateOptions.md)

    Additional options like schema.

  #### Returns Promise<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md)>

  The dataset object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset_collection.ts#L59)list

* ****list**(options): Promise<[DatasetCollectionClientListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#DatasetCollectionClientListResult)> & AsyncIterable<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md), any, any>

- Lists all Datasets.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/datasets-get>

  ***

  #### Parameters

  * ##### options: [DatasetCollectionClientListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetCollectionClientListOptions.md) = <!-- -->{}

    Pagination options.

  #### Returns Promise<[DatasetCollectionClientListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#DatasetCollectionClientListResult)> & AsyncIterable<[Dataset](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Dataset.md), any, any>

  A paginated iterator of Datasets.
