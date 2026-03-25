# Source: https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolEvents.md

# BrowserPoolEvents<!-- --> \<BC, Page>

## Index[**](#Index)

### Properties

* [**browserLaunched](#browserLaunched)
* [**browserRetired](#browserRetired)
* [**pageClosed](#pageClosed)
* [**pageCreated](#pageCreated)

## Properties<!-- -->[**](#Properties)

### [**](#browserLaunched)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L33)browserLaunched

**browserLaunched: (browserController) => void | Promise\<void>

#### Type declaration

* * **(browserController): void | Promise\<void>

  - #### Parameters

    * ##### browserController: BC

    #### Returns void | Promise\<void>

### [**](#browserRetired)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L32)browserRetired

**browserRetired: (browserController) => void | Promise\<void>

#### Type declaration

* * **(browserController): void | Promise\<void>

  - #### Parameters

    * ##### browserController: BC

    #### Returns void | Promise\<void>

### [**](#pageClosed)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L31)pageClosed

**pageClosed: (page) => void | Promise\<void>

#### Type declaration

* * **(page): void | Promise\<void>

  - #### Parameters

    * ##### page: Page

    #### Returns void | Promise\<void>

### [**](#pageCreated)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-pool/src/browser-pool.ts#L30)pageCreated

**pageCreated: (page) => void | Promise\<void>

#### Type declaration

* * **(page): void | Promise\<void>

  - #### Parameters

    * ##### page: Page

    #### Returns void | Promise\<void>
