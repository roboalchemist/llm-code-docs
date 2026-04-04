# Source: https://scrapfly.io/docs/sdk/typescript

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/sdk/typescript

Markdown Content:
Typescript SDK
--------------

Typescript SDK is the easiest way to access Scrapfly API in **Typescript, Javascript and NodeJS**.

It provides a client that streamlines the scraping process by:

*   Handling common errors
*   Automatically encoding and decoding sensitive API parameters
*   Handling and simplifying concurrency
*   Implementing CSS selector engine for result HTML

> For more on Typescript SDK use with Scrapfly, select "Typescript SDK" option in Scrapfly docs top bar.

### Step by Step Introduction

For a hands-on introduction and example projects see our Scrapfly SDK introduction page!

[Discover Now](https://scrapfly.io/docs/onboarding/typescript)

[Installation](https://scrapfly.io/docs/sdk/typescript#installation)
--------------------------------------------------------------------

Source code of Typescript SDK is available on [Github](https://github.com/scrapfly/typescript-scrapfly) and the **scrapfly-sdk** package is available in all Javascript and Typescript runtimes:

*   [Deno](https://scrapfly.io/docs/sdk/typescript#deno)
*   [Bun](https://scrapfly.io/docs/sdk/typescript#bun)
*   [NodeJS](https://scrapfly.io/docs/sdk/typescript#nodejs)
*   [Serverless](https://scrapfly.io/docs/sdk/typescript#serverless)

[Deno](https://deno.com/) is a modern and secure runtime for JavaScript and TypeScript that uses V8 and is built in Rust. It's incredibly easy to use and runs Typescript natively as well as being backwards compatible with NodeJS. This makes Deno a great option for web-scraping related development.

To setup Scrapfly SDK with Deno, first install the SDK through [jsr.io package index](https://jsr.io/@scrapfly/scrapfly-sdk):

`$ deno add jsr:@scrapfly/scrapfly-sdk`

Try out the following code snippet for Web Scraping API to get started:

```
import {
  ScrapflyClient, ScrapeConfig,
} from 'jsr:@scrapfly/scrapfly-sdk';

const client = new ScrapflyClient({ key: "" });

let scrape_result = await client.scrape(
  new ScrapeConfig({
    url: 'https://httpbin.dev/html',
  }),
);
console.log(scrape_result.result.log_url);
console.log(scrape_result.result.content);
```

[Bun](https://bun.sh/) is a modern runtime for JavaScript and TypeScript that is fully interchangeable with NodeJS. It's incredibly easy to use and runs Typescript natively which makes it a great option for web-scraping related development.

To setup Scrapfly SDK with Bun, first install the SDK through [jsr.io package index](https://jsr.io/@scrapfly/scrapfly-sdk):

`$ bunx jsr add @scrapfly/scrapfly-sdk`

Try out the following code snippet for Web Scraping API to get started:

```
import {
  ScrapflyClient, ScrapeConfig,
} from '@scrapfly/scrapfly-sdk';

const client = new ScrapflyClient({ key: "" });

let scrape_result = await client.scrape(
  new ScrapeConfig({
    url: 'https://httpbin.dev/html',
  }),
);
console.log(scrape_result.result.log_url);
console.log(scrape_result.result.content);
```

[NodeJS](https://bun.sh/) is the classic Javascript server runtime and is supported by the SDK through both CommonJS and ESM modules.

To setup Scrapfly SDK with Node, first install the SDK through [NPM package index](https://www.npmjs.com/package/scrapfly-sdk):

`$ npm install scrapfly-sdk`

Try out the following code snippet for Web Scraping API to get started:

```
import {
  ScrapflyClient, ScrapeConfig, ScreenshotConfig, ExtractionConfig
} from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "" });

let scrape_result = await client.scrape(
  new ScrapeConfig({
    url: 'https://httpbin.dev/html',
  }),
);

console.log(scrape_result.result.log_url);
console.log(scrape_result.result.content);
```

Serverless platforms like Cloudflare Workers, AWS Lambda etc. are also supported by Scrapfly SDK.

Most serverless platforms can run full NodeJS, Python or other runtimes though there are a few exceptions and differences in runtime implementations.

For the best experience see our recommended use through Denoflare 👇

[Quick Use](https://scrapfly.io/docs/sdk/typescript#quick-use)
--------------------------------------------------------------

Here's a quick preview of what Typescript SDK can do:

```
import { ScrapflyClient, ScrapeConfig, ScrapeResult, log } from "scrapfly-sdk";
// Optional: set log level to debug to see all details
log.setLevel("DEBUG");

// 1. Create a scrapfly client with your API key
const scrapfly = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" })
// 2. Start scraping!
const result: ScrapeResult = await scrapfly.scrape(new ScrapeConfig({
  url: "https://web-scraping.dev/product/1",
  // optional configuration:
  asp: true,  // enable scraper blocking bypass
  country: "US", // set proxy country
  render_js: true,  // enable headless web browser
  // ... and much more
}))
// 3. access scraped result data
console.log(result.result.content);
// 3.1 and even process it with CSS selectors:
console.log(result.selector("h3").text())
```

In short, we first create a `ScrapflyClient` object with our scrapfly key. Then, we can use the `.scrape()` method to issue our scraping commands which are defined by `ScrapeConfig` object.

The returned `ScrapeResult` object contains result data (like page HTML), request metadata and convenience extensions like CSS selector engine `.selector()` which can further parse the HTML result to specific details.

[Configuring Scrape](https://scrapfly.io/docs/sdk/typescript#scrape_config)
---------------------------------------------------------------------------

The SDK supports all features of Scrapfly API, which can be configured through `ScrapeConfig` object:

> For scraping websites protected against web scraping **make sure to enable [Anti Scraping Protection bypass](https://scrapfly.io/docs/onboarding#asp)**using `asp: true`option.

```
const result: ScrapeResult = await scrapfly.scrape(new ScrapeConfig({
  url: "https://web-scraping.dev/product/1",
  // Request details
  method: "GET",  // GET, POST, PUT etc.
  headers: {
      "X-Csrf-Token": "1234",
  },

  // enable scraper blocking bypass (recommended)
  asp: true,
  // set proxy countries
  country: "US,CA,FR",

  // enable cache (recommended when developing)
  cache: true,
  cache_ttl: 3600,  // expire cache in 1 hour (default 24h)
  // enable debug to see more details in scrapfly web dashboard
  debug: true,

  // enable javascript rendering
  render_js: true,
  // wait for element to load when using js rendering:
  wait_for_selector: ".review",
  // or explicit amount of time
  rendering_wait: 5000,  // 5 seconds
  // run custom javascript code
  js: "return document.title",
  // scroll to the bottom of the page (for loading details)
  auto_scroll: true,
  // ...
}))
```

For more on available options see [API specification](https://scrapfly.io/docs/scrape-api/getting-started#spec) which is matched in the SDK where applicable.

[Handling Result](https://scrapfly.io/docs/sdk/typescript#scrape_config)
------------------------------------------------------------------------

The `ScrapeResult` object contains all data returned by Scrapfly API such as response data, api use information, scrape metadata and more:

```
const apiResult: ScrapeResult = await scrapfly.scrape(new ScrapeConfig({
  url: "https://web-scraping.dev/product/1",
}))
// get response body (HTML) and status code:
apiResult.result.content
apiResult.result.status_code
// response headers:
apiResult.result.response_headers
// log url for accessing this scrape in scrapfly dashboard:
apiResult.result.log_url

// if render_js is used then browser context is available as well
// get data from javascript execution:
apiResult.result.browser_data.javascript_evaluation_result
// javascript scenario apiResults:
apiResult.result.browser_data.js_scenario
```

[Concurrent Scraping](https://scrapfly.io/docs/sdk/typescript#scrape_config)
----------------------------------------------------------------------------

The main scraping method `.scrape()` is asynchronous meaning it can be used in javascript idioms like `Promise.all()` and `.then()` callbacks. Additionally, the SDK provides `.concurrentScrape()` async generator that can be used to concurrently scrape at your scrapfly plan's concurrency limit:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';
const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const configs = [
    // these two will succeed:
    ...new Array(2).fill(null).map(() => new ScrapeConfig({ url: 'https://httpbin.dev/status/200' })),
    // these two will fail:
    ...new Array(2).fill(null).map(() => new ScrapeConfig({ url: 'https://httpbin.dev/status/403' })),
];
const results = [];
const errors = [];
for await (const resultOrError of client.concurrentScrape(configs)) {
    if (resultOrError instanceof Error) {
        errors.push(resultOrError);
    } else {
        results.push(resultOrError);
    }
}
console.log(`got ${results.length} results:`);
console.log(results);
console.log(`got ${errors.length} errors:`);
console.log(errors);
```

[Getting Account Details](https://scrapfly.io/docs/sdk/typescript#example-account)
----------------------------------------------------------------------------------

To access Scrapfly account information the `.account()` method can be used:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
console.log(await client.account());
```

[Examples](https://scrapfly.io/docs/sdk/typescript#examples)
------------------------------------------------------------

To provide additional headers, use `headers` option of `ScrapeConfig`. Note that when using `asp=True` Scrapfly can add additional headers automatically to prevent scraper blocking.

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
  new ScrapeConfig({
      url: 'https://httpbin.dev/headers',
      headers: { 'X-My-Header': 'foo' },
  }),
);
console.log(JSON.parse(result.result.content));
```

### [Post Form](https://scrapfly.io/docs/sdk/typescript#example-post-form)

To post FormData, use `data` option:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
  new ScrapeConfig({
      url: 'https://httpbin.dev/post',
      method: 'POST',
      data: { foo: 'bar' },
  }),
);
console.log(JSON.parse(result.result.content));
```

### [Post JSON](https://scrapfly.io/docs/sdk/typescript#example-post-json)

To post JSON data, use `data` option with a `'Content-Type':'application/json'` header in `ScrapeConfig`:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
    new ScrapeConfig({
        url: 'https://httpbin.dev/post',
        // set method to POST
        method: 'POST',
        // set appropriate header
        headers: { 'content-type': 'application/json' },
        data: { foo: 'bar' },
    }),
);
console.log(JSON.parse(result.result.content));
```

### [Javascript Rendering](https://scrapfly.io/docs/sdk/typescript#example-javascript-rendering)

To render pages using headless browsers using [Javascript Rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering#spec) feature use `render_js=true` option of `ScrapeConfig`:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
    new ScrapeConfig({
        url: 'https://web-scraping.dev/product/1',
        render_js: true,
        // additionally we can wait for specific element to appear on the page:
        wait_for_selector: '.review',
        // or wait for a set amount of time:
        wait_for: 5000,  // seconds
    }),
);
console.log(JSON.parse(result.result.content));
```

### [Javascript Scenario](https://scrapfly.io/docs/sdk/typescript#example-javascript-scenario)

To execute [Javascript Scenario](https://scrapfly.io/docs/scrape-api/javascript-scenario) use `scenario` option of `ScrapeConfig`:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
    new ScrapeConfig({
        url: 'https://web-scraping.dev/product/1',
        debug: true,
        // js rendering has to be enabled!
        render_js: true,
        // scenario is an array of actions listed in the docs:
        // https://scrapfly.io/docs/scrape-api/javascript-scenario
        js_scenario: [
            // wait for reviews to load on the page
            { wait_for_selector: { selector: '.review' } },
            // retrieve browser's user agent
            { execute: { script: 'return navigator.userAgent' } },
            // click load more reviews button
            { click: { selector: '#load-more-reviews' } },
            // wait for more reviews to load
            { wait_for_navigation: {} },
            // retrieve all reviews using javascript DOM parser:
            {
                execute: {
                    script: "[...document.querySelectorAll('.review p')].map(p=>p.outerText)",
                },
            },
        ],
    }),
);
console.log(result.result.browser_data.js_scenario);
```

### [Capturing Screenshots](https://scrapfly.io/docs/sdk/typescript#example-screeenshots)

To capture screenshots `render_js=true` and `screenshots` options of `ScrapeConfig` can be used:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
    new ScrapeConfig({
        url: 'https://web-scraping.dev/product/1',
        // enable headless browsers for screenshots
        render_js: true,
        // optional: you can wait for page to load before capturing
        wait_for_selector: '.review',
        screenshots: {
            // name: what-to-capture
            // fullpage - will capture everything
            // css selector (e.g. #reviews) - will capture just that element
            everything: 'fullpage',
            reviews: '#reviews',
        },
    }),
);
console.log(result.result.screenshots);
/*
{
  everything: {
    css_selector: null,
    extension: 'jpg',
    format: 'fullpage',
    size: 63803,
    url: 'https://api.scrapfly.io/scrape/screenshot/01H5S96DFN48V5RH32ZM9WM8WQ/everything'
  },
  reviews: {
    css_selector: '#reviews',
    extension: 'jpg',
    format: 'element',
    size: 12602,
    url: 'https://api.scrapfly.io/scrape/screenshot/01H5S96DFN48V5RH32ZM9WM8WQ/reviews'
  }
}
*/

// To save a screenshot to a file you can download the screenshot from the result URLs
import axios from 'axios';
import fs from 'fs';
for (let [name, screenshot] of Object.entries(result.result.screenshots)) {
    let response = await axios.get(screenshot.url, {
        // note: don't forget to add your API key parameter:
        params: { key: key },
        // this indicates that response is binary data:
        responseType: 'arraybuffer',
    });
    // write to screenshot data to a file in current directory:
    fs.writeFileSync(`example-screenshot-${name}.${screenshot.extension}`, response.data);
}
```

### [Scraping Binary Data](https://scrapfly.io/docs/sdk/typescript#example-screeenshots)

Binary data can be scraped like any other page however it's returned **b64 encoded**. To decode it, the `Buffer.from()` method can be used:

```
import { ScrapflyClient, ScrapeConfig } from 'scrapfly-sdk';
import fs from "fs";

const client = new ScrapflyClient({ key: "{{ YOUR_API_KEY }}" });
const result = await client.scrape(
    new ScrapeConfig({
        url: 'https://web-scraping.dev/assets/products/orange-chocolate-box-small-1.png',
    }),
);
const data = Buffer.from(result.result.content, 'base64');
fs.writeFileSync("image.png", data);
```
