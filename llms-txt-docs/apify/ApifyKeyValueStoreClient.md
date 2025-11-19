# Source: https://docs.apify.com/sdk/python/reference/class/ApifyKeyValueStoreClient.md

# ApifyKeyValueStoreClient<!-- -->

An Apify platform implementation of the key-value store client.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#__init__)
* [**delete\_value](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#delete_value)
* [**drop](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#drop)
* [**get\_metadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#get_metadata)
* [**get\_public\_url](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#get_public_url)
* [**get\_value](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#get_value)
* [**iterate\_keys](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#iterate_keys)
* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#open)
* [**purge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#purge)
* [**record\_exists](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#record_exists)
* [**set\_value](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md#set_value)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L29)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, api\_public\_base\_url, lock): None

- Initialize a new instance.

  Preferably use the `ApifyKeyValueStoreClient.open` class method to create a new instance.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: KeyValueStoreClientAsync
  * ##### keyword-onlyapi\_public\_base\_url: str
  * ##### keyword-onlylock: asyncio.Lock

  #### Returns None

### [**](#delete_value)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L132)delete\_value

* **async **delete\_value**(\*, key): None

- #### Parameters

  * ##### keyword-onlykey: str

  #### Returns None

### [**](#drop)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L113)drop

* **async **drop**(): None

- #### Returns None

### [**](#get_metadata)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L55)get\_metadata

* **async **get\_metadata**(): [ApifyKeyValueStoreMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreMetadata.md)

- #### Returns [ApifyKeyValueStoreMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreMetadata.md)

### [**](#get_public_url)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L174)get\_public\_url

* **async **get\_public\_url**(\*, key): str

- Get a URL for the given key that may be used to publicly access the value in the remote key-value store.

  ***

  #### Parameters

  * ##### keyword-onlykey: str

    The key for which the URL should be generated.

  #### Returns str

### [**](#get_value)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L118)get\_value

* **async **get\_value**(\*, key): KeyValueStoreRecord | None

- #### Parameters

  * ##### keyword-onlykey: str

  #### Returns KeyValueStoreRecord | None

### [**](#iterate_keys)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L137)iterate\_keys

* **async **iterate\_keys**(\*, exclusive\_start\_key, limit): AsyncIterator\[KeyValueStoreRecordMetadata]

- #### Parameters

  * ##### optionalkeyword-onlyexclusive\_start\_key: str | None = <!-- -->None
  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

  #### Returns AsyncIterator\[KeyValueStoreRecordMetadata]

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L60)open

* **async **open**(\*, id, name, alias, configuration): [ApifyKeyValueStoreClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md)

- Open an Apify key-value store client.

  This method creates and initializes a new instance of the Apify key-value store client. It handles authentication, storage lookup/creation, and metadata retrieval.

  ***

  #### Parameters

  * ##### keyword-onlyid: str | None

    The ID of the KVS to open. If provided, searches for existing KVS by ID. Mutually exclusive with name and alias.

  * ##### keyword-onlyname: str | None

    The name of the KVS to open (global scope, persists across runs). Mutually exclusive with id and alias.

  * ##### keyword-onlyalias: str | None

    The alias of the KVS to open (run scope, creates unnamed storage). Mutually exclusive with id and name.

  * ##### keyword-onlyconfiguration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)

    The configuration object containing API credentials and settings. Must include a valid `token` and `api_base_url`. May also contain a `default_key_value_store_id` for fallback when neither `id`, `name`, nor `alias` is provided.

  #### Returns [ApifyKeyValueStoreClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md)

### [**](#purge)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L106)purge

* **async **purge**(): None

- #### Returns None

### [**](#record_exists)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L170)record\_exists

* **async **record\_exists**(\*, key): bool

- #### Parameters

  * ##### keyword-onlykey: str

  #### Returns bool

### [**](#set_value)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_key_value_store_client.py#L123)set\_value

* **async **set\_value**(\*, key, value, content\_type): None

- #### Parameters

  * ##### keyword-onlykey: str
  * ##### keyword-onlyvalue: Any
  * ##### optionalkeyword-onlycontent\_type: str | None = <!-- -->None

  #### Returns None
