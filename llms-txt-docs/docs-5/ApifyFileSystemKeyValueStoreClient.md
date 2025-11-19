# Source: https://docs.apify.com/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md

# ApifyFileSystemKeyValueStoreClient<!-- -->

Apify-specific implementation of the `FileSystemKeyValueStoreClient`.

The only difference is that it overrides the `purge` method to delete all files in the key-value store directory, except for the metadata file and the `INPUT.json` file.

## Index[**](#Index)

### Methods

* [**get\_value](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#get_value)
* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#open)
* [**purge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemKeyValueStoreClient.md#purge)

## Methods<!-- -->[**](#Methods)

### [**](#get_value)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_file_system/_key_value_store_client.py#L94)get\_value

* **async **get\_value**(\*, key): KeyValueStoreRecord | None

- #### Parameters

  * ##### keyword-onlykey: str

  #### Returns KeyValueStoreRecord | None

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_file_system/_key_value_store_client.py#L27)open

* **async **open**(\*, id, name, alias, configuration): Self

- #### Parameters

  * ##### keyword-onlyid: str | None
  * ##### keyword-onlyname: str | None
  * ##### keyword-onlyalias: str | None
  * ##### keyword-onlyconfiguration: CrawleeConfiguration

  #### Returns Self

### [**](#purge)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_file_system/_key_value_store_client.py#L42)purge

* **async **purge**(): None

- Purges the key-value store by deleting all its contents.

  It deletes all files in the key-value store directory, except for the metadata file and the `INPUT.json` file. It also updates the metadata to reflect that the store has been purged.

  ***

  #### Returns None
