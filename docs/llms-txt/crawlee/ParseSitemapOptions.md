# Source: https://crawlee.dev/js/api/utils/interface/ParseSitemapOptions.md

# ParseSitemapOptions<!-- -->

## Index[**](#Index)

### Properties

* [**emitNestedSitemaps](#emitNestedSitemaps)
* [**maxDepth](#maxDepth)
* [**networkTimeouts](#networkTimeouts)
* [**reportNetworkErrors](#reportNetworkErrors)
* [**sitemapRetries](#sitemapRetries)

## Properties<!-- -->[**](#Properties)

### [**](#emitNestedSitemaps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L179)optionalemitNestedSitemaps

**emitNestedSitemaps?

<!-- -->

: boolean

If set to `true`, elements referring to other sitemaps will be emitted as special objects with `originSitemapUrl` set to `null`.

### [**](#maxDepth)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L183)optionalmaxDepth

**maxDepth?

<!-- -->

: number

Maximum depth of nested sitemaps to follow.

### [**](#networkTimeouts)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L191)optionalnetworkTimeouts

**networkTimeouts?

<!-- -->

: Delays

Network timeouts for sitemap fetching. See [Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/6-timeout.md) for more details.

### [**](#reportNetworkErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L196)optionalreportNetworkErrors

**reportNetworkErrors?

<!-- -->

: boolean = true

If true, the parser will log a warning if it fails to fetch a sitemap due to a network error

### [**](#sitemapRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L187)optionalsitemapRetries

**sitemapRetries?

<!-- -->

: number

Number of retries for fetching sitemaps. The counter resets for each nested sitemap.
