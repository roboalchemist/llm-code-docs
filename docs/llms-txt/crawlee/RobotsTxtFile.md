# Source: https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md

# RobotsTxtFile<!-- -->

Loads and queries information from a [robots.txt file](https://en.wikipedia.org/wiki/Robots.txt).

**Example usage:**

```
// Load the robots.txt file
const robots = await RobotsTxtFile.find('https://crawlee.dev/js/docs/introduction/first-crawler');

// Check if a URL should be crawled according to robots.txt
const url = 'https://crawlee.dev/api/puppeteer-crawler/class/PuppeteerCrawler';
if (robots.isAllowed(url)) {
  await crawler.addRequests([url]);
}

// Enqueue all links in the sitemap(s)
await crawler.addRequests(await robots.parseUrlsFromSitemaps());
```

## Index[**](#Index)

### Methods

* [**getSitemaps](#getSitemaps)
* [**isAllowed](#isAllowed)
* [**parseSitemaps](#parseSitemaps)
* [**parseUrlsFromSitemaps](#parseUrlsFromSitemaps)
* [**find](#find)
* [**from](#from)

## Methods<!-- -->[**](#Methods)

### [**](#getSitemaps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L102)getSitemaps

* ****getSitemaps**(): string\[]

- Get URLs of sitemaps referenced in the robots file.

  ***

  #### Returns string\[]

### [**](#isAllowed)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L95)isAllowed

* ****isAllowed**(url, userAgent): boolean

- Check if a URL should be crawled by robots.

  ***

  #### Parameters

  * ##### url: string

    the URL to check against the rules in robots.txt

  * ##### optionaluserAgent: string = <!-- -->'\*'

    relevant user agent, default to `*`

  #### Returns boolean

### [**](#parseSitemaps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L109)parseSitemaps

* ****parseSitemaps**(): Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

- Parse all the sitemaps referenced in the robots file.

  ***

  #### Returns Promise<[Sitemap](https://crawlee.dev/js/api/utils/class/Sitemap.md)>

### [**](#parseUrlsFromSitemaps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L116)parseUrlsFromSitemaps

* ****parseUrlsFromSitemaps**(): Promise\<string\[]>

- Get all URLs from all the sitemaps referenced in the robots file. A shorthand for `(await robots.parseSitemaps()).urls`.

  ***

  #### Returns Promise\<string\[]>

### [**](#find)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L40)staticfind

* ****find**(url, proxyUrl): Promise<[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md)>

- Determine the location of a robots.txt file for a URL and fetch it.

  ***

  #### Parameters

  * ##### url: string

    the URL to fetch robots.txt for

  * ##### optionalproxyUrl: string

    a proxy to be used for fetching the robots.txt file

  #### Returns Promise<[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md)>

### [**](#from)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/utils/src/internals/robots.ts#L54)staticfrom

* ****from**(url, content, proxyUrl): [RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md)

- Allows providing the URL and robots.txt content explicitly instead of loading it from the target site.

  ***

  #### Parameters

  * ##### url: string

    the URL for robots.txt file

  * ##### content: string

    contents of robots.txt

  * ##### optionalproxyUrl: string

    a proxy to be used for fetching the robots.txt file

  #### Returns [RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md)
