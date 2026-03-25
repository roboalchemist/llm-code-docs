# Source: https://crawlee.dev/js/api/utils/function/gotScraping.md

# gotScraping<!-- -->

### Callable

* ****gotScraping**(url, options): CancelableRequest\<Response\<string>>
* ****gotScraping**\<T>(url, options): CancelableRequest\<Response\<T>>
* ****gotScraping**(url, options): CancelableRequest\<Response\<Buffer\<ArrayBufferLike>>>
* ****gotScraping**(url, options): CancelableRequest\<Response>
* ****gotScraping**(options): CancelableRequest\<Response\<string>>
* ****gotScraping**\<T>(options): CancelableRequest\<Response\<T>>
* ****gotScraping**(options): CancelableRequest\<Response\<Buffer\<ArrayBufferLike>>>
* ****gotScraping**(options): CancelableRequest\<Response>
* ****gotScraping**(url, options): CancelableRequest\<string>
* ****gotScraping**\<T>(url, options): CancelableRequest\<T>
* ****gotScraping**(url, options): CancelableRequest\<Buffer\<ArrayBufferLike>>
* ****gotScraping**(options): CancelableRequest\<string>
* ****gotScraping**\<T>(options): CancelableRequest\<T>
* ****gotScraping**(options): CancelableRequest\<Buffer\<ArrayBufferLike>>
* ****gotScraping**(url, options): Request
* ****gotScraping**(options): Request
* ****gotScraping**(url, options): Request | CancelableRequest\<unknown>
* ****gotScraping**(options): Request | CancelableRequest\<unknown>
* ****gotScraping**(url, options, defaults): Request | CancelableRequest\<unknown>

***

* #### Parameters

  * ##### url: string | URL
  * ##### optionaloptions: ExtendedOptionsOfTextResponseBody

  #### Returns CancelableRequest\<Response\<string>>

## Index[**](#Index)

### Properties

* [**defaults](#defaults)
* [**delete](#delete)
* [**extend](#extend)
* [**get](#get)
* [**head](#head)
* [**paginate](#paginate)
* [**patch](#patch)
* [**post](#post)
* [**put](#put)
* [**stream](#stream)

## Properties<!-- -->[**](#Properties)

### [**](#defaults)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/got-scraping/src/index.d.ts#L224)externaldefaults

**defaults: InstanceDefaults

### [**](#delete)delete

**delete: ExtendedGotRequestFunction

### [**](#extend)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/got-scraping/src/index.d.ts#L225)externalextend

**extend: (...instancesOrOptions) => GotScraping

#### Type declaration

* * **(...instancesOrOptions): GotScraping

  - #### Parameters

    * ##### externalrest...instancesOrOptions: (GotScraping | ExtendedExtendOptions)\[]

    #### Returns GotScraping

### [**](#get)get

**get: ExtendedGotRequestFunction

### [**](#head)head

**head: ExtendedGotRequestFunction

### [**](#paginate)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/got-scraping/src/index.d.ts#L223)externalpaginate

**paginate: ExtendedGotPaginate

### [**](#patch)patch

**patch: ExtendedGotRequestFunction

### [**](#post)post

**post: ExtendedGotRequestFunction

### [**](#put)put

**put: ExtendedGotRequestFunction

### [**](#stream)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/got-scraping/src/index.d.ts#L222)externalstream

**stream: ExtendedGotStream
