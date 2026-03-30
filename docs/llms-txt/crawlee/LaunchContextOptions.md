# Source: https://crawlee.dev/js/api/browser-pool/interface/LaunchContextOptions.md

# LaunchContextOptions<!-- --> \<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

`LaunchContext` holds information about the launched browser. It's useful to retrieve the `launchOptions`, the proxy the browser was launched with or any other information user chose to add to the `LaunchContext` by calling its `extend` function. This is very useful to keep track of browser-scoped values, such as session IDs.

## Index[**](#Index)

### Properties

* [**browserPerProxy](#browserPerProxy)
* [**browserPlugin](#browserPlugin)
* [**experimentalContainers](#experimentalContainers)
* [**id](#id)
* [**launchOptions](#launchOptions)
* [**proxyTier](#proxyTier)
* [**proxyUrl](#proxyUrl)
* [**useIncognitoPages](#useIncognitoPages)
* [**userDataDir](#userDataDir)

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L43)optionalbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

If set to `true`, the crawler respects the proxy url generated for the given request. This aligns the browser-based crawlers with the `HttpCrawler`.

Might cause performance issues, as Crawlee might launch too many browser instances.

### [**](#browserPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L31)browserPlugin

**browserPlugin: [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

The `BrowserPlugin` instance used to launch the browser.

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L54)optionalexperimentalContainersexperimental

**experimentalContainers?

<!-- -->

: boolean

Like `useIncognitoPages`, but for persistent contexts, so cache is used for faster loading. Works best with Firefox. Unstable on Chromium.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L27)optionalid

**id?

<!-- -->

: string

To make identification of `LaunchContext` easier, `BrowserPool` assigns the `LaunchContext` an `id` that's equal to the `id` of the page that triggered the browser launch. This is useful, because many pages share a single launch context (single browser).

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L36)launchOptions

**launchOptions: LibraryOptions

The actual options the browser was launched with, after changes. Those changes would be typically made in pre-launch hooks.

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L60)optionalproxyTier

**proxyTier?

<!-- -->

: number

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L59)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L48)optionaluseIncognitoPages

**useIncognitoPages?

<!-- -->

: boolean

By default pages share the same browser context. If set to `true` each page uses its own context that is destroyed once the page is closed or crashes.

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L58)optionaluserDataDir

**userDataDir?

<!-- -->

: string

Path to a User Data Directory, which stores browser session data like cookies and local storage.
