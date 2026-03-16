# Source: https://crawlee.dev/js/api/utils.md

# @crawlee/utils<!-- -->

## Index[**](#Index)

### References

* [**Cheerio](https://crawlee.dev/js/api/utils.md#Cheerio)
* [**CheerioAPI](https://crawlee.dev/js/api/utils.md#CheerioAPI)
* [**CheerioRoot](https://crawlee.dev/js/api/utils.md#CheerioRoot)
* [**Element](https://crawlee.dev/js/api/utils.md#Element)
* [**RobotsFile](https://crawlee.dev/js/api/utils.md#RobotsFile)
* [**tryAbsoluteURL](https://crawlee.dev/js/api/utils.md#tryAbsoluteURL)

### Namespaces

* [**social](https://crawlee.dev/js/api/utils/namespace/social.md)

### Classes

* [**RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md)
* [**Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)

### Interfaces

* [**DownloadListOfUrlsOptions](https://crawlee.dev/js/api/utils/interface/DownloadListOfUrlsOptions.md)
* [**ExtractUrlsOptions](https://crawlee.dev/js/api/utils/interface/ExtractUrlsOptions.md)
* [**MemoryInfo](https://crawlee.dev/js/api/utils/interface/MemoryInfo.md)
* [**OpenGraphProperty](https://crawlee.dev/js/api/utils/interface/OpenGraphProperty.md)
* [**ParseSitemapOptions](https://crawlee.dev/js/api/utils/interface/ParseSitemapOptions.md)

### Type Aliases

* [**SearchParams](https://crawlee.dev/js/api/utils.md#SearchParams)
* [**SitemapUrl](https://crawlee.dev/js/api/utils.md#SitemapUrl)

### Variables

* [**CLOUDFLARE\_RETRY\_CSS\_SELECTORS](https://crawlee.dev/js/api/utils.md#CLOUDFLARE_RETRY_CSS_SELECTORS)
* [**RETRY\_CSS\_SELECTORS](https://crawlee.dev/js/api/utils.md#RETRY_CSS_SELECTORS)
* [**ROTATE\_PROXY\_ERRORS](https://crawlee.dev/js/api/utils.md#ROTATE_PROXY_ERRORS)
* [**URL\_NO\_COMMAS\_REGEX](https://crawlee.dev/js/api/utils.md#URL_NO_COMMAS_REGEX)
* [**URL\_WITH\_COMMAS\_REGEX](https://crawlee.dev/js/api/utils.md#URL_WITH_COMMAS_REGEX)

### Functions

* [**chunk](https://crawlee.dev/js/api/utils/function/chunk.md)
* [**createRequestDebugInfo](https://crawlee.dev/js/api/utils/function/createRequestDebugInfo.md)
* [**discoverValidSitemaps](https://crawlee.dev/js/api/utils/function/discoverValidSitemaps.md)
* [**downloadListOfUrls](https://crawlee.dev/js/api/utils/function/downloadListOfUrls.md)
* [**extractUrls](https://crawlee.dev/js/api/utils/function/extractUrls.md)
* [**extractUrlsFromCheerio](https://crawlee.dev/js/api/utils/function/extractUrlsFromCheerio.md)
* [**getCgroupsVersion](https://crawlee.dev/js/api/utils/function/getCgroupsVersion.md)
* [**getMemoryInfo](https://crawlee.dev/js/api/utils/function/getMemoryInfo.md)
* [**getObjectType](https://crawlee.dev/js/api/utils/function/getObjectType.md)
* [**gotScraping](https://crawlee.dev/js/api/utils/function/gotScraping.md)
* [**htmlToText](https://crawlee.dev/js/api/utils/function/htmlToText.md)
* [**isContainerized](https://crawlee.dev/js/api/utils/function/isContainerized.md)
* [**isDocker](https://crawlee.dev/js/api/utils/function/isDocker.md)
* [**isLambda](https://crawlee.dev/js/api/utils/function/isLambda.md)
* [**mergeAsyncIterables](https://crawlee.dev/js/api/utils/function/mergeAsyncIterables.md)
* [**parseOpenGraph](https://crawlee.dev/js/api/utils/function/parseOpenGraph.md)
* [**parseSitemap](https://crawlee.dev/js/api/utils/function/parseSitemap.md)
* [**sleep](https://crawlee.dev/js/api/utils/function/sleep.md)

## References<!-- -->[**](#References)

### [**](#Cheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/cheerio.ts#L9)Cheerio

Re-exports

<!-- -->

[Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)

### [**](#CheerioAPI)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/cheerio.ts#L9)CheerioAPI

Re-exports

<!-- -->

[CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

### [**](#CheerioRoot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/cheerio.ts#L8)CheerioRoot

Re-exports

<!-- -->

[CheerioRoot](https://crawlee.dev/js/api/basic-crawler.md#CheerioRoot)

### [**](#Element)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/cheerio.ts#L9)Element

Re-exports

<!-- -->

[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)

### [**](#RobotsFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L122)RobotsFile

Renames and re-exports

<!-- -->

[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md)

### [**](#tryAbsoluteURL)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/extract-urls.ts#L96)tryAbsoluteURL

Re-exports

<!-- -->

[tryAbsoluteURL](https://crawlee.dev/js/api/core/function/tryAbsoluteURL.md)

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#SearchParams)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/url.ts#L1)SearchParams

**SearchParams: string | URLSearchParams | Record\<string, string | number | boolean | null | undefined>

### [**](#SitemapUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L24)SitemapUrl

**SitemapUrl: SitemapUrlData & { originSitemapUrl: string }

## Variables<!-- -->[**](#Variables)

### [**](#CLOUDFLARE_RETRY_CSS_SELECTORS)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/blocked.ts#L1)constCLOUDFLARE\_RETRY\_CSS\_SELECTORS

**CLOUDFLARE\_RETRY\_CSS\_SELECTORS: string\[] =

<!-- -->

...

### [**](#RETRY_CSS_SELECTORS)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/blocked.ts#L6)constRETRY\_CSS\_SELECTORS

**RETRY\_CSS\_SELECTORS: string\[] =

<!-- -->

...

CSS selectors for elements that should trigger a retry, as the crawler is likely getting blocked.

### [**](#ROTATE_PROXY_ERRORS)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/blocked.ts#L15)constROTATE\_PROXY\_ERRORS

**ROTATE\_PROXY\_ERRORS: string\[] =

<!-- -->

...

Content of proxy errors that should trigger a retry, as the proxy is likely getting blocked / is malfunctioning.

### [**](#URL_NO_COMMAS_REGEX)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/general.ts#L8)constURL\_NO\_COMMAS\_REGEX

**URL\_NO\_COMMAS\_REGEX: RegExp =

<!-- -->

...

Default regular expression to match URLs in a string that may be plain text, JSON, CSV or other. It supports common URL characters and does not support URLs containing commas or spaces. The URLs also may contain Unicode letters (not symbols).

### [**](#URL_WITH_COMMAS_REGEX)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/general.ts#L15)constURL\_WITH\_COMMAS\_REGEX

**URL\_WITH\_COMMAS\_REGEX: RegExp =

<!-- -->

...

Regular expression that, in addition to the default regular expression `URL_NO_COMMAS_REGEX`, supports matching commas in URL path and query. Note, however, that this may prevent parsing URLs from comma delimited lists, or the URLs may become malformed.
