# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageInNewBrowserOptions.md

# BrowserPoolNewPageInNewBrowserOptions<!-- --> \<PageOptions, BP>

## Index[**](#Index)

### Properties

* [**browserPlugin](#browserPlugin)
* [**id](#id)
* [**launchOptions](#launchOptions)
* [**pageOptions](#pageOptions)

## Properties<!-- -->[**](#Properties)

### [**](#browserPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L912)optionalbrowserPlugin

**browserPlugin?

<!-- -->

: BP

Provide a plugin to launch the browser. If none is provided, one of the pool's available plugins will be used.

If you configured `BrowserPool` to rotate multiple libraries, such as both Puppeteer and Playwright, you should always set the `browserPlugin` when using the `launchOptions` option.

The plugin will not be added to the list of plugins used by the pool. You can either use one of those, to launch a specific browser, or provide a completely new configuration.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L894)optionalid

**id?

<!-- -->

: string

Assign a custom ID to the page. If you don't a random string ID will be generated.

### [**](#launchOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L916)optionallaunchOptions

**launchOptions?

<!-- -->

: BP\[launchOptions]

Options that will be used to launch the new browser.

### [**](#pageOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L899)optionalpageOptions

**pageOptions?

<!-- -->

: PageOptions

Some libraries (Playwright) allow you to open new pages with specific options. Use this property to set those options.
