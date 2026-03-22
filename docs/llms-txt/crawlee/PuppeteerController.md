# Source: https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md

# PuppeteerController<!-- -->

The `BrowserController` serves two purposes. First, it is the base class that specialized controllers like `PuppeteerController` or `PlaywrightController` extend. Second, it defines the public interface of the specialized classes which provide only private methods. Therefore, we do not keep documentation for the specialized classes, because it's the same for all of them.

### Hierarchy

* [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<typeof Puppeteer, PuppeteerTypes.LaunchOptions, PuppeteerTypes.Browser, PuppeteerNewPageOptions>
  * *PuppeteerController*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**activePages](#activePages)
* [**browser](#browser)
* [**browserPlugin](#browserPlugin)
* [**id](#id)
* [**isActive](#isActive)
* [**lastPageOpenedAt](#lastPageOpenedAt)
* [**launchContext](#launchContext)
* [**proxyTier](#proxyTier)
* [**proxyUrl](#proxyUrl)
* [**totalPages](#totalPages)
* [**defaultMaxListeners](#defaultMaxListeners)

### Methods

* [**addListener](#addListener)
* [**close](#close)
* [**emit](#emit)
* [**eventNames](#eventNames)
* [**getCookies](#getCookies)
* [**getMaxListeners](#getMaxListeners)
* [**kill](#kill)
* [**listenerCount](#listenerCount)
* [**listeners](#listeners)
* [**off](#off)
* [**on](#on)
* [**once](#once)
* [**prependListener](#prependListener)
* [**prependOnceListener](#prependOnceListener)
* [**rawListeners](#rawListeners)
* [**removeAllListeners](#removeAllListeners)
* [**removeListener](#removeListener)
* [**setCookies](#setCookies)
* [**setMaxListeners](#setMaxListeners)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L91)constructor

* ****new PuppeteerController**(browserPlugin): [PuppeteerController](https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md)

- Inherited from BrowserController< typeof Puppeteer, PuppeteerTypes.LaunchOptions, PuppeteerTypes.Browser, PuppeteerNewPageOptions >.constructor

  #### Parameters

  * ##### browserPlugin: [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>

  #### Returns [PuppeteerController](https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md)

## Properties<!-- -->[**](#Properties)

### [**](#activePages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L73)inheritedactivePages

**activePages: number =

<!-- -->

0

Inherited from BrowserController.activePages

### [**](#browser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L52)inheritedbrowser

**browser: Browser =

<!-- -->

...

Inherited from BrowserController.browser

Browser representation of the underlying automation library.

### [**](#browserPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L47)inheritedbrowserPlugin

**browserPlugin: [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>

Inherited from BrowserController.browserPlugin

The `BrowserPlugin` instance used to launch the browser.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L42)inheritedid

**id: string =

<!-- -->

...

Inherited from BrowserController.id

### [**](#isActive)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L71)inheritedisActive

**isActive: boolean =

<!-- -->

false

Inherited from BrowserController.isActive

### [**](#lastPageOpenedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L77)inheritedlastPageOpenedAt

**lastPageOpenedAt: number =

<!-- -->

...

Inherited from BrowserController.lastPageOpenedAt

### [**](#launchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L57)inheritedlaunchContext

**launchContext: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page> =

<!-- -->

...

Inherited from BrowserController.launchContext

The configuration the browser was launched with.

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L63)optionalinheritedproxyTier

**proxyTier?

<!-- -->

: number

Inherited from BrowserController.proxyTier

The proxy tier tied to this browser controller. `undefined` if no tiered proxy is used.

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L69)optionalinheritedproxyUrl

**proxyUrl?

<!-- -->

: string

Inherited from BrowserController.proxyUrl

The proxy URL used by the browser controller. This is set every time the browser controller uses proxy (even the tiered one). `undefined` if no proxy is used

### [**](#totalPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L75)inheritedtotalPages

**totalPages: number =

<!-- -->

0

Inherited from BrowserController.totalPages

### [**](#defaultMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L10)staticexternalinheriteddefaultMaxListeners

**defaultMaxListeners: number

Inherited from BrowserController.defaultMaxListeners

## Methods<!-- -->[**](#Methods)

### [**](#addListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L11)externalinheritedaddListener

* ****addListener**\<U>(event, listener): this

- Inherited from BrowserController.addListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#close)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L131)inheritedclose

* ****close**(): Promise\<void>

- Inherited from BrowserController.close

  Gracefully closes the browser and makes sure there will be no lingering browser processes.

  Emits 'browserClosed' event.

  ***

  #### Returns Promise\<void>

### [**](#emit)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L19)externalinheritedemit

* ****emit**\<U>(event, ...args): boolean

- Inherited from BrowserController.emit

  #### Parameters

  * ##### externalevent: U
  * ##### externalrest...args: Parameters<[BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]>

  #### Returns boolean

### [**](#eventNames)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L20)externalinheritedeventNames

* ****eventNames**\<U>(): U\[]

- Inherited from BrowserController.eventNames

  #### Returns U\[]

### [**](#getCookies)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L181)inheritedgetCookies

* ****getCookies**(page): Promise<[Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]>

- Inherited from BrowserController.getCookies

  #### Parameters

  * ##### page: Page

  #### Returns Promise<[Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]>

### [**](#getMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L24)externalinheritedgetMaxListeners

* ****getMaxListeners**(): number

- Inherited from BrowserController.getMaxListeners

  #### Returns number

### [**](#kill)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L156)inheritedkill

* ****kill**(): Promise\<void>

- Inherited from BrowserController.kill

  Immediately kills the browser process.

  Emits 'browserClosed' event.

  ***

  #### Returns Promise\<void>

### [**](#listenerCount)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L21)externalinheritedlistenerCount

* ****listenerCount**(type): number

- Inherited from BrowserController.listenerCount

  #### Parameters

  * ##### externaltype: BROWSER\_CLOSED

  #### Returns number

### [**](#listeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L22)externalinheritedlisteners

* ****listeners**\<U>(type): [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]\[]

- Inherited from BrowserController.listeners

  #### Parameters

  * ##### externaltype: U

  #### Returns [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]\[]

### [**](#off)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L18)externalinheritedoff

* ****off**\<U>(event, listener): this

- Inherited from BrowserController.off

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#on)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L17)externalinheritedon

* ****on**\<U>(event, listener): this

- Inherited from BrowserController.on

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#once)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L16)externalinheritedonce

* ****once**\<U>(event, listener): this

- Inherited from BrowserController.once

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#prependListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L12)externalinheritedprependListener

* ****prependListener**\<U>(event, listener): this

- Inherited from BrowserController.prependListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#prependOnceListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L13)externalinheritedprependOnceListener

* ****prependOnceListener**\<U>(event, listener): this

- Inherited from BrowserController.prependOnceListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#rawListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L23)externalinheritedrawListeners

* ****rawListeners**\<U>(type): [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]\[]

- Inherited from BrowserController.rawListeners

  #### Parameters

  * ##### externaltype: U

  #### Returns [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]\[]

### [**](#removeAllListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L15)externalinheritedremoveAllListeners

* ****removeAllListeners**(event): this

- Inherited from BrowserController.removeAllListeners

  #### Parameters

  * ##### externaloptionalevent: BROWSER\_CLOSED

  #### Returns this

### [**](#removeListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L14)externalinheritedremoveListener

* ****removeListener**\<U>(event, listener): this

- Inherited from BrowserController.removeListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<PuppeteerNode, LaunchOptions, Browser, PuppeteerNewPageOptions, Page>\[U]

  #### Returns this

### [**](#setCookies)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L177)inheritedsetCookies

* ****setCookies**(page, cookies): Promise\<void>

- Inherited from BrowserController.setCookies

  #### Parameters

  * ##### page: Page
  * ##### cookies: [Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]

  #### Returns Promise\<void>

### [**](#setMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L25)externalinheritedsetMaxListeners

* ****setMaxListeners**(n): this

- Inherited from BrowserController.setMaxListeners

  #### Parameters

  * ##### externaln: number

  #### Returns this
