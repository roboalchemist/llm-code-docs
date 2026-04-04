# Source: https://crawlee.dev/js/api/browser-pool.md

# @crawlee/browser-pool<!-- -->

Browser Pool is a small, but powerful and extensible library, that allows you to seamlessly control multiple headless browsers at the same time with only a little configuration, and a single function call. Currently, it supports [Puppeteer](https://github.com/puppeteer/puppeteer), [Playwright](https://github.com/microsoft/playwright), and it can be easily extended with plugins.

We created Browser Pool because we regularly needed to execute tasks concurrently in many headless browsers and their pages, but we did not want to worry about launching browsers, closing browsers, restarting them after crashes and so on. We also wanted to easily and reliably manage the whole browser/page lifecycle.

You can use Browser Pool for scraping the internet at scale, testing your website in multiple browsers at the same time or launching web automation robots.

## Installation[​](#installation "Direct link to Installation")

Use NPM or Yarn to install `@crawlee/browser-pool`. Note that `@crawlee/browser-pool` does not come preinstalled with browser automation libraries. This allows you to choose your own libraries and their versions, and it also makes `@crawlee/browser-pool` much smaller.

Run this command to install `@crawlee/browser-pool` and the `playwright` browser automation library.

```
npm install @crawlee/browser-pool playwright
```

## Usage[​](#usage "Direct link to Usage")

This simple example shows how to open a page in a browser using Browser Pool. We use the provided `PlaywrightPlugin` to wrap a Playwright installation of your own. By calling `browserPool.newPage()` you launch a new Firefox browser and open a new page in that browser.

```
import { BrowserPool, PlaywrightPlugin } from '@crawlee/browser-pool';
import playwright from 'playwright';

const browserPool = new BrowserPool({
    browserPlugins: [new PlaywrightPlugin(playwright.chromium)],
});

// Launches Chromium with Playwright and returns a Playwright Page.
const page1 = await browserPool.newPage();
// You can interact with the page as you're used to.
await page1.goto('https://example.com');
// When you're done, close the page.
await page1.close();

// Opens a second page in the same browser.
const page2 = await browserPool.newPage();
// When everything's finished, tear down the pool.
await browserPool.destroy();
```

## Launching multiple browsers[​](#launching-multiple-browsers "Direct link to Launching multiple browsers")

The basic example shows how to launch a single browser, but the purpose of Browser Pool is to launch many browsers. This is done automatically in the background. You only need to provide the relevant plugins and call `browserPool.newPage()`.

```
import { BrowserPool, PlaywrightPlugin } from '@crawlee/browser-pool';
import playwright from 'playwright';

const browserPool = new BrowserPool({
    browserPlugins: [
        new PlaywrightPlugin(playwright.chromium),
        new PlaywrightPlugin(playwright.firefox),
        new PlaywrightPlugin(playwright.webkit),
    ],
});

// Open 4 pages in 3 browsers. The browsers are launched
// in a round-robin fashion based on the plugin order.
const chromiumPage = await browserPool.newPage();
const firefoxPage = await browserPool.newPage();
const webkitPage = await browserPool.newPage();
const chromiumPage2 = await browserPool.newPage();

// Don't forget to close pages / destroy pool when you're done.
```

This round-robin way of opening pages may not be useful for you, if you need to consistently run tasks in multiple environments. For that, there's the `newPageWithEachPlugin` function.

```
import { BrowserPool, PlaywrightPlugin, PuppeteerPlugin } from '@crawlee/browser-pool';
import playwright from 'playwright';
import puppeteer from 'puppeteer';

const browserPool = new BrowserPool({
    browserPlugins: [
        new PlaywrightPlugin(playwright.chromium),
        new PuppeteerPlugin(puppeteer),
    ],
});

const pages = await browserPool.newPageWithEachPlugin();
const promises = pages.map(async page => {
    // Run some task with each page
    // pages are in order of plugins:
    // [playwrightPage, puppeteerPage]
    await page.close();
});
await Promise.all(promises);

// Continue with some more work.
```

## Features[​](#features "Direct link to Features")

Besides a simple interface for launching browsers, Browser Pool includes other helpful features that make browser management more convenient.

### Simple configuration[​](#simple-configuration "Direct link to Simple configuration")

You can easily set the maximum number of pages that can be open in a given browser and also the maximum number of pages to process before a browser [is retired](#graceful-browser-closing).

```
const browserPool = new BrowserPool({
    maxOpenPagesPerBrowser: 20,
    retireBrowserAfterPageCount: 100,
});
```

You can configure the browser launch options either right in the plugins:

```
const playwrightPlugin = new PlaywrightPlugin(playwright.chromium, {
    launchOptions: {
        headless: true,
    }
})
```

Or dynamically in [pre-launch hooks](#lifecycle-management-with-hooks):

```
const browserPool = new BrowserPool({
    preLaunchHooks: [(pageId, launchContext) => {
        if (pageId === 'headful') {
            launchContext.launchOptions.headless = false;
        }
    }]
});
```

### Proxy management[​](#proxy-management "Direct link to Proxy management")

When scraping at scale or testing websites from multiple geolocations, one often needs to use proxy servers. Setting up an authenticated proxy in Puppeteer can be cumbersome, so we created a helper that does all the heavy lifting for you. Simply provide a proxy URL with authentication credentials, and you're done. It works the same for Playwright too.

```
const puppeteerPlugin = new PuppeteerPlugin(puppeteer, {
    proxyUrl: 'http://<username>:<password>@proxy.com:8000'
});
```

> We plan to extend this by adding a proxy-per-page functionality, allowing you to rotate proxies per page, rather than per browser.

### Lifecycle management with hooks[​](#lifecycle-management-with-hooks "Direct link to Lifecycle management with hooks")

Browser Pool allows you to manage the full browser / page lifecycle by attaching hooks to the most important events. Asynchronous hooks are supported, and their execution order is guaranteed.

The first parameter of each hook is either a `pageId` for the hooks executed before a `page` is created or a `page` afterward. This is useful to keep track of which hook was triggered by which `newPage()` call.

```
const browserPool = new BrowserPool({
    browserPlugins: [
        new PlaywrightPlugin(playwright.chromium),
    ],
    preLaunchHooks: [(pageId, launchContext) => {
        // You can use pre-launch hooks to make dynamic changes
        // to the launchContext, such as changing a proxyUrl
        // or updating the browser launchOptions

        pageId === 'my-page' // true
    }],
    postPageCreateHooks: [(page, browserController) => {
        // It makes sense to make global changes to pages
        // in post-page-create hooks. For example, you can
        // inject some JavaScript library, such as jQuery.

        browserPool.getPageId(page) === 'my-page' // true
    }]
});

await browserPool.newPage({ id: 'my-page' });
```

> See the API Documentation for all hooks and their arguments.

### Manipulating playwright context using `pageOptions` or `launchOptions`[​](#manipulating-playwright-context-using-pageoptions-or-launchoptions "Direct link to manipulating-playwright-context-using-pageoptions-or-launchoptions")

Playwright allows customizing multiple browser attributes by browser context. You can customize some of them once the context is created, but some need to be customized within its creation. This part of the documentation should explain how you can effectively customize the browser context.

First of all, let's take a look at what kind of context strategy you chose. You can choose between two strategies by `useIncognitoPages` `LaunchContext` option.

Suppose you decide to keep `useIncognitoPages` default `false` and create a shared context across all pages launched by one browser. In this case, you should pass the `contextOptions` as a `launchOptions` since the context is created within the new browser launch. The `launchOptions` corresponds to these [playwright options](https://playwright.dev/docs/api/class-browsertype#browsertypelaunchpersistentcontextuserdatadir-options). As you can see, these options contain not only ordinary playwright launch options but also the context options.

If you set `useIncognitoPages` to `true`, you will create a new context within each new page, which allows you to handle each page its cookies and application data. This approach allows you to pass the context options as `pageOptions` because a new context is created once you create a new page. In this case, the `pageOptions` corresponds to these [playwright options](https://playwright.dev/docs/api/class-browser#browsernewpageoptions).

**Changing context options with `LaunchContext`:**

This will only work if you keep the default value for `useIncognitoPages` (`false`).

```
const browserPool = new BrowserPool({
    browserPlugins: [
        new PlaywrightPlugin(
            playwright.chromium,
            {
                launchOptions: {
                    deviceScaleFactor: 2,
                },
            },
        ),
    ],
});
```

**Changing context options with `browserPool.newPage` options:**

```
const browserPool = new BrowserPool({
     browserPlugins: [
        new PlaywrightPlugin(
            playwright.chromium,
            {
                useIncognitoPages: true, // You must turn on incognito pages.
                launchOptions: {
                    // launch options
                    headless: false,
                    devtools: true,
                },
            },
        ),
    ],
});

// Launches Chromium with Playwright and returns a Playwright Page.
const page = await browserPool.newPage({
    pageOptions: {
        // context options
        deviceScaleFactor: 2,
        colorScheme: 'light',
        locale: 'de-DE',
    },
});
```

**Changing context options with `prePageCreateHooks` options:**

```
const browserPool = new BrowserPool({
    browserPlugins: [
        new PlaywrightPlugin(
            playwright.chromium,
            {
                useIncognitoPages: true,
                launchOptions: {
                // launch options
                    headless: false,
                    devtools: true,
                },
            },
        ),
    ],
    prePageCreateHooks: [
        (pageId, browserController, pageOptions) => {
            pageOptions.deviceScaleFactor = 2;
            pageOptions.colorScheme = 'dark';
            pageOptions.locale = 'de-DE';

            // You must modify the 'pageOptions' object, not assign to the variable.
            // pageOptions = {deviceScaleFactor: 2, ...etc} => This will not work!
        },
    ],
});

// Launches Chromium with Playwright and returns a Playwright Page.
const page = await browserPool.newPage();
```

### Single API for common operations[​](#single-api-for-common-operations "Direct link to Single API for common operations")

Puppeteer and Playwright handle some things differently. Browser Pool attempts to remove those differences for the most common use-cases.

```
// Playwright
const cookies = await context.cookies();
await context.addCookies(cookies);

// Puppeteer
const cookies = await page.cookies();
await page.setCookie(...cookies);

// BrowserPool uses the same API for all plugins
const cookies = await browserController.getCookies(page);
await browserController.setCookies(page, cookies);
```

### Graceful browser closing[​](#graceful-browser-closing "Direct link to Graceful browser closing")

With Browser Pool, browsers are not closed, but retired. A retired browser will no longer open new pages, but it will wait until the open pages are closed, allowing your running tasks to finish. If a browser gets stuck in limbo, it will be killed after a timeout to prevent hanging browser processes.

### Changing browser fingerprints a.k.a. browser signatures[​](#changing-browser-fingerprints-aka-browser-signatures "Direct link to Changing browser fingerprints a.k.a. browser signatures")

> Fingerprints are enabled by default since v3.

Changing browser fingerprints is beneficial for avoiding getting blocked and simulating real user browsers. With Browser Pool, you can do this otherwise complicated technique by enabling the `useFingerprints` option. The fingerprints are by default tied to the respective proxy urls to not use the same unique fingerprint from various IP addresses. You can disable this behavior in the [`fingerprintOptions`](https://crawlee.dev/js/api/browser-pool/interface/FingerprintOptions.md). In the `fingerprintOptions`, You can also control which fingerprints are generated. You can control parameters as browser, operating system, and browser versions.

The `browser-pool` module exports three constructors. One for `BrowserPool` itself and two for the included Puppeteer and Playwright plugins.

**Example:**

```
import {
 BrowserPool,
 PuppeteerPlugin,
 PlaywrightPlugin
} from '@crawlee/browser-pool';
import puppeteer from 'puppeteer';
import playwright from 'playwright';

const browserPool = new BrowserPool({
    browserPlugins: [
        new PuppeteerPlugin(puppeteer),
        new PlaywrightPlugin(playwright.chromium),
    ]
});
```

## Index[**](#Index)

### Enumerations

* [**BROWSER\_CONTROLLER\_EVENTS](https://crawlee.dev/js/api/browser-pool/enum/BROWSER_CONTROLLER_EVENTS.md)
* [**BROWSER\_POOL\_EVENTS](https://crawlee.dev/js/api/browser-pool/enum/BROWSER_POOL_EVENTS.md)
* [**BrowserName](https://crawlee.dev/js/api/browser-pool/enum/BrowserName.md)
* [**DeviceCategory](https://crawlee.dev/js/api/browser-pool/enum/DeviceCategory.md)
* [**OperatingSystemsName](https://crawlee.dev/js/api/browser-pool/enum/OperatingSystemsName.md)

### Classes

* [**BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)
* [**BrowserLaunchError](https://crawlee.dev/js/api/browser-pool/class/BrowserLaunchError.md)
* [**BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)
* [**BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md)
* [**LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)
* [**PlaywrightBrowser](https://crawlee.dev/js/api/browser-pool/class/PlaywrightBrowser.md)
* [**PlaywrightController](https://crawlee.dev/js/api/browser-pool/class/PlaywrightController.md)
* [**PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)
* [**PuppeteerController](https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md)
* [**PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md)

### Interfaces

* [**BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)
* [**BrowserPluginOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPluginOptions.md)
* [**BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)
* [**BrowserPoolHooks](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolHooks.md)
* [**BrowserPoolNewPageInNewBrowserOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageInNewBrowserOptions.md)
* [**BrowserPoolNewPageOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageOptions.md)
* [**BrowserPoolOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolOptions.md)
* [**BrowserSpecification](https://crawlee.dev/js/api/browser-pool/interface/BrowserSpecification.md)
* [**CommonLibrary](https://crawlee.dev/js/api/browser-pool/interface/CommonLibrary.md)
* [**CreateLaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/CreateLaunchContextOptions.md)
* [**FingerprintGenerator](https://crawlee.dev/js/api/browser-pool/interface/FingerprintGenerator.md)
* [**FingerprintGeneratorOptions](https://crawlee.dev/js/api/browser-pool/interface/FingerprintGeneratorOptions.md)
* [**FingerprintOptions](https://crawlee.dev/js/api/browser-pool/interface/FingerprintOptions.md)
* [**GetFingerprintReturn](https://crawlee.dev/js/api/browser-pool/interface/GetFingerprintReturn.md)
* [**LaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/LaunchContextOptions.md)

### Type Aliases

* [**InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)
* [**PostLaunchHook](https://crawlee.dev/js/api/browser-pool.md#PostLaunchHook)
* [**PostPageCloseHook](https://crawlee.dev/js/api/browser-pool.md#PostPageCloseHook)
* [**PostPageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PostPageCreateHook)
* [**PreLaunchHook](https://crawlee.dev/js/api/browser-pool.md#PreLaunchHook)
* [**PrePageCloseHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCloseHook)
* [**PrePageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCreateHook)
* [**UnwrapPromise](https://crawlee.dev/js/api/browser-pool.md#UnwrapPromise)

### Variables

* [**DEFAULT\_USER\_AGENT](https://crawlee.dev/js/api/browser-pool.md#DEFAULT_USER_AGENT)

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#InferBrowserPluginArray)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/utils.ts#L15)InferBrowserPluginArray

**InferBrowserPluginArray\<Input, Result>: Input extends readonly

<!-- -->

\[infer

<!-- -->

FirstValue, ...infer

<!-- -->

Rest] | \[infer

<!-- -->

FirstValue, ...infer

<!-- -->

Rest] ? FirstValue extends [PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md) ? [InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<Rest, \[...Result, [PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)]> : FirstValue extends [PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md) ? [InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<Rest, \[...Result, [PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md)]> : never : Input extends \[] ? Result : Input extends readonly

<!-- -->

infer

<!-- -->

U\[] ? \[U] extends \[[PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md) | [PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)] ? U\[] : never : Result

#### Type parameters

* **Input**: readonly
  <!-- -->
  unknown\[]
* **Result**: [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\[] = \[]

### [**](#PostLaunchHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L136)PostLaunchHook

**PostLaunchHook\<BC>: (pageId, browserController) => void | Promise\<void>

Post-launch hooks are executed as soon as a browser is launched. The hooks are called with two arguments: `pageId`: `string` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) To guarantee order of execution before other hooks in the same browser, the [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) methods cannot be used until the post-launch hooks complete. If you attempt to call `await browserController.close()` from a post-launch hook, it will deadlock the process. This API is subject to change.

***

#### Type parameters

* **BC**: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

#### Type declaration

* * **(pageId, browserController): void | Promise\<void>

  - #### Parameters

    * ##### pageId: string
    * ##### browserController: BC

    #### Returns void | Promise\<void>

### [**](#PostPageCloseHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L186)PostPageCloseHook

**PostPageCloseHook\<BC>: (pageId, browserController) => void | Promise\<void>

Post-page-close hooks allow you to do page related clean up. The hooks are called with two arguments: `pageId`: `string` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

***

#### Type parameters

* **BC**: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

#### Type declaration

* * **(pageId, browserController): void | Promise\<void>

  - #### Parameters

    * ##### pageId: string
    * ##### browserController: BC

    #### Returns void | Promise\<void>

### [**](#PostPageCreateHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L164)PostPageCreateHook

**PostPageCreateHook\<BC, Page>: (page, browserController) => void | Promise\<void>

Post-page-create hooks are called right after a new page is created and all internal actions of Browser Pool are completed. This is the place to make changes to a page that you would like to apply to all pages. Such as injecting a JavaScript library into all pages. The hooks are called with two arguments: `page`: `Page` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

***

#### Type parameters

* **BC**: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)
* **Page** = [UnwrapPromise](https://crawlee.dev/js/api/browser-pool.md#UnwrapPromise)\<ReturnType\<BC\[newPage]>>

#### Type declaration

* * **(page, browserController): void | Promise\<void>

  - #### Parameters

    * ##### page: Page
    * ##### browserController: BC

    #### Returns void | Promise\<void>

### [**](#PreLaunchHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L125)PreLaunchHook

**PreLaunchHook\<LC>: (pageId, launchContext) => void | Promise\<void>

Pre-launch hooks are executed just before a browser is launched and provide a good opportunity to dynamically change the launch options. The hooks are called with two arguments: `pageId`: `string` and `launchContext`: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)

***

#### Type parameters

* **LC**: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)

#### Type declaration

* * **(pageId, launchContext): void | Promise\<void>

  - #### Parameters

    * ##### pageId: string
    * ##### launchContext: LC

    #### Returns void | Promise\<void>

### [**](#PrePageCloseHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L176)PrePageCloseHook

**PrePageCloseHook\<BC, Page>: (page, browserController) => void | Promise\<void>

Pre-page-close hooks give you the opportunity to make last second changes in a page that's about to be closed, such as saving a snapshot or updating state. The hooks are called with two arguments: `page`: `Page` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

***

#### Type parameters

* **BC**: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)
* **Page** = [UnwrapPromise](https://crawlee.dev/js/api/browser-pool.md#UnwrapPromise)\<ReturnType\<BC\[newPage]>>

#### Type declaration

* * **(page, browserController): void | Promise\<void>

  - #### Parameters

    * ##### page: Page
    * ##### browserController: BC

    #### Returns void | Promise\<void>

### [**](#PrePageCreateHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L150)PrePageCreateHook

**PrePageCreateHook\<BC, PO>: (pageId, browserController, pageOptions) => void | Promise\<void>

Pre-page-create hooks are executed just before a new page is created. They are useful to make dynamic changes to the browser before opening a page. The hooks are called with three arguments: `pageId`: `string`, `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) and `pageOptions`: `object|undefined` - This only works if the underlying `BrowserController` supports new page options. So far, new page options are only supported by `PlaywrightController` in incognito contexts. If the page options are not supported by `BrowserController` the `pageOptions` argument is `undefined`.

***

#### Type parameters

* **BC**: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)
* **PO** = Parameters\<BC\[newPage]>\[0]

#### Type declaration

* * **(pageId, browserController, pageOptions): void | Promise\<void>

  - #### Parameters

    * ##### pageId: string
    * ##### browserController: BC
    * ##### optionalpageOptions: PO

    #### Returns void | Promise\<void>

### [**](#UnwrapPromise)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/utils.ts#L5)UnwrapPromise

**UnwrapPromise\<T>: T extends PromiseLike\<infer

<!-- -->

R> ? [UnwrapPromise](https://crawlee.dev/js/api/browser-pool.md#UnwrapPromise)\<R> : T

#### Type parameters

* **T**

## Variables<!-- -->[**](#Variables)

### [**](#DEFAULT_USER_AGENT)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L20)constDEFAULT\_USER\_AGENT

**DEFAULT\_USER\_AGENT: Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 =

<!-- -->

'Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'

The default User Agent used by `PlaywrightCrawler`, `launchPlaywright`, 'PuppeteerCrawler' and 'launchPuppeteer' when Chromium/Chrome browser is launched:

* in headless mode,
* without using a fingerprint,
* without specifying a user agent. Last updated on 2022-05-05.

After you update it here, please update it also in jsdom-crawler.ts
