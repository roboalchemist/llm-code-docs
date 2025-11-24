# Source: https://docs.apify.com/sdk/python/reference/class/SitemapRequestLoader.md

# SitemapRequestLoader<!-- -->

A request loader that reads URLs from sitemap(s).

The loader is designed to handle sitemaps that follow the format described in the Sitemaps protocol (<https://www.sitemaps.org/protocol.html>). It supports both XML and plain text sitemap formats. Note that HTML pages containing links are not supported - those should be handled by regular crawlers and the `enqueue_links` functionality.

The loader fetches and parses sitemaps in the background, allowing crawling to start before all URLs are loaded. It supports filtering URLs using glob and regex patterns.

The loader supports state persistence, allowing it to resume from where it left off after interruption when a `persist_state_key` is provided during initialization.

### Hierarchy

* [RequestLoader](https://crawlee.dev/python/api/class/RequestLoader)
  * *SitemapRequestLoader*

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#__init__)
* [**abort\_loading](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#abort_loading)
* [**close](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#close)
* [**fetch\_next\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#fetch_next_request)
* [**get\_handled\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#get_handled_count)
* [**get\_total\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#get_total_count)
* [**is\_empty](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#is_empty)
* [**is\_finished](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#is_finished)
* [**mark\_request\_as\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#mark_request_as_handled)
* [**start](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#start)
* [**to\_tandem](https://docs.apify.com/sdk/python/sdk/python/reference/class/SitemapRequestLoader.md#to_tandem)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L353)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): [SitemapRequestLoader](https://crawlee.dev/python/api/class/SitemapRequestLoader)

- Enter the context manager.

  ***

  #### Returns [SitemapRequestLoader](https://crawlee.dev/python/api/class/SitemapRequestLoader)

### [**](#__aexit__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L358)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- Exit the context manager.

  ***

  #### Parameters

  * ##### exc\_type: [type](https://crawlee.dev/python/api/class/SitemapSource#type)\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L105)\_\_init\_\_

* ****\_\_init\_\_**(sitemap\_urls, http\_client, \*, proxy\_info, include, exclude, max\_buffer\_size, persist\_state\_key): None

- Initialize the sitemap request loader.

  ***

  #### Parameters

  * ##### sitemap\_urls: list\[str]

    Configuration options for the loader.

  * ##### http\_client: [HttpClient](https://crawlee.dev/python/api/class/HttpClient)

    the instance of `HttpClient` to use for fetching sitemaps.

  * ##### optionalkeyword-onlyproxy\_info: [ProxyInfo](https://crawlee.dev/python/api/class/ProxyInfo) | None = <!-- -->None

    Optional proxy to use for fetching sitemaps.

  * ##### optionalkeyword-onlyinclude: list\[re.Pattern\[Any] | [Glob](https://crawlee.dev/python/api/class/Glob)] | None = <!-- -->None

    List of glob or regex patterns to include URLs.

  * ##### optionalkeyword-onlyexclude: list\[re.Pattern\[Any] | [Glob](https://crawlee.dev/python/api/class/Glob)] | None = <!-- -->None

    List of glob or regex patterns to exclude URLs.

  * ##### optionalkeyword-onlymax\_buffer\_size: int = <!-- -->200

    Maximum number of URLs to buffer in memory.

  * ##### optionalkeyword-onlypersist\_state\_key: str | None = <!-- -->None

    A key for persisting the loader's state in the KeyValueStore. When provided, allows resuming from where it left off after interruption. If None, no state persistence occurs.

  #### Returns None

### [**](#abort_loading)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L335)abort\_loading

* **async **abort\_loading**(): None

- Abort the sitemap loading process.

  ***

  #### Returns None

### [**](#close)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L348)close

* **async **close**(): None

- Close the request loader.

  ***

  #### Returns None

### [**](#fetch_next_request)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L306)fetch\_next\_request

* **async **fetch\_next\_request**(): [Request](https://crawlee.dev/python/api/class/Request) | None

- Overrides [RequestLoader.fetch\_next\_request](https://crawlee.dev/python/api/class/RequestLoader#fetch_next_request)

  Fetch the next request to process.

  ***

  #### Returns [Request](https://crawlee.dev/python/api/class/Request) | None

### [**](#get_handled_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L288)get\_handled\_count

* **async **get\_handled\_count**(): int

- Overrides [RequestLoader.get\_handled\_count](https://crawlee.dev/python/api/class/RequestLoader#get_handled_count)

  Return the number of URLs that have been handled.

  ***

  #### Returns int

### [**](#get_total_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L282)get\_total\_count

* **async **get\_total\_count**(): int

- Overrides [RequestLoader.get\_total\_count](https://crawlee.dev/python/api/class/RequestLoader#get_total_count)

  Return the total number of URLs found so far.

  ***

  #### Returns int

### [**](#is_empty)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L294)is\_empty

* **async **is\_empty**(): bool

- Overrides [RequestLoader.is\_empty](https://crawlee.dev/python/api/class/RequestLoader#is_empty)

  Check if there are no more URLs to process.

  ***

  #### Returns bool

### [**](#is_finished)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L300)is\_finished

* **async **is\_finished**(): bool

- Overrides [RequestLoader.is\_finished](https://crawlee.dev/python/api/class/RequestLoader#is_finished)

  Check if all URLs have been processed.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L327)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): [ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest) | None

- Overrides [RequestLoader.mark\_request\_as\_handled](https://crawlee.dev/python/api/class/RequestLoader#mark_request_as_handled)

  Mark a request as successfully handled.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/python/api/class/Request)

  #### Returns [ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest) | None

### [**](#start)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_sitemap_request_loader.py#L342)start

* **async **start**(): None

- Start the sitemap loading process.

  ***

  #### Returns None

### [**](#to_tandem)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_loader.py#L56)to\_tandem

* **async **to\_tandem**(request\_manager): [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)

- Inherited from [RequestLoader.to\_tandem](https://crawlee.dev/python/api/class/RequestLoader#to_tandem)

  Combine the loader with a request manager to support adding and reclaiming requests.

  ***

  #### Parameters

  * ##### optionalrequest\_manager: RequestManager | None = <!-- -->None

    Request manager to combine the loader with. If None is given, the default request queue is used.

  #### Returns [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)
