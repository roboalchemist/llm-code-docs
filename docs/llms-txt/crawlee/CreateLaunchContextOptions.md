# Source: https://crawlee.dev/js/api/browser-pool/interface/CreateLaunchContextOptions.md

# CreateLaunchContextOptions<!-- --> \<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

### Hierarchy

* Partial\<Omit<[LaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/LaunchContextOptions.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>, browserPlugin>>
  * *CreateLaunchContextOptions*

## Index[**](#Index)

### Properties

* [**browserPerProxy](#browserPerProxy)
* [**experimentalContainers](#experimentalContainers)
* [**id](#id)
* [**launchOptions](#launchOptions)
* [**proxyTier](#proxyTier)
* [**proxyUrl](#proxyUrl)
* [**useIncognitoPages](#useIncognitoPages)
* [**userDataDir](#userDataDir)

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L43)optionalinheritedbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

Inherited from Partial.browserPerProxy

If set to `true`, the crawler respects the proxy url generated for the given request. This aligns the browser-based crawlers with the `HttpCrawler`.

Might cause performance issues, as Crawlee might launch too many browser instances.

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L54)optionalinheritedexperimentalContainersexperimental

**experimentalContainers?

<!-- -->

: boolean

Inherited from Partial.experimentalContainers

Like `useIncognitoPages`, but for persistent contexts, so cache is used for faster loading. Works best with Firefox. Unstable on Chromium.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L27)optionalinheritedid

**id?

<!-- -->

: string

Inherited from Partial.id

To make identification of `LaunchContext` easier, `BrowserPool` assigns the `LaunchContext` an `id` that's equal to the `id` of the page that triggered the browser launch. This is useful, because many pages share a single launch context (single browser).

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L36)optionalinheritedlaunchOptions

**launchOptions?

<!-- -->

: LibraryOptions

Inherited from Partial.launchOptions

The actual options the browser was launched with, after changes. Those changes would be typically made in pre-launch hooks.

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L60)optionalinheritedproxyTier

**proxyTier?

<!-- -->

: number

Inherited from Partial.proxyTier

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L59)optionalinheritedproxyUrl

**proxyUrl?

<!-- -->

: string

Inherited from Partial.proxyUrl

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L48)optionalinheriteduseIncognitoPages

**useIncognitoPages?

<!-- -->

: boolean

Inherited from Partial.useIncognitoPages

By default pages share the same browser context. If set to `true` each page uses its own context that is destroyed once the page is closed or crashes.

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L58)optionalinheriteduserDataDir

**userDataDir?

<!-- -->

: string

Inherited from Partial.userDataDir

Path to a User Data Directory, which stores browser session data like cookies and local storage.
