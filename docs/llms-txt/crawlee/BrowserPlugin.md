# Source: https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md

# abstractBrowserPlugin<!-- --> \<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

The `BrowserPlugin` serves two purposes. First, it is the base class that specialized controllers like `PuppeteerPlugin` or `PlaywrightPlugin` extend. Second, it allows the user to configure the automation libraries and feed them to [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) for use.

### Hierarchy

* *BrowserPlugin*

  * [PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)
  * [PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

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

* ****new BrowserPlugin**\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>(library, options): [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

- #### Parameters

  * ##### library: Library
  * ##### options: [BrowserPluginOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPluginOptions.md)\<LibraryOptions> = <!-- -->{}

  #### Returns [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L127)optionalbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L125)experimentalContainers

**experimentalContainers: boolean

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L117)launchOptions

**launchOptions: LibraryOptions

### [**](#library)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L115)library

**library: Library

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L113)name

**name: string =

<!-- -->

...

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L119)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

### [**](#useIncognitoPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L123)useIncognitoPages

**useIncognitoPages: boolean

### [**](#userDataDir)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L121)optionaluserDataDir

**userDataDir?

<!-- -->

: string

## Methods<!-- -->[**](#Methods)

### [**](#createController)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L181)createController

* ****createController**(): [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

- #### Returns [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

### [**](#createLaunchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L154)createLaunchContext

* ****createLaunchContext**(options): [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

- Creates a `LaunchContext` with all the information needed to launch a browser. Aside from library specific launch options, it also includes internal properties used by `BrowserPool` for management of the pool and extra features.

  ***

  #### Parameters

  * ##### options: [CreateLaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/CreateLaunchContextOptions.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult> = <!-- -->{}

  #### Returns [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

### [**](#launch)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L188)launch

* ****launch**(launchContext): Promise\<LaunchResult>

- Launches the browser using provided launch context.

  ***

  #### Parameters

  * ##### launchContext: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult> = <!-- -->...

  #### Returns Promise\<LaunchResult>
