# Source: https://crawlee.dev/js/docs/guides/request-storage.md

# Request Storage

Copy for LLM

Crawlee has several request storage types that are useful for specific tasks. The requests are stored on local disk to a directory defined by the `CRAWLEE_STORAGE_DIR` environment variable. If this variable is not defined, by default Crawlee sets `CRAWLEE_STORAGE_DIR` to `./storage` in the current working directory.

## Request queue[​](#request-queue "Direct link to Request queue")

The request queue is a storage of URLs to crawl. The queue is used for the deep crawling of websites, where we start with several URLs and then recursively follow links to other pages. The data structure supports both breadth-first and depth-first crawling orders.

Each Crawlee project run is associated with a **default request queue**. Typically, it is used to store URLs to crawl in the specific crawler run. Its usage is optional.

In Crawlee, the request queue is represented by the [`RequestQueue`](https://crawlee.dev/js/api/core/class/RequestQueue.md) class.

The request queue is managed by [`MemoryStorage`](https://crawlee.dev/js/api/memory-storage/class/MemoryStorage.md) class and its data is stored in memory, while also being off-loaded to the local directory specified by the `CRAWLEE_STORAGE_DIR` environment variable as follows:

```
{CRAWLEE_STORAGE_DIR}/request_queues/{QUEUE_ID}/entries.json
```

note

`{QUEUE_ID}` is the name or ID of the request queue. The default queue has ID `default`, unless we override it by setting the `CRAWLEE_DEFAULT_REQUEST_QUEUE_ID` environment variable.

note

`entries.json` contains an array of requests.

The following code demonstrates the usage of the request queue:

* Usage with Crawler
* Explicit usage with Crawler
* Basic Operations

```
import { CheerioCrawler } from 'crawlee';

// The crawler will automatically process requests from the queue.
// It's used the same way for Puppeteer/Playwright crawlers.
const crawler = new CheerioCrawler({
    // Note that we're not specifying the requestQueue here
    async requestHandler({ crawler, enqueueLinks }) {
        // Add new request to the queue
        await crawler.addRequests([{ url: 'https://example.com/new-page' }]);
        // Add links found on page to the queue
        await enqueueLinks();
    },
});

// Add the initial requests.
// Note that we are not opening the request queue explicitly before
await crawler.addRequests([
    { url: 'https://example.com/1' },
    { url: 'https://example.com/2' },
    { url: 'https://example.com/3' },
    // ...
]);

// Run the crawler
await crawler.run();
```

```
import { RequestQueue, CheerioCrawler } from 'crawlee';

// Open the default request queue associated with the current run
const requestQueue = await RequestQueue.open();

// Enqueue the initial requests
await requestQueue.addRequests([
    { url: 'https://example.com/1' },
    { url: 'https://example.com/2' },
    { url: 'https://example.com/3' },
    // ...
]);

// The crawler will automatically process requests from the queue.
// It's used the same way for Puppeteer/Playwright crawlers
const crawler = new CheerioCrawler({
    requestQueue,
    async requestHandler({ enqueueLinks }) {
        // Add new request to the queue
        await requestQueue.addRequests([{ url: 'https://example.com/new-page' }]);
        // Add links found on page to the queue
        await enqueueLinks();
    },
});

// Run the crawler
await crawler.run();
```

```
import { RequestQueue } from 'crawlee';

// Open the default request queue associated with the crawler run
const requestQueue = await RequestQueue.open();

// Enqueue the initial batch of requests (could be an array of just one)
await requestQueue.addRequests([
    { url: 'https://example.com/1' },
    { url: 'https://example.com/2' },
    { url: 'https://example.com/3' },
]);

// Open the named request queue
const namedRequestQueue = await RequestQueue.open('named-queue');

// Remove the named request queue
await namedRequestQueue.drop();
```

To see more detailed example of how to use the request queue with a crawler, see the [Puppeteer Crawler](https://crawlee.dev/js/docs/examples/puppeteer-crawler.md) example.

## Request list[​](#request-list "Direct link to Request list")

The request list is not a storage per se - it represents the list of URLs to crawl that is stored in a crawler run memory (or optionally in default [Key-Value Store](https://crawlee.dev/js/docs/guides/result-storage.md#key-value-store) associated with the run, if specified). The list is used for the crawling of a large number of URLs, when we know all the URLs which should be visited by the crawler and no URLs would be added during the run. The URLs can be provided either in code or parsed from a text file hosted on the web.

Request list is created exclusively for the crawler run and only if its usage is explicitly specified in the code. Its usage is optional.

In Crawlee, the request list is represented by the [`RequestList`](https://crawlee.dev/js/api/core/class/RequestList.md) class.

The following code demonstrates basic operations of the request list:

```
import { RequestList, PuppeteerCrawler } from 'crawlee';

// Prepare the sources array with URLs to visit
const sources = [
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
];

// Open the request list.
// List name is used to persist the sources and the list state in the key-value store
const requestList = await RequestList.open('my-list', sources);

// The crawler will automatically process requests from the list
// It's used the same way for Cheerio /Playwright crawlers.
const crawler = new PuppeteerCrawler({
    requestList,
    async requestHandler({ page, request }) {
        // Process the page (extract data, take page screenshot, etc).
        // No more requests could be added to the request list here
    },
});
```

## Which one to choose?[​](#which-one-to-choose "Direct link to Which one to choose?")

When using Request queue - we would normally have several start URLs (e.g. category pages on e-commerce website) and then recursively add more (e.g. individual item pages) programmatically to the queue, it supports dynamic adding and removing of requests. No more URLs can be added to Request list after its initialization as it is immutable, URLs cannot be removed from the list either.

On the other hand, the Request queue is not optimized for adding or removing numerous URLs in a batch. This is technically possible, but requests are added one by one to the queue, and thus it would take significant time with a larger number of requests. Request list however can contain even millions of URLs, and it would take significantly less time to add them to the list, compared to the queue.

Note that Request queue and Request list can be used together by the same crawler. In such cases, each request from the Request list is enqueued into the Request queue first (to the foremost position in the queue, even if Request queue is not empty) and then consumed from the latter. This is necessary to avoid the same URL being processed more than once (from the list first and then possibly from the queue). In practical terms, such a combination can be useful when there are numerous initial URLs, but more URLs would be added dynamically by the crawler.

tip

In Crawlee, there is not much need to combine the request queue together with the request list (although it's technically possible).

Previously there was no way to add the initial requests to the queue in batches (to add an array of requests), i.e. we could have only added the requests one by one to the queue with the help of [`addRequest()`](https://crawlee.dev/js/api/core/class/RequestQueue.md#addRequest) function.

However, now we could use the [`addRequests()`](https://crawlee.dev/js/api/core/class/RequestQueue.md#addRequests) function, which adds requests in batches. Thus, instead of combining the request queue and the request list, we can use only the request queue for such use-cases now. See the examples below.

* Request Queue
* Request Queue + Request List

```
// This is the suggested way.
// Note that we are not using the request list at all,
// and not using the request queue explicitly here.

import { PuppeteerCrawler } from 'crawlee';

// Prepare the sources array with URLs to visit (it can contain millions of URLs)
const sources = [
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
    // ...
];

// The crawler will automatically process requests from the queue.
// It's used the same way for Cheerio/Playwright crawlers
const crawler = new PuppeteerCrawler({
    async requestHandler({ crawler, enqueueLinks }) {
        // Add new request to the queue
        await crawler.addRequests(['http://www.example.com/new-page']);

        // Add links found on page to the queue
        await enqueueLinks();

        // The requests above would be added to the queue
        // and would be processed after the initial requests are processed.
    },
});

// Add the initial sources array to the request queue
// and run the crawler
await crawler.run(sources);
```

```
// This is technically correct, but
// we need to explicitly open/use both the request queue and the request list.
// We suggest using the request queue and batch add the requests instead.

import { RequestList, RequestQueue, PuppeteerCrawler } from 'crawlee';

// Prepare the sources array with URLs to visit (it can contain millions of URLs)
const sources = [
    { url: 'http://www.example.com/page-1' },
    { url: 'http://www.example.com/page-2' },
    { url: 'http://www.example.com/page-3' },
    // ...
];

// Open the request list with the initial sources array
const requestList = await RequestList.open('my-list', sources);

// Open the default request queue. It's not necessary to add any requests to the queue
const requestQueue = await RequestQueue.open();

// The crawler will automatically process requests from the list and the queue.
// It's used the same way for Cheerio/Playwright crawlers
const crawler = new PuppeteerCrawler({
    requestList,
    requestQueue,
    // Each request from the request list is enqueued to the request queue one by one.
    // At this point request with the same URL would exist in the list and the queue
    async requestHandler({ crawler, enqueueLinks }) {
        // Add new request to the queue
        await crawler.addRequests(['http://www.example.com/new-page']);

        // Add links found on page to the queue
        await enqueueLinks();

        // The requests above would be added to the queue (but not to the list)
        // and would be processed after the request list is empty.
        // No more requests could be added to the list here
    },
});

// Run the crawler
await crawler.run();
```

## Cleaning up the storages[​](#cleaning-up-the-storages "Direct link to Cleaning up the storages")

Default storages are purged before the crawler starts if not specified otherwise. This happens as early as when we try to open some storage (e.g. via `RequestQueue.open()`) or when we try to work with a default storage via one of the helper methods (e.g. `crawler.addRequests()` that under the hood calls `RequestQueue.open()`). If we don't work with storages explicitly in our code, the purging will eventually happen when the `run` method of our crawler is executed. In case we need to purge the storages sooner, we can use the [`purgeDefaultStorages()`](https://crawlee.dev/js/api/core/function/purgeDefaultStorages.md) helper explicitly:

```
import { purgeDefaultStorages } from 'crawlee';

await purgeDefaultStorages();
```

Calling this function will clean up the default request storage directory (and also the request list stored in default key-value store). This is a shortcut for running (optional) `purge` method on the [`StorageClient`](https://crawlee.dev/js/api/core/interface/StorageClient.md) interface, in other words it will call the `purge` method of the underlying storage implementation we are currently using. You can make sure the storage is purged only once for a given execution context if you set `onlyPurgeOnce` to `true` in the `options` object.
