# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/KeyValueStoreCollectionClient.md

# KeyValueStoreCollectionClient<!-- -->

Client for managing the collection of Key-value stores in your account.

Key-value stores are used to store arbitrary data records or files. This client provides methods to list, create, or get key-value stores by name.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const storesClient = client.keyValueStores();

  // List all key-value stores
  const { items } = await storesClient.list();

  // Get or create a key-value store by name
  const store = await storesClient.getOrCreate('my-store');
  ```

* **@see**

  <https://docs.apify.com/platform/storage/key-value-store>

### Hierarchy

* ResourceCollectionClient
  * *KeyValueStoreCollectionClient*

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

### [**](#getOrCreate)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store_collection.ts#L83)getOrCreate

* ****getOrCreate**(name, options): Promise<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

- Gets or creates a key-value store with the specified name.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-stores-post>

  ***

  #### Parameters

  * ##### optionalname: string

    Name of the key-value store. If not provided, a default store is used.

  * ##### optionaloptions: [KeyValueStoreCollectionClientGetOrCreateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreCollectionClientGetOrCreateOptions.md)

    Additional options like schema.

  #### Returns Promise<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

  The key-value store object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store_collection.ts#L59)list

* ****list**(options): Promise<[KeyValueStoreCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#KeyValueStoreCollectionListResult)> & AsyncIterable<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md), any, any>

- Lists all Key-value stores.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/key-value-stores-get>

  ***

  #### Parameters

  * ##### options: [KeyValueStoreCollectionClientListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreCollectionClientListOptions.md) = <!-- -->{}

    Pagination options.

  #### Returns Promise<[KeyValueStoreCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#KeyValueStoreCollectionListResult)> & AsyncIterable<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md), any, any>

  A paginated iterator of Key-value stores.
