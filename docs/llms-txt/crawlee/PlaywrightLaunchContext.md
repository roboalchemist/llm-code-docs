# Source: https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightLaunchContext.md

# PlaywrightLaunchContext<!-- -->

Apify extends the launch options of Playwright. You can use any of the Playwright compatible [`LaunchOptions`](https://playwright.dev/docs/api/class-browsertype#browsertypelaunchoptions) options by providing the `launchOptions` property.

**Example:**

```
// launch a headless Chrome (not Chromium)
const launchContext = {
    // Apify helpers
    useChrome: true,
    proxyUrl: 'http://user:password@some.proxy.com'
    // Native Playwright options
    launchOptions: {
        headless: true,
        args: ['--some-flag'],
    }
}
```

### Hierarchy

* [BrowserLaunchContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md)\<LaunchOptions, BrowserType>
  * *PlaywrightLaunchContext*

## Index[**](#Index)

### Properties

* [**browserPerProxy](#browserPerProxy)
* [**experimentalContainers](#experimentalContainers)
* [**launcher](#launcher)
* [**launchOptions](#launchOptions)
* [**proxyUrl](#proxyUrl)
* [**useChrome](#useChrome)
* [**useIncognitoPages](#useIncognitoPages)
* [**userAgent](#userAgent)
* [**userDataDir](#userDataDir)

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L40)optionalinheritedbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

Inherited from BrowserLaunchContext.browserPerProxy

If set to `true`, the crawler respects the proxy url generated for the given request. This aligns the browser-based crawlers with the `HttpCrawler`.

Might cause performance issues, as Crawlee might launch too many browser instances.

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L66)optionalexperimentalContainersexperimental

**experimentalContainers?

<!-- -->

: boolean

Overrides BrowserLaunchContext.experimentalContainers

Like `useIncognitoPages`, but for persistent contexts, so cache is used for faster loading. Works best with Firefox. Unstable on Chromium.

### [**](#launcher)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L79)optionallauncher

**launcher?

<!-- -->

: BrowserType<{}>

Overrides BrowserLaunchContext.launcher

By default this function uses `require("playwright").chromium`. If you want to use a different browser you can pass it by this property as e.g. `require("playwright").firefox`

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L33)optionallaunchOptions

**launchOptions?

<!-- -->

: LaunchOptions & { acceptDownloads?

<!-- -->

: boolean; args?

<!-- -->

: string\[]; baseURL?

<!-- -->

: string; bypassCSP?

<!-- -->

: boolean; channel?

<!-- -->

: string; chromiumSandbox?

<!-- -->

: boolean; clientCertificates?

<!-- -->

: { cert?

<!-- -->

: Buffer\<ArrayBufferLike>; certPath?

<!-- -->

: string; key?

<!-- -->

: Buffer\<ArrayBufferLike>; keyPath?

<!-- -->

: string; origin: string; passphrase?

<!-- -->

: string; pfx?

<!-- -->

: Buffer\<ArrayBufferLike>; pfxPath?

<!-- -->

: string }\[]; colorScheme?

<!-- -->

: null | light | dark | no-preference; contrast?

<!-- -->

: null | no-preference | more; deviceScaleFactor?

<!-- -->

: number; downloadsPath?

<!-- -->

: string; env?

<!-- -->

: {}; executablePath?

<!-- -->

: string; extraHTTPHeaders?

<!-- -->

: {}; firefoxUserPrefs?

<!-- -->

: {}; forcedColors?

<!-- -->

: null | active | none; geolocation?

<!-- -->

: { accuracy?

<!-- -->

: number; latitude: number; longitude: number }; handleSIGHUP?

<!-- -->

: boolean; handleSIGINT?

<!-- -->

: boolean; handleSIGTERM?

<!-- -->

: boolean; hasTouch?

<!-- -->

: boolean; headless?

<!-- -->

: boolean; httpCredentials?

<!-- -->

: { origin?

<!-- -->

: string; password: string; send?

<!-- -->

: unauthorized | always; username: string }; ignoreDefaultArgs?

<!-- -->

: boolean | string\[]; ignoreHTTPSErrors?

<!-- -->

: boolean; isMobile?

<!-- -->

: boolean; javaScriptEnabled?

<!-- -->

: boolean; locale?

<!-- -->

: string; logger?

<!-- -->

: Logger; offline?

<!-- -->

: boolean; permissions?

<!-- -->

: string\[]; proxy?

<!-- -->

: { bypass?

<!-- -->

: string; password?

<!-- -->

: string; server: string; username?

<!-- -->

: string }; recordHar?

<!-- -->

: { content?

<!-- -->

: omit | embed | attach; mode?

<!-- -->

: full | minimal; omitContent?

<!-- -->

: boolean; path: string; urlFilter?

<!-- -->

: string | RegExp }; recordVideo?

<!-- -->

: { dir: string; size?

<!-- -->

: { height: number; width: number } }; reducedMotion?

<!-- -->

: null | reduce | no-preference; screen?

<!-- -->

: { height: number; width: number }; serviceWorkers?

<!-- -->

: allow | block; slowMo?

<!-- -->

: number; strictSelectors?

<!-- -->

: boolean; timeout?

<!-- -->

: number; timezoneId?

<!-- -->

: string; tracesDir?

<!-- -->

: string; userAgent?

<!-- -->

: string; videoSize?

<!-- -->

: { height: number; width: number }; videosPath?

<!-- -->

: string; viewport?

<!-- -->

: null | { height: number; width: number } }

Overrides BrowserLaunchContext.launchOptions

`browserType.launch` [options](https://playwright.dev/docs/api/class-browsertype#browser-type-launch) or `browserType.launchContextOptions` [options](https://playwright.dev/docs/api/class-browsertype#browser-type-launch-persistent-context)

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L41)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Overrides BrowserLaunchContext.proxyUrl

URL to a HTTP proxy server. It must define the port number, and it may also contain proxy username and password.

Example: `http://bob:pass123@proxy.example.com:1234`.

### [**](#useChrome)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L52)optionaluseChrome

**useChrome?

<!-- -->

: boolean = false

Overrides BrowserLaunchContext.useChrome

If `true` and `executablePath` is not set, Playwright will launch full Google Chrome browser available on the machine rather than the bundled Chromium. The path to Chrome executable is taken from the `CRAWLEE_CHROME_EXECUTABLE_PATH` environment variable if provided, or defaults to the typical Google Chrome executable location specific for the operating system. By default, this option is `false`.

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L59)optionaluseIncognitoPages

**useIncognitoPages?

<!-- -->

: boolean = false

Overrides BrowserLaunchContext.useIncognitoPages

With this option selected, all pages will be opened in a new incognito browser context. This means they will not share cookies nor cache and their resources will not be throttled by one another.

### [**](#userAgent)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L68)optionalinheriteduserAgent

**userAgent?

<!-- -->

: string

Inherited from BrowserLaunchContext.userAgent

The `User-Agent` HTTP header used by the browser. If not provided, the function sets `User-Agent` to a reasonable default to reduce the chance of detection of the crawler.

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-launcher.ts#L73)optionaluserDataDir

**userDataDir?

<!-- -->

: string

Overrides BrowserLaunchContext.userDataDir

Sets the [User Data Directory](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md) path. The user data directory contains profile data such as history, bookmarks, and cookies, as well as other per-installation local state. If not specified, a temporary directory is used instead.
