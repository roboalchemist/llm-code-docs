# Source: https://crawlee.dev/js/api/browser-pool/class/BrowserController.md

# abstractBrowserController<!-- --> \<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

The `BrowserController` serves two purposes. First, it is the base class that specialized controllers like `PuppeteerController` or `PlaywrightController` extend. Second, it defines the public interface of the specialized classes which provide only private methods. Therefore, we do not keep documentation for the specialized classes, because it's the same for all of them.

### Hierarchy

* TypedEmitter<[BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>>

  * *BrowserController*

    * [PuppeteerController](https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md)
    * [PlaywrightController](https://crawlee.dev/js/api/browser-pool/class/PlaywrightController.md)

## Index[**](#Index)

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

## Properties<!-- -->[**](#Properties)

### [**](#activePages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L73)activePages

**activePages: number =

<!-- -->

0

### [**](#browser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L52)browser

**browser: LaunchResult =

<!-- -->

...

Browser representation of the underlying automation library.

### [**](#browserPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L47)browserPlugin

**browserPlugin: [BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>

The `BrowserPlugin` instance used to launch the browser.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L42)id

**id: string =

<!-- -->

...

### [**](#isActive)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L71)isActive

**isActive: boolean =

<!-- -->

false

### [**](#lastPageOpenedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L77)lastPageOpenedAt

**lastPageOpenedAt: number =

<!-- -->

...

### [**](#launchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L57)launchContext

**launchContext: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult> =

<!-- -->

...

The configuration the browser was launched with.

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L63)optionalproxyTier

**proxyTier?

<!-- -->

: number

The proxy tier tied to this browser controller. `undefined` if no tiered proxy is used.

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L69)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

The proxy URL used by the browser controller. This is set every time the browser controller uses proxy (even the tiered one). `undefined` if no proxy is used

### [**](#totalPages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L75)totalPages

**totalPages: number =

<!-- -->

0

### [**](#defaultMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L10)staticexternalinheriteddefaultMaxListeners

**defaultMaxListeners: number

Inherited from TypedEmitter.defaultMaxListeners

## Methods<!-- -->[**](#Methods)

### [**](#addListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L11)externalinheritedaddListener

* ****addListener**\<U>(event, listener): this

- Inherited from TypedEmitter.addListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#close)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L131)close

* ****close**(): Promise\<void>

- Gracefully closes the browser and makes sure there will be no lingering browser processes.

  Emits 'browserClosed' event.

  ***

  #### Returns Promise\<void>

### [**](#emit)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L19)externalinheritedemit

* ****emit**\<U>(event, ...args): boolean

- Inherited from TypedEmitter.emit

  #### Parameters

  * ##### externalevent: U
  * ##### externalrest...args: Parameters<[BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]>

  #### Returns boolean

### [**](#eventNames)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L20)externalinheritedeventNames

* ****eventNames**\<U>(): U\[]

- Inherited from TypedEmitter.eventNames

  #### Returns U\[]

### [**](#getCookies)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L181)getCookies

* ****getCookies**(page): Promise<[Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]>

- #### Parameters

  * ##### page: NewPageResult

  #### Returns Promise<[Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]>

### [**](#getMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L24)externalinheritedgetMaxListeners

* ****getMaxListeners**(): number

- Inherited from TypedEmitter.getMaxListeners

  #### Returns number

### [**](#kill)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L156)kill

* ****kill**(): Promise\<void>

- Immediately kills the browser process.

  Emits 'browserClosed' event.

  ***

  #### Returns Promise\<void>

### [**](#listenerCount)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L21)externalinheritedlistenerCount

* ****listenerCount**(type): number

- Inherited from TypedEmitter.listenerCount

  #### Parameters

  * ##### externaltype: BROWSER\_CLOSED

  #### Returns number

### [**](#listeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L22)externalinheritedlisteners

* ****listeners**\<U>(type): [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]\[]

- Inherited from TypedEmitter.listeners

  #### Parameters

  * ##### externaltype: U

  #### Returns [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]\[]

### [**](#off)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L18)externalinheritedoff

* ****off**\<U>(event, listener): this

- Inherited from TypedEmitter.off

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#on)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L17)externalinheritedon

* ****on**\<U>(event, listener): this

- Inherited from TypedEmitter.on

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#once)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L16)externalinheritedonce

* ****once**\<U>(event, listener): this

- Inherited from TypedEmitter.once

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#prependListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L12)externalinheritedprependListener

* ****prependListener**\<U>(event, listener): this

- Inherited from TypedEmitter.prependListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#prependOnceListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L13)externalinheritedprependOnceListener

* ****prependOnceListener**\<U>(event, listener): this

- Inherited from TypedEmitter.prependOnceListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#rawListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L23)externalinheritedrawListeners

* ****rawListeners**\<U>(type): [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]\[]

- Inherited from TypedEmitter.rawListeners

  #### Parameters

  * ##### externaltype: U

  #### Returns [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]\[]

### [**](#removeAllListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L15)externalinheritedremoveAllListeners

* ****removeAllListeners**(event): this

- Inherited from TypedEmitter.removeAllListeners

  #### Parameters

  * ##### externaloptionalevent: BROWSER\_CLOSED

  #### Returns this

### [**](#removeListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L14)externalinheritedremoveListener

* ****removeListener**\<U>(event, listener): this

- Inherited from TypedEmitter.removeListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserControllerEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserControllerEvents.md)\<Library, LibraryOptions, LaunchResult, NewPageOptions, NewPageResult>\[U]

  #### Returns this

### [**](#setCookies)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/abstract-classes/browser-controller.ts#L177)setCookies

* ****setCookies**(page, cookies): Promise\<void>

- #### Parameters

  * ##### page: NewPageResult
  * ##### cookies: [Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)\[]

  #### Returns Promise\<void>

### [**](#setMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L25)externalinheritedsetMaxListeners

* ****setMaxListeners**(n): this

- Inherited from TypedEmitter.setMaxListeners

  #### Parameters

  * ##### externaln: number

  #### Returns this
