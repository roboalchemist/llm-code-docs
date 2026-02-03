# Source: https://docs.apify.com/sdk/python/reference/class/SmartApifyStorageClient.md

# SmartApifyStorageClient<!-- -->

Storage client that automatically selects cloud or local storage client based on the environment.

This storage client provides access to datasets, key-value stores, and request queues by intelligently delegating to either the cloud or local storage client based on the execution environment and configuration.

When running on the Apify platform (which is detected via environment variables), this client automatically uses the `cloud_storage_client` to store storage data there. When running locally, it uses the `local_storage_client` to store storage data there. You can also force cloud storage usage from your local machine by using the `force_cloud` argument.

This storage client is designed to work specifically in `Actor` context and provides a seamless development experience where the same code works both locally and on the Apify platform without any changes.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#__init__)
* [**\_\_str\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#__str__)
* [**create\_dataset\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#create_dataset_client)
* [**create\_kvs\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#create_kvs_client)
* [**create\_rq\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#create_rq_client)
* [**get\_storage\_client\_cache\_key](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#get_storage_client_cache_key)
* [**get\_suitable\_storage\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SmartApifyStorageClient.md#get_suitable_storage_client)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L35)\_\_init\_\_

* ****\_\_init\_\_**(\*, cloud\_storage\_client, local\_storage\_client): None

- Initialize a new instance.

  ***

  #### Parameters

  * ##### optionalkeyword-onlycloud\_storage\_client: StorageClient | None = <!-- -->None

    Storage client used when an Actor is running on the Apify platform, or when explicitly enabled via the `force_cloud` argument. Defaults to `ApifyStorageClient`.

  * ##### optionalkeyword-onlylocal\_storage\_client: StorageClient | None = <!-- -->None

    Storage client used when an Actor is not running on the Apify platform and when `force_cloud` flag is not set. Defaults to `FileSystemStorageClient`.

  #### Returns None

### [**](#__str__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L52)\_\_str\_\_

* ****\_\_str\_\_**(): str

- #### Returns str

### [**](#create_dataset_client)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L68)create\_dataset\_client

* **async **create\_dataset\_client**(\*, id, name, alias, configuration): DatasetClient

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: CrawleeConfiguration | None = <!-- -->None

  #### Returns DatasetClient

### [**](#create_kvs_client)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L81)create\_kvs\_client

* **async **create\_kvs\_client**(\*, id, name, alias, configuration): KeyValueStoreClient

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: CrawleeConfiguration | None = <!-- -->None

  #### Returns KeyValueStoreClient

### [**](#create_rq_client)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L94)create\_rq\_client

* **async **create\_rq\_client**(\*, id, name, alias, configuration): RequestQueueClient

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: CrawleeConfiguration | None = <!-- -->None

  #### Returns RequestQueueClient

### [**](#get_storage_client_cache_key)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L59)get\_storage\_client\_cache\_key

* ****get\_storage\_client\_cache\_key**(configuration): Hashable

- #### Parameters

  * ##### configuration: CrawleeConfiguration

  #### Returns Hashable

### [**](#get_suitable_storage_client)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_smart_apify/_storage_client.py#L106)get\_suitable\_storage\_client

* ****get\_suitable\_storage\_client**(\*, force\_cloud): StorageClient

- Get a suitable storage client based on the global configuration and the value of the force\_cloud flag.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyforce\_cloud: bool = <!-- -->False

    If True, return `cloud_storage_client`.

  #### Returns StorageClient
