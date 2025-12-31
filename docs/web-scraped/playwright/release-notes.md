# Source: https://playwright.dev/docs/release-notes

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Release notes]

On this page

<div>

# Release notes

</div>

## Version 1.57[​](#version-157 "Direct link to Version 1.57") 

### Speedboard[​](#speedboard "Direct link to Speedboard") 

In HTML reporter, there\'s a new tab we call \"Speedboard\":

![Speedboard](/assets/images/speedboard-a8fe4e48388f4075fdd70e83d2b53e7a.png)

It shows you all your executed tests sorted by slowness, and can help you understand where your test suite is taking longer than expected. Take a look at yours - maybe you\'ll find some tests that are spending a longer time waiting than they should!

### Chrome for Testing[​](#chrome-for-testing "Direct link to Chrome for Testing") 

Starting with this release, Playwright switches from Chromium, to using [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) builds. Both headed and headless browsers are subject to this. Your tests should still be passing after upgrading to Playwright 1.57.

We\'re expecting no functional changes to come from this switch. The biggest change is the new icon and title in your toolbar.

![new and old logo](/assets/images/cft-logo-change-e6c83cd629c1cf92a7856fe6e42ab80a.png)

If you still see an unexpected behaviour change, please [file an issue](https://github.com/microsoft/playwright/issues/new).

On Arm64 Linux, Playwright continues to use Chromium.

### Waiting for webserver output[​](#waiting-for-webserver-output "Direct link to Waiting for webserver output") 

[testConfig.webServer](/docs/api/class-testconfig#test-config-web-server) added a `wait` field. Pass a regular expression, and Playwright will wait until the webserver logs match it.

``` 
import  from '@playwright/test';

export default defineConfig(,
  },
});
```

If you include a named capture group into the expression, then Playwright will provide the capture group contents via environment variables:

``` 
import  from '@playwright/test';

test.use(` });

test('homepage', async () => );
```

This is not just useful for capturing varying ports of dev servers. You can also use it to wait for readiness of a service that doesn\'t expose an HTTP readiness check, but instead prints a readiness message to stdout or stderr.

### Breaking Change[​](#breaking-change "Direct link to Breaking Change") 

After 3 years of being deprecated, we removed `page.accessibility` from our API. Please use other libraries such as [Axe](https://www.deque.com/axe/) if you need to test page accessibility. See our Node.js [guide](https://playwright.dev/docs/accessibility-testing) for integration with Axe.

### New APIs[​](#new-apis "Direct link to New APIs") 

-   New property [testConfig.tag](/docs/api/class-testconfig#test-config-tag) adds a tag to all tests in this run. This is useful when using [merge-reports](/docs/test-sharding#merging-reports-from-multiple-shards).
-   [worker.on(\'console\')](/docs/api/class-worker#worker-event-console) event is emitted when JavaScript within the worker calls one of console API methods, e.g. console.log or console.dir. [worker.waitForEvent()](/docs/api/class-worker#worker-wait-for-event) can be used to wait for it.
-   [locator.description()](/docs/api/class-locator#locator-description) returns locator description previously set with [locator.describe()](/docs/api/class-locator#locator-describe), and `Locator.toString()` now uses the description when available.
-   New option [steps](/docs/api/class-locator#locator-click-option-steps) in [locator.click()](/docs/api/class-locator#locator-click) and [locator.dragTo()](/docs/api/class-locator#locator-drag-to) that configures the number of `mousemove` events emitted while moving the mouse pointer to the target element.
-   Network requests issued by [Service Workers](/docs/service-workers#network-events-and-routing) are now reported and can be routed through the [BrowserContext](/docs/api/class-browsercontext), only in Chromium. You can opt out using the `PLAYWRIGHT_DISABLE_SERVICE_WORKER_NETWORK` environment variable.
-   Console messages from Service Workers are dispatched through [worker.on(\'console\')](/docs/api/class-worker#worker-event-console). You can opt out of this using the `PLAYWRIGHT_DISABLE_SERVICE_WORKER_CONSOLE` environment variable.

### Browser Versions[​](#browser-versions "Direct link to Browser Versions") 

-   Chromium 143.0.7499.4
-   Mozilla Firefox 144.0.2
-   WebKit 26.0

## Version 1.56[​](#version-156 "Direct link to Version 1.56")