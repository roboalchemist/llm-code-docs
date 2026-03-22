# Source: https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md

# PuppeteerPlugin<!-- -->

The `BrowserPlugin` serves two purposes. First, it is the base class that specialized controllers like `PuppeteerPlugin` or `PlaywrightPlugin` extend. Second, it allows the user to configure the automation libraries and feed them to [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) for use.

### Hierarchy

* [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<typeof Puppeteer, PuppeteerTypes.LaunchOptions, PuppeteerTypes.Browser, PuppeteerNewPageOptions>
  * *PuppeteerPlugin*

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

* ****new PuppeteerPlugin**(library, options): [PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md)

- Inherited from BrowserPlugin.constructor

  #### Parameters

  * ##### library: PuppeteerNode
  * ##### options: [BrowserPluginOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPluginOptions.md)\<LaunchOptions> = <!-- -->{}

  #### Returns [PuppeteerPlugin](https://crawlee.dev/js/api/browser-pool/class/PuppeteerPlugin.md)

## Properties<!-- -->[**](#Properties)

### [**](#browserPerProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L127)optionalinheritedbrowserPerProxy

**browserPerProxy?

<!-- -->

: boolean

Inherited from BrowserPlugin.browserPerProxy

### [**](#experimentalContainers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L125)inheritedexperimentalContainers

**experimentalContainers: boolean

Inherited from BrowserPlugin.experimentalContainers

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L117)inheritedlaunchOptions

**launchOptions: LaunchOptions

Inherited from BrowserPlugin.launchOptions

### [**](#library)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L115)inheritedlibrary

**library: PuppeteerNode

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

* ****createController**(): [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>

- Inherited from BrowserPlugin.createController

  #### Returns [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>

### [**](#createLaunchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L154)inheritedcreateLaunchContext

* ****createLaunchContext**(options): [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>

- Inherited from BrowserPlugin.createLaunchContext

  Creates a `LaunchContext` with all the information needed to launch a browser. Aside from library specific launch options, it also includes internal properties used by `BrowserPool` for management of the pool and extra features.

  ***

  #### Parameters

  * ##### options: [CreateLaunchContextOptions](https://crawlee.dev/js/api/browser-pool/interface/CreateLaunchContextOptions.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page> = <!-- -->{}

  #### Returns [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>

### [**](#launch)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-plugin.ts#L188)inheritedlaunch

* ****launch**(launchContext): Promise\<Browser>

- Inherited from BrowserPlugin.launch

  Launches the browser using provided launch context.

  ***

  #### Parameters

  * ##### launchContext: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page> = <!-- -->...

  #### Returns Promise\<Browser>
