# Source: https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md

# BrowserPool<!-- --> \<Options, BrowserPlugins, BrowserControllerReturn, LaunchContextReturn, PageOptions, PageReturn>

The `BrowserPool` class is the most important class of the `browser-pool` module. It manages opening and closing of browsers and their pages and its constructor options allow easy configuration of the browsers' and pages' lifecycle.

The most important and useful constructor options are the various lifecycle hooks. Those allow you to sequentially call a list of (asynchronous) functions at each stage of the browser / page lifecycle.

**Example:**

```
import { BrowserPool, PlaywrightPlugin } from '@crawlee/browser-pool';
import playwright from 'playwright';

const browserPool = new BrowserPool({
    browserPlugins: [new PlaywrightPlugin(playwright.chromium)],
    preLaunchHooks: [(pageId, launchContext) => {
        // do something before a browser gets launched
        launchContext.launchOptions.headless = false;
    }],
    postLaunchHooks: [(pageId, browserController) => {
        // manipulate the browser right after launch
        console.dir(browserController.browser.contexts());
    }],
    prePageCreateHooks: [(pageId, browserController) => {
        if (pageId === 'my-page') {
            // make changes right before a specific page is created
        }
    }],
    postPageCreateHooks: [async (page, browserController) => {
        // update some or all new pages
        await page.evaluate(() => {
            // now all pages will have 'foo'
            window.foo = 'bar'
        })
    }],
    prePageCloseHooks: [async (page, browserController) => {
        // collect information just before a page closes
        await page.screenshot();
    }],
    postPageCloseHooks: [(pageId, browserController) => {
        // clean up or log after a job is done
        console.log('Page closed: ', pageId)
    }]
});
```

### Hierarchy

