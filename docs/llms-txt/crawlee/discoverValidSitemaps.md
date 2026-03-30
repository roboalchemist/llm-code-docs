# Source: https://crawlee.dev/js/api/utils/function/discoverValidSitemaps.md

# discoverValidSitemaps<!-- -->

### Callable

* ****discoverValidSitemaps**(urls, options): AsyncIterable\<string>

***

* Given a list of URLs, discover related sitemap files for these domains by checking the `robots.txt` file, the default `sitemap.xml` & `sitemap.txt` files and the URLs themselves.

  ***

  #### Parameters

  * ##### urls: string\[]
  * ##### options: { proxyUrl?<!-- -->: string } = <!-- -->{}
    * ##### optionalproxyUrl: string

      Proxy URL to be used for network requests.

  #### Returns AsyncIterable\<string>

  An async iterable with the discovered sitemap URLs.
