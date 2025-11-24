# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueClientAsync.md

# RequestQueueClientAsync<!-- -->

Async sub-client for manipulating a single request queue.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *RequestQueueClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#__init__)
* [**add\_request](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#add_request)
* [**batch\_add\_requests](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#batch_add_requests)
* [**batch\_delete\_requests](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#batch_delete_requests)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#delete)
* [**delete\_request](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#delete_request)
* [**delete\_request\_lock](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#delete_request_lock)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#get)
* [**get\_request](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#get_request)
* [**list\_and\_lock\_head](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#list_and_lock_head)
* [**list\_head](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#list_head)
* [**list\_requests](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#list_requests)
* [**prolong\_request\_lock](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#prolong_request_lock)
* [**unlock\_requests](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#unlock_requests)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#update)
* [**update\_request](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#update_request)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L431)\_\_init\_\_

* ****\_\_init\_\_**(args, \*, client\_key, kwargs): None

- Overrides [ResourceClientAsync.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md#__init__)

  Initialize a new instance.

  ***

  #### Parameters

  * ##### args: Any

  * ##### optionalkeyword-onlyclient\_key: str | None = <!-- -->None

    A unique identifier of the client accessing the request queue.

  * ##### kwargs: Any

  #### Returns None

### [**](#add_request)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L527)add\_request

* **async **add\_request**(request, \*, forefront): dict

- Add a request to the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/request-collection/add-request>

  ***

  #### Parameters

  * ##### request: dict

    The request to add to the queue.

  * ##### optionalkeyword-onlyforefront: bool | None = <!-- -->None

    Whether to add the request to the head or the end of the queue.

  #### Returns dict

### [**](#batch_add_requests)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L713)batch\_add\_requests

* **async **batch\_add\_requests**(requests, \*, forefront, max\_parallel, max\_unprocessed\_requests\_retries, min\_delay\_between\_unprocessed\_requests\_retries): [BatchAddRequestsResult](https://docs.apify.com/api/client/python/api/client/python/reference/class/BatchAddRequestsResult.md)

- Add requests to the request queue in batches.

  Requests are split into batches based on size and processed in parallel.

  <https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/add-requests>

  ***

  #### Parameters

  * ##### requests: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict]

    List of requests to be added to the queue.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    Whether to add requests to the front of the queue.

  * ##### optionalkeyword-onlymax\_parallel: int = <!-- -->5

    Specifies the maximum number of parallel tasks for API calls. This is only applicable to the async client. For the sync client, this value must be set to 1, as parallel execution is not supported.

  * ##### optionalkeyword-onlymax\_unprocessed\_requests\_retries: int | None = <!-- -->None

    Deprecated argument. Will be removed in next major release.

  * ##### optionalkeyword-onlymin\_delay\_between\_unprocessed\_requests\_retries: timedelta | None = <!-- -->None

    Deprecated argument. Will be removed in next major release.

  #### Returns [BatchAddRequestsResult](https://docs.apify.com/api/client/python/api/client/python/reference/class/BatchAddRequestsResult.md)

### [**](#batch_delete_requests)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L793)batch\_delete\_requests

* **async **batch\_delete\_requests**(requests): dict

- Delete given requests from the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/delete-requests>

  ***

  #### Parameters

  * ##### requests: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict]

    List of the requests to delete.

  #### Returns dict

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L475)delete

* **async **delete**(): None

- Delete the request queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/queue/delete-request-queue>

  ***

  #### Returns None

### [**](#delete_request)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L602)delete\_request

* **async **delete\_request**(request\_id): None

- Delete a request from the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/request/delete-request>

  ***

  #### Parameters

  * ##### request\_id: str

    ID of the request to delete.

  #### Returns None

### [**](#delete_request_lock)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L646)delete\_request\_lock

* **async **delete\_request\_lock**(request\_id, \*, forefront): None

- Delete the lock on a request.

  <https://docs.apify.com/api/v2#/reference/request-queues/request-lock/delete-request-lock>

  ***

  #### Parameters

  * ##### request\_id: str

    ID of the request to delete the lock.

  * ##### optionalkeyword-onlyforefront: bool | None = <!-- -->None

    Whether to put the request in the beginning or the end of the queue after the lock is deleted.

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L446)get

* **async **get**(): dict | None

- Retrieve the request queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/queue/get-request-queue>

  ***

  #### Returns dict | None

### [**](#get_request)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L551)get\_request

* **async **get\_request**(request\_id): dict | None

- Retrieve a request from the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/request/get-request>

  ***

  #### Parameters

  * ##### request\_id: str

    ID of the request to retrieve.

  #### Returns dict | None

### [**](#list_and_lock_head)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L504)list\_and\_lock\_head

* **async **list\_and\_lock\_head**(\*, lock\_secs, limit): dict

- Retrieve a given number of unlocked requests from the beginning of the queue and lock them for a given time.

  <https://docs.apify.com/api/v2#/reference/request-queues/queue-head-with-locks/get-head-and-lock>

  ***

  #### Parameters

  * ##### keyword-onlylock\_secs: int

    How long the requests will be locked for, in seconds.

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many requests to retrieve.

  #### Returns dict

### [**](#list_head)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L482)list\_head

* **async **list\_head**(\*, limit): dict

- Retrieve a given number of requests from the beginning of the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/queue-head/get-head>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many requests to retrieve.

  #### Returns dict

### [**](#list_requests)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L812)list\_requests

* **async **list\_requests**(\*, limit, exclusive\_start\_id): dict

- List requests in the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/request-collection/list-requests>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many requests to retrieve.

  * ##### optionalkeyword-onlyexclusive\_start\_id: str | None = <!-- -->None

    All requests up to this one (including) are skipped from the result.

  #### Returns dict

### [**](#prolong_request_lock)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L619)prolong\_request\_lock

* **async **prolong\_request\_lock**(request\_id, \*, forefront, lock\_secs): dict

- Prolong the lock on a request.

  <https://docs.apify.com/api/v2#/reference/request-queues/request-lock/prolong-request-lock>

  ***

  #### Parameters

  * ##### request\_id: str

    ID of the request to prolong the lock.

  * ##### optionalkeyword-onlyforefront: bool | None = <!-- -->None

    Whether to put the request in the beginning or the end of the queue after lock expires.

  * ##### keyword-onlylock\_secs: int

    By how much to prolong the lock, in seconds.

  #### Returns dict

### [**](#unlock_requests)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L837)unlock\_requests

* **async **unlock\_requests**(): dict

- Unlock all requests in the queue, which were locked by the same clientKey or from the same Actor run.

  <https://docs.apify.com/api/v2#/reference/request-queues/request-collection/unlock-requests>

  ***

  #### Returns dict

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L456)update

* **async **update**(\*, name, general\_access): dict

- Update the request queue with specified fields.

  <https://docs.apify.com/api/v2#/reference/request-queues/queue/update-request-queue>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyname: str | None = <!-- -->None

    The new name for the request queue.

  * ##### optionalkeyword-onlygeneral\_access: StorageGeneralAccess | None = <!-- -->None

    Determines how others can access the request queue.

  #### Returns dict

### [**](#update_request)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/request_queue.py#L576)update\_request

* **async **update\_request**(request, \*, forefront): dict

- Update a request in the queue.

  <https://docs.apify.com/api/v2#/reference/request-queues/request/update-request>

  ***

  #### Parameters

  * ##### request: dict

    The updated request.

  * ##### optionalkeyword-onlyforefront: bool | None = <!-- -->None

    Whether to put the updated request in the beginning or the end of the queue.

  #### Returns dict

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L94)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClientAsync.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L95)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClientAsync.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
