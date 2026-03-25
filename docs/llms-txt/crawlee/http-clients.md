# Source: https://crawlee.dev/js/docs/guides/http-clients.md

# HTTP clients

Copy for LLM

HTTP clients are utilized by HTTP-based crawlers (e.g., [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md)) to communicate with web servers. They use external HTTP libraries for communication rather than a browser. Examples of such libraries include [`impit`](https://apify.github.io/impit/) or [`got-scraping`](https://github.com/apify/got-scraping/). After retrieving page content, an HTML parsing library is typically used to facilitate data extraction. Examples of such libraries include [Cheerio](https://cheerio.js.org/), [`jsdom`](https://github.com/jsdom/jsdom) or [`linkedom`](https://github.com/WebReflection/linkedom). These crawlers are faster than browser-based crawlers but generally cannot execute client-side JavaScript.

<!-- -->

## Switching between HTTP clients[​](#switching-between-http-clients "Direct link to Switching between HTTP clients")

Crawlee currently provides two main HTTP clients: [`GotScrapingHttpClient`](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md), which uses the `got-scraping` library, and [`ImpitHttpClient`](https://crawlee.dev/js/api/impit-client/class/ImpitHttpClient.md), which uses the `impit` library. You can switch between them by setting the `BasehttpClient` parameter when initializing a crawler class. The default HTTP client is [`GotScrapingHttpClient`](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md). For more details on anti-blocking features, see our [avoid getting blocked guide](https://crawlee.dev/js/docs/guides/avoid-blocking.md).

Below are examples of how to configure the HTTP client for the [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md):

* CheerioCrawler with got-scraping
* CheerioCrawler with impit

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyLCBHb3RTY3JhcGluZ0h0dHBDbGllbnQgfSBmcm9tICdjcmF3bGVlJztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IENoZWVyaW9DcmF3bGVyKHtcXG4gICAgaHR0cENsaWVudDogbmV3IEdvdFNjcmFwaW5nSHR0cENsaWVudCgpLFxcbiAgICBhc3luYyByZXF1ZXN0SGFuZGxlcigpIHtcXG4gICAgICAgIC8qIC4uLiAqL1xcbiAgICB9LFxcbn0pO1xcblwifSIsIm9wdGlvbnMiOnsiYnVpbGQiOiJsYXRlc3QiLCJjb250ZW50VHlwZSI6ImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9dXRmLTgiLCJtZW1vcnkiOjEwMjQsInRpbWVvdXQiOjE4MH19.gVbxQc8YHS-heqm2fIMqyh4K1TDRG4xLsBOxCcZVosM\&asrc=run_on_apify)

```
import { CheerioCrawler, GotScrapingHttpClient } from 'crawlee';

const crawler = new CheerioCrawler({
    httpClient: new GotScrapingHttpClient(),
    async requestHandler() {
        /* ... */
    },
});
```

[Run on](https://console.apify.com/actors/6i5QsHBMtm3hKph70?runConfig=eyJ1IjoiRWdQdHczb2VqNlRhRHQ1cW4iLCJ2IjoxfQ.eyJpbnB1dCI6IntcImNvZGVcIjpcImltcG9ydCB7IENoZWVyaW9DcmF3bGVyIH0gZnJvbSAnY3Jhd2xlZSc7XFxuaW1wb3J0IHsgSW1waXRIdHRwQ2xpZW50IH0gZnJvbSAnQGNyYXdsZWUvaW1waXQtY2xpZW50JztcXG5cXG5jb25zdCBjcmF3bGVyID0gbmV3IENoZWVyaW9DcmF3bGVyKHtcXG4gICAgaHR0cENsaWVudDogbmV3IEltcGl0SHR0cENsaWVudCh7XFxuICAgICAgICAvLyBTZXQtdXAgb3B0aW9ucyBmb3IgdGhlIGltcGl0IGxpYnJhcnlcXG4gICAgICAgIGlnbm9yZVRsc0Vycm9yczogdHJ1ZSxcXG4gICAgICAgIGJyb3dzZXI6ICdmaXJlZm94JyxcXG4gICAgfSksXFxuICAgIGFzeW5jIHJlcXVlc3RIYW5kbGVyKCkge1xcbiAgICAgICAgLyogLi4uICovXFxuICAgIH0sXFxufSk7XFxuXCJ9Iiwib3B0aW9ucyI6eyJidWlsZCI6ImxhdGVzdCIsImNvbnRlbnRUeXBlIjoiYXBwbGljYXRpb24vanNvbjsgY2hhcnNldD11dGYtOCIsIm1lbW9yeSI6MTAyNCwidGltZW91dCI6MTgwfX0.61KJ6GZIe3uUC6YCQVmfJ5rjmmk37iVIh5W0icmZIG0\&asrc=run_on_apify)

```
import { CheerioCrawler } from 'crawlee';
import { ImpitHttpClient } from '@crawlee/impit-client';

const crawler = new CheerioCrawler({
    httpClient: new ImpitHttpClient({
        // Set-up options for the impit library
        ignoreTlsErrors: true,
        browser: 'firefox',
    }),
    async requestHandler() {
        /* ... */
    },
});
```

## Installation requirements[​](#installation-requirements "Direct link to Installation requirements")

Since [`GotScrapingHttpClient`](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md) is the default HTTP client, it's included with the base Crawlee installation and requires no additional packages.

For [`ImpitHttpClient`](https://crawlee.dev/js/api/impit-client/class/ImpitHttpClient.md), you need to install a separate `@crawlee/impit-client` package:

```
npm i @crawlee/impit-client
```

## Creating custom HTTP clients[​](#creating-custom-http-clients "Direct link to Creating custom HTTP clients")

Crawlee provides an interface, [`BaseHttpClient`](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md), which defines the interface that all HTTP clients must implement. This allows you to create custom HTTP clients tailored to your specific requirements.

HTTP clients are responsible for several key operations:

* sending HTTP requests and receiving responses,
* managing cookies and sessions,
* handling headers and authentication,
* managing proxy configurations,
* connection pooling with timeout management.

To create a custom HTTP client, you need to implement the [`BaseHttpClient`](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md) interface. Your implementation must be async-compatible and include proper cleanup and resource management to work seamlessly with Crawlee's concurrent processing model.

## Conclusion[​](#conclusion "Direct link to Conclusion")

This guide introduced you to the HTTP clients available in Crawlee and demonstrated how to switch between them, including their installation requirements and usage examples. You also learned about the responsibilities of HTTP clients and how to implement your own custom HTTP client by inheriting from the [`BaseHttpClient`](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md) base class.

If you have questions or need assistance, feel free to reach out on our [GitHub](https://github.com/apify/crawlee) or join our [Discord community](https://discord.com/invite/jyEM2PRvMU). Happy scraping!
