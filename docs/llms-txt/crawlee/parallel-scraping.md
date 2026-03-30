# Source: https://crawlee.dev/js/docs/guides/parallel-scraping.md

# Parallel Scraping Guide

Copy for LLM

Experimental features ahead

At the time of writing this guide (December 2023), request locking is still an experimental feature. You can read more about the experiment by visiting the [request locking experiment](https://crawlee.dev/js/docs/experiments/experiments-request-locking.md) page.

In this guide, we will walk you through how you can turn your single scraper into a scraper that can be parallelized and run in multiple instances. This guide assumes you've read and walked through our [introduction guide](https://crawlee.dev/js/docs/introduction/setting-up.md) (or have a fully-fledged scraper already built), but if you haven't done so yet, take a break, go read through all that, and come back. We'll be waiting...

*Oh, you're back already! Let's proceed in making that scraper parallel!*

## Things to consider before parallelizing[​](#things-to-consider-before-parallelizing "Direct link to Things to consider before parallelizing")

Before you rush ahead and change your scraper to support parallelization, take a minute to consider the following factors:

* Do you plan on scraping so many pages that you need to parallelize your scraper?

  <!-- -->

  * For example, if your scraper goes across a few pages, you probably don't need parallelization
  * But if you scrape a lot of pages, or you scrape pages that take a long time to load, you might want to consider parallelization

* Can you parallelize your scraper while not overloading the target website?
  <!-- -->
  * For example, if you scrape a website that has a lot of traffic, you don't want to add to that traffic by running multiple scrapers in parallel as that might cause the website to go down for all its users

* Do you have the resources available to run multiple scrapers in parallel?

  <!-- -->

  * When running locally, depending on your scraper type, do you have enough CPU and RAM available to sustain multiple scrapers running in parallel
  * When running in the cloud, will the extra speed from parallelization be worth the extra cost of running multiple scrapers in parallel?

Let's assume you answered yes to all of those. Yes? Yes. Before we go ahead and get to the actual guide, we'd like to ask you to also take a read on [Apify's Ethical Web Scraping](https://blog.apify.com/what-is-ethical-web-scraping-and-how-do-you-do-it/) blog post!

Now that we've gone through all that, the guide is split into two parts: converting the initial scraper we built in the [introduction guide](https://crawlee.dev/js/docs/introduction/setting-up.md) to one that prepares requests to be usable in parallel scrapers, and then running scrapers in parallel.

Want to see the final result?

You can see it on the [Crawlee Parallel Scraping Example](https://github.com/apify/crawlee-parallel-scraping-example) repository! It's the same scraper we built in the [introduction guide](https://crawlee.dev/js/docs/introduction/setting-up.md), but in TypeScript and parallelized!

### But isn't Crawlee already concurrent? What's the difference between concurrency and parallelization?[​](#but-isnt-crawlee-already-concurrent-whats-the-difference-between-concurrency-and-parallelization "Direct link to But isn't Crawlee already concurrent? What's the difference between concurrency and parallelization?")

> *Hold on! I've used Crawlee before, and it has a `maxConcurrency` option! What's this for then?!*

You're correct, Crawlee already supports scraping in "parallel" (more accurately called concurrent). What that enables is one process having multiple tasks that run in the background at the same time. But, as your scraping operation scales up, you are likely to encounter bottlenecks. These can range from the runtime environment's inability to process more requests simultaneously, to resources like RAM and CPU being maxed out. You can only scale up resources so much before it stops providing a real benefit.

This is what people refer to when saying vertical or horizontal scaling. Vertical scaling is when you increase the resources of a single process or machine, while horizontal scaling is when you increase the number of processes or machines. Horizontal scaling, on the other hand, is the kind of scaling (or what we're referring to as "parallelization") we are showcasing in this guide!

## Preparing your scraper for parallelization[​](#preparing-your-scraper-for-parallelization "Direct link to Preparing your scraper for parallelization")

One of the best parts of Crawlee is that, for the most part, we do not need to change much to make this happen! Just create the queue that supports locking, enqueue links to it from the initial scraper, then build scrapers that run in parallel that use that queue!

### Creating the request queue with locking support[​](#creating-the-request-queue-with-locking-support "Direct link to Creating the request queue with locking support")

The first step in our conversion process will be creating a common file (let's call it `requestQueue.mjs`) that will store the request queue that supports request locking.

src/requestQueue.mjs

```
import { RequestQueueV2 } from 'crawlee';

// Create the request queue that also supports parallelization
let queue;

/**
 * @param {boolean} makeFresh Whether the queue should be cleared before returning it
 * @returns The queue
 */
export async function getOrInitQueue(makeFresh = false) {
    if (queue) {
        return queue;
    }

    queue = await RequestQueueV2.open('shop-urls');

    if (makeFresh) {
        await queue.drop();
        queue = await RequestQueueV2.open('shop-urls');
    }

    return queue;
}
```

The exported function, `getOrInitQueue`, might seem like it does a lot. In essence, it just ensures the request queue is initialized, and if requested, ensures it starts off with an empty state.

### Adapting our previous scraper to enqueue the product URLs to the new queue[​](#adapting-our-previous-scraper-to-enqueue-the-product-urls-to-the-new-queue "Direct link to Adapting our previous scraper to enqueue the product URLs to the new queue")

In the `src/routes.mjs` file of the scraper we previously built, we have a handler for the `CATEGORY` label. Let's adapt that handler to enqueue the product URLs to the new queue we created.

Firstly, let's import the `getOrInitQueue` function from the `requestQueue.mjs` file we created earlier. Add the following line at the start of the file:

src/routes.mjs

```
import { getOrInitQueue } from './requestQueue.mjs';
```

Then, replace the `CATEGORY` handler with the following:

src/routes.mjs

```
router.addHandler('CATEGORY', async ({ page, enqueueLinks, request, log }) => {
    log.debug(`Enqueueing pagination for: ${request.url}`);
    // We are now on a category page. We can use this to paginate through and enqueue all products,
    // as well as any subsequent pages we find

    await page.waitForSelector('.product-item > a');
    await enqueueLinks({
        selector: '.product-item > a',
        label: 'DETAIL', // <= note the different label,
        requestQueue: await getOrInitQueue(), // <= note the different request queue
    });

    // Now we need to find the "Next" button and enqueue the next page of results (if it exists)
    const nextButton = await page.$('a.pagination__next');
    if (nextButton) {
        await enqueueLinks({
            selector: 'a.pagination__next',
            label: 'CATEGORY', // <= note the same label
        });
    }
});
```

Now, let's rename our entry point file `src/main.mjs` to `src/initial-scraper.mjs` and run it. You should see the crawler not scrape any detail pages, but now the URLs are being enqueued to the queue that supports locking!

Before we wrap up, let's also add the following line before `crawler.run()`:

src/initial-scraper.mjs

```
import { getOrInitQueue } from './requestQueue.mjs';

// Pre-initialize the queue so that we have a blank slate that will get filled out by the crawler
await getOrInitQueue(true);
```

We need this to ensure the queue always starts on an empty slate when we run the scraper. But you may not need this in your use case - remember to always experiment and see what works best!

And that's it with preparing our initial scraper to save all URLs we want to scrape to the queue that supports locking!

### Creating the parallel scrapers[​](#creating-the-parallel-scrapers "Direct link to Creating the parallel scrapers")

Up next, let's build another scraper that will schedule the URLs from the queue to be scraped in parallel! For this, we will be using child processes from Node.js, but you can use any other method you want to run multiple scrapers in parallel. You will need to adjust your code if you use other methods.

The scraper will fork itself twice (but you can experiment with this), and each fork will re-use the queue we created earlier. The best part? We can re-use the previous router we built for the initial scraper! Yay for code reuse!

src/parallel-scraper.mjs

```
import { fork } from 'node:child_process';

import { Configuration, Dataset, PlaywrightCrawler, log } from 'crawlee';

import { router } from './routes.mjs';
import { getOrInitQueue } from './shared.mjs';

// For this example, we will spawn 2 separate processes that will scrape the store in parallel.

if (!process.env.IN_WORKER_THREAD) {
    // This is the main process. We will use this to spawn the worker threads.
    log.info('Setting up worker threads.');

    const currentFile = new URL(import.meta.url).pathname;

    // Store a promise per worker, so we wait for all to finish before exiting the main process
    const promises = [];

    // You can decide how many workers you want to spawn, but keep in mind you can only spawn so many before you overload your machine
    for (let i = 0; i < 2; i++) {
        const proc = fork(currentFile, {
            env: {
                // Share the current process's env across to the newly created process
                ...process.env,
                // ...but also tell the process that it's a worker process
                IN_WORKER_THREAD: 'true',
                // ...as well as which worker it is
                WORKER_INDEX: String(i),
            },
        });

        proc.on('online', () => {
            log.info(`Process ${i} is online.`);

            // Log out what the crawlers are doing
            // Note: we want to use console.log instead of log.info because we already get formatted output from the crawlers
            proc.stdout.on('data', (data) => {
                // eslint-disable-next-line no-console
                console.log(data.toString());
            });

            proc.stderr.on('data', (data) => {
                // eslint-disable-next-line no-console
                console.error(data.toString());
            });
        });

        proc.on('message', async (data) => {
            log.debug(`Process ${i} sent data.`, data);
            await Dataset.pushData(data);
        });

        promises.push(
            new Promise((resolve) => {
                proc.once('exit', (code, signal) => {
                    log.info(`Process ${i} exited with code ${code} and signal ${signal}`);
                    resolve();
                });
            }),
        );
    }

    await Promise.all(promises);

    log.info('Crawling complete!');
} else {
    // This is the worker process. We will use this to scrape the store.

    // Let's build a logger that will prefix the log messages with the worker index
    const workerLogger = log.child({ prefix: `[Worker ${process.env.WORKER_INDEX}]` });

    // This is better set with CRAWLEE_LOG_LEVEL env var
    // or a configuration option. This is just for show 😈
    workerLogger.setLevel(log.LEVELS.DEBUG);

    // Disable the automatic purge on start
    // This is needed when running locally, as otherwise multiple processes will try to clear the default storage (and that will cause clashes)
    Configuration.set('purgeOnStart', false);

    // Get the request queue
    const requestQueue = await getOrInitQueue(false);

    // Configure crawlee to store the worker-specific data in a separate directory (needs to be done AFTER the queue is initialized when running locally)
    const config = new Configuration({
        storageClientOptions: {
            localDataDirectory: `./storage/worker-${process.env.WORKER_INDEX}`,
        },
    });

    workerLogger.debug('Setting up crawler.');
    const crawler = new PlaywrightCrawler(
        {
            log: workerLogger,
            // Instead of the long requestHandler with
            // if clauses we provide a router instance.
            requestHandler: router,
            // Enable the request locking experiment so that we can actually use the queue.
            experiments: {
                requestLocking: true,
            },
            // Provide the request queue we've pre-filled in previous steps
            requestQueue,
            // Let's also limit the crawler's concurrency, we don't want to overload a single process 🐌
            maxConcurrency: 5,
        },
        config,
    );

    await crawler.run();
}
```

We'll also need to do one small change in the `DETAIL` route handler. Instead of calling `context.pushData`, we want to replace that with `process.send` instead.

But why?

Since we use child processes, and each worker process has its own storage space, calling `context.pushData` will not work as we want it to work. Instead, we need to send the data back to the parent process, which has the context where we want to store the data.

This might not be needed depending on your use case! You'll need to experiment and see what works best for you

src/routes.mjs

```
// This replaces the request.label === DETAIL branch of the if clause.
router.addHandler('DETAIL', async ({ request, page, log }) => {
    log.debug(`Extracting data: ${request.url}`);
    const urlPart = request.url.split('/').slice(-1); // ['sennheiser-mke-440-professional-stereo-shotgun-microphone-mke-440']
    const manufacturer = urlPart[0].split('-')[0]; // 'sennheiser'

    const title = await page.locator('.product-meta h1').textContent();
    const sku = await page.locator('span.product-meta__sku-number').textContent();

    const priceElement = page
        .locator('span.price')
        .filter({
            hasText: '$',
        })
        .first();

    const currentPriceString = await priceElement.textContent();
    const rawPrice = currentPriceString.split('$')[1];
    const price = Number(rawPrice.replaceAll(',', ''));

    const inStockElement = page
        .locator('span.product-form__inventory')
        .filter({
            hasText: 'In stock',
        })
        .first();

    const inStock = (await inStockElement.count()) > 0;

    const results = {
        url: request.url,
        manufacturer,
        title,
        sku,
        currentPrice: price,
        availableInStock: inStock,
    };

    log.debug(`Saving data: ${request.url}`);

    // Send the data to the parent process
    // Depending on how you build your crawler, this line could instead be something like `context.pushData()`! Experiment, and see what you can build
    process.send(results);
});
```

There is a lot of code, so let's break it down:

#### The `if` check for `process.env.IS_WORKER_THREAD`[​](#the-if-check-for-processenvis_worker_thread "Direct link to the-if-check-for-processenvis_worker_thread")

This will check how the script is executed as. If this value has *any* value, it will assume it's meant to start scraping. If not, it's considered the **parent** process and will fork copies of itself to do the scraping.

#### Why do we create a Promise per worker process?[​](#why-do-we-create-a-promise-per-worker-process "Direct link to Why do we create a Promise per worker process?")

We use this to ensure the parent process stays alive until all the worker processes exit. Otherwise, the worker processes would just get spawned, and lose the ability to communicate with the parent. You might not need this depending on your use case (maybe you just need to spawn workers and let them process).

#### What's with all those `Configuration` calls?[​](#whats-with-all-those-configuration-calls "Direct link to whats-with-all-those-configuration-calls")

There are three steps we want to do for the worker processes:

* ensure the default storages do **not** get purged on start, as otherwise we'd lose the queue we prepared
* get the queue that supports locking from the same location as the parent process
* initialize a special storage for worker processes so they do not collide with each other

In order, that's what these lines do:

src/parallel-scraper.mjs

```
// Disable the automatic purge on start (step 1)
// This is needed when running locally, as otherwise multiple processes will try to clear the default storage (and that will cause clashes)
Configuration.set('purgeOnStart', false);

// Get the request queue from the parent process (step 2)
const requestQueue = await getOrInitQueue(false);

// Configure crawlee to store the worker-specific data in a separate directory (needs to be done AFTER the queue is initialized when running locally) (step 3)
const config = new Configuration({
    storageClientOptions: {
        localDataDirectory: `./storage/worker-${process.env.WORKER_INDEX}`,
    },
});
```

#### Enabling the request locking experiment, and telling the crawler to use the worker configuration[​](#enabling-the-request-locking-experiment-and-telling-the-crawler-to-use-the-worker-configuration "Direct link to Enabling the request locking experiment, and telling the crawler to use the worker configuration")

You might have noticed several lines highlighted in the code above. Those show how you can enable the request locking experiment, as well as how you provide the request queue to the crawler. You can read more about the experiment by visiting the [request locking experiment](https://crawlee.dev/js/docs/experiments/experiments-request-locking.md) page.

You might have also noticed we passed in a second parameter to the constructor of the crawler, the `config` variable we created earlier. This is needed to ensure the crawler uses the worker-specific storages for internal states, and that they do not collide with each other.

#### Why do we use `process.send` instead of `context.pushData`?[​](#why-do-we-use-processsend-instead-of-contextpushdata "Direct link to why-do-we-use-processsend-instead-of-contextpushdata")

Since we use child processes, and each worker process has its own storage space, calling `context.pushData` will not work as we want it to work (each worker would just push to its own personal dataset that is considered the "default" one). Instead, we need to send the data back to the parent process, which has the dataset where we want to store the data, in a centralized place.

Why don't we apply the same logic we did to the request queue to the dataset?

This is a very valid question, but it has a simple answer: since each process tracks its own internal state of how a dataset looks like (when we are scrapping locally), the worker processes would get out of sync real fast and would either miss or override data. This is why we need to send the data back to the parent process, which has the dataset where we want to store the data, in a centralized place.

Depending on your crawler, this might not be an issue! Each use case has its own quirks, but this is something you should keep in mind when building your scraper.

#### Why did we limit the maximum concurrency to `5`?[​](#why-did-we-limit-the-maximum-concurrency-to-5 "Direct link to why-did-we-limit-the-maximum-concurrency-to-5")

This question has a two-fold answer:

* we don't want to overload the target website with requests, so we limit the number of concurrent requests to a reasonable number per worker process
* we don't want to overload the machine that is running the scraper

This circles back to the initial paragraph about whether you should parallelize your scraper or not.

## Other questions[​](#other-questions "Direct link to Other questions")

#### Couldn't the `initial-scraper` be merged into the `parallel-scraper`?[​](#couldnt-the-initial-scraper-be-merged-into-the-parallel-scraper "Direct link to couldnt-the-initial-scraper-be-merged-into-the-parallel-scraper")

Technically, it could! Nothing stops you from first enqueuing all the URLs in the parent process, and then run the worker process logic after to scrape them. We separated them so it's easier to follow and understand what each part does, but you can merge them if you want to.

#### Will I benefit from this if I run XYZ scraper / want to scrape XYZ website?[​](#will-i-benefit-from-this-if-i-run-xyz-scraper--want-to-scrape-xyz-website "Direct link to Will I benefit from this if I run XYZ scraper / want to scrape XYZ website?")

We don't know! 🤷

What we do know is that first, you should build your scraper to work as a single scraper, then monitor its performance. Do you see it being too slow? Do you scrape many pages, or do the few pages you scrape take a long time to load? If so, then you might benefit from parallelization. When in doubt, follow the list of things to consider before parallelizing at the start of this guide.
