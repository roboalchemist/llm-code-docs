# Source: https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md

# LaunchContext<!-- --> \<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**browserPerProxy](#browserPerProxy)
* [**browserPlugin](#browserPlugin)
* [**experimentalContainers](#experimentalContainers)
* [**fingerprint](#fingerprint)
* [**id](#id)
* [**launchOptions](#launchOptions)
* [**proxyTier](#proxyTier)
* [**useIncognitoPages](#useIncognitoPages)
* [**userDataDir](#userDataDir)

### Accessors

* [**proxyUrl](#proxyUrl)

### Methods

* [**extend](#extend)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L85)constructor

* ****new LaunchContext**\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>(options): [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

- #### Parameters

  * ##### options: [LaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/LaunchContextOptions.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

  #### Returns [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L74)optionalbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

### [**](#browserPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L71)browserPlugin

**browserPlugin: [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L75)experimentalContainers

**experimentalContainers: boolean

### [**](#fingerprint)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L82)optionalfingerprint

**fingerprint?

<!-- -->

: BrowserFingerprintWithHeaders

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L70)optionalid

**id?

<!-- -->

: string

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L72)launchOptions

**launchOptions: LibraryOptions

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L77)optionalproxyTier

**proxyTier?

<!-- -->

: number

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L73)useIncognitoPages

**useIncognitoPages: boolean

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L76)userDataDir

**userDataDir: string

## Accessors<!-- -->[**](#Accessors)

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L131)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L148)proxyUrl

* **get proxyUrl(): undefined | string
* **set proxyUrl(url): void

- Returns the proxy URL of the browser.

  ***

  #### Returns undefined | string

- Sets a proxy URL for the browser. Use `undefined` to unset existing proxy URL.

  ***

  #### Parameters

  * ##### url: undefined | string

  #### Returns void

## Methods<!-- -->[**](#Methods)

### [**](#extend)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/launch-context.ts#L117)extend

* ****extend**\<T>(fields): void

- Extend the launch context with any extra fields. This is useful to keep state information relevant to the browser being launched. It ensures that no internal fields are overridden and should be used instead of property assignment.

  ***

  #### Parameters

  * ##### fields: T

  #### Returns void
