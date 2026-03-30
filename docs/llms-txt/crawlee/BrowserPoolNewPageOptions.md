# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolNewPageOptions.md

# BrowserPoolNewPageOptions<!-- --> \<PageOptions, BP>

## Index[**](#Index)

### Properties

* [**browserPlugin](#browserPlugin)
* [**id](#id)
* [**pageOptions](#pageOptions)
* [**proxyTier](#proxyTier)
* [**proxyUrl](#proxyUrl)

## Properties<!-- -->[**](#Properties)

### [**](#browserPlugin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L878)optionalbrowserPlugin

**browserPlugin?

<!-- -->

: BP

Choose a plugin to open the page with. If none is provided, one of the pool's available plugins will be used.

It must be one of the plugins browser pool was created with. If you wish to start a browser with a different configuration, see the `newPageInNewBrowser` function.

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L864)optionalid

**id?

<!-- -->

: string

Assign a custom ID to the page. If you don't a random string ID will be generated.

### [**](#pageOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L869)optionalpageOptions

**pageOptions?

<!-- -->

: PageOptions

Some libraries (Playwright) allow you to open new pages with specific options. Use this property to set those options.

### [**](#proxyTier)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L886)optionalproxyTier

**proxyTier?

<!-- -->

: number

Proxy tier.

### [**](#proxyUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L882)optionalproxyUrl

**proxyUrl?

<!-- -->

: string

Proxy URL.
