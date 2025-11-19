# Source: https://docs.apify.com/sdk/python/reference/class/SqlStorageClient.md

# SqlStorageClient<!-- -->

SQL implementation of the storage client.

This storage client provides access to datasets, key-value stores, and request queues that persist data to a SQL database using SQLAlchemy 2+. Each storage type uses two tables: one for metadata and one for records.

The client accepts either a database connection string or a pre-configured AsyncEngine. If neither is provided, it creates a default SQLite database 'crawlee.db' in the storage directory.

Database schema is automatically created during initialization. SQLite databases receive performance optimizations including WAL mode and increased cache size.

### Hierarchy

* [StorageClient](https://crawlee.dev/python/api/class/StorageClient)
  * *SqlStorageClient*

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#__init__)
* [**close](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#close)
* [**create\_dataset\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#create_dataset_client)
* [**create\_kvs\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#create_kvs_client)
* [**create\_rq\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#create_rq_client)
* [**create\_session](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#create_session)
* [**get\_accessed\_modified\_update\_interval](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#get_accessed_modified_update_interval)
* [**get\_dialect\_name](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#get_dialect_name)
* [**get\_rate\_limit\_errors](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#get_rate_limit_errors)
* [**get\_storage\_client\_cache\_key](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#get_storage_client_cache_key)
* [**initialize](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#initialize)

### Properties

* [**engine](https://docs.apify.com/sdk/python/sdk/python/reference/class/SqlStorageClient.md#engine)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L85)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): [SqlStorageClient](https://crawlee.dev/python/api/class/SqlStorageClient)

- Async context manager entry.

  ***

  #### Returns [SqlStorageClient](https://crawlee.dev/python/api/class/SqlStorageClient)

### [**](#__aexit__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L89)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- Async context manager exit.

  ***

  #### Parameters

  * ##### exc\_type: [type](https://crawlee.dev/python/api/class/SitemapSource#type)\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L50)\_\_init\_\_

* ****\_\_init\_\_**(\*, connection\_string, engine): None

- Initialize the SQL storage client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyconnection\_string: str | None = <!-- -->None

    Database connection string (e.g., "sqlite+aiosqlite:///crawlee.db"). If not provided, defaults to SQLite database in the storage directory.

  * ##### optionalkeyword-onlyengine: AsyncEngine | None = <!-- -->None

    Pre-configured AsyncEngine instance. If provided, connection\_string is ignored.

  #### Returns None

### [**](#close)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L167)close

* **async **close**(): None

- Close the database connection pool.

  ***

  #### Returns None

### [**](#create_dataset_client)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L184)create\_dataset\_client

* **async **create\_dataset\_client**(\*, id, name, alias, configuration): [DatasetClient](https://crawlee.dev/python/api/class/DatasetClient)

- Overrides [StorageClient.create\_dataset\_client](https://crawlee.dev/python/api/class/StorageClient#create_dataset_client)

  Create a dataset client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

  #### Returns [DatasetClient](https://crawlee.dev/python/api/class/DatasetClient)

### [**](#create_kvs_client)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L206)create\_kvs\_client

* **async **create\_kvs\_client**(\*, id, name, alias, configuration): [KeyValueStoreClient](https://crawlee.dev/python/api/class/KeyValueStoreClient)

- Overrides [StorageClient.create\_kvs\_client](https://crawlee.dev/python/api/class/StorageClient#create_kvs_client)

  Create a key-value store client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

  #### Returns [KeyValueStoreClient](https://crawlee.dev/python/api/class/KeyValueStoreClient)

### [**](#create_rq_client)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L228)create\_rq\_client

* **async **create\_rq\_client**(\*, id, name, alias, configuration): [RequestQueueClient](https://crawlee.dev/python/api/class/RequestQueueClient)

- Overrides [StorageClient.create\_rq\_client](https://crawlee.dev/python/api/class/StorageClient#create_rq_client)

  Create a request queue client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

  #### Returns [RequestQueueClient](https://crawlee.dev/python/api/class/RequestQueueClient)

### [**](#create_session)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L173)create\_session

* ****create\_session**(): AsyncSession

- Create a new database session.

  ***

  #### Returns AsyncSession

### [**](#get_accessed_modified_update_interval)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L109)get\_accessed\_modified\_update\_interval

* ****get\_accessed\_modified\_update\_interval**(): timedelta

- Get the interval for accessed and modified updates.

  ***

  #### Returns timedelta

### [**](#get_dialect_name)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L105)get\_dialect\_name

* ****get\_dialect\_name**(): str | None

- Get the database dialect name.

  ***

  #### Returns str | None

### [**](#get_rate_limit_errors)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_base/_storage_client.py#L74)get\_rate\_limit\_errors

* ****get\_rate\_limit\_errors**(): dict\[int, int]

- Inherited from [StorageClient.get\_rate\_limit\_errors](https://crawlee.dev/python/api/class/StorageClient#get_rate_limit_errors)

  Return statistics about rate limit errors encountered by the HTTP client in storage client.

  ***

  #### Returns dict\[int, int]

### [**](#get_storage_client_cache_key)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_base/_storage_client.py#L33)get\_storage\_client\_cache\_key

* ****get\_storage\_client\_cache\_key**(configuration): Hashable

- Inherited from [StorageClient.get\_storage\_client\_cache\_key](https://crawlee.dev/python/api/class/StorageClient#get_storage_client_cache_key)

  Return a cache key that can differentiate between different storages of this and other clients.

  Can be based on configuration or on the client itself. By default, returns a module and name of the client class.

  ***

  #### Parameters

  * ##### configuration: [Configuration](https://crawlee.dev/python/api/class/Configuration)

  #### Returns Hashable

### [**](#initialize)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L113)initialize

* **async **initialize**(configuration): None

- Initialize the database schema.

  This method creates all necessary tables if they don't exist. Should be called before using the storage client.

  ***

  #### Parameters

  * ##### configuration: [Configuration](https://crawlee.dev/python/api/class/Configuration)

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#engine)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/_sql/_storage_client.py#L99)engine

**engine: AsyncEngine

Get the SQLAlchemy AsyncEngine instance.
