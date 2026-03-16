# Source: https://crawlee.dev/js/api/linkedom-crawler/interface/LinkeDOMCrawlerEnqueueLinksOptions.md

# LinkeDOMCrawlerEnqueueLinksOptions<!-- -->

### Hierarchy

* Omit<[EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md), urls | requestQueue>
  * *LinkeDOMCrawlerEnqueueLinksOptions*

## Index[**](#Index)

### Properties

* [**baseUrl](#baseUrl)
* [**exclude](#exclude)
* [**forefront](#forefront)
* [**globs](#globs)
* [**label](#label)
* [**limit](#limit)
* [**onSkippedRequest](#onSkippedRequest)
* [**pseudoUrls](#pseudoUrls)
* [**regexps](#regexps)
* [**robotsTxtFile](#robotsTxtFile)
* [**selector](#selector)
* [**skipNavigation](#skipNavigation)
* [**strategy](#strategy)
* [**transformRequestFunction](#transformRequestFunction)
* [**userData](#userData)
* [**waitForAllRequestsToBeAdded](#waitForAllRequestsToBeAdded)

## Properties<!-- -->[**](#Properties)

### [**](#baseUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L68)optionalinheritedbaseUrl

**baseUrl?

<!-- -->

: string

Inherited from Omit.baseUrl

A base URL that will be used to resolve relative URLs when using Cheerio. Ignored when using Puppeteer, since the relative URL resolution is done inside the browser automatically.

### [**](#exclude)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L94)optionalinheritedexclude

**exclude?

<!-- -->

: readonly

<!-- -->

([GlobInput](https://crawlee.dev/js/api/core.md#GlobInput) | [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput))\[]

Inherited from Omit.exclude

An array of glob pattern strings, regexp patterns or plain objects containing patterns matching URLs that will **never** be enqueued.

The plain objects must include either the `glob` property or the `regexp` property.

Glob matching is always case-insensitive. If you need case-sensitive matching, provide a regexp.

### [**](#forefront)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L950)optionalinheritedforefront

**forefront?

<!-- -->

: boolean = false

Inherited from Omit.forefront

If set to `true`:

* while adding the request to the queue: the request will be added to the foremost position in the queue.
* while reclaiming the request: the request will be placed to the beginning of the queue, so that it's returned in the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). By default, it's put to the end of the queue.

In case the request is already present in the queue, this option has no effect.

If more requests are added with this option at once, their order in the following `fetchNextRequest` call is arbitrary.

### [**](#globs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L83)optionalinheritedglobs

**globs?

<!-- -->

: readonly

<!-- -->

[GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)\[]

Inherited from Omit.globs

An array of glob pattern strings or plain objects containing glob pattern strings matching the URLs to be enqueued.

The plain objects must include at least the `glob` property, which holds the glob pattern string. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

The matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

If `globs` is an empty array or `undefined`, and `regexps` are also not defined, then the function enqueues the links with the same subdomain.

### [**](#label)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L56)optionalinheritedlabel

**label?

<!-- -->

: string

Inherited from Omit.label

Sets [Request.label](https://crawlee.dev/js/api/core/class/Request.md#label) for newly enqueued requests.

Note that the request options specified in `globs`, `regexps`, or `pseudoUrls` objects have priority over this option.

### [**](#limit)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L36)optionalinheritedlimit

**limit?

<!-- -->

: number

Inherited from Omit.limit

Limit the amount of actually enqueued URLs to this number. Useful for testing across the entire crawling scope.

### [**](#onSkippedRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L192)optionalinheritedonSkippedRequest

**onSkippedRequest?

<!-- -->

: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)

Inherited from Omit.onSkippedRequest

When a request is skipped for some reason, you can use this callback to act on it. This is currently fired for requests skipped

1. based on robots.txt file,
2. because they don't match enqueueLinks filters,
3. or because the maxRequestsPerCrawl limit has been reached

### [**](#pseudoUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L126)optionalinheritedpseudoUrls

**pseudoUrls?

<!-- -->

: readonly

<!-- -->

[PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)\[]

Inherited from Omit.pseudoUrls

*NOTE:* In future versions of SDK the options will be removed. Please use `globs` or `regexps` instead.

An array of [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) strings or plain objects containing [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) strings matching the URLs to be enqueued.

The plain objects must include at least the `purl` property, which holds the pseudo-URL string. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

With a pseudo-URL string, the matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

If `pseudoUrls` is an empty array or `undefined`, then the function enqueues the links with the same subdomain.

* **@deprecated**

  prefer using `globs` or `regexps` instead

### [**](#regexps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L106)optionalinheritedregexps

**regexps?

<!-- -->

: readonly

<!-- -->

[RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)\[]

Inherited from Omit.regexps

An array of regular expressions or plain objects containing regular expressions matching the URLs to be enqueued.

The plain objects must include at least the `regexp` property, which holds the regular expression. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

If `regexps` is an empty array or `undefined`, and `globs` are also not defined, then the function enqueues the links with the same subdomain.

### [**](#robotsTxtFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L183)optionalinheritedrobotsTxtFile

**robotsTxtFile?

<!-- -->

: Pick<[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md), isAllowed>

Inherited from Omit.robotsTxtFile

RobotsTxtFile instance for the current request that triggered the `enqueueLinks`. If provided, disallowed URLs will be ignored.

### [**](#selector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L45)optionalinheritedselector

**selector?

<!-- -->

: string

Inherited from Omit.selector

A CSS selector matching links to be enqueued.

### [**](#skipNavigation)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L62)optionalinheritedskipNavigation

**skipNavigation?

<!-- -->

: boolean = false

Inherited from Omit.skipNavigation

If set to `true`, tells the crawler to skip navigation and process the request directly.

### [**](#strategy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L171)optionalinheritedstrategy

**strategy?

<!-- -->

: [EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md) | all | same-domain | same-hostname | same-origin = [EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md) | all | same-domain | same-hostname | same-origin

Inherited from Omit.strategy

The strategy to use when enqueueing the urls.

Depending on the strategy you select, we will only check certain parts of the URLs found. Here is a diagram of each URL part and their name:

```
Protocol          Domain
┌────┐          ┌─────────┐
https://example.crawlee.dev/...
│       └─────────────────┤
│             Hostname    │
│                         │
└─────────────────────────┘
         Origin
```

### [**](#transformRequestFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L151)optionalinheritedtransformRequestFunction

**transformRequestFunction?

<!-- -->

: [RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md)

Inherited from Omit.transformRequestFunction

Just before a new [Request](https://crawlee.dev/js/api/core/class/Request.md) is constructed and enqueued to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md), this function can be used to remove it or modify its contents such as `userData`, `payload` or, most importantly `uniqueKey`. This is useful when you need to enqueue multiple `Requests` to the queue that share the same URL, but differ in methods or payloads, or to dynamically update or create `userData`.

For example: by adding `keepUrlFragment: true` to the `request` object, URL fragments will not be removed when `uniqueKey` is computed.

**Example:**

```
{
    transformRequestFunction: (request) => {
        request.userData.foo = 'bar';
        request.keepUrlFragment = true;
        return request;
    }
}
```

Note that the request options specified in `globs`, `regexps`, or `pseudoUrls` objects have priority over this function. Some request options returned by `transformRequestFunction` may be overwritten by pattern-based options from `globs`, `regexps`, or `pseudoUrls`.

### [**](#userData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L48)optionalinheriteduserData

**userData?

<!-- -->

: Dictionary

Inherited from Omit.userData

Sets [Request.userData](https://crawlee.dev/js/api/core/class/Request.md#userData) for newly enqueued requests.

### [**](#waitForAllRequestsToBeAdded)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L177)optionalinheritedwaitForAllRequestsToBeAdded

**waitForAllRequestsToBeAdded?

<!-- -->

: boolean

Inherited from Omit.waitForAllRequestsToBeAdded

By default, only the first batch (1000) of found requests will be added to the queue before resolving the call. You can use this option to wait for adding all of them.
