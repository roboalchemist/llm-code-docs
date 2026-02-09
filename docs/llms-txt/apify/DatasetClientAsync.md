# Source: https://docs.apify.com/api/client/python/reference/class/DatasetClientAsync.md

# DatasetClientAsync<!-- -->

Async sub-client for manipulating a single dataset.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *DatasetClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#__init__)
* [**create\_items\_public\_url](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#create_items_public_url)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#delete)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#get)
* [**get\_items\_as\_bytes](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#get_items_as_bytes)
* [**get\_statistics](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#get_statistics)
* [**iterate\_items](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#iterate_items)
* [**list\_items](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#list_items)
* [**push\_items](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#push_items)
* [**stream\_items](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#stream_items)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#update)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L647)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ResourceClientAsync.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md#__init__)

  Initialize a new instance.

  ***

  #### Parameters

  * ##### keyword-onlybase\_url: str

    Base URL of the API server.

  * ##### keyword-onlyroot\_client: [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

    The ApifyClientAsync instance under which this resource client exists.

  * ##### keyword-onlyhttp\_client: [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

    The HTTPClientAsync instance to be used in this client.

  * ##### optionalkeyword-onlyresource\_id: str | None = <!-- -->None

    ID of the manipulated resource, in case of a single-resource client.

  * ##### keyword-onlyresource\_path: str

    Path to the resource's endpoint on the API server.

  * ##### optionalkeyword-onlyparams: dict | None = <!-- -->None

    Parameters to include in all requests from this client.

  #### Returns None

### [**](#create_items_public_url)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L1101)create\_items\_public\_url

* **async **create\_items\_public\_url**(\*, offset, limit, clean, desc, fields, omit, unwind, skip\_empty, skip\_hidden, flatten, view, expires\_in\_secs): str

- Generate a URL that can be used to access dataset items.

  If the client has permission to access the dataset's URL signing key, the URL will include a signature to verify its authenticity.

  You can optionally control how long the signed URL should be valid using the `expires_in_secs` option. This value sets the expiration duration in seconds from the time the URL is generated. If not provided, the URL will not expire.

  Any other options (like `limit` or `offset`) will be included as query parameters in the URL.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None
  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None
  * ##### optionalkeyword-onlyclean: bool | None = <!-- -->None
  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None
  * ##### optionalkeyword-onlyfields: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyomit: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyunwind: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyskip\_empty: bool | None = <!-- -->None
  * ##### optionalkeyword-onlyskip\_hidden: bool | None = <!-- -->None
  * ##### optionalkeyword-onlyflatten: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None
  * ##### optionalkeyword-onlyview: str | None = <!-- -->None
  * ##### optionalkeyword-onlyexpires\_in\_secs: int | None = <!-- -->None

  #### Returns str

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L680)delete

* **async **delete**(): None

- Delete the dataset.

  <https://docs.apify.com/api/v2#/reference/datasets/dataset/delete-dataset>

  ***

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L651)get

* **async **get**(): dict | None

- Retrieve the dataset.

  <https://docs.apify.com/api/v2#/reference/datasets/dataset/get-dataset>

  ***

  #### Returns dict | None

### [**](#get_items_as_bytes)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L860)get\_items\_as\_bytes

* **async **get\_items\_as\_bytes**(\*, item\_format, offset, limit, desc, clean, bom, delimiter, fields, omit, unwind, skip\_empty, skip\_header\_row, skip\_hidden, xml\_root, xml\_row, flatten, signature): bytes

- Get the items in the dataset as raw bytes.

  <https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyitem\_format: str = <!-- -->'json'

    Format of the results, possible values are: json, jsonl, csv, html, xlsx, xml and rss. The default value is json.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    Number of items that should be skipped at the start. The default value is 0.

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    Maximum number of items to return. By default there is no limit.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    By default, results are returned in the same order as they were stored. To reverse the order, set this parameter to True.

  * ##### optionalkeyword-onlyclean: bool | None = <!-- -->None

    If True, returns only non-empty items and skips hidden fields (i.e. fields starting with the # character). The clean parameter is just a shortcut for skip\_hidden=True and skip\_empty=True parameters. Note that since some objects might be skipped from the output, that the result might contain less items than the limit value.

  * ##### optionalkeyword-onlybom: bool | None = <!-- -->None

    All text responses are encoded in UTF-8 encoding. By default, csv files are prefixed with the UTF-8 Byte Order Mark (BOM), while json, jsonl, xml, html and rss files are not. If you want to override this default behavior, specify bom=True query parameter to include the BOM or bom=False to skip it.

  * ##### optionalkeyword-onlydelimiter: str | None = <!-- -->None

    A delimiter character for CSV files. The default delimiter is a simple comma (,).

  * ##### optionalkeyword-onlyfields: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields parameter. You can use this feature to effectively fix the output format. You can use this feature to effectively fix the output format.

  * ##### optionalkeyword-onlyomit: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be omitted from the items.

  * ##### optionalkeyword-onlyunwind: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be unwound, in order which they should be processed. Each field should be either an array or an object. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object. If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object, then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

  * ##### optionalkeyword-onlyskip\_empty: bool | None = <!-- -->None

    If True, then empty items are skipped from the output. Note that if used, the results might contain less items than the limit value.

  * ##### optionalkeyword-onlyskip\_header\_row: bool | None = <!-- -->None

    If True, then header row in the csv format is skipped.

  * ##### optionalkeyword-onlyskip\_hidden: bool | None = <!-- -->None

    If True, then hidden fields are skipped from the output, i.e. fields starting with the # character.

  * ##### optionalkeyword-onlyxml\_root: str | None = <!-- -->None

    Overrides default root element name of xml output. By default the root element is items.

  * ##### optionalkeyword-onlyxml\_row: str | None = <!-- -->None

    Overrides default element name that wraps each page or page function result object in xml output. By default the element name is item.

  * ##### optionalkeyword-onlyflatten: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields that should be flattened.

  * ##### optionalkeyword-onlysignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns bytes

### [**](#get_statistics)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L1080)get\_statistics

* **async **get\_statistics**(): dict | None

- Get the dataset statistics.

  <https://docs.apify.com/api/v2#tag/DatasetsStatistics/operation/dataset_statistics_get>

  ***

  #### Returns dict | None

### [**](#iterate_items)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L776)iterate\_items

* **async **iterate\_items**(\*, offset, limit, clean, desc, fields, omit, unwind, skip\_empty, skip\_hidden, signature): AsyncIterator\[dict]

- Iterate over the items in the dataset.

  <https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyoffset: int = <!-- -->0

    Number of items that should be skipped at the start. The default value is 0.

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    Maximum number of items to return. By default there is no limit.

  * ##### optionalkeyword-onlyclean: bool | None = <!-- -->None

    If True, returns only non-empty items and skips hidden fields (i.e. fields starting with the # character). The clean parameter is just a shortcut for skip\_hidden=True and skip\_empty=True parameters. Note that since some objects might be skipped from the output, that the result might contain less items than the limit value.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    By default, results are returned in the same order as they were stored. To reverse the order, set this parameter to True.

  * ##### optionalkeyword-onlyfields: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields parameter. You can use this feature to effectively fix the output format.

  * ##### optionalkeyword-onlyomit: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be omitted from the items.

  * ##### optionalkeyword-onlyunwind: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be unwound, in order which they should be processed. Each field should be either an array or an object. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object. If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object, then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

  * ##### optionalkeyword-onlyskip\_empty: bool | None = <!-- -->None

    If True, then empty items are skipped from the output. Note that if used, the results might contain less items than the limit value.

  * ##### optionalkeyword-onlyskip\_hidden: bool | None = <!-- -->None

    If True, then hidden fields are skipped from the output, i.e. fields starting with the # character.

  * ##### optionalkeyword-onlysignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns AsyncIterator\[dict]

### [**](#list_items)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L687)list\_items

* **async **list\_items**(\*, offset, limit, clean, desc, fields, omit, unwind, skip\_empty, skip\_hidden, flatten, view, signature): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)

- List the items of the dataset.

  <https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    Number of items that should be skipped at the start. The default value is 0.

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    Maximum number of items to return. By default there is no limit.

  * ##### optionalkeyword-onlyclean: bool | None = <!-- -->None

    If True, returns only non-empty items and skips hidden fields (i.e. fields starting with the # character). The clean parameter is just a shortcut for skip\_hidden=True and skip\_empty=True parameters. Note that since some objects might be skipped from the output, that the result might contain less items than the limit value.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    By default, results are returned in the same order as they were stored. To reverse the order, set this parameter to True.

  * ##### optionalkeyword-onlyfields: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields parameter. You can use this feature to effectively fix the output format.

  * ##### optionalkeyword-onlyomit: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be omitted from the items.

  * ##### optionalkeyword-onlyunwind: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be unwound, in order which they should be processed. Each field should be either an array or an object. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object. If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object, then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

  * ##### optionalkeyword-onlyskip\_empty: bool | None = <!-- -->None

    If True, then empty items are skipped from the output. Note that if used, the results might contain less items than the limit value.

  * ##### optionalkeyword-onlyskip\_hidden: bool | None = <!-- -->None

    If True, then hidden fields are skipped from the output, i.e. fields starting with the # character.

  * ##### optionalkeyword-onlyflatten: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields that should be flattened.

  * ##### optionalkeyword-onlyview: str | None = <!-- -->None

    Name of the dataset view to be used.

  * ##### optionalkeyword-onlysignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)

### [**](#push_items)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L1053)push\_items

* **async **push\_items**(items): None

- Push items to the dataset.

  <https://docs.apify.com/api/v2#/reference/datasets/item-collection/put-items>

  ***

  #### Parameters

  * ##### items: [JSONSerializable](https://docs.apify.com/api/client/python/api/client/python/reference.md#JSONSerializable)

    The items which to push in the dataset. Either a stringified JSON, a dictionary, or a list of strings or dictionaries.

  #### Returns None

### [**](#stream_items)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L956)stream\_items

* **async **stream\_items**(\*, item\_format, offset, limit, desc, clean, bom, delimiter, fields, omit, unwind, skip\_empty, skip\_header\_row, skip\_hidden, xml\_root, xml\_row, signature): AsyncIterator\[impit.Response]

- Retrieve the items in the dataset as a stream.

  <https://docs.apify.com/api/v2#/reference/datasets/item-collection/get-items>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyitem\_format: str = <!-- -->'json'

    Format of the results, possible values are: json, jsonl, csv, html, xlsx, xml and rss. The default value is json.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    Number of items that should be skipped at the start. The default value is 0.

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    Maximum number of items to return. By default there is no limit.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    By default, results are returned in the same order as they were stored. To reverse the order, set this parameter to True.

  * ##### optionalkeyword-onlyclean: bool | None = <!-- -->None

    If True, returns only non-empty items and skips hidden fields (i.e. fields starting with the # character). The clean parameter is just a shortcut for skip\_hidden=True and skip\_empty=True parameters. Note that since some objects might be skipped from the output, that the result might contain less items than the limit value.

  * ##### optionalkeyword-onlybom: bool | None = <!-- -->None

    All text responses are encoded in UTF-8 encoding. By default, csv files are prefixed with the UTF-8 Byte Order Mark (BOM), while json, jsonl, xml, html and rss files are not. If you want to override this default behavior, specify bom=True query parameter to include the BOM or bom=False to skip it.

  * ##### optionalkeyword-onlydelimiter: str | None = <!-- -->None

    A delimiter character for CSV files. The default delimiter is a simple comma (,).

  * ##### optionalkeyword-onlyfields: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be picked from the items, only these fields will remain in the resulting record objects. Note that the fields in the outputted items are sorted the same way as they are specified in the fields parameter. You can use this feature to effectively fix the output format. You can use this feature to effectively fix the output format.

  * ##### optionalkeyword-onlyomit: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be omitted from the items.

  * ##### optionalkeyword-onlyunwind: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    A list of fields which should be unwound, in order which they should be processed. Each field should be either an array or an object. If the field is an array then every element of the array will become a separate record and merged with parent object. If the unwound field is an object then it is merged with the parent object. If the unwound field is missing or its value is neither an array nor an object and therefore cannot be merged with a parent object, then the item gets preserved as it is. Note that the unwound items ignore the desc parameter.

  * ##### optionalkeyword-onlyskip\_empty: bool | None = <!-- -->None

    If True, then empty items are skipped from the output. Note that if used, the results might contain less items than the limit value.

  * ##### optionalkeyword-onlyskip\_header\_row: bool | None = <!-- -->None

    If True, then header row in the csv format is skipped.

  * ##### optionalkeyword-onlyskip\_hidden: bool | None = <!-- -->None

    If True, then hidden fields are skipped from the output, i.e. fields starting with the # character.

  * ##### optionalkeyword-onlyxml\_root: str | None = <!-- -->None

    Overrides default root element name of xml output. By default the root element is items.

  * ##### optionalkeyword-onlyxml\_row: str | None = <!-- -->None

    Overrides default element name that wraps each page or page function result object in xml output. By default the element name is item.

  * ##### optionalkeyword-onlysignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns AsyncIterator\[impit.Response]

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/dataset.py#L661)update

* **async **update**(\*, name, general\_access): dict

- Update the dataset with specified fields.

  <https://docs.apify.com/api/v2#/reference/datasets/dataset/update-dataset>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyname: str | None = <!-- -->None

    The new name for the dataset.

  * ##### optionalkeyword-onlygeneral\_access: StorageGeneralAccess | None = <!-- -->None

    Determines how others can access the dataset.

  #### Returns dict

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L94)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClientAsync.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L95)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClientAsync.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
