# Source: https://crawlee.dev/js/api/core/class/ErrorSnapshotter.md

# ErrorSnapshotter<!-- -->

ErrorSnapshotter class is used to capture a screenshot of the page and a snapshot of the HTML when an error occurs during web crawling.

This functionality is opt-in, and can be enabled via the crawler options:

```
const crawler = new BasicCrawler({
  // ...
  statisticsOptions: {
    saveErrorSnapshots: true,
  },
});
```

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**BASE\_MESSAGE](#BASE_MESSAGE)
* [**MAX\_ERROR\_CHARACTERS](#MAX_ERROR_CHARACTERS)
* [**MAX\_FILENAME\_LENGTH](#MAX_FILENAME_LENGTH)
* [**MAX\_HASH\_LENGTH](#MAX_HASH_LENGTH)
* [**SNAPSHOT\_PREFIX](#SNAPSHOT_PREFIX)

### Methods

* [**captureSnapshot](#captureSnapshot)
* [**contextCaptureSnapshot](#contextCaptureSnapshot)
* [**generateFilename](#generateFilename)
* [**saveHTMLSnapshot](#saveHTMLSnapshot)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new ErrorSnapshotter**(): [ErrorSnapshotter](https://crawlee.dev/js/api/core/class/ErrorSnapshotter.md)

- #### Returns [ErrorSnapshotter](https://crawlee.dev/js/api/core/class/ErrorSnapshotter.md)

## Properties<!-- -->[**](#Properties)

### [**](#BASE_MESSAGE)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L46)staticreadonlyBASE\_MESSAGE

**BASE\_MESSAGE: An error occurred =

<!-- -->

'An error occurred'

### [**](#MAX_ERROR_CHARACTERS)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L43)staticreadonlyMAX\_ERROR\_CHARACTERS

**MAX\_ERROR\_CHARACTERS: 30 =

<!-- -->

30

### [**](#MAX_FILENAME_LENGTH)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L45)staticreadonlyMAX\_FILENAME\_LENGTH

**MAX\_FILENAME\_LENGTH: 250 =

<!-- -->

250

### [**](#MAX_HASH_LENGTH)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L44)staticreadonlyMAX\_HASH\_LENGTH

**MAX\_HASH\_LENGTH: 30 =

<!-- -->

30

### [**](#SNAPSHOT_PREFIX)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L47)staticreadonlySNAPSHOT\_PREFIX

**SNAPSHOT\_PREFIX: ERROR\_SNAPSHOT =

<!-- -->

'ERROR\_SNAPSHOT'

## Methods<!-- -->[**](#Methods)

### [**](#captureSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L52)captureSnapshot

* ****captureSnapshot**(error, context): Promise\<ErrorSnapshot>

- Capture a snapshot of the error context.

  ***

  #### Parameters

  * ##### error: [ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)
  * ##### context: [CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)\<unknown, Dictionary>

  #### Returns Promise\<ErrorSnapshot>

### [**](#contextCaptureSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L105)contextCaptureSnapshot

* ****contextCaptureSnapshot**(context, fileName): Promise\<undefined | [SnapshotResult](https://crawlee.dev/js/api/core/interface/SnapshotResult.md)>

- Captures a snapshot of the current page using the context.saveSnapshot function. This function is applicable for browser contexts only. Returns an object containing the filenames of the screenshot and HTML file.

  ***

  #### Parameters

  * ##### context: BrowserCrawlingContext
  * ##### fileName: string

  #### Returns Promise\<undefined | [SnapshotResult](https://crawlee.dev/js/api/core/interface/SnapshotResult.md)>

### [**](#generateFilename)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L135)generateFilename

* ****generateFilename**(error): string

- Generate a unique fileName for each error snapshot.

  ***

  #### Parameters

  * ##### error: [ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)

  #### Returns string

### [**](#saveHTMLSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L123)saveHTMLSnapshot

* ****saveHTMLSnapshot**(html, keyValueStore, fileName): Promise\<undefined | string>

- Save the HTML snapshot of the page, and return the fileName with the extension.

  ***

  #### Parameters

  * ##### html: string
  * ##### keyValueStore: [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)
  * ##### fileName: string

  #### Returns Promise\<undefined | string>
