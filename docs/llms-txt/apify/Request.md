# Source: https://docs.apify.com/sdk/python/reference/class/Request.md

# Request<!-- -->

Represents a request in the Crawlee framework, containing the necessary information for crawling operations.

The `Request` class is one of the core components in Crawlee, utilized by various components such as request providers, HTTP clients, crawlers, and more. It encapsulates the essential data for executing web requests, including the URL, HTTP method, headers, payload, and user data. The user data allows custom information to be stored and persisted throughout the request lifecycle, including its retries.

Key functionalities include managing the request's identifier (`id`), unique key (`unique_key`) that is used for request deduplication, controlling retries, handling state management, and enabling configuration for session rotation and proxy handling.

The recommended way to create a new instance is by using the `Request.from_url` constructor, which automatically generates a unique key and identifier based on the URL and request parameters.

### Usage

```
from crawlee import Request

request = Request.from_url('https://crawlee.dev')
```

### Hierarchy

* *Request*
  * [RequestWithLock](https://crawlee.dev/python/api/class/RequestWithLock)

## Index[**](#Index)

### Methods

* [**crawl\_depth](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#crawl_depth)
* [**enqueue\_strategy](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#enqueue_strategy)
* [**forefront](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#forefront)
* [**from\_url](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#from_url)
* [**get\_query\_param\_from\_url](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#get_query_param_from_url)
* [**last\_proxy\_tier](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#last_proxy_tier)
* [**max\_retries](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#max_retries)
* [**session\_rotation\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#session_rotation_count)
* [**state](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#state)

### Properties

* [**crawl\_depth](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#crawl_depth)
* [**crawlee\_data](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#crawlee_data)
* [**enqueue\_strategy](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#enqueue_strategy)
* [**forefront](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#forefront)
* [**handled\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#handled_at)
* [**label](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#label)
* [**last\_proxy\_tier](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#last_proxy_tier)
* [**loaded\_url](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#loaded_url)
* [**max\_retries](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#max_retries)
* [**method](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#method)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#model_config)
* [**no\_retry](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#no_retry)
* [**payload](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#payload)
* [**retry\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#retry_count)
* [**session\_id](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#session_id)
* [**session\_rotation\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#session_rotation_count)
* [**state](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#state)
* [**unique\_key](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#unique_key)
* [**url](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#url)
* [**was\_already\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/Request.md#was_already_handled)

## Methods<!-- -->[**](#Methods)

### [**](#crawl_depth)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L351)crawl\_depth

* ****crawl\_depth**(new\_value): None

- #### Parameters

  * ##### new\_value: int

  #### Returns None

### [**](#enqueue_strategy)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L387)enqueue\_strategy

* ****enqueue\_strategy**(new\_enqueue\_strategy): None

- #### Parameters

  * ##### new\_enqueue\_strategy: [EnqueueStrategy](https://crawlee.dev/python/api#EnqueueStrategy)

  #### Returns None

### [**](#forefront)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L405)forefront

* ****forefront**(new\_value): None

- #### Parameters

  * ##### new\_value: bool

  #### Returns None

### [**](#from_url)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L240)from\_url

* ****from\_url**(url, \*, method, headers, payload, label, session\_id, unique\_key, keep\_url\_fragment, use\_extended\_unique\_key, always\_enqueue, kwargs): Self

- Create a new `Request` instance from a URL.

  This is recommended constructor for creating new `Request` instances. It generates a `Request` object from a given URL with additional options to customize HTTP method, payload, unique key, and other request properties. If no `unique_key` or `id` is provided, they are computed automatically based on the URL, method and payload. It depends on the `keep_url_fragment` and `use_extended_unique_key` flags.

  ***

  #### Parameters

  * ##### url: str

    The URL of the request.

  * ##### optionalkeyword-onlymethod: [HttpMethod](https://crawlee.dev/python/api#HttpMethod) = <!-- -->'GET'

    The HTTP method of the request.

  * ##### optionalkeyword-onlyheaders: ([HttpHeaders](https://crawlee.dev/python/api/class/HttpHeaders) | dict\[str, str]) | None = <!-- -->None

    The HTTP headers of the request.

  * ##### optionalkeyword-onlypayload: ([HttpPayload](https://crawlee.dev/python/api#HttpPayload) | str) | None = <!-- -->None

    The data to be sent as the request body. Typically used with 'POST' or 'PUT' requests.

  * ##### optionalkeyword-onlylabel: str | None = <!-- -->None

    A custom label to differentiate between request types. This is stored in `user_data`, and it is used for request routing (different requests go to different handlers).

  * ##### optionalkeyword-onlysession\_id: str | None = <!-- -->None

    ID of a specific `Session` to which the request will be strictly bound. If the session becomes unavailable when the request is processed, a `RequestCollisionError` will be raised.

  * ##### optionalkeyword-onlyunique\_key: str | None = <!-- -->None

    A unique key identifying the request. If not provided, it is automatically computed based on the URL and other parameters. Requests with the same `unique_key` are treated as identical.

  * ##### optionalkeyword-onlykeep\_url\_fragment: bool = <!-- -->False

    Determines whether the URL fragment (e.g., `` `section` ``) should be included in the `unique_key` computation. This is only relevant when `unique_key` is not provided.

  * ##### optionalkeyword-onlyuse\_extended\_unique\_key: bool = <!-- -->False

    Determines whether to include the HTTP method, ID Session and payload in the `unique_key` computation. This is only relevant when `unique_key` is not provided.

  * ##### optionalkeyword-onlyalways\_enqueue: bool = <!-- -->False

    If set to `True`, the request will be enqueued even if it is already present in the queue. Using this is not allowed when a custom `unique_key` is also provided and will result in a `ValueError`.

  * ##### kwargs: Any

  #### Returns Self

### [**](#get_query_param_from_url)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L321)get\_query\_param\_from\_url

* ****get\_query\_param\_from\_url**(param, \*, default): str | None

- Get the value of a specific query parameter from the URL.

  ***

  #### Parameters

  * ##### param: str
  * ##### optionalkeyword-onlydefault: str | None = <!-- -->None

  #### Returns str | None

### [**](#last_proxy_tier)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L396)last\_proxy\_tier

* ****last\_proxy\_tier**(new\_value): None

- #### Parameters

  * ##### new\_value: int

  #### Returns None

### [**](#max_retries)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L369)max\_retries

* ****max\_retries**(new\_max\_retries): None

- #### Parameters

  * ##### new\_max\_retries: int

  #### Returns None

### [**](#session_rotation_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L378)session\_rotation\_count

* ****session\_rotation\_count**(new\_session\_rotation\_count): None

- #### Parameters

  * ##### new\_session\_rotation\_count: int

  #### Returns None

### [**](#state)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L360)state

* ****state**(new\_state): None

- #### Parameters

  * ##### new\_state: [RequestState](https://crawlee.dev/python/api/class/RequestState)

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#crawl_depth)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L346)crawl\_depth

**crawl\_depth: int

The depth of the request in the crawl tree.

### [**](#crawlee_data)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L337)crawlee\_data

**crawlee\_data: [CrawleeRequestData](https://crawlee.dev/python/api/class/CrawleeRequestData)

Crawlee-specific configuration stored in the `user_data`.

### [**](#enqueue_strategy)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L382)enqueue\_strategy

**enqueue\_strategy: [EnqueueStrategy](https://crawlee.dev/python/api#EnqueueStrategy)

The strategy that was used for enqueuing the request.

### [**](#forefront)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L400)forefront

**forefront: bool

Indicate whether the request should be enqueued at the front of the queue.

### [**](#handled_at)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L236)handled\_at

**handled\_at: datetime | None

Timestamp when the request was handled.

### [**](#label)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L327)label

**label: str | None

A string used to differentiate between arbitrary request types.

### [**](#last_proxy_tier)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L391)last\_proxy\_tier

**last\_proxy\_tier: int | None

The last proxy tier used to process the request.

### [**](#loaded_url)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L233)loaded\_url

**loaded\_url: str | None

URL of the web page that was loaded. This can differ from the original URL in case of redirects.

### [**](#max_retries)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L364)max\_retries

**max\_retries: int | None

Crawlee-specific limit on the number of retries of the request.

### [**](#method)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L185)method

**method: [HttpMethod](https://crawlee.dev/python/api#HttpMethod)

HTTP request method.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L167)model\_config

**model\_config: Undefined

### [**](#no_retry)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L230)no\_retry

**no\_retry: bool

If set to `True`, the request will not be retried in case of failure.

### [**](#payload)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L188)payload

**payload: [HttpPayload](https://crawlee.dev/python/api#HttpPayload) | None

HTTP request payload.

### [**](#retry_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L227)retry\_count

**retry\_count: int

Number of times the request has been retried.

### [**](#session_id)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L332)session\_id

**session\_id: str | None

The ID of the bound session, if there is any.

### [**](#session_rotation_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L373)session\_rotation\_count

**session\_rotation\_count: int | None

Crawlee-specific number of finished session rotations for the request.

### [**](#state)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L355)state

**state: [RequestState](https://crawlee.dev/python/api/class/RequestState) | None

Crawlee-specific request handling state.

### [**](#unique_key)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L169)unique\_key

**unique\_key: str

A unique key identifying the request. Two requests with the same `unique_key` are considered as pointing to the same URL.

If `unique_key` is not provided, then it is automatically generated by normalizing the URL. For example, the URL of `HTTP://www.EXAMPLE.com/something/` will produce the `unique_key` of `http://www.example.com/something`.

Pass an arbitrary non-empty text value to the `unique_key` property to override the default behavior and specify which URLs shall be considered equal.

### [**](#url)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L181)url

**url: str

The URL of the web page to crawl. Must be a valid HTTP or HTTPS URL, and may include query parameters and fragments.

### [**](#was_already_handled)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/_request.py#L409)was\_already\_handled

**was\_already\_handled: bool

Indicates whether the request was handled.
