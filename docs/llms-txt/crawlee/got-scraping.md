# Source: https://crawlee.dev/js/docs/guides/got-scraping.md

# Got Scraping

Copy for LLM

## Intro[​](#intro "Direct link to Intro")

When using `BasicCrawler`, we have to send the requests manually. In order to do this, we can use the context-aware `sendRequest()` function:

```
import { BasicCrawler } from 'crawlee';

const crawler = new BasicCrawler({
    async requestHandler({ sendRequest, log }) {
        const res = await sendRequest();
        log.info('received body', res.body);
    },
});
```

It uses [`got-scraping`](https://github.com/apify/got-scraping) under the hood. Got Scraping is a [Got](https://github.com/sindresorhus/got) extension developed to mimic browser requests, so there's a high chance we'll open the webpage without getting blocked.

## `sendRequest` API[​](#sendrequest-api "Direct link to sendrequest-api")

```
async sendRequest(overrideOptions?: GotOptionsInit) => {
    return gotScraping({
        url: request.url,
        method: request.method,
        body: request.payload,
        headers: request.headers,
        proxyUrl: crawlingContext.proxyInfo?.url,
        sessionToken: session,
        responseType: 'text',
        ...overrideOptions,
        retry: {
            limit: 0,
            ...overrideOptions?.retry,
        },
        cookieJar: {
            getCookieString: (url: string) => session!.getCookieString(url),
            setCookie: (rawCookie: string, url: string) => session!.setCookie(rawCookie, url),
            ...overrideOptions?.cookieJar,
        },
    });
}
```

### `url`[​](#url "Direct link to url")

By default, it's the URL of current task. However you can override this with a `string` or a `URL` instance if necessary.

*More details in [Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/2-options.md#url).*

### `method`[​](#method "Direct link to method")

By default, it's the HTTP method of current task. Possible values are `'GET', 'POST', 'HEAD', 'PUT', 'PATCH', 'DELETE'`.

*More details in [Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/2-options.md#method).*

### `body`[​](#body "Direct link to body")

By default, it's the HTTP payload of current task.

*More details in [Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/2-options.md#body).*

### `headers`[​](#headers "Direct link to headers")

By default, it's the HTTP headers of current task. It's an object with `string` values.

*More details in [Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/2-options.md#headers).*

### `proxyUrl`[​](#proxyurl "Direct link to proxyurl")

It's a string representing the proxy server in the format of `protocol://username:password@hostname:port`.

For example, an Apify proxy server looks like this: `http://auto:password@proxy.apify.com:8000`.

Basic Crawler does not have the concept of a session or proxy, therefore we need to manually pass the `proxyUrl` option:

```
import { BasicCrawler } from 'crawlee';

const crawler = new BasicCrawler({
    async requestHandler({ sendRequest, log }) {
        const res = await sendRequest({
            proxyUrl: 'http://auto:password@proxy.apify.com:8000',
        });
        log.info('received body', res.body);
    },
});
```

We use proxies to hide our real IP address.

*More details in [Got Scraping documentation](https://github.com/apify/got-scraping#proxyurl).*

### `sessionToken`[​](#sessiontoken "Direct link to sessiontoken")

It's a non-primitive object used as a key when generating browser fingerprint. Fingerprints with the same token don't change. This can be used to retain the `user-agent` header when using the same Apify Session.

*More details in [Got Scraping documentation](https://github.com/apify/got-scraping#sessiontoken).*

### `responseType`[​](#responsetype "Direct link to responsetype")

This option defines how the response should be parsed.

By default, we fetch HTML websites - that is plaintext. Hence, we set `responseType` to `'text'`. However, JSON is possible as well:

```
import { BasicCrawler } from 'crawlee';

const crawler = new BasicCrawler({
    async requestHandler({ sendRequest, log }) {
        const res = await sendRequest({ responseType: 'json' });
        log.info('received body', res.body);
    },
});
```

*More details in [Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/2-options.md#responsetype).*

### `cookieJar`[​](#cookiejar "Direct link to cookiejar")

`Got` uses a `cookieJar` to manage cookies. It's an object with an interface of a [`tough-cookie` package](https://github.com/salesforce/tough-cookie).

Example:

```
import { BasicCrawler } from 'crawlee';
import { CookieJar } from 'tough-cookie';

const cookieJar = new CookieJar();

const crawler = new BasicCrawler({
    async requestHandler({ sendRequest, log }) {
        const res = await sendRequest({ cookieJar });
        log.info('received body', res.body);
    },
});
```

*More details in*

* *[Got documentation](https://github.com/sindresorhus/got/blob/main/documentation/2-options.md#cookiejar)*
* *[Tough Cookie documentation](https://github.com/salesforce/tough-cookie#cookiejarstore-options)*

### `retry.limit`[​](#retrylimit "Direct link to retrylimit")

This option specifies the maximum number of `Got` retries.

By default, `retry.limit` is set to `0`. This is because Crawlee has its own (complicated enough) retry management.

We suggest NOT changing this value for stability reasons.

### `useHeaderGenerator`[​](#useheadergenerator "Direct link to useheadergenerator")

It's a boolean for whether to generate browser headers. By default, it's set to `true`, and we recommend keeping this for better results.

### `headerGeneratorOptions`[​](#headergeneratoroptions "Direct link to headergeneratoroptions")

This option represents an object how to generate browser fingerprint. Example:

```
import { BasicCrawler } from 'crawlee';

const crawler = new BasicCrawler({
    async requestHandler({ sendRequest, log }) {
        const res = await sendRequest({
            headerGeneratorOptions: {
                devices: ['mobile', 'desktop'],
                locales: ['en-US'],
                operatingSystems: ['windows', 'macos', 'android', 'ios'],
                browsers: ['chrome', 'edge', 'firefox', 'safari'],
            },
        });
        log.info('received body', res.body);
    },
});
```

*More details in [`HeaderGeneratorOptions` documentation](https://apify.github.io/fingerprint-suite/api/fingerprint-generator/interface/HeaderGeneratorOptions/).*

**Related links**

* [Got documentation](https://github.com/sindresorhus/got#documentation)
* [Got Scraping documentation](https://github.com/apify/got-scraping)
* [Header Generator documentation](https://apify.github.io/fingerprint-suite/docs/guides/fingerprint-generator/)
