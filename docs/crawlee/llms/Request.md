# Source: https://crawlee.dev/js/api/core/class/Request.md

# Request<!-- --> \<UserData>

Represents a URL to be crawled, optionally including HTTP method, headers, payload and other metadata. The `Request` object also stores information about errors that occurred during processing of the request.

Each `Request` instance has the `uniqueKey` property, which can be either specified manually in the constructor or generated automatically from the URL. Two requests with the same `uniqueKey` are considered as pointing to the same web resource. This behavior applies to all Crawlee classes, such as [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md), [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md), [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) or [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md).

> To access and examine the actual request sent over http, with all autofilled headers you can access `response.request` object from the request handler

Example use:

```
const request = new Request({
    url: 'http://www.example.com',
    headers: { Accept: 'application/json' },
});

...

request.userData.foo = 'bar';
request.pushErrorMessage(new Error('Request failed!'));

...

const foo = request.userData.foo;
```

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**errorMessages](#errorMessages)
* [**handledAt](#handledAt)
* [**headers](#headers)
* [**id](#id)
* [**loadedUrl](#loadedUrl)
* [**method](#method)
* [**noRetry](#noRetry)
* [**payload](#payload)
* [**retryCount](#retryCount)
* [**uniqueKey](#uniqueKey)
* [**url](#url)
* [**userData](#userData)

### Accessors

* [**crawlDepth](#crawlDepth)
* [**label](#label)
* [**maxRetries](#maxRetries)
* [**sessionRotationCount](#sessionRotationCount)
* [**skipNavigation](#skipNavigation)
* [**state](#state)

### Methods

* [**pushErrorMessage](#pushErrorMessage)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L145)constructor

* ****new Request**\<UserData>(options): [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

- `Request` parameters including the URL, HTTP method and headers, and others.

  ***

  #### Parameters

  * ##### options: [RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<UserData>

  #### Returns [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

## Properties<!-- -->[**](#Properties)

### [**](#errorMessages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L120)errorMessages

**errorMessages: string\[]

An array of error messages from request processing.

### [**](#handledAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L140)optionalhandledAt

**handledAt?

<!-- -->

: string

ISO datetime string that indicates the time when the request has been processed. Is `null` if the request has not been crawled yet.

### [**](#headers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L123)optionalheaders

**headers?

<!-- -->

: Record\<string, string>

Object with HTTP headers. Key is header name, value is the value.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L86)optionalid

**id?

<!-- -->

: string

Request ID

### [**](#loadedUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L99)optionalloadedUrl

**loadedUrl?

<!-- -->

: string

An actually loaded URL after redirects, if present. HTTP redirects are guaranteed to be included.

When using [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) or [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md), meta tag and JavaScript redirects may, or may not be included, depending on their nature. This generally means that redirects, which happen immediately will most likely be included, but delayed redirects will not.

### [**](#method)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L108)method

**method: AllowedHttpMethods

HTTP method, e.g. `GET` or `POST`.

### [**](#noRetry)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L114)noRetry

**noRetry: boolean

The `true` value indicates that the request will not be automatically retried on error.

### [**](#payload)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L111)optionalpayload

**payload?

<!-- -->

: string

HTTP request payload, e.g. for POST requests.

### [**](#retryCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L117)retryCount

**retryCount: number

Indicates the number of times the crawling of the request has been retried on error.

### [**](#uniqueKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L105)uniqueKey

**uniqueKey: string

A unique key identifying the request. Two requests with the same `uniqueKey` are considered as pointing to the same URL.

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L89)url

**url: string

URL of the web page to crawl.

### [**](#userData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L134)userData

**userData: UserData =

<!-- -->

...

Custom user data assigned to the request.

All data stored in `userData` must be JSON-serializable. Storing non-serializable values (e.g. functions, symbols) may result in unexpected results.

## Accessors<!-- -->[**](#Accessors)

### [**](#crawlDepth)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L285)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L293)crawlDepth

* **get crawlDepth(): number
* **set crawlDepth(value): void

- Depth of the request in the current crawl tree. Note that this is dependent on the crawler setup and might produce unexpected results when used with multiple crawlers.

  ***

  #### Returns number

- Depth of the request in the current crawl tree. Note that this is dependent on the crawler setup and might produce unexpected results when used with multiple crawlers.

  ***

  #### Parameters

  * ##### value: number

  #### Returns void

### [**](#label)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L313)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L318)label

* **get label(): undefined | string
* **set label(value): void

- shortcut for getting `request.userData.label`

  ***

  #### Returns undefined | string

- shortcut for setting `request.userData.label`

  ***

  #### Parameters

  * ##### value: undefined | string

  #### Returns void

### [**](#maxRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L323)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L328)maxRetries

* **get maxRetries(): undefined | number
* **set maxRetries(value): void

- Maximum number of retries for this request. Allows to override the global `maxRequestRetries` option of `BasicCrawler`.

  ***

  #### Returns undefined | number

- Maximum number of retries for this request. Allows to override the global `maxRequestRetries` option of `BasicCrawler`.

  ***

  #### Parameters

  * ##### value: undefined | number

  #### Returns void

### [**](#sessionRotationCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L299)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L304)sessionRotationCount

* **get sessionRotationCount(): number
* **set sessionRotationCount(value): void

- Indicates the number of times the crawling of the request has rotated the session due to a session or a proxy error.

  ***

  #### Returns number

- Indicates the number of times the crawling of the request has rotated the session due to a session or a proxy error.

  ***

  #### Parameters

  * ##### value: number

  #### Returns void

### [**](#skipNavigation)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L268)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L273)skipNavigation

* **get skipNavigation(): boolean
* **set skipNavigation(value): void

- Tells the crawler processing this request to skip the navigation and process the request directly.

  ***

  #### Returns boolean

- Tells the crawler processing this request to skip the navigation and process the request directly.

  ***

  #### Parameters

  * ##### value: boolean

  #### Returns void

### [**](#state)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L337)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L342)state

* **get state(): [RequestState](https://crawlee.dev/js/api/core/enum/RequestState.md)
* **set state(value): void

- Describes the request's current lifecycle state.

  ***

  #### Returns [RequestState](https://crawlee.dev/js/api/core/enum/RequestState.md)

- Describes the request's current lifecycle state.

  ***

  #### Parameters

  * ##### value: [RequestState](https://crawlee.dev/js/api/core/enum/RequestState.md)

  #### Returns void

## Methods<!-- -->[**](#Methods)

### [**](#pushErrorMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L375)pushErrorMessage

* ****pushErrorMessage**(errorOrMessage, options): void

- Stores information about an error that occurred during processing of this request.

  You should always use Error instances when throwing errors in JavaScript.

  Nevertheless, to improve the debugging experience when using third party libraries that may not always throw an Error instance, the function performs a type inspection of the passed argument and attempts to extract as much information as possible, since just throwing a bad type error makes any debugging rather difficult.

  ***

  #### Parameters

  * ##### errorOrMessage: unknown

    Error object or error message to be stored in the request.

  * ##### optionaloptions: [PushErrorMessageOptions](https://crawlee.dev/js/api/core/interface/PushErrorMessageOptions.md) = <!-- -->{}

  #### Returns void
