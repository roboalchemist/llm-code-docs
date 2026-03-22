# Source: https://crawlee.dev/js/api/core/class/ErrorTracker.md

# ErrorTracker<!-- -->

This class tracks errors and computes a summary of information like:

* where the errors happened
* what the error names are
* what the error codes are
* what is the general error message

This is extremely useful when there are dynamic error messages, such as argument validation.

Since the structure of the `tracker.result` object differs when using different options, it's typed as `Record<string, unknown>`. The most deep object has a `count` property, which is a number.

It's possible to get the total amount of errors via the `tracker.total` property.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**errorSnapshotter](#errorSnapshotter)
* [**result](#result)
* [**total](#total)

### Methods

* [**add](#add)
* [**addAsync](#addAsync)
* [**captureSnapshot](#captureSnapshot)
* [**getMostPopularErrors](#getMostPopularErrors)
* [**getUniqueErrorCount](#getUniqueErrorCount)
* [**reset](#reset)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L295)constructor

* ****new ErrorTracker**(options): [ErrorTracker](https://crawlee.dev/js/api/core/class/ErrorTracker.md)

- #### Parameters

  * ##### options: Partial<[ErrorTrackerOptions](https://crawlee.dev/js/api/core/interface/ErrorTrackerOptions.md)> = <!-- -->{}

  #### Returns [ErrorTracker](https://crawlee.dev/js/api/core/class/ErrorTracker.md)

## Properties<!-- -->[**](#Properties)

### [**](#errorSnapshotter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L293)optionalerrorSnapshotter

**errorSnapshotter?

<!-- -->

: [ErrorSnapshotter](https://crawlee.dev/js/api/core/class/ErrorSnapshotter.md)

### [**](#result)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L289)result

**result: Record\<string, unknown>

### [**](#total)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L291)total

**total: number

## Methods<!-- -->[**](#Methods)

### [**](#add)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L339)add

* ****add**(error): void

- #### Parameters

  * ##### error: [ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)

  #### Returns void

### [**](#addAsync)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L353)addAsync

* ****addAsync**(error, context): Promise\<void>

- This method is async, because it captures a snapshot of the error context. We added this new method to avoid breaking changes.

  ***

  #### Parameters

  * ##### error: [ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)
  * ##### optionalcontext: [CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)\<unknown, Dictionary>

  #### Returns Promise\<void>

### [**](#captureSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L408)captureSnapshot

* ****captureSnapshot**(storage, error, context): Promise\<void>

- #### Parameters

  * ##### storage: Record\<string, unknown>
  * ##### error: [ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)
  * ##### context: [CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)\<unknown, Dictionary>

  #### Returns Promise\<void>

### [**](#getMostPopularErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L388)getMostPopularErrors

* ****getMostPopularErrors**(count): \[number, string\[]]\[]

- #### Parameters

  * ##### count: number

  #### Returns \[number, string\[]]\[]

### [**](#getUniqueErrorCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L368)getUniqueErrorCount

* ****getUniqueErrorCount**(): number

- #### Returns number

### [**](#reset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L419)reset

* ****reset**(): void

- #### Returns void