* TypedEmitter<[BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>>
  * *BrowserPool*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**activeBrowserControllers](#activeBrowserControllers)
* [**browserPlugins](#browserPlugins)
* [**closeInactiveBrowserAfterMillis](#closeInactiveBrowserAfterMillis)
* [**fingerprintCache](#fingerprintCache)
* [**fingerprintGenerator](#fingerprintGenerator)
* [**fingerprintInjector](#fingerprintInjector)
* [**fingerprintOptions](#fingerprintOptions)
* [**maxOpenPagesPerBrowser](#maxOpenPagesPerBrowser)
* [**operationTimeoutMillis](#operationTimeoutMillis)
* [**pageCounter](#pageCounter)
* [**pageIds](#pageIds)
* [**pages](#pages)
* [**pageToBrowserController](#pageToBrowserController)
* [**postLaunchHooks](#postLaunchHooks)
* [**postPageCloseHooks](#postPageCloseHooks)
* [**postPageCreateHooks](#postPageCreateHooks)
* [**preLaunchHooks](#preLaunchHooks)
* [**prePageCloseHooks](#prePageCloseHooks)
* [**prePageCreateHooks](#prePageCreateHooks)
* [**retireBrowserAfterPageCount](#retireBrowserAfterPageCount)
* [**retiredBrowserControllers](#retiredBrowserControllers)
* [**startingBrowserControllers](#startingBrowserControllers)
* [**useFingerprints](#useFingerprints)
* [**defaultMaxListeners](#defaultMaxListeners)

### Methods

* [**addListener](#addListener)
* [**closeAllBrowsers](#closeAllBrowsers)
* [**destroy](#destroy)
* [**emit](#emit)
* [**eventNames](#eventNames)
* [**getBrowserControllerByPage](#getBrowserControllerByPage)
* [**getMaxListeners](#getMaxListeners)
* [**getPage](#getPage)
* [**getPageId](#getPageId)
* [**listenerCount](#listenerCount)
* [**listeners](#listeners)
* [**newPage](#newPage)
* [**newPageInNewBrowser](#newPageInNewBrowser)
* [**newPageWithEachPlugin](#newPageWithEachPlugin)
* [**off](#off)
* [**on](#on)
* [**once](#once)
* [**prependListener](#prependListener)
* [**prependOnceListener](#prependOnceListener)
* [**rawListeners](#rawListeners)
* [**removeAllListeners](#removeAllListeners)
* [**removeListener](#removeListener)
* [**retireAllBrowsers](#retireAllBrowsers)
* [**retireBrowserByPage](#retireBrowserByPage)
* [**retireBrowserController](#retireBrowserController)
* [**setMaxListeners](#setMaxListeners)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L338)constructor

* ****new BrowserPool**\<Options, BrowserPlugins, BrowserControllerReturn, LaunchContextReturn, PageOptions, PageReturn>(options): [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md)\<Options, BrowserPlugins, BrowserControllerReturn, LaunchContextReturn, PageOptions, PageReturn>

- Overrides TypedEmitter\<BrowserPoolEvents\<BrowserControllerReturn, PageReturn>>.constructor

  #### Parameters

  * ##### options: Options & [BrowserPoolHooks](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolHooks.md)\<BrowserControllerReturn, LaunchContextReturn, PageReturn>

  #### Returns [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md)\<Options, BrowserPlugins, BrowserControllerReturn, LaunchContextReturn, PageOptions, PageReturn>

## Properties<!-- -->[**](#Properties)

### [**](#activeBrowserControllers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L322)activeBrowserControllers

**activeBrowserControllers: Set\<BrowserControllerReturn> =

<!-- -->

...

### [**](#browserPlugins)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L305)browserPlugins

**browserPlugins: BrowserPlugins

### [**](#closeInactiveBrowserAfterMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L309)closeInactiveBrowserAfterMillis

**closeInactiveBrowserAfterMillis: number

### [**](#fingerprintCache)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L327)optionalfingerprintCache

**fingerprintCache?

<!-- -->

: QuickLRU\<string, BrowserFingerprintWithHeaders>

### [**](#fingerprintGenerator)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L326)optionalfingerprintGenerator

**fingerprintGenerator?

<!-- -->

: FingerprintGenerator

### [**](#fingerprintInjector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L325)optionalfingerprintInjector

**fingerprintInjector?

<!-- -->

: FingerprintInjector

### [**](#fingerprintOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L311)fingerprintOptions

**fingerprintOptions: [FingerprintOptions](https://crawlee.dev/js/api/browser-pool/interface/FingerprintOptions.md)

### [**](#maxOpenPagesPerBrowser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L306)maxOpenPagesPerBrowser

**maxOpenPagesPerBrowser: number

### [**](#operationTimeoutMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L308)operationTimeoutMillis

**operationTimeoutMillis: number

### [**](#pageCounter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L318)pageCounter

**pageCounter: number =

<!-- -->

0

### [**](#pageIds)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L320)pageIds

**pageIds: WeakMap\<PageReturn, string> =

<!-- -->

...

### [**](#pages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L319)pages

**pages: Map\<string, PageReturn> =

<!-- -->

...

### [**](#pageToBrowserController)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L324)pageToBrowserController

**pageToBrowserController: WeakMap\<PageReturn, BrowserControllerReturn> =

<!-- -->

...

### [**](#postLaunchHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L313)postLaunchHooks

**postLaunchHooks: [PostLaunchHook](https://crawlee.dev/js/api/browser-pool.md#PostLaunchHook)\<BrowserControllerReturn>\[]

### [**](#postPageCloseHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L317)postPageCloseHooks

**postPageCloseHooks: [PostPageCloseHook](https://crawlee.dev/js/api/browser-pool.md#PostPageCloseHook)\<BrowserControllerReturn>\[]

### [**](#postPageCreateHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L315)postPageCreateHooks

**postPageCreateHooks: [PostPageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PostPageCreateHook)\<BrowserControllerReturn, PageReturn>\[]

### [**](#preLaunchHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L312)preLaunchHooks

**preLaunchHooks: [PreLaunchHook](https://crawlee.dev/js/api/browser-pool.md#PreLaunchHook)\<LaunchContextReturn>\[]

### [**](#prePageCloseHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L316)prePageCloseHooks

**prePageCloseHooks: [PrePageCloseHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCloseHook)\<BrowserControllerReturn, PageReturn>\[]

### [**](#prePageCreateHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L314)prePageCreateHooks

**prePageCreateHooks: [PrePageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCreateHook)\<BrowserControllerReturn, PageOptions>\[]

### [**](#retireBrowserAfterPageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L307)retireBrowserAfterPageCount

**retireBrowserAfterPageCount: number

### [**](#retiredBrowserControllers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L323)retiredBrowserControllers

**retiredBrowserControllers: Set\<BrowserControllerReturn> =

<!-- -->

...

### [**](#startingBrowserControllers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L321)startingBrowserControllers

**startingBrowserControllers: Set\<BrowserControllerReturn> =

<!-- -->

...

### [**](#useFingerprints)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L310)optionaluseFingerprints

**useFingerprints?

<!-- -->

: boolean

### [**](#defaultMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L10)staticexternalinheriteddefaultMaxListeners

**defaultMaxListeners: number

Inherited from TypedEmitter.defaultMaxListeners

## Methods<!-- -->[**](#Methods)

### [**](#addListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L11)externalinheritedaddListener

* ****addListener**\<U>(event, listener): this

- Inherited from TypedEmitter.addListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#closeAllBrowsers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L649)closeAllBrowsers

* ****closeAllBrowsers**(): Promise\<void>

- Closes all managed browsers without waiting for pages to close.

  ***

  #### Returns Promise\<void>

### [**](#destroy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L661)destroy

* ****destroy**(): Promise\<void>

- Closes all managed browsers and tears down the pool.

  ***

  #### Returns Promise\<void>

### [**](#emit)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L19)externalinheritedemit

* ****emit**\<U>(event, ...args): boolean

- Inherited from TypedEmitter.emit

  #### Parameters

  * ##### externalevent: U
  * ##### externalrest...args: Parameters<[BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]>

  #### Returns boolean

### [**](#eventNames)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L20)externalinheritedeventNames

* ****eventNames**\<U>(): U\[]

- Inherited from TypedEmitter.eventNames

  #### Returns U\[]

### [**](#getBrowserControllerByPage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L525)getBrowserControllerByPage

* ****getBrowserControllerByPage**(page): undefined | BrowserControllerReturn

- Retrieves a [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) for a given page. This is useful when you're working only with pages and need to access the browser manipulation functionality.

  You could access the browser directly from the page, but that would circumvent `BrowserPool` and most likely cause weird things to happen, so please always use `BrowserController` to control your browsers. The function returns `undefined` if the browser is closed.

  ***

  #### Parameters

  * ##### page: PageReturn

    Browser plugin page

  #### Returns undefined | BrowserControllerReturn

### [**](#getMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L24)externalinheritedgetMaxListeners

* ****getMaxListeners**(): number

- Inherited from TypedEmitter.getMaxListeners

  #### Returns number

### [**](#getPage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L535)getPage

* ****getPage**(id): undefined | PageReturn

- If you provided a custom ID to one of your pages or saved the randomly generated one, you can use this function to retrieve the page. If the page is no longer open, the function will return `undefined`.

  ***

  #### Parameters

  * ##### id: string

  #### Returns undefined | PageReturn

### [**](#getPageId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L545)getPageId

* ****getPageId**(page): undefined | string

- Page IDs are used throughout `BrowserPool` as a method of linking events. You can use a page ID to track the full lifecycle of the page. It is created even before a browser is launched and stays with the page until it's closed.

  ***

  #### Parameters

  * ##### page: PageReturn

  #### Returns undefined | string

### [**](#listenerCount)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L21)externalinheritedlistenerCount

* ****listenerCount**(type): number

- Inherited from TypedEmitter.listenerCount

  #### Parameters

  * ##### externaltype: keyof<!-- --> [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>

  #### Returns number

### [**](#listeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L22)externalinheritedlisteners

* ****listeners**\<U>(type): [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]\[]

- Inherited from TypedEmitter.listeners

  #### Parameters

  * ##### externaltype: U

  #### Returns [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]\[]

### [**](#newPage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L437)newPage

* ****newPage**(options): Promise\<PageReturn>

- Opens a new page in one of the running browsers or launches a new browser and opens a page there, if no browsers are active, or their page limits have been exceeded.

  ***

  #### Parameters

  * ##### options: [BrowserPoolNewPageOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageOptions.md)\<PageOptions, BrowserPlugins\[number]> = <!-- -->{}

  #### Returns Promise\<PageReturn>

### [**](#newPageInNewBrowser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L465)newPageInNewBrowser

* ****newPageInNewBrowser**(options): Promise\<PageReturn>

- Unlike newPage, `newPageInNewBrowser` always launches a new browser to open the page in. Use the `launchOptions` option to configure the new browser.

  ***

  #### Parameters

  * ##### options: [BrowserPoolNewPageInNewBrowserOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageInNewBrowserOptions.md)\<PageOptions, BrowserPlugins\[number]> = <!-- -->{}

  #### Returns Promise\<PageReturn>

### [**](#newPageWithEachPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L499)newPageWithEachPlugin

* ****newPageWithEachPlugin**(optionsList): Promise\<PageReturn\[]>

- Opens new pages with all available plugins and returns an array of pages in the same order as the plugins were provided to `BrowserPool`. This is useful when you want to run a script in multiple environments at the same time, typically in testing or website analysis.

  **Example:**

  ```
  const browserPool = new BrowserPool({
      browserPlugins: [
          new PlaywrightPlugin(playwright.chromium),
          new PlaywrightPlugin(playwright.firefox),
          new PlaywrightPlugin(playwright.webkit),
      ]
  });

  const pages = await browserPool.newPageWithEachPlugin();
  const [chromiumPage, firefoxPage, webkitPage] = pages;
  ```

  ***

  #### Parameters

  * ##### optionsList: Omit<[BrowserPoolNewPageOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageOptions.md)\<PageOptions, BrowserPlugins\[number]>, browserPlugin>\[] = <!-- -->\[]

  #### Returns Promise\<PageReturn\[]>

### [**](#off)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L18)externalinheritedoff

* ****off**\<U>(event, listener): this

- Inherited from TypedEmitter.off

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#on)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L17)externalinheritedon

* ****on**\<U>(event, listener): this

- Inherited from TypedEmitter.on

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#once)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L16)externalinheritedonce

* ****once**\<U>(event, listener): this

- Inherited from TypedEmitter.once

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#prependListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L12)externalinheritedprependListener

* ****prependListener**\<U>(event, listener): this

- Inherited from TypedEmitter.prependListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#prependOnceListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L13)externalinheritedprependOnceListener

* ****prependOnceListener**\<U>(event, listener): this

- Inherited from TypedEmitter.prependOnceListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#rawListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L23)externalinheritedrawListeners

* ****rawListeners**\<U>(type): [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]\[]

- Inherited from TypedEmitter.rawListeners

  #### Parameters

  * ##### externaltype: U

  #### Returns [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]\[]

### [**](#removeAllListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L15)externalinheritedremoveAllListeners

* ****removeAllListeners**(event): this

- Inherited from TypedEmitter.removeAllListeners

  #### Parameters

  * ##### externaloptionalevent: keyof BrowserPoolEvents\<BrowserControllerReturn, PageReturn>

  #### Returns this

### [**](#removeListener)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L14)externalinheritedremoveListener

* ****removeListener**\<U>(event, listener): this

- Inherited from TypedEmitter.removeListener

  #### Parameters

  * ##### externalevent: U
  * ##### externallistener: [BrowserPoolEvents](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md)\<BrowserControllerReturn, PageReturn>\[U]

  #### Returns this

### [**](#retireAllBrowsers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L639)retireAllBrowsers

* ****retireAllBrowsers**(): void

- Removes all active browsers from the pool. The browsers will be closed after all their pages are closed.

  ***

  #### Returns void

### [**](#retireBrowserByPage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L630)retireBrowserByPage

* ****retireBrowserByPage**(page): void

- Removes a browser from the pool. It will be closed after all its pages are closed.

  ***

  #### Parameters

  * ##### page: PageReturn

  #### Returns void

### [**](#retireBrowserController)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L613)retireBrowserController

* ****retireBrowserController**(browserController): void

- Removes a browser controller from the pool. The underlying browser will be closed after all its pages are closed.

  ***

  #### Parameters

  * ##### browserController: BrowserControllerReturn

  #### Returns void

### [**](#setMaxListeners)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/tiny-typed-emitter/src/index.d.ts#L25)externalinheritedsetMaxListeners

* ****setMaxListeners**(n): this

- Inherited from TypedEmitter.setMaxListeners

  #### Parameters

  * ##### externaln: number

  #### Returns this
