# Source: https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md

# BrowserLaunchContext<!-- --> \<TOptions, Launcher>

### Hierarchy

* [BrowserPluginOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPluginOptions.md)\<TOptions>

  * *BrowserLaunchContext*

    * [PuppeteerLaunchContext](https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerLaunchContext.md)
    * [PlaywrightLaunchContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightLaunchContext.md)
    * [StagehandLaunchContext](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandLaunchContext.md)

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

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L40)optionalbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

Overrides BrowserPluginOptions.browserPerProxy

If set to `true`, the crawler respects the proxy url generated for the given request. This aligns the browser-based crawlers with the `HttpCrawler`.

Might cause performance issues, as Crawlee might launch too many browser instances.

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L54)optionalexperimentalContainersexperimental

**experimentalContainers?

<!-- -->

: boolean

Overrides BrowserPluginOptions.experimentalContainers

Like `useIncognitoPages`, but for persistent contexts, so cache is used for faster loading. Works best with Firefox. Unstable on Chromium.

### [**](#launcher)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L82)optionallauncher

**launcher?

<!-- -->

: Launcher

The type of browser to be launched. By default, `chromium` is used. Other browsers like `webkit` or `firefox` can be used.

* **@example**

  ```
  // import the browser from the library first
  import { firefox } from 'playwright';
  ```

  For more details, check out the [example](https://crawlee.dev/js/docs/examples/playwright-crawler-firefox.md).

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L54)optionalinheritedlaunchOptions

**launchOptions?

<!-- -->

: TOptions

Inherited from BrowserPluginOptions.launchOptions

Options that will be passed down to the automation library. E.g. `puppeteer.launch(launchOptions);`. This is a good place to set options that you want to apply as defaults. To dynamically override those options per-browser, see the `preLaunchHooks` of [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md).

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L22)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Overrides BrowserPluginOptions.proxyUrl

URL to an HTTP proxy server. It must define the port number, and it may also contain proxy username and password.

* **@example**

  ```
  `http://bob:pass123@proxy.example.com:1234`.
  ```

### [**](#useChrome)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L32)optionaluseChrome

**useChrome?

<!-- -->

: boolean = false

If `true` and the `executablePath` option of [`launchOptions`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md#launchOptions) is not set, the launcher will launch full Google Chrome browser available on the machine rather than the bundled Chromium. The path to Chrome executable is taken from the `CRAWLEE_CHROME_EXECUTABLE_PATH` environment variable if provided, or defaults to the typical Google Chrome executable location specific for the operating system.

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L47)optionaluseIncognitoPages

**useIncognitoPages?

<!-- -->

: boolean = false

Overrides BrowserPluginOptions.useIncognitoPages

With this option selected, all pages will be opened in a new incognito browser context. This means they will not share cookies nor cache and their resources will not be throttled by one another.

### [**](#userAgent)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L68)optionaluserAgent

**userAgent?

<!-- -->

: string

The `User-Agent` HTTP header used by the browser. If not provided, the function sets `User-Agent` to a reasonable default to reduce the chance of detection of the crawler.

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L61)optionaluserDataDir

**userDataDir?

<!-- -->

: string

Overrides BrowserPluginOptions.userDataDir

Sets the [User Data Directory](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md) path. The user data directory contains profile data such as history, bookmarks, and cookies, as well as other per-installation local state. If not specified, a temporary directory is used instead.
