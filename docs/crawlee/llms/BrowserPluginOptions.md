# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserPluginOptions.md

# BrowserPluginOptions<!-- --> \<LibraryOptions>

### Hierarchy

* *BrowserPluginOptions*
  * [BrowserLaunchContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md)

## Index[**](#Index)

### Properties

* [**browserPerProxy](#browserPerProxy)
* [**experimentalContainers](#experimentalContainers)
* [**launchOptions](#launchOptions)
* [**proxyUrl](#proxyUrl)
* [**useIncognitoPages](#useIncognitoPages)
* [**userDataDir](#userDataDir)

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L84)optionalbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

If set to `true`, the crawler respects the proxy url generated for the given request. This aligns the browser-based crawlers with the `HttpCrawler`.

Might cause performance issues, as Crawlee might launch too many browser instances.

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L73)optionalexperimentalContainersexperimental

**experimentalContainers?

<!-- -->

: boolean

Like `useIncognitoPages`, but for persistent contexts, so cache is used for faster loading. Works best with Firefox. Unstable on Chromium.

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L54)optionallaunchOptions

**launchOptions?

<!-- -->

: LibraryOptions

Options that will be passed down to the automation library. E.g. `puppeteer.launch(launchOptions);`. This is a good place to set options that you want to apply as defaults. To dynamically override those options per-browser, see the `preLaunchHooks` of [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md).

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L60)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Automation libraries configure proxies differently. This helper allows you to set a proxy URL without worrying about specific implementations. It also allows you use an authenticated proxy without extra code.

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L67)optionaluseIncognitoPages

**useIncognitoPages?

<!-- -->

: boolean = false

By default pages share the same browser context. If set to true each page uses its own context that is destroyed once the page is closed or crashes.

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L77)optionaluserDataDir

**userDataDir?

<!-- -->

: string

Path to a User Data Directory, which stores browser session data like cookies and local storage.
