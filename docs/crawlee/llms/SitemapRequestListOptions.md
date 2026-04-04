# Source: https://crawlee.dev/js/api/core/interface/SitemapRequestListOptions.md

# SitemapRequestListOptions<!-- -->

### Hierarchy

* UrlConstraints
  * *SitemapRequestListOptions*

## Index[**](#Index)

### Properties

* [**config](#config)
* [**exclude](#exclude)
* [**globs](#globs)
* [**maxBufferSize](#maxBufferSize)
* [**parseSitemapOptions](#parseSitemapOptions)
* [**persistenceOptions](#persistenceOptions)
* [**persistStateKey](#persistStateKey)
* [**proxyUrl](#proxyUrl)
* [**regexps](#regexps)
* [**signal](#signal)
* [**sitemapUrls](#sitemapUrls)
* [**timeoutMillis](#timeoutMillis)

## Properties<!-- -->[**](#Properties)

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L105)optionalconfig

**config?

<!-- -->

: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

Crawlee configuration

### [**](#exclude)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L46)optionalinheritedexclude

**exclude?

<!-- -->

: readonly

<!-- -->

(RegExp | [GlobInput](https://crawlee.dev/js/api/core.md#GlobInput))\[]

Inherited from UrlConstraints.exclude

An array of glob pattern strings, regexp patterns or plain objects containing patterns matching URLs that will **never** be included.

The plain objects must include either the `glob` property or the `regexp` property.

Glob matching is always case-insensitive. If you need case-sensitive matching, provide a regexp.

### [**](#globs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L35)optionalinheritedglobs

**globs?

<!-- -->

: readonly

<!-- -->

[GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)\[]

Inherited from UrlConstraints.globs

An array of glob pattern strings or plain objects containing glob pattern strings matching the URLs to be enqueued.

The plain objects must include at least the `glob` property, which holds the glob pattern string.

The matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

If `globs` is an empty array or `undefined`, and `regexps` are also not defined, then the `SitemapRequestList` includes all the URLs from the sitemap.

### [**](#maxBufferSize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L97)optionalmaxBufferSize

**maxBufferSize?

<!-- -->

: number = 200

Maximum number of buffered URLs for the sitemap loading stream. If the buffer is full, the stream will pause until the buffer is drained.

### [**](#parseSitemapOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L101)optionalparseSitemapOptions

**parseSitemapOptions?

<!-- -->

: Omit<[ParseSitemapOptions](https://crawlee.dev/js/api/utils/interface/ParseSitemapOptions.md), emitNestedSitemaps | maxDepth>

Advanced options for the underlying `parseSitemap` call.

### [**](#persistenceOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L76)optionalpersistenceOptions

**persistenceOptions?

<!-- -->

: { enable?

<!-- -->

: boolean }

Persistence-related options to control how and when crawler's data gets persisted.

***

#### Type declaration

* ##### optionalenable?<!-- -->: boolean

  Use this flag to disable or enable periodic persistence to key value store.

### [**](#persistStateKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L72)optionalpersistStateKey

**persistStateKey?

<!-- -->

: string

Key for persisting the state of the request list in the `KeyValueStore`.

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L68)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Proxy URL to be used for sitemap loading.

### [**](#regexps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L57)optionalinheritedregexps

**regexps?

<!-- -->

: readonly

<!-- -->

[RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)\[]

Inherited from UrlConstraints.regexps

An array of regular expressions or plain objects containing regular expressions matching the URLs to be enqueued.

The plain objects must include at least the `regexp` property, which holds the regular expression.

If `regexps` is an empty array or `undefined`, and `globs` are also not defined, then the `SitemapRequestList` includes all the URLs from the sitemap.

### [**](#signal)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L86)optionalsignal

**signal?

<!-- -->

: AbortSignal

Abort signal to be used for sitemap loading.

### [**](#sitemapUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L64)sitemapUrls

**sitemapUrls: string\[]

List of sitemap URLs to parse.

### [**](#timeoutMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L90)optionaltimeoutMillis

**timeoutMillis?

<!-- -->

: number

Timeout for sitemap loading in milliseconds. If both `signal` and `timeoutMillis` are provided, either of them can abort the loading.
