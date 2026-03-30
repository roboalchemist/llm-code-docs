# Source: https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerLaunchContext.md

# PuppeteerLaunchContext<!-- -->

Apify extends the launch options of Puppeteer. You can use any of the Puppeteer compatible [`LaunchOptions`](https://pptr.dev/api/puppeteer.launchoptions) options by providing the `launchOptions` property.

**Example:**

```
// launch a headless Chrome (not Chromium)
const launchContext = {
    // Apify helpers
    useChrome: true,
    proxyUrl: 'http://user:password@some.proxy.com'
    // Native Puppeteer options
    launchOptions: {
        headless: true,
        args: ['--some-flag'],
    }
}
```

### Hierarchy

* [BrowserLaunchContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md)<[PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md)\[launchOptions], unknown>
  * *PuppeteerLaunchContext*

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

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L54)optionalinheritedexperimentalContainersexperimental

**experimentalContainers?

<!-- -->

: boolean

Inherited from BrowserLaunchContext.experimentalContainers

Like `useIncognitoPages`, but for persistent contexts, so cache is used for faster loading. Works best with Firefox. Unstable on Chromium.

### [**](#launcher)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/puppeteer-launcher.ts#L60)optionallauncher

**launcher?

<!-- -->

: unknown

Overrides BrowserLaunchContext.launcher

Already required module (`Object`). This enables usage of various Puppeteer wrappers such as `puppeteer-extra`.

Take caution, because it can cause all kinds of unexpected errors and weird behavior. Crawlee is not tested with any other library besides `puppeteer` itself.

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/puppeteer-launcher.ts#L32)optionallaunchOptions

**launchOptions?

<!-- -->

: LaunchOptions

Overrides BrowserLaunchContext.launchOptions

`puppeteer.launch` [options](https://pptr.dev/api/puppeteer.launchoptions)

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/puppeteer-launcher.ts#L40)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Overrides BrowserLaunchContext.proxyUrl

URL to a HTTP proxy server. It must define the port number, and it may also contain proxy username and password.

Example: `http://bob:pass123@proxy.example.com:1234`.

### [**](#useChrome)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/puppeteer-launcher.ts#L51)optionaluseChrome

**useChrome?

<!-- -->

: boolean = false

Overrides BrowserLaunchContext.useChrome

If `true` and `executablePath` is not set, Puppeteer will launch full Google Chrome browser available on the machine rather than the bundled Chromium. The path to Chrome executable is taken from the `CRAWLEE_CHROME_EXECUTABLE_PATH` environment variable if provided, or defaults to the typical Google Chrome executable location specific for the operating system. By default, this option is `false`.

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/puppeteer-launcher.ts#L67)optionaluseIncognitoPages

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

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L61)optionalinheriteduserDataDir

**userDataDir?

<!-- -->

: string

Inherited from BrowserLaunchContext.userDataDir

Sets the [User Data Directory](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md) path. The user data directory contains profile data such as history, bookmarks, and cookies, as well as other per-installation local state. If not specified, a temporary directory is used instead.
