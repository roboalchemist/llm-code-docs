# Source: https://crawlee.dev/js/docs/guides/session-management.md

# Session Management

Copy for LLM

​[`SessionPool`](https://crawlee.dev/js/api/core/class/SessionPool.md) is a class that allows us to handle the rotation of proxy IP addresses along with cookies and other custom settings in Crawlee.

The main benefit of using Session pool is that we can filter out blocked or non-working proxies, so our actor does not retry requests over known blocked/non-working proxies. Another benefit of using SessionPool is that we can store information tied tightly to an IP address, such as cookies, auth tokens, and particular headers. Having our cookies and other identifiers used only with a specific IP will reduce the chance of being blocked. The last but not least benefit is the even rotation of IP addresses - SessionPool picks the session randomly, which should prevent burning out a small pool of available IPs.

Check out the [avoid blocking guide](https://crawlee.dev/js/docs/guides/avoid-blocking.md) for more information about blocking.

Now let's take a look at the examples of how to use Session pool:

* with [`BasicCrawler`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md);
* with [`HttpCrawler`](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md);
* with [`CheerioCrawler`](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md);
* with [`JSDOMCrawler`](https://crawlee.dev/js/api/jsdom-crawler/class/JSDOMCrawler.md);
* with [`PlaywrightCrawler`](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md);
* with [`PuppeteerCrawler`](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md);
* without a crawler (standalone usage to manage sessions manually).

- BasicCrawler
- HttpCrawler
- CheerioCrawler
- JSDOMCrawler
- PlaywrightCrawler
- PuppeteerCrawler
- Standalone

```
import { BasicCrawler, ProxyConfiguration } from 'crawlee';
import { gotScraping } from 'got-scraping';

const proxyConfiguration = new ProxyConfiguration({
    /* opts */
});

const crawler = new BasicCrawler({
    // Activates the Session pool (default is true).
    useSessionPool: true,
    // Overrides default Session pool configuration.
    sessionPoolOptions: { maxPoolSize: 100 },
    async requestHandler({ request, session }) {
        const { url } = request;
        const requestOptions = {
            url,
            // We use session id in order to have the same proxyUrl
            // for all the requests using the same session.
            proxyUrl: await proxyConfiguration.newUrl(session?.id),
            throwHttpErrors: false,
            headers: {
                // If you want to use the cookieJar.
                // This way you get the Cookie headers string from session.
                Cookie: session?.getCookieString(url),
            },
        };
        let response;

        try {
            response = await gotScraping(requestOptions);
        } catch (e) {
            if (e === 'SomeNetworkError') {
                // If a network error happens, such as timeout, socket hangup, etc.
                // There is usually a chance that it was just bad luck
                // and the proxy works. No need to throw it away.
                session?.markBad();
            }
            throw e;
        }

        // Automatically retires the session based on response HTTP status code.
        session?.retireOnBlockedStatusCodes(response.statusCode);

        if (response.body.includes('You are blocked!')) {
            // You are sure it is blocked.
            // This will throw away the session.
            session?.retire();
        }

        // Everything is ok, you can get the data.
        // No need to call session.markGood -> BasicCrawler calls it for you.

        // If you want to use the CookieJar in session you need.
        session?.setCookiesFromResponse(response);
    },
});
```

```
import { HttpCrawler, ProxyConfiguration } from 'crawlee';

const proxyConfiguration = new ProxyConfiguration({
    /* opts */
});

const crawler = new HttpCrawler({
    // To use the proxy IP session rotation logic, you must turn the proxy usage on.
    proxyConfiguration,
    // Activates the Session pool (default is true).
    useSessionPool: true,
    // Overrides default Session pool configuration.
    sessionPoolOptions: { maxPoolSize: 100 },
    // Set to true if you want the crawler to save cookies per session,
    // and set the cookie header to request automatically (default is true).
    persistCookiesPerSession: true,
    async requestHandler({ session, body }) {
        const title = (body as string).match(/<title(?:.*?)>(.*?)<\/title>/)?.[1];

        if (title === 'Blocked') {
            session?.retire();
        } else if (title === 'Not sure if blocked, might also be a connection error') {
            session?.markBad();
        } else {
            // session.markGood() - this step is done automatically in BasicCrawler.
        }
    },
});
```

```
import { CheerioCrawler, ProxyConfiguration } from 'crawlee';

const proxyConfiguration = new ProxyConfiguration({
    /* opts */
});

const crawler = new CheerioCrawler({
    // To use the proxy IP session rotation logic, you must turn the proxy usage on.
    proxyConfiguration,
    // Activates the Session pool (default is true).
    useSessionPool: true,
    // Overrides default Session pool configuration.
    sessionPoolOptions: { maxPoolSize: 100 },
    // Set to true if you want the crawler to save cookies per session,
    // and set the cookie header to request automatically (default is true).
    persistCookiesPerSession: true,
    async requestHandler({ session, $ }) {
        const title = $('title').text();

        if (title === 'Blocked') {
            session?.retire();
        } else if (title === 'Not sure if blocked, might also be a connection error') {
            session?.markBad();
        } else {
            // session.markGood() - this step is done automatically in BasicCrawler.
        }
    },
});
```

```
import { JSDOMCrawler, ProxyConfiguration } from 'crawlee';

const proxyConfiguration = new ProxyConfiguration({
    /* opts */
});

const crawler = new JSDOMCrawler({
    // To use the proxy IP session rotation logic, you must turn the proxy usage on.
    proxyConfiguration,
    // Activates the Session pool (default is true).
    useSessionPool: true,
    // Overrides default Session pool configuration.
    sessionPoolOptions: { maxPoolSize: 100 },
    // Set to true if you want the crawler to save cookies per session,
    // and set the cookie header to request automatically (default is true).
    persistCookiesPerSession: true,
    async requestHandler({ session, window }) {
        const title = window.document.title;

        if (title === 'Blocked') {
            session?.retire();
        } else if (title === 'Not sure if blocked, might also be a connection error') {
            session?.markBad();
        } else {
            // session.markGood() - this step is done automatically in BasicCrawler.
        }
    },
});
```

```
import { PlaywrightCrawler, ProxyConfiguration } from 'crawlee';

const proxyConfiguration = new ProxyConfiguration({
    /* opts */
});

const crawler = new PlaywrightCrawler({
    // To use the proxy IP session rotation logic, you must turn the proxy usage on.
    proxyConfiguration,
    // Activates the Session pool (default is true).
    useSessionPool: true,
    // Overrides default Session pool configuration
    sessionPoolOptions: { maxPoolSize: 100 },
    // Set to true if you want the crawler to save cookies per session,
    // and set the cookies to page before navigation automatically (default is true).
    persistCookiesPerSession: true,
    async requestHandler({ page, session }) {
        const title = await page.title();

        if (title === 'Blocked') {
            session?.retire();
        } else if (title === 'Not sure if blocked, might also be a connection error') {
            session?.markBad();
        } else {
            // session.markGood() - this step is done automatically in PlaywrightCrawler.
        }
    },
});
```

```
import { PuppeteerCrawler, ProxyConfiguration } from 'crawlee';

const proxyConfiguration = new ProxyConfiguration({
    /* opts */
});

const crawler = new PuppeteerCrawler({
    // To use the proxy IP session rotation logic, you must turn the proxy usage on.
    proxyConfiguration,
    // Activates the Session pool (default is true).
    useSessionPool: true,
    // Overrides default Session pool configuration
    sessionPoolOptions: { maxPoolSize: 100 },
    // Set to true if you want the crawler to save cookies per session,
    // and set the cookies to page before navigation automatically (default is true).
    persistCookiesPerSession: true,
    async requestHandler({ page, session }) {
        const title = await page.title();

        if (title === 'Blocked') {
            session?.retire();
        } else if (title === 'Not sure if blocked, might also be a connection error') {
            session?.markBad();
        } else {
            // session.markGood() - this step is done automatically in PuppeteerCrawler.
        }
    },
});
```

```
import { SessionPool } from 'crawlee';

// Override the default Session pool configuration.
const sessionPoolOptions = {
    maxPoolSize: 100,
};

// Open Session Pool.
const sessionPool = await SessionPool.open(sessionPoolOptions);

// Get session.
const session = await sessionPool.getSession();

// Increase the errorScore.
session.markBad();

// Throw away the session.
session.retire();

// Lower the errorScore and mark the session good.
session.markGood();
```

These are the basics of configuring SessionPool. Please, bear in mind that a Session pool needs time to find working IPs and build up the pool, so we will probably see a lot of errors until it becomes stabilized.
