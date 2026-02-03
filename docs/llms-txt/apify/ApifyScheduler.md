# Source: https://docs.apify.com/sdk/python/reference/class/ApifyScheduler.md

# ApifyScheduler<!-- -->

A Scrapy scheduler that uses the Apify `RequestQueue` to manage requests.

This scheduler requires the asyncio Twisted reactor to be installed.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyScheduler.md#__init__)
* [**close](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyScheduler.md#close)
* [**enqueue\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyScheduler.md#enqueue_request)
* [**has\_pending\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyScheduler.md#has_pending_requests)
* [**next\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyScheduler.md#next_request)
* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyScheduler.md#open)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/scheduler.py#L30)\_\_init\_\_

* ****\_\_init\_\_**(): None

- #### Returns None

### [**](#close)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/scheduler.py#L69)close

* ****close**(reason): None

- Close the scheduler.

  Shut down the event loop and its thread gracefully.

  ***

  #### Parameters

  * ##### reason: str

    The reason for closing the spider.

  #### Returns None

### [**](#enqueue_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/scheduler.py#L107)enqueue\_request

* ****enqueue\_request**(request): bool

- Add a request to the scheduler.

  This could be called from either from a spider or a downloader middleware (e.g. redirect, retry, ...).

  ***

  #### Parameters

  * ##### request: Request

    The request to add to the scheduler.

  #### Returns bool

### [**](#has_pending_requests)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/scheduler.py#L90)has\_pending\_requests

* ****has\_pending\_requests**(): bool

- Check if the scheduler has any pending requests.

  ***

  #### Returns bool

### [**](#next_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/scheduler.py#L141)next\_request

* ****next\_request**(): Request | None

- Fetch the next request from the scheduler.

  ***

  #### Returns Request | None

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/scheduler.py#L43)open

* ****open**(spider): Deferred\[None] | None

- Open the scheduler.

  ***

  #### Parameters

  * ##### spider: Spider

    The spider that the scheduler is associated with.

  #### Returns Deferred\[None] | None
