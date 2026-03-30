# Source: https://crawlee.dev/js/api/core/interface/RouterHandler.md

# RouterHandler<!-- --> \<Context>

Simple router that works based on request labels. This instance can then serve as a `requestHandler` of your crawler.

```
import { Router, CheerioCrawler, CheerioCrawlingContext } from 'crawlee';

const router = Router.create<CheerioCrawlingContext>();

// we can also use factory methods for specific crawling contexts, the above equals to:
// import { createCheerioRouter } from 'crawlee';
// const router = createCheerioRouter();

router.addHandler('label-a', async (ctx) => {
   ctx.log.info('...');
});
router.addDefaultHandler(async (ctx) => {
   ctx.log.info('...');
});

const crawler = new CheerioCrawler({
    requestHandler: router,
});
await crawler.run();
```

Alternatively we can use the default router instance from crawler object:

```
import { CheerioCrawler } from 'crawlee';

const crawler = new CheerioCrawler();

crawler.router.addHandler('label-a', async (ctx) => {
   ctx.log.info('...');
});
crawler.router.addDefaultHandler(async (ctx) => {
   ctx.log.info('...');
});

await crawler.run();
```

For convenience, we can also define the routes right when creating the router:

```
import { CheerioCrawler, createCheerioRouter } from 'crawlee';
const crawler = new CheerioCrawler({
    requestHandler: createCheerioRouter({
        'label-a': async (ctx) => { ... },
        'label-b': async (ctx) => { ... },
    })},
});
await crawler.run();
```

Middlewares are also supported via the `router.use` method. There can be multiple middlewares for a single router, they will be executed sequentially in the same order as they were registered.

```
crawler.router.use(async (ctx) => {
   ctx.log.info('...');
});
```

### Hierarchy

* [Router](https://crawlee.dev/js/api/core/class/Router.md)\<Context>
  * *RouterHandler*

### Callable

* ****RouterHandler**(ctx): Awaitable\<void>

***

* #### Parameters

  * ##### ctx: Context

  #### Returns Awaitable\<void>

## Index[**](#Index)

### Methods

* [**addDefaultHandler](#addDefaultHandler)
* [**addHandler](#addHandler)
* [**getHandler](#getHandler)
* [**use](#use)

## Methods<!-- -->[**](#Methods)

### [**](#addDefaultHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L110)inheritedaddDefaultHandler

* ****addDefaultHandler**\<UserData>(handler): void

- Inherited from Router.addDefaultHandler

  Registers default route handler.

  ***

  #### Parameters

  * ##### handler: (ctx) => Awaitable\<void>


  #### Returns void

### [**](#addHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L99)inheritedaddHandler

* ****addHandler**\<UserData>(label, handler): void

- Inherited from Router.addHandler

  Registers new route handler for given label.

  ***

  #### Parameters

  * ##### label: string | symbol
  * ##### handler: (ctx) => Awaitable\<void>


  #### Returns void

### [**](#getHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L128)inheritedgetHandler

* ****getHandler**(label): (ctx) => Awaitable\<void>

- Inherited from Router.getHandler

  Returns route handler for given label. If no label is provided, the default request handler will be returned.

  ***

  #### Parameters

  * ##### optionallabel: string | symbol

  #### Returns (ctx) => Awaitable\<void>

  * * **(ctx): Awaitable\<void>

    - #### Parameters

      * ##### ctx: Context

      #### Returns Awaitable\<void>

### [**](#use)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L121)inheriteduse

* ****use**(middleware): void

- Inherited from Router.use

  Registers a middleware that will be fired before the matching route handler. Multiple middlewares can be registered, they will be fired in the same order.

  ***

  #### Parameters

  * ##### middleware: (ctx) => Awaitable\<void>


  #### Returns void
