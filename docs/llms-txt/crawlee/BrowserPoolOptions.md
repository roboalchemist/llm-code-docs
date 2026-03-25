# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolOptions.md

# BrowserPoolOptions<!-- --> \<Plugin>

## Index[**](#Index)

### Properties

* [**browserPlugins](#browserPlugins)
* [**closeInactiveBrowserAfterSecs](#closeInactiveBrowserAfterSecs)
* [**fingerprintOptions](#fingerprintOptions)
* [**maxOpenPagesPerBrowser](#maxOpenPagesPerBrowser)
* [**operationTimeoutSecs](#operationTimeoutSecs)
* [**retireBrowserAfterPageCount](#retireBrowserAfterPageCount)
* [**retireInactiveBrowserAfterSecs](#retireInactiveBrowserAfterSecs)
* [**useFingerprints](#useFingerprints)

## Properties<!-- -->[**](#Properties)

### [**](#browserPlugins)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L67)browserPlugins

**browserPlugins: readonly

<!-- -->

Plugin\[]

Browser plugins are wrappers of browser automation libraries that allow `BrowserPool` to control browsers with those libraries. `browser-pool` comes with a `PuppeteerPlugin` and a `PlaywrightPlugin`.

### [**](#closeInactiveBrowserAfterSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L101)optionalcloseInactiveBrowserAfterSecs

**closeInactiveBrowserAfterSecs?

<!-- -->

: number = 300

Browsers normally close immediately after their last page is processed. However, there could be situations where this does not happen. Browser Pool makes sure all inactive browsers are closed regularly, to free resources.

### [**](#fingerprintOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L116)optionalfingerprintOptions

**fingerprintOptions?

<!-- -->

: [FingerprintOptions](https://crawlee.dev/js/api/browser-pool/interface/FingerprintOptions.md)

### [**](#maxOpenPagesPerBrowser)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L74)optionalmaxOpenPagesPerBrowser

**maxOpenPagesPerBrowser?

<!-- -->

: number = 20

Sets the maximum number of pages that can be open in a browser at the same time. Once reached, a new browser will be launched to handle the excess.

### [**](#operationTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L93)optionaloperationTimeoutSecs

**operationTimeoutSecs?

<!-- -->

: number = 15

As we know from experience, async operations of the underlying libraries, such as launching a browser or opening a new page, can get stuck. To prevent `BrowserPool` from getting stuck, we add a timeout to those operations and you can configure it with this option.

### [**](#retireBrowserAfterPageCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L84)optionalretireBrowserAfterPageCount

**retireBrowserAfterPageCount?

<!-- -->

: number = 100

Browsers tend to get bloated after processing a lot of pages. This option configures the maximum number of processed pages after which the browser will automatically retire and close. A new browser will launch in its place. The browser might be retired sooner if the connected [Session](https://crawlee.dev/js/api/core/class/Session.md) is retired. You can change session retirement behavior using [SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md).

### [**](#retireInactiveBrowserAfterSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L111)optionalretireInactiveBrowserAfterSecs

**retireInactiveBrowserAfterSecs?

<!-- -->

: number = 10

Browsers are marked as retired after they have been inactive for a certain amount of time. This option sets the interval at which the browsers are checked and retired if they are inactive.

Retired browsers are closed after all their pages are closed.

### [**](#useFingerprints)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L115)optionaluseFingerprints

**useFingerprints?

<!-- -->

: boolean = true
