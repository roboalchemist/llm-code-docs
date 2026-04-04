# Source: https://docs.apify.com/api/client/python/reference/class/KeyValueStoreClientAsync.md

# KeyValueStoreClientAsync<!-- -->

Async sub-client for manipulating a single key-value store.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *KeyValueStoreClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#__init__)
* [**create\_keys\_public\_url](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#create_keys_public_url)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#delete)
* [**delete\_record](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#delete_record)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#get)
* [**get\_record](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#get_record)
* [**get\_record\_as\_bytes](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#get_record_as_bytes)
* [**get\_record\_public\_url](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#get_record_public_url)
* [**list\_keys](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#list_keys)
* [**record\_exists](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#record_exists)
* [**set\_record](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#set_record)
* [**stream\_record](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#stream_record)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#update)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L357)\_\_init\_\_

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

### [**](#create_keys_public_url)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L629)create\_keys\_public\_url

* **async **create\_keys\_public\_url**(\*, limit, exclusive\_start\_key, collection, prefix, expires\_in\_secs): str

- Generate a URL that can be used to access key-value store keys.

  If the client has permission to access the key-value store's URL signing key, the URL will include a signature to verify its authenticity.

  You can optionally control how long the signed URL should be valid using the `expires_in_secs` option. This value sets the expiration duration in seconds from the time the URL is generated. If not provided, the URL will not expire.

  Any other options (like `limit` or `prefix`) will be included as query parameters in the URL.

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None
  * ##### optionalkeyword-onlyexclusive\_start\_key: str | None = <!-- -->None
  * ##### optionalkeyword-onlycollection: str | None = <!-- -->None
  * ##### optionalkeyword-onlyprefix: str | None = <!-- -->None
  * ##### optionalkeyword-onlyexpires\_in\_secs: int | None = <!-- -->None

  #### Returns str

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L390)delete

* **async **delete**(): None

- Delete the key-value store.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object/delete-store>

  ***

  #### Returns None

### [**](#delete_record)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L584)delete\_record

* **async **delete\_record**(key): None

- Delete the specified record from the key-value store.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/delete-record>

  ***

  #### Parameters

  * ##### key: str

    The key of the record which to delete.

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L361)get

* **async **get**(): dict | None

- Retrieve the key-value store.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object/get-store>

  ***

  #### Returns dict | None

### [**](#get_record)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L437)get\_record

* **async **get\_record**(key, signature): dict | None

- Retrieve the given record from the key-value store.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/get-record>

  ***

  #### Parameters

  * ##### key: str

    Key of the record to retrieve.

  * ##### optionalsignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns dict | None

### [**](#get_record_as_bytes)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L492)get\_record\_as\_bytes

* **async **get\_record\_as\_bytes**(key, signature): dict | None

- Retrieve the given record from the key-value store, without parsing it.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/get-record>

  ***

  #### Parameters

  * ##### key: str

    Key of the record to retrieve.

  * ##### optionalsignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns dict | None

### [**](#get_record_public_url)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L599)get\_record\_public\_url

* **async **get\_record\_public\_url**(key): str

- Generate a URL that can be used to access key-value store record.

  If the client has permission to access the key-value store's URL signing key, the URL will include a signature to verify its authenticity.

  ***

  #### Parameters

  * ##### key: str

    The key for which the URL should be generated.

  #### Returns str

### [**](#list_keys)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L397)list\_keys

* **async **list\_keys**(\*, limit, exclusive\_start\_key, collection, prefix, signature): dict

- List the keys in the key-value store.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/key-collection/get-list-of-keys>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    Number of keys to be returned. Maximum value is 1000.

  * ##### optionalkeyword-onlyexclusive\_start\_key: str | None = <!-- -->None

    All keys up to this one (including) are skipped from the result.

  * ##### optionalkeyword-onlycollection: str | None = <!-- -->None

    The name of the collection in store schema to list keys from.

  * ##### optionalkeyword-onlyprefix: str | None = <!-- -->None

    The prefix of the keys to be listed.

  * ##### optionalkeyword-onlysignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns dict

### [**](#record_exists)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L467)record\_exists

* **async **record\_exists**(key): bool

- Check if given record is present in the key-value store.

  <https://docs.apify.com/api/v2/key-value-store-record-head>

  ***

  #### Parameters

  * ##### key: str

    Key of the record to check.

  #### Returns bool

### [**](#set_record)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L557)set\_record

* **async **set\_record**(key, value, content\_type): None

- Set a value to the given record in the key-value store.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/put-record>

  ***

  #### Parameters

  * ##### key: str

    The key of the record to save the value to.

  * ##### value: Any

    The value to save into the record.

  * ##### optionalcontent\_type: str | None = <!-- -->None

    The content type of the saved value.

  #### Returns None

### [**](#stream_record)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L523)stream\_record

* **async **stream\_record**(key, signature): AsyncIterator\[dict | None]

- Retrieve the given record from the key-value store, as a stream.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/record/get-record>

  ***

  #### Parameters

  * ##### key: str

    Key of the record to retrieve.

  * ##### optionalsignature: str | None = <!-- -->None

    Signature used to access the items.

  #### Returns AsyncIterator\[dict | None]

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/key_value_store.py#L371)update

* **async **update**(\*, name, general\_access): dict

- Update the key-value store with specified fields.

  <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object/update-store>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyname: str | None = <!-- -->None

    The new name for key-value store.

  * ##### optionalkeyword-onlygeneral\_access: StorageGeneralAccess | None = <!-- -->None

    Determines how others can access the key-value store.

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
