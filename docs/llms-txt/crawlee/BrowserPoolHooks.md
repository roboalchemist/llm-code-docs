# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolHooks.md

# BrowserPoolHooks<!-- --> \<BC, LC, PR>

## Index[**](#Index)

### Properties

* [**postLaunchHooks](#postLaunchHooks)
* [**postPageCloseHooks](#postPageCloseHooks)
* [**postPageCreateHooks](#postPageCreateHooks)
* [**preLaunchHooks](#preLaunchHooks)
* [**prePageCloseHooks](#prePageCloseHooks)
* [**prePageCreateHooks](#prePageCreateHooks)

## Properties<!-- -->[**](#Properties)

### [**](#postLaunchHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L212)optionalpostLaunchHooks

**postLaunchHooks?

<!-- -->

: [PostLaunchHook](https://crawlee.dev/js/api/browser-pool.md#PostLaunchHook)\<BC>\[]

Post-launch hooks are executed as soon as a browser is launched. The hooks are called with two arguments: `pageId`: `string` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) To guarantee order of execution before other hooks in the same browser, the [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) methods cannot be used until the post-launch hooks complete. If you attempt to call `await browserController.close()` from a post-launch hook, it will deadlock the process. This API is subject to change.

### [**](#postPageCloseHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L245)optionalpostPageCloseHooks

**postPageCloseHooks?

<!-- -->

: [PostPageCloseHook](https://crawlee.dev/js/api/browser-pool.md#PostPageCloseHook)\<BC>\[]

Post-page-close hooks allow you to do page related clean up. The hooks are called with two arguments: `pageId`: `string` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

### [**](#postPageCreateHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L231)optionalpostPageCreateHooks

**postPageCreateHooks?

<!-- -->

: [PostPageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PostPageCreateHook)\<BC, PR>\[]

Post-page-create hooks are called right after a new page is created and all internal actions of Browser Pool are completed. This is the place to make changes to a page that you would like to apply to all pages. Such as injecting a JavaScript library into all pages. The hooks are called with two arguments: `page`: `Page` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

### [**](#preLaunchHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L202)optionalpreLaunchHooks

**preLaunchHooks?

<!-- -->

: [PreLaunchHook](https://crawlee.dev/js/api/browser-pool.md#PreLaunchHook)\<LC>\[]

Pre-launch hooks are executed just before a browser is launched and provide a good opportunity to dynamically change the launch options. The hooks are called with two arguments: `pageId`: `string` and `launchContext`: [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)

### [**](#prePageCloseHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L239)optionalprePageCloseHooks

**prePageCloseHooks?

<!-- -->

: [PrePageCloseHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCloseHook)\<BC, PR>\[]

Pre-page-close hooks give you the opportunity to make last second changes in a page that's about to be closed, such as saving a snapshot or updating state. The hooks are called with two arguments: `page`: `Page` and `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)

### [**](#prePageCreateHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L222)optionalprePageCreateHooks

**prePageCreateHooks?

<!-- -->

: [PrePageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCreateHook)\<BC, Parameters\<BC\[newPage]>\[0]>\[]

Pre-page-create hooks are executed just before a new page is created. They are useful to make dynamic changes to the browser before opening a page. The hooks are called with three arguments: `pageId`: `string`, `browserController`: [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md) and `pageOptions`: `object|undefined` - This only works if the underlying `BrowserController` supports new page options. So far, new page options are only supported by `PlaywrightController` in incognito contexts. If the page options are not supported by `BrowserController` the `pageOptions` argument is `undefined`.
