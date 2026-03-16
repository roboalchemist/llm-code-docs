# Source: https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightClickElements.md

# playwrightClickElements<!-- -->

## Index[**](#Index)

### References

* [**enqueueLinksByClickingElements](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightClickElements.md#enqueueLinksByClickingElements)

### Interfaces

* [**EnqueueLinksByClickingElementsOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightClickElements.md#EnqueueLinksByClickingElementsOptions)

## References<!-- -->[**](#References)

### [**](#enqueueLinksByClickingElements)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L225)enqueueLinksByClickingElements

Re-exports

<!-- -->

[enqueueLinksByClickingElements](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#enqueueLinksByClickingElements)

## Interfaces<!-- -->[**](#Interfaces)

### [**](#EnqueueLinksByClickingElementsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L30)EnqueueLinksByClickingElementsOptions

**EnqueueLinksByClickingElementsOptions:

### [**](#clickOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L56)optionalclickOptions

**clickOptions?

<!-- -->

: { button?

<!-- -->

: left | right | middle; clickCount?

<!-- -->

: number; delay?

<!-- -->

: number; force?

<!-- -->

: boolean; modifiers?

<!-- -->

: (Alt | Control | ControlOrMeta | Meta | Shift)\[]; noWaitAfter?

<!-- -->

: boolean; position?

<!-- -->

: { x: number; y: number }; strict?

<!-- -->

: boolean; timeout?

<!-- -->

: number; trial?

<!-- -->

: boolean }

Click options for use in Playwright click handler.

***

#### Type declaration

* ##### externaloptionalbutton?<!-- -->: left | right | middle

  Defaults to `left`.

* ##### externaloptionalclickCount?<!-- -->: number

  defaults to 1. See \[UIEvent.detail].

* ##### externaloptionaldelay?<!-- -->: number

  Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

* ##### externaloptionalforce?<!-- -->: boolean

  Whether to bypass the [actionability](https://playwright.dev/docs/actionability) checks. Defaults to `false`.

* ##### externaloptionalmodifiers?<!-- -->: (Alt | Control | ControlOrMeta | Meta | Shift)\[]

  Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS.

* ##### externaloptionalnoWaitAfter?<!-- -->: boolean

  Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`.

  * **@deprecated**

    This option will default to `true` in the future.

* ##### externaloptionalposition?<!-- -->: { x: number; y: number }

  A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element.

  * ##### externalx: number
  * ##### externaly: number

* ##### externaloptionalstrict?<!-- -->: boolean

  When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception.

* ##### externaloptionaltimeout?<!-- -->: number

  Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout(timeout)](https://playwright.dev/docs/api/class-page#page-set-default-timeout) methods.

* ##### externaloptionaltrial?<!-- -->: boolean

  When set, this method only performs the [actionability](https://playwright.dev/docs/actionability) checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed.

### [**](#exclude)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L83)optionalexclude

**exclude?

<!-- -->

: readonly

<!-- -->

([GlobInput](https://crawlee.dev/js/api/core.md#GlobInput) | [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput))\[]

An array of glob pattern strings, regexp patterns or plain objects containing patterns matching URLs that will **never** be enqueued.

The plain objects must include either the `glob` property or the `regexp` property.

Glob matching is always case-insensitive. If you need case-sensitive matching, provide a regexp.

### [**](#forefront)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L175)optionalforefront

**forefront?

<!-- -->

: boolean = false

If set to `true`:

* while adding the request to the queue: the request will be added to the foremost position in the queue.
* while reclaiming the request: the request will be placed to the beginning of the queue, so that it's returned in the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). By default, it's put to the end of the queue.

### [**](#globs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L72)optionalglobs

**globs?

<!-- -->

: [GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)\[]

An array of glob pattern strings or plain objects containing glob pattern strings matching the URLs to be enqueued.

The plain objects must include at least the `glob` property, which holds the glob pattern string. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

The matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

If `globs` is an empty array or `undefined`, then the function enqueues all the intercepted navigation requests produced by the page after clicking on elements matching the provided CSS selector.

### [**](#label)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L51)optionallabel

**label?

<!-- -->

: string

Sets [Request.label](https://crawlee.dev/js/api/core/class/Request.md#label) for newly enqueued requests.

### [**](#maxWaitForPageIdleSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L165)optionalmaxWaitForPageIdleSecs

**maxWaitForPageIdleSecs?

<!-- -->

: number = 5

This is the maximum period for which the function will keep tracking events, even if more events keep coming. Its purpose is to prevent a deadlock in the page by periodic events, often unrelated to the clicking itself. See `waitForPageIdleSecs` above for an explanation.

### [**](#page)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L34)page

**page: Page

Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

### [**](#pseudoUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L117)optionalpseudoUrls

**pseudoUrls?

<!-- -->

: [PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)\[]

*NOTE:* In future versions of SDK the options will be removed. Please use `globs` or `regexps` instead.

An array of [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) strings or plain objects containing [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) strings matching the URLs to be enqueued.

The plain objects must include at least the `purl` property, which holds the pseudo-URL pattern string. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

With a pseudo-URL string, the matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

If `pseudoUrls` is an empty array or `undefined`, then the function enqueues all the intercepted navigation requests produced by the page after clicking on elements matching the provided CSS selector.

* **@deprecated**

  prefer using `globs` or `regexps` instead

### [**](#regexps)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L96)optionalregexps

**regexps?

<!-- -->

: [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)\[]

An array of regular expressions or plain objects containing regular expressions matching the URLs to be enqueued.

The plain objects must include at least the `regexp` property, which holds the regular expression. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

If `regexps` is an empty array or `undefined`, then the function enqueues all the intercepted navigation requests produced by the page after clicking on elements matching the provided CSS selector.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L39)requestQueue

**requestQueue: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

A request queue to which the URLs will be enqueued.

### [**](#selector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L45)selector

**selector: string

A CSS selector matching elements to be clicked on. Unlike in enqueueLinks, there is no default value. This is to prevent suboptimal use of this function by using it too broadly.

### [**](#skipNavigation)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L181)optionalskipNavigation

**skipNavigation?

<!-- -->

: boolean = false

If set to `true`, tells the crawler to skip navigation and process the request directly.

### [**](#transformRequestFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L140)optionaltransformRequestFunction

**transformRequestFunction?

<!-- -->

: [RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md)

Just before a new [Request](https://crawlee.dev/js/api/core/class/Request.md) is constructed and enqueued to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md), this function can be used to remove it or modify its contents such as `userData`, `payload` or, most importantly `uniqueKey`. This is useful when you need to enqueue multiple `Requests` to the queue that share the same URL, but differ in methods or payloads, or to dynamically update or create `userData`.

For example: by adding `useExtendedUniqueKey: true` to the `request` object, `uniqueKey` will be computed from a combination of `url`, `method` and `payload` which enables crawling of websites that navigate using form submits (POST requests).

**Example:**

```
{
    transformRequestFunction: (request) => {
        request.userData.foo = 'bar';
        request.useExtendedUniqueKey = true;
        return request;
    }
}
```

### [**](#userData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L48)optionaluserData

**userData?

<!-- -->

: Dictionary

Sets [Request.userData](https://crawlee.dev/js/api/core/class/Request.md#userData) for newly enqueued requests.

### [**](#waitForPageIdleSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L157)optionalwaitForPageIdleSecs

**waitForPageIdleSecs?

<!-- -->

: number = 1

Clicking in the page triggers various asynchronous operations that lead to new URLs being shown by the browser. It could be a simple JavaScript redirect or opening of a new tab in the browser. These events often happen only some time after the actual click. Requests typically take milliseconds while new tabs open in hundreds of milliseconds.

To be able to capture all those events, the `enqueueLinksByClickingElements()` function repeatedly waits for the `waitForPageIdleSecs`. By repeatedly we mean that whenever a relevant event is triggered, the timer is restarted. As long as new events keep coming, the function will not return, unless the below `maxWaitForPageIdleSecs` timeout is reached.

You may want to reduce this for example when you're sure that your clicks do not open new tabs, or increase when you're not getting all the expected URLs.
