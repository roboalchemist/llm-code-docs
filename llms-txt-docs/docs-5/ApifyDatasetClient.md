# Source: https://docs.apify.com/sdk/python/reference/class/ApifyDatasetClient.md

# ApifyDatasetClient<!-- -->

An Apify platform implementation of the dataset client.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#__init__)
* [**drop](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#drop)
* [**get\_data](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#get_data)
* [**get\_metadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#get_metadata)
* [**iterate\_items](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#iterate_items)
* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#open)
* [**purge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#purge)
* [**push\_data](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md#push_data)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L40)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, api\_public\_base\_url, lock): None

- Initialize a new instance.

  Preferably use the `ApifyDatasetClient.open` class method to create a new instance.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: DatasetClientAsync
  * ##### keyword-onlyapi\_public\_base\_url: str
  * ##### keyword-onlylock: asyncio.Lock

  #### Returns None

### [**](#drop)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L125)drop

* **async **drop**(): None

- #### Returns None

### [**](#get_data)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L148)get\_data

* **async **get\_data**(\*, offset, limit, clean, desc, fields, omit, unwind, skip\_empty, skip\_hidden, flatten, view): DatasetItemsListPage

- #### Parameters

  * ##### optionalkeyword-onlyoffset: int = <!-- -->0
  * ##### optionalkeyword-onlylimit: int | None = <!-- -->999\_999\_999\_999
  * ##### optionalkeyword-onlyclean: bool = <!-- -->False
  * ##### optionalkeyword-onlydesc: bool = <!-- -->False
  * ##### optionalkeyword-onlyfields: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyomit: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyunwind: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyskip\_empty: bool = <!-- -->False
  * ##### optionalkeyword-onlyskip\_hidden: bool = <!-- -->False
  * ##### optionalkeyword-onlyflatten: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyview: str | None = <!-- -->None

  #### Returns DatasetItemsListPage

### [**](#get_metadata)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L66)get\_metadata

* **async **get\_metadata**(): DatasetMetadata

- #### Returns DatasetMetadata

### [**](#iterate_items)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L179)iterate\_items

* **async **iterate\_items**(\*, offset, limit, clean, desc, fields, omit, unwind, skip\_empty, skip\_hidden): AsyncIterator\[dict]

- #### Parameters

  * ##### optionalkeyword-onlyoffset: int = <!-- -->0
  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None
  * ##### optionalkeyword-onlyclean: bool = <!-- -->False
  * ##### optionalkeyword-onlydesc: bool = <!-- -->False
  * ##### optionalkeyword-onlyfields: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyomit: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyunwind: list\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyskip\_empty: bool = <!-- -->False
  * ##### optionalkeyword-onlyskip\_hidden: bool = <!-- -->False

  #### Returns AsyncIterator\[dict]

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L71)open

* **async **open**(\*, id, name, alias, configuration): [ApifyDatasetClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md)

- Open an Apify dataset client.

  This method creates and initializes a new instance of the Apify dataset client. It handles authentication, storage lookup/creation, and metadata retrieval.

  ***

  #### Parameters

  * ##### keyword-onlyid: str | None

    The ID of the dataset to open. If provided, searches for existing dataset by ID. Mutually exclusive with name and alias.

  * ##### keyword-onlyname: str | None

    The name of the dataset to open (global scope, persists across runs). Mutually exclusive with id and alias.

  * ##### keyword-onlyalias: str | None

    The alias of the dataset to open (run scope, creates unnamed storage). Mutually exclusive with id and name.

  * ##### keyword-onlyconfiguration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)

    The configuration object containing API credentials and settings. Must include a valid `token` and `api_base_url`. May also contain a `default_dataset_id` for fallback when neither `id`, `name`, nor `alias` is provided.

  #### Returns [ApifyDatasetClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md)

### [**](#purge)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L118)purge

* **async **purge**(): None

- #### Returns None

### [**](#push_data)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_dataset_client.py#L130)push\_data

* **async **push\_data**(data): None

- #### Parameters

  * ##### data: list\[Any] | dict\[str, Any]

  #### Returns None
