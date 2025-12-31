# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/KeyValueStoreClient.md

# KeyValueStoreClient<!-- -->

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

### [**](#createKeysPublicUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L122)createKeysPublicUrl

* ****createKeysPublicUrl**(options): Promise\<string>

- Generates a URL that can be used to access key-value store keys.

  If the client has permission to access the key-value store's URL signing key, the URL will include a signature which will allow the link to work even without authentication.

  You can optionally control how long the signed URL should be valid using the `expiresInSecs` option. This value sets the expiration duration in seconds from the time the URL is generated. If not provided, the URL will not expire.

  Any other options (like `limit` or `prefix`) will be included as query parameters in the URL.

  ***

  #### Parameters

  * ##### options: [KeyValueClientCreateKeysUrlOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientCreateKeysUrlOptions.md) = <!-- -->{}

  #### Returns Promise\<string>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L60)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object/delete-store>

  ***

  #### Returns Promise\<void>

### [**](#deleteRecord)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L314)deleteRecord

* ****deleteRecord**(key): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/key-value-stores/record/delete-record>

  ***

  #### Parameters

  * ##### key: string

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L44)get

* ****get**(): Promise\<undefined | [KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

- <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object/get-store>

  ***

  #### Returns Promise\<undefined | [KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

### [**](#getRecord)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L187)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L189)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L194)getRecord

* ****getRecord**(key): Promise\<undefined | [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)\<JsonValue>>
* ****getRecord**\<Options>(key, options): Promise\<undefined | [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)<[ReturnTypeFromOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#ReturnTypeFromOptions)\<Options>>>

- You can use the `buffer` option to get the value in a Buffer (Node.js) or ArrayBuffer (browser) format. In Node.js (not in browser) you can also use the `stream` option to get a Readable stream.

  When the record does not exist, the function resolves to `undefined`. It does NOT resolve to a `KeyValueStore` record with an `undefined` value. <https://docs.apify.com/api/v2#/reference/key-value-stores/record/get-record>

  ***

  #### Parameters

  * ##### key: string

  #### Returns Promise\<undefined | [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)\<JsonValue>>

### [**](#getRecordPublicUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L95)getRecordPublicUrl

* ****getRecordPublicUrl**(key): Promise\<string>

- Generates a URL that can be used to access key-value store record.

  If the client has permission to access the key-value store's URL signing key, the URL will include a signature to verify its authenticity.

  ***

  #### Parameters

  * ##### key: string

  #### Returns Promise\<string>

### [**](#listKeys)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L67)listKeys

* ****listKeys**(options): Promise<[KeyValueClientListKeysResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysResult.md)>

- <https://docs.apify.com/api/v2#/reference/key-value-stores/key-collection/get-list-of-keys>

  ***

  #### Parameters

  * ##### options: [KeyValueClientListKeysOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysOptions.md) = <!-- -->{}

  #### Returns Promise<[KeyValueClientListKeysResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysResult.md)>

### [**](#recordExists)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L161)recordExists

* ****recordExists**(key): Promise\<boolean>

- Tests whether a record with the given key exists in the key-value store without retrieving its value.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/get-record>

  ***

  #### Parameters

  * ##### key: string

    The queried record key.

  #### Returns Promise\<boolean>

  `true` if the record exists, `false` if it does not.

### [**](#setRecord)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L258)setRecord

* ****setRecord**(record, options): Promise\<void>

- The value in the record can be a stream object (detected by having the `.pipe` and `.on` methods). However, note that in that case following redirects or retrying the request if it fails (for example due to rate limiting) isn't possible. If you want to keep that behavior, you need to collect the whole stream contents into a Buffer and then send the full buffer. See [this StackOverflow answer](https://stackoverflow.com/a/14269536/7292139) for an example how to do that.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/put-record>

  ***

  #### Parameters

  * ##### record: [KeyValueStoreRecord](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecord.md)\<JsonValue>
  * ##### options: [KeyValueStoreRecordOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStoreRecordOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/key_value_store.ts#L51)update

* ****update**(newFields): Promise<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>

- <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object/update-store>

  ***

  #### Parameters

  * ##### newFields: [KeyValueClientUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientUpdateOptions.md)

  #### Returns Promise<[KeyValueStore](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueStore.md)>
