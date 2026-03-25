# Source: https://crawlee.dev/js/api/utils/function/extractUrlsFromCheerio.md

# extractUrlsFromCheerio<!-- -->

### Callable

* ****extractUrlsFromCheerio**($, selector, baseUrl): string\[]

***

* Extracts URLs from a given Cheerio object.

  * **@throws**

    when a relative URL is encountered with no baseUrl set

  ***

  #### Parameters

  * ##### $: [CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

    the Cheerio object to extract URLs from

  * ##### selector: string = <!-- -->'a'

    a CSS selector for matching link elements

  * ##### baseUrl: string = <!-- -->''

    a URL for resolving relative links

  #### Returns string\[]

  An array of absolute URLs
