# Source: https://docs.apify.com/sdk/python/reference/class/ApifyFileSystemStorageClient.md

# ApifyFileSystemStorageClient<!-- -->

Apify-specific implementation of the file system storage client.

The only difference is that it uses `ApifyFileSystemKeyValueStoreClient` for key-value stores, which overrides the `purge` method to delete all files in the key-value store directory except for the metadata file and the `INPUT.json` file.

## Index[**](#Index)

### Methods

* [**create\_kvs\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyFileSystemStorageClient.md#create_kvs_client)

## Methods<!-- -->[**](#Methods)

### [**](#create_kvs_client)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_file_system/_storage_client.py#L25)create\_kvs\_client

* **async **create\_kvs\_client**(\*, id, name, alias, configuration): FileSystemKeyValueStoreClient

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md) | None = <!-- -->None

  #### Returns FileSystemKeyValueStoreClient
