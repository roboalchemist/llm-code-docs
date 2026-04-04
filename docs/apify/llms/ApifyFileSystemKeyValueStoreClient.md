# Source: https://docs.apify.com/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md

# ApifyFileSystemKeyValueStoreClient<!-- -->

Apify-specific implementation of the `FileSystemKeyValueStoreClient`.

The only difference is that it overrides the `purge` method to delete all files in the key-value store directory, except for the metadata file and the `INPUT.json` file.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#__init__)
* [**get\_value](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#get_value)
* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#open)
* [**purge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#purge)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_file_system/_key_value_store_client.py#L27)\_\_init\_\_

* ****\_\_init\_\_**(\*, metadata, path\_to\_kvs, lock): None

- #### Parameters

  * ##### keyword-onlymetadata: KeyValueStoreMetadata
  * ##### keyword-onlypath\_to\_kvs: Path
  * ##### keyword-onlylock: asyncio.Lock

  #### Returns None

### [**](#get_value)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_file_system/_key_value_store_client.py#L89)get\_value

* **async **get\_value**(\*, key): KeyValueStoreRecord | None

- #### Parameters

  * ##### keyword-onlykey: str

  #### Returns KeyValueStoreRecord | None

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_file_system/_key_value_store_client.py#L41)open

* **async **open**(\*, id, name, alias, configuration): Self

- #### Parameters

  * ##### keyword-onlyid: str | None
  * ##### keyword-onlyname: str | None
  * ##### keyword-onlyalias: str | None
  * ##### keyword-onlyconfiguration: CrawleeConfiguration

  #### Returns Self

### [**](#purge)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_file_system/_key_value_store_client.py#L67)purge

* **async **purge**(): None

- Purges the key-value store by deleting all its contents.

  It deletes all files in the key-value store directory, except for the metadata file and the input related file and its metadata.

  ***

  #### Returns None
