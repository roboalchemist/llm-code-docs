# Source: https://crawlee.dev/js/api/utils/class/Sitemap.md

# Sitemap<!-- -->

Loads one or more sitemaps from given URLs, following references in sitemap index files, and exposes the contained URLs.

**Example usage:**

```
// Load a sitemap
const sitemap = await Sitemap.load(['https://example.com/sitemap.xml', 'https://example.com/sitemap_2.xml.gz']);

// Enqueue all the contained URLs (including those from sub-sitemaps from sitemap indexes)
await crawler.addRequests(sitemap.urls);
```

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**urls](#urls)

### Methods

* [**fromXmlString](#fromXmlString)
* [**load](#load)
* [**tryCommonNames](#tryCommonNames)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L375)constructor

* ****new Sitemap**(urls): [Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)

- #### Parameters

  * ##### urls: string\[]

  #### Returns [Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)

## Properties<!-- -->[**](#Properties)

### [**](#urls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L375)readonlyurls

**urls: string\[]

## Methods<!-- -->[**](#Methods)

### [**](#fromXmlString)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L420)staticfromXmlString

* ****fromXmlString**(content, proxyUrl): Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

- Parse XML sitemap content from a string and return URLs of referenced pages. If the sitemap references other sitemaps, they will be loaded via HTTP.

  ***

  #### Parameters

  * ##### content: string

    XML sitemap content

  * ##### optionalproxyUrl: string

    URL of a proxy to be used for fetching sitemap contents

  #### Returns Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

### [**](#load)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L403)staticload

* ****load**(urls, proxyUrl, parseSitemapOptions): Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

- Fetch sitemap content from given URL or URLs and return URLs of referenced pages.

  ***

  #### Parameters

  * ##### urls: string | string\[]

    sitemap URL(s)

  * ##### optionalproxyUrl: string

    URL of a proxy to be used for fetching sitemap contents

  * ##### optionalparseSitemapOptions: [ParseSitemapOptions](https://crawlee.dev/js/api/utils/interface/ParseSitemapOptions.md)

  #### Returns Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

### [**](#tryCommonNames)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/sitemap.ts#L383)statictryCommonNames

* ****tryCommonNames**(url, proxyUrl): Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

- Try to load sitemap from the most common locations - `/sitemap.xml` and `/sitemap.txt`. For loading based on `Sitemap` entries in `robots.txt`, the [RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md) class should be used.

  ***

  #### Parameters

  * ##### url: string

    The domain URL to fetch the sitemap for.

  * ##### optionalproxyUrl: string

    A proxy to be used for fetching the sitemap file.

  #### Returns Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>
