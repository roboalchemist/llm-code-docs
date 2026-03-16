# Source: https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md

# PlaywrightPlugin<!-- -->

The `BrowserPlugin` serves two purposes. First, it is the base class that specialized controllers like `PuppeteerPlugin` or `PlaywrightPlugin` extend. Second, it allows the user to configure the automation libraries and feed them to [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) for use.

### Hierarchy

* [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<BrowserType, SafeParameters\<BrowserType\[launch]>\[0], PlaywrightBrowser>
  * *PlaywrightPlugin*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**\_containerProxyServer](#_containerProxyServer)
* [**browserPerProxy](#browserPerProxy)
* [**experimentalContainers](#experimentalContainers)
* [**launchOptions](#launchOptions)
* [**library](#library)
* [**name](#name)
* [**proxyUrl](#proxyUrl)
* [**useIncognitoPages](#useIncognitoPages)
* [**userDataDir](#userDataDir)

### Methods

* [**createController](#createController)
* [**createLaunchContext](#createLaunchContext)
* [**launch](#launch)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L129)constructor

* ****new PlaywrightPlugin**(library, options): [PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)

- Inherited from BrowserPlugin.constructor

  #### Parameters

  * ##### library: BrowserType<{}>
  * ##### options: [BrowserPluginOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPluginOptions.md)\<undefined | LaunchOptions> = <!-- -->{}

  #### Returns [PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)

## Properties<!-- -->[**](#Properties)

### [**](#_containerProxyServer)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/playwright/playwright-plugin.ts#L42)optional\_containerProxyServer

**\_containerProxyServer?

<!-- -->

: { ipToProxy: Map\<string, string>; port: number; close: any }

#### Type declaration

* ##### ipToProxy: Map\<string, string>

* ##### port: number

* ##### close: function

  * ****close**(closeConnections): Promise\<void>

  ***

  * #### Parameters

    * ##### closeConnections: boolean

    #### Returns Promise\<void>

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L127)optionalinheritedbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

Inherited from BrowserPlugin.browserPerProxy

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L125)inheritedexperimentalContainers

**experimentalContainers: boolean

Inherited from BrowserPlugin.experimentalContainers

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L117)inheritedlaunchOptions

**launchOptions: undefined | LaunchOptions

Inherited from BrowserPlugin.launchOptions

### [**](#library)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L115)inheritedlibrary

**library: BrowserType<{}>

Inherited from BrowserPlugin.library

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L113)inheritedname

**name: string =

<!-- -->

...

Inherited from BrowserPlugin.name

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L119)optionalinheritedproxyUrl

**proxyUrl?

<!-- -->

: string

Inherited from BrowserPlugin.proxyUrl

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L123)inheriteduseIncognitoPages

**useIncognitoPages: boolean

Inherited from BrowserPlugin.useIncognitoPages

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L121)optionalinheriteduserDataDir

**userDataDir?

<!-- -->

: string

Inherited from BrowserPlugin.userDataDir

## Methods<!-- -->[**](#Methods)

### [**](#createController)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L181)inheritedcreateController

* ****createController**(): [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?
  <!-- -->
  : boolean; baseURL?
  <!-- -->
  : string; bypassCSP?
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
  : number; extraHTTPHeaders?
  <!-- -->
  : {}; forcedColors?
  <!-- -->
  : null | active | none; geolocation?
  <!-- -->
  : { accuracy?
  <!-- -->
  : number; latitude: number; longitude: number }; hasTouch?
  <!-- -->
  : boolean; httpCredentials?
  <!-- -->
  : { origin?
  <!-- -->
  : string; password: string; send?
  <!-- -->
  : unauthorized | always; username: string }; ignoreHTTPSErrors?
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
  : allow | block; storageState?
  <!-- -->
  : string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?
  <!-- -->
  : boolean; timezoneId?
  <!-- -->
  : string; userAgent?
  <!-- -->
  : string; videoSize?
  <!-- -->
  : { height: number; width: number }; videosPath?
  <!-- -->
  : string; viewport?
  <!-- -->
  : null | { height: number; width: number } }, Page>

- Inherited from BrowserPlugin.createController

  #### Returns [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?<!-- -->: boolean; baseURL?<!-- -->: string; bypassCSP?<!-- -->: boolean; clientCertificates?<!-- -->: { cert?<!-- -->: Buffer\<ArrayBufferLike>; certPath?<!-- -->: string; key?<!-- -->: Buffer\<ArrayBufferLike>; keyPath?<!-- -->: string; origin: string; passphrase?<!-- -->: string; pfx?<!-- -->: Buffer\<ArrayBufferLike>; pfxPath?<!-- -->: string }\[]; colorScheme?<!-- -->: null | light | dark | no-preference; contrast?<!-- -->: null | no-preference | more; deviceScaleFactor?<!-- -->: number; extraHTTPHeaders?<!-- -->: {}; forcedColors?<!-- -->: null | active | none; geolocation?<!-- -->: { accuracy?<!-- -->: number; latitude: number; longitude: number }; hasTouch?<!-- -->: boolean; httpCredentials?<!-- -->: { origin?<!-- -->: string; password: string; send?<!-- -->: unauthorized | always; username: string }; ignoreHTTPSErrors?<!-- -->: boolean; isMobile?<!-- -->: boolean; javaScriptEnabled?<!-- -->: boolean; locale?<!-- -->: string; logger?<!-- -->: Logger; offline?<!-- -->: boolean; permissions?<!-- -->: string\[]; proxy?<!-- -->: { bypass?<!-- -->: string; password?<!-- -->: string; server: string; username?<!-- -->: string }; recordHar?<!-- -->: { content?<!-- -->: omit | embed | attach; mode?<!-- -->: full | minimal; omitContent?<!-- -->: boolean; path: string; urlFilter?<!-- -->: string | RegExp }; recordVideo?<!-- -->: { dir: string; size?<!-- -->: { height: number; width: number } }; reducedMotion?<!-- -->: null | reduce | no-preference; screen?<!-- -->: { height: number; width: number }; serviceWorkers?<!-- -->: allow | block; storageState?<!-- -->: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?<!-- -->: boolean; timezoneId?<!-- -->: string; userAgent?<!-- -->: string; videoSize?<!-- -->: { height: number; width: number }; videosPath?<!-- -->: string; viewport?<!-- -->: null | { height: number; width: number } }, Page>

### [**](#createLaunchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L154)inheritedcreateLaunchContext

* ****createLaunchContext**(options): [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?
  <!-- -->
  : boolean; baseURL?
  <!-- -->
  : string; bypassCSP?
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
  : number; extraHTTPHeaders?
  <!-- -->
  : {}; forcedColors?
  <!-- -->
  : null | active | none; geolocation?
  <!-- -->
  : { accuracy?
  <!-- -->
  : number; latitude: number; longitude: number }; hasTouch?
  <!-- -->
  : boolean; httpCredentials?
  <!-- -->
  : { origin?
  <!-- -->
  : string; password: string; send?
  <!-- -->
  : unauthorized | always; username: string }; ignoreHTTPSErrors?
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
  : allow | block; storageState?
  <!-- -->
  : string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?
  <!-- -->
  : boolean; timezoneId?
  <!-- -->
  : string; userAgent?
  <!-- -->
  : string; videoSize?
  <!-- -->
  : { height: number; width: number }; videosPath?
  <!-- -->
  : string; viewport?
  <!-- -->
  : null | { height: number; width: number } }, Page>

- Inherited from BrowserPlugin.createLaunchContext

  Creates a `LaunchContext` with all the information needed to launch a browser. Aside from library specific launch options, it also includes internal properties used by `BrowserPool` for management of the pool and extra features.

  ***

  #### Parameters

  * ##### options: [CreateLaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/CreateLaunchContextOptions.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?<!-- -->: boolean; baseURL?<!-- -->: string; bypassCSP?<!-- -->: boolean; clientCertificates?<!-- -->: { cert?<!-- -->: Buffer\<ArrayBufferLike>; certPath?<!-- -->: string; key?<!-- -->: Buffer\<ArrayBufferLike>; keyPath?<!-- -->: string; origin: string; passphrase?<!-- -->: string; pfx?<!-- -->: Buffer\<ArrayBufferLike>; pfxPath?<!-- -->: string }\[]; colorScheme?<!-- -->: null | light | dark | no-preference; contrast?<!-- -->: null | no-preference | more; deviceScaleFactor?<!-- -->: number; extraHTTPHeaders?<!-- -->: {}; forcedColors?<!-- -->: null | active | none; geolocation?<!-- -->: { accuracy?<!-- -->: number; latitude: number; longitude: number }; hasTouch?<!-- -->: boolean; httpCredentials?<!-- -->: { origin?<!-- -->: string; password: string; send?<!-- -->: unauthorized | always; username: string }; ignoreHTTPSErrors?<!-- -->: boolean; isMobile?<!-- -->: boolean; javaScriptEnabled?<!-- -->: boolean; locale?<!-- -->: string; logger?<!-- -->: Logger; offline?<!-- -->: boolean; permissions?<!-- -->: string\[]; proxy?<!-- -->: { bypass?<!-- -->: string; password?<!-- -->: string; server: string; username?<!-- -->: string }; recordHar?<!-- -->: { content?<!-- -->: omit | embed | attach; mode?<!-- -->: full | minimal; omitContent?<!-- -->: boolean; path: string; urlFilter?<!-- -->: string | RegExp }; recordVideo?<!-- -->: { dir: string; size?<!-- -->: { height: number; width: number } }; reducedMotion?<!-- -->: null | reduce | no-preference; screen?<!-- -->: { height: number; width: number }; serviceWorkers?<!-- -->: allow | block; storageState?<!-- -->: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?<!-- -->: boolean; timezoneId?<!-- -->: string; userAgent?<!-- -->: string; videoSize?<!-- -->: { height: number; width: number }; videosPath?<!-- -->: string; viewport?<!-- -->: null | { height: number; width: number } }, Page> = <!-- -->{}

  #### Returns [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?<!-- -->: boolean; baseURL?<!-- -->: string; bypassCSP?<!-- -->: boolean; clientCertificates?<!-- -->: { cert?<!-- -->: Buffer\<ArrayBufferLike>; certPath?<!-- -->: string; key?<!-- -->: Buffer\<ArrayBufferLike>; keyPath?<!-- -->: string; origin: string; passphrase?<!-- -->: string; pfx?<!-- -->: Buffer\<ArrayBufferLike>; pfxPath?<!-- -->: string }\[]; colorScheme?<!-- -->: null | light | dark | no-preference; contrast?<!-- -->: null | no-preference | more; deviceScaleFactor?<!-- -->: number; extraHTTPHeaders?<!-- -->: {}; forcedColors?<!-- -->: null | active | none; geolocation?<!-- -->: { accuracy?<!-- -->: number; latitude: number; longitude: number }; hasTouch?<!-- -->: boolean; httpCredentials?<!-- -->: { origin?<!-- -->: string; password: string; send?<!-- -->: unauthorized | always; username: string }; ignoreHTTPSErrors?<!-- -->: boolean; isMobile?<!-- -->: boolean; javaScriptEnabled?<!-- -->: boolean; locale?<!-- -->: string; logger?<!-- -->: Logger; offline?<!-- -->: boolean; permissions?<!-- -->: string\[]; proxy?<!-- -->: { bypass?<!-- -->: string; password?<!-- -->: string; server: string; username?<!-- -->: string }; recordHar?<!-- -->: { content?<!-- -->: omit | embed | attach; mode?<!-- -->: full | minimal; omitContent?<!-- -->: boolean; path: string; urlFilter?<!-- -->: string | RegExp }; recordVideo?<!-- -->: { dir: string; size?<!-- -->: { height: number; width: number } }; reducedMotion?<!-- -->: null | reduce | no-preference; screen?<!-- -->: { height: number; width: number }; serviceWorkers?<!-- -->: allow | block; storageState?<!-- -->: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?<!-- -->: boolean; timezoneId?<!-- -->: string; userAgent?<!-- -->: string; videoSize?<!-- -->: { height: number; width: number }; videosPath?<!-- -->: string; viewport?<!-- -->: null | { height: number; width: number } }, Page>

### [**](#launch)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L188)inheritedlaunch

* ****launch**(launchContext): Promise\<Browser>

- Inherited from BrowserPlugin.launch

  Launches the browser using provided launch context.

  ***

  #### Parameters

  * ##### launchContext: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?<!-- -->: boolean; baseURL?<!-- -->: string; bypassCSP?<!-- -->: boolean; clientCertificates?<!-- -->: { cert?<!-- -->: Buffer\<ArrayBufferLike>; certPath?<!-- -->: string; key?<!-- -->: Buffer\<ArrayBufferLike>; keyPath?<!-- -->: string; origin: string; passphrase?<!-- -->: string; pfx?<!-- -->: Buffer\<ArrayBufferLike>; pfxPath?<!-- -->: string }\[]; colorScheme?<!-- -->: null | light | dark | no-preference; contrast?<!-- -->: null | no-preference | more; deviceScaleFactor?<!-- -->: number; extraHTTPHeaders?<!-- -->: {}; forcedColors?<!-- -->: null | active | none; geolocation?<!-- -->: { accuracy?<!-- -->: number; latitude: number; longitude: number }; hasTouch?<!-- -->: boolean; httpCredentials?<!-- -->: { origin?<!-- -->: string; password: string; send?<!-- -->: unauthorized | always; username: string }; ignoreHTTPSErrors?<!-- -->: boolean; isMobile?<!-- -->: boolean; javaScriptEnabled?<!-- -->: boolean; locale?<!-- -->: string; logger?<!-- -->: Logger; offline?<!-- -->: boolean; permissions?<!-- -->: string\[]; proxy?<!-- -->: { bypass?<!-- -->: string; password?<!-- -->: string; server: string; username?<!-- -->: string }; recordHar?<!-- -->: { content?<!-- -->: omit | embed | attach; mode?<!-- -->: full | minimal; omitContent?<!-- -->: boolean; path: string; urlFilter?<!-- -->: string | RegExp }; recordVideo?<!-- -->: { dir: string; size?<!-- -->: { height: number; width: number } }; reducedMotion?<!-- -->: null | reduce | no-preference; screen?<!-- -->: { height: number; width: number }; serviceWorkers?<!-- -->: allow | block; storageState?<!-- -->: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?<!-- -->: boolean; timezoneId?<!-- -->: string; userAgent?<!-- -->: string; videoSize?<!-- -->: { height: number; width: number }; videosPath?<!-- -->: string; viewport?<!-- -->: null | { height: number; width: number } }, Page> = <!-- -->...

  #### Returns Promise\<Browser>
