# Source: https://crawlee.dev/js/docs/guides/running-in-web-server.md

# Running in web server

Copy for LLM

Most of the time, Crawlee jobs are run as batch jobs. You have a list of URLs you want to scrape every week or you might want to scrape a whole website once per day. After the scrape, you send the data to your warehouse for analytics. Batch jobs are efficient because they can use [Crawlee's built-in autoscaling](https://crawlee.dev/js/docs/guides/scaling-crawlers.md) to fully utilize the resources you have available. But sometimes you have a use-case where you need to return scrape data as soon as possible. There might be a user waiting on the other end so every millisecond counts. This is where running Crawlee in a web server comes in.

We will build a simple HTTP server that receives a page URL and returns the page title in the response. We will base this guide on the approach used in [Apify's Super Scraper API repository](https://github.com/apify/super-scraper) which maps incoming HTTP requests to Crawlee [Request](https://crawlee.dev/js/api/core/class/Request.md).

## Set up a web server[​](#set-up-a-web-server "Direct link to Set up a web server")

There are many popular web server frameworks for Node.js, such as Express, Koa, Fastify, and Hapi but in this guide, we will use the built-in `http` Node.js module to keep things simple.

This will be our core server setup:

```
import { createServer } from 'http';
import { log } from 'crawlee';

const server = createServer(async (req, res) => {
    log.info(`Request received: ${req.method} ${req.url}`);

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    // We will return the page title here later instead
    res.end('Hello World\n');
});

server.listen(3000, () => {
    log.info('Server is listening for user requests');
});
```

## Create the Crawler[​](#create-the-crawler "Direct link to Create the Crawler")

We will create a standard [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md) and use the [`keepAlive: true`](https://crawlee.dev/js/api/cheerio-crawler/interface/CheerioCrawlerOptions.md#keepAlive) option to keep the crawler running even if there are no requests currently in the [Request Queue](https://crawlee.dev/js/api/core/class/RequestQueue.md). This way it will always be waiting for new requests to come in.

```
import { CheerioCrawler, log } from 'crawlee';

const crawler = new CheerioCrawler({
    keepAlive: true,
    requestHandler: async ({ request, $ }) => {
        const title = $('title').text();
        // We will send the response here later
        log.info(`Page title: ${title} on ${request.url}`);
    },
});
```

## Glue it together[​](#glue-it-together "Direct link to Glue it together")

Now we need to glue the server and the crawler together using the mapping of Crawlee Requests to HTTP responses discussed above. The whole program is actually quite simple. For production-grade service, you will need to improve error handling, logging, and monitoring but this is a good starting point.

src/web-server.mjs

```
import { randomUUID } from 'node:crypto';
import { CheerioCrawler, log } from 'crawlee';
import { createServer } from 'http';

// We will bind an HTTP response that we want to send to the Request.uniqueKey
const requestsToResponses = new Map();

const crawler = new CheerioCrawler({
    keepAlive: true,
    requestHandler: async ({ request, $ }) => {
        const title = $('title').text();
        log.info(`Page title: ${title} on ${request.url}, sending response`);

        // We will pick the response from the map and send it to the user
        // We know the response is there with this uniqueKey
        const httpResponse = requestsToResponses.get(request.uniqueKey);
        httpResponse.writeHead(200, { 'Content-Type': 'application/json' });
        httpResponse.end(JSON.stringify({ title }));
        // We can delete the response from the map now to free up memory
        requestsToResponses.delete(request.uniqueKey);
    },
});

const server = createServer(async (req, res) => {
    // We parse the requested URL from the query parameters, e.g. localhost:3000/?url=https://example.com
    const urlObj = new URL(req.url, 'http://localhost:3000');
    const requestedUrl = urlObj.searchParams.get('url');

    log.info(`HTTP request received for ${requestedUrl}, adding to the queue`);
    if (!requestedUrl) {
        log.error('No URL provided as query parameter, returning 400');
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'No URL provided as query parameter' }));
        return;
    }

    // We will add it first to the map and then enqueue it to the crawler that immediately processes it
    // uniqueKey must be random so we process the same URL again
    const crawleeRequest = { url: requestedUrl, uniqueKey: randomUUID() };
    requestsToResponses.set(crawleeRequest.uniqueKey, res);
    await crawler.addRequests([crawleeRequest]);
});

// Now we start the server, the crawler and wait for incoming connections
server.listen(3000, () => {
    log.info('Server is listening for user requests');
});

await crawler.run();
```
