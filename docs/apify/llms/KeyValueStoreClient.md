# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient.md

# KeyValueStoreClient<!-- -->

Client for managing a specific key-value store.

Key-value stores are used to store arbitrary data records or files. Each record is identified by a unique key and can contain any type of data. This client provides methods to get, set, and delete records, list keys, and manage the store.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const storeClient = client.keyValueStore('my-store-id');

  // Set a record
  await storeClient.setRecord({
    key: 'OUTPUT',
    value: { foo: 'bar' },
    contentType: 'application/json'
  });

  // Get a record
  const record = await storeClient.getRecord('OUTPUT');

  // List all keys
  const { items } = await storeClient.listKeys();
  ```

* **@see**

  <https://docs.apify.com/platform/storage/key-value-store>

### Hierarchy

* ResourceClient
  * *KeyValueStoreClient*

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

* [**createKeysPublicUrl](#createKeysPublicUrl)
* [**delete](#delete)
* [**deleteRecord](#deleteRecord)
* [**get](#get)
* [**getRecord](#getRecord)
* [**getRecordPublicUrl](#getRecordPublicUrl)
* [**listKeys](#listKeys)
* [**recordExists](#recordExists)
* [**setRecord](#setRecord)
* [**update](#update)

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

### [**](#createKeysPublicUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L250)createKeysPublicUrl

* ****createKeysPublicUrl**(options): Promise\<string>

- Generates a public URL for accessing the list of keys in the key-value store.

  If the client has permission to access the key-value store's URL signing key, the URL will include a cryptographic signature which allows access without authentication.

  * **@example**

    ```
    // Create a URL that expires in 1 hour
    const url = await client.keyValueStore('my-store').createKeysPublicUrl({
      expiresInSecs: 3600,
      prefix: 'image-'
    });
    console.log(`Share this URL: ${url}`);
    ```

  ***

  #### Parameters

  * ##### options: [KeyValueClientCreateKeysUrlOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientCreateKeysUrlOptions.md) = <!-- -->{}

    URL generation options (extends all options from listKeys)

  #### Returns Promise\<string>

  A public URL string for accessing the keys list

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L100)delete

* ****delete**(): Promise\<void>

- Deletes the key-value store.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-delete>

  ***

  #### Returns Promise\<void>

### [**](#deleteRecord)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L497)deleteRecord

* ****deleteRecord**(key): Promise\<void>

- Deletes a record from the key-value store.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-record-delete>

  * **@example**

    ```
    await client.keyValueStore('my-store').deleteRecord('temp-data');
    ```

  ***

  #### Parameters

  * ##### key: string

    The record key to delete

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L75)get

* ****get**(): Promise\<undefined | [KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

- Gets the key-value store object from the Apify API.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-get>

  ***

  #### Returns Promise\<undefined | [KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

  The KeyValueStore object, or `undefined` if it does not exist

### [**](#getRecord)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L326)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L328)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L333)getRecord

* ****getRecord**(key): Promise\<undefined | [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)\<JsonValue>>
* ****getRecord**\<Options>(key, options): Promise\<undefined | [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)<[ReturnTypeFromOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#ReturnTypeFromOptions)\<Options>>>

- You can use the `buffer` option to get the value in a Buffer (Node.js) or ArrayBuffer (browser) format. In Node.js (not in browser) you can also use the `stream` option to get a Readable stream.

  When the record does not exist, the function resolves to `undefined`. It does NOT resolve to a `KeyValueStore` record with an `undefined` value.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-record-get>

  ***

  #### Parameters

  * ##### key: string

  #### Returns Promise\<undefined | [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)\<JsonValue>>

### [**](#getRecordPublicUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L213)getRecordPublicUrl

* ****getRecordPublicUrl**(key): Promise\<string>

- Generates a public URL for accessing a specific record in the key-value store.

  If the client has permission to access the key-value store's URL signing key, the URL will include a cryptographic signature for authenticated access without requiring an API token.

  * **@example**

    ```
    const url = await client.keyValueStore('my-store').getRecordPublicUrl('OUTPUT');
    console.log(`Public URL: ${url}`);
    // You can now share this URL or use it in a browser
    ```

  ***

  #### Parameters

  * ##### key: string

    The record key

  #### Returns Promise\<string>

  A public URL string for accessing the record

### [**](#listKeys)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L139)listKeys

* ****listKeys**(options): Promise<[KeyValueClientListKeysResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysResult.md)> & AsyncIterable<[KeyValueListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueListItem.md), any, any>

- Lists all keys in the key-value store.

  Returns a paginated list of all record keys in the store. Use pagination parameters to retrieve large lists efficiently.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-keys-get>

  * **@example**

    ```
    // List all keys
    const { items, isTruncated } = await client.keyValueStore('my-store').listKeys();
    items.forEach(item => console.log(`${item.key}: ${item.size} bytes`));

    // List keys with prefix
    const { items } = await client.keyValueStore('my-store').listKeys({ prefix: 'user-' });

    // Paginate through all keys
    let exclusiveStartKey;
    do {
      const result = await client.keyValueStore('my-store').listKeys({
        limit: 100,
        exclusiveStartKey
      });
      // Process result.items...
      exclusiveStartKey = result.nextExclusiveStartKey;
    } while (result.isTruncated);
    ```

  ***

  #### Parameters

  * ##### options: [KeyValueClientListKeysOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysOptions.md) = <!-- -->{}

    Listing options

  #### Returns Promise<[KeyValueClientListKeysResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysResult.md)> & AsyncIterable<[KeyValueListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueListItem.md), any, any>

  Object containing `items` array of key metadata, pagination info (`count`, `limit`, `isTruncated`, `nextExclusiveStartKey`)

### [**](#recordExists)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L299)recordExists

* ****recordExists**(key): Promise\<boolean>

- Tests whether a record with the given key exists in the key-value store without retrieving its value.

  This is more efficient than getRecord when you only need to check for existence.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-record-get>

  * **@example**

    ```
    const exists = await client.keyValueStore('my-store').recordExists('OUTPUT');
    if (exists) {
      console.log('OUTPUT record exists');
    }
    ```

  ***

  #### Parameters

  * ##### key: string

    The record key to check

  #### Returns Promise\<boolean>

  `true` if the record exists, `false` if it does not

### [**](#setRecord)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L433)setRecord

* ****setRecord**(record, options): Promise\<void>

- Stores a record in the key-value store.

  The record value can be any JSON-serializable object, a string, or a Buffer/Stream. The content type is automatically determined based on the value type, but can be overridden using the `contentType` property.

  **Note about streams:** If the value is a stream object (has `.pipe` and `.on` methods), the upload cannot be retried on failure or follow redirects. For reliable uploads, buffer the entire stream into memory first.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-record-put>

  * **@example**

    ```
    // Store JSON object
    await client.keyValueStore('my-store').setRecord({
      key: 'OUTPUT',
      value: { crawledUrls: 100, items: [...] }
    });

    // Store text
    await client.keyValueStore('my-store').setRecord({
      key: 'README',
      value: 'This is my readme text',
      contentType: 'text/plain'
    });

    // Store binary data
    const imageBuffer = await fetchImageBuffer();
    await client.keyValueStore('my-store').setRecord({
      key: 'screenshot.png',
      value: imageBuffer,
      contentType: 'image/png'
    });
    ```

  ***

  #### Parameters

  * ##### record: [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)\<JsonValue>

    The record to store

  * ##### options: [KeyValueStoreRecordOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecordOptions.md) = <!-- -->{}

    Storage options

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L89)update

* ****update**(newFields): Promise<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

- Updates the key-value store with specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/key-value-store-put>

  ***

  #### Parameters

  * ##### newFields: [KeyValueClientUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientUpdateOptions.md)

    Fields to update in the key-value store

  #### Returns Promise<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

  The updated KeyValueStore object
