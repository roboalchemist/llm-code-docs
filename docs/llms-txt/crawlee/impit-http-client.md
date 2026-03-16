# Source: https://crawlee.dev/js/docs/guides/impit-http-client.md

# Impit HTTP Client

Copy for LLM

## Introduction[​](#introduction "Direct link to Introduction")

The `ImpitHttpClient` is an HTTP client implementation based on the [Impit](https://github.com/apify/impit) library. It enables browser impersonation for HTTP requests, helping you bypass bot detection systems without running an actual browser.

Successor to got-scraping

Impit is the successor to `got-scraping`, which is no longer actively maintained. We recommend using `ImpitHttpClient` for all new projects. Impit provides better anti-bot evasion through TLS fingerprinting and HTTP/3 support, while maintaining a smaller package size.

**Impit will become the default HTTP client in the next major version of Crawlee.**

### Why use Impit?[​](#why-use-impit "Direct link to Why use Impit?")

Websites increasingly use sophisticated bot detection that analyzes:

* **HTTP fingerprints**: User-Agent strings, header ordering, HTTP/2 pseudo-header sequences
* **TLS fingerprints**: Cipher suites, TLS extensions, and cryptographic details in the ClientHello message

Standard HTTP clients like `fetch` or `axios` are easily detected because their fingerprints don't match real browsers. Unlike `got-scraping` which only handles HTTP-level fingerprinting, Impit also mimics TLS fingerprints, making requests appear to come from real browsers.

## Installation[​](#installation "Direct link to Installation")

Install the `@crawlee/impit-client` package:

```
npm install @crawlee/impit-client
```

note

The `impit` package includes native binaries and supports Windows, macOS (including ARM), and Linux out of the box.

## Basic usage[​](#basic-usage "Direct link to Basic usage")

Pass the `ImpitHttpClient` instance to the `httpClient` option of any Crawlee crawler:

```
import { BasicCrawler } from 'crawlee';
import { ImpitHttpClient, Browser } from '@crawlee/impit-client';

const crawler = new BasicCrawler({
    httpClient: new ImpitHttpClient({
        browser: Browser.Firefox,
    }),
    async requestHandler({ sendRequest, log }) {
        const response = await sendRequest();
        log.info('Received response', { statusCode: response.statusCode });
    },
});

await crawler.run(['https://example.com']);
```

## Usage with different crawlers[​](#usage-with-different-crawlers "Direct link to Usage with different crawlers")

### CheerioCrawler[​](#cheeriocrawler "Direct link to CheerioCrawler")

```
import { CheerioCrawler } from 'crawlee';
import { ImpitHttpClient, Browser } from '@crawlee/impit-client';

const crawler = new CheerioCrawler({
    httpClient: new ImpitHttpClient({
        browser: Browser.Chrome,
    }),
    async requestHandler({ $, request, enqueueLinks, pushData }) {
        const title = $('title').text();
        const h1 = $('h1').first().text();

        await pushData({
            url: request.url,
            title,
            h1,
        });

        // Enqueue links found on the page
        await enqueueLinks();
    },
});

await crawler.run(['https://example.com']);
```

### HttpCrawler[​](#httpcrawler "Direct link to HttpCrawler")

```
import { HttpCrawler } from 'crawlee';
import { ImpitHttpClient, Browser } from '@crawlee/impit-client';

const crawler = new HttpCrawler({
    httpClient: new ImpitHttpClient({
        browser: Browser.Firefox,
        http3: true,
    }),
    async requestHandler({ body, request, log, pushData }) {
        log.info(`Processing ${request.url}`);

        // body is the raw HTML string
        await pushData({
            url: request.url,
            bodyLength: body.length,
        });
    },
});

await crawler.run(['https://example.com']);
```

## Configuration options[​](#configuration-options "Direct link to Configuration options")

The `ImpitHttpClient` constructor accepts the following options:

| Option            | Type                               | Default     | Description                                                                    |
| ----------------- | ---------------------------------- | ----------- | ------------------------------------------------------------------------------ |
| `browser`         | `'chrome'` \| `'firefox'` \| `...` | `undefined` | Browser to impersonate. Affects TLS fingerprint and default headers.           |
| `http3`           | `boolean`                          | `false`     | Enable HTTP/3 (QUIC) protocol support.                                         |
| `ignoreTlsErrors` | `boolean`                          | `false`     | Ignore TLS certificate errors. Useful for testing or self-signed certificates. |

### Available fingerprints[​](#available-fingerprints "Direct link to Available fingerprints")

Impit bundles several realistic browser fingerprints. Using version-specific fingerprints can improve success rates against sophisticated bot detection systems that track browser versions and flag outdated signatures.

When using generic fingerprints (`chrome` or `firefox`), Impit automatically selects an appropriate version. For most use cases, the generic options are sufficient. However, if you're targeting a site with particularly strict bot detection, or need to match a specific browser environment, you can specify an exact version:

```
import { ImpitHttpClient } from '@crawlee/impit-client';

// Use a generic Chrome fingerprint
const chromeClient = new ImpitHttpClient({ browser: 'chrome' });

// Use a specific Chrome version
const chrome131Client = new ImpitHttpClient({ browser: 'chrome131' });

// Or a specific Firefox version
const firefox144Client = new ImpitHttpClient({ browser: 'firefox144' });
```

### Advanced configuration[​](#advanced-configuration "Direct link to Advanced configuration")

```
import { CheerioCrawler } from 'crawlee';
import { ImpitHttpClient, Browser } from '@crawlee/impit-client';

const crawler = new CheerioCrawler({
    httpClient: new ImpitHttpClient({
        // Impersonate Chrome browser
        browser: Browser.Chrome,
        // Enable HTTP/3 protocol
        http3: true,
    }),
    async requestHandler({ $ }) {
        console.log(`Title: ${$('title').text()}`);
    },
});

await crawler.run(['https://example.com']);
```

## Proxy support[​](#proxy-support "Direct link to Proxy support")

Proxies are configured per-request through Crawlee's proxy management system, not on the `ImpitHttpClient` itself. Use `ProxyConfiguration` as you normally would:

```
import { CheerioCrawler, ProxyConfiguration } from 'crawlee';
import { ImpitHttpClient, Browser } from '@crawlee/impit-client';

const proxyConfiguration = new ProxyConfiguration({
    proxyUrls: ['http://proxy1.example.com:8080', 'http://proxy2.example.com:8080'],
});

const crawler = new CheerioCrawler({
    httpClient: new ImpitHttpClient({ browser: Browser.Chrome }),
    proxyConfiguration,
    async requestHandler({ $, request }) {
        console.log(`Scraped ${request.url}`);
    },
});
```

## How it works[​](#how-it-works "Direct link to How it works")

Impit achieves browser impersonation at two levels:

1. **HTTP level**: Mimics browser-specific header ordering, HTTP/2 settings, and pseudo-header sequences that antibot services analyze.

2. **TLS level**: Uses a patched version of `rustls` to replicate the exact TLS ClientHello message that browsers send, including cipher suites and extensions.

This dual-layer approach makes requests appear to come from a real browser, significantly reducing blocks from bot detection systems.

## Comparison with other solutions[​](#comparison-with-other-solutions "Direct link to Comparison with other solutions")

| Feature                | got-scraping | curl-impersonate   | Impit  |
| ---------------------- | ------------ | ------------------ | ------ |
| TLS fingerprinting     | No           | Yes                | Yes    |
| HTTP/3 support         | No           | Yes                | Yes    |
| Native Node.js package | Yes          | No (child process) | Yes    |
| Windows/macOS ARM      | Yes          | No                 | Yes    |
| Package size           | \~10 MB      | \~20 MB            | \~8 MB |

**Related links**

* [Impit GitHub repository](https://github.com/apify/impit)
* [Custom HTTP Client guide](https://crawlee.dev/js/docs/guides/custom-http-client.md)
* [Proxy Management guide](https://crawlee.dev/js/docs/guides/proxy-management.md)
* [Avoiding blocking guide](https://crawlee.dev/js/docs/guides/avoid-blocking.md)
