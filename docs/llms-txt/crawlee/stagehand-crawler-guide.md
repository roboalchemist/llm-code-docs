# Source: https://crawlee.dev/js/docs/guides/stagehand-crawler-guide.md

# StagehandCrawler guide

Copy for LLM

​[`StagehandCrawler`](https://crawlee.dev/js/api/stagehand-crawler/class/StagehandCrawler.md) combines Crawlee's powerful crawling infrastructure with [Stagehand's](https://github.com/browserbase/stagehand) AI-powered browser automation. Instead of writing CSS selectors or XPath queries, you can interact with web pages using natural language instructions.

## What is Stagehand[​](#what-is-stagehand "Direct link to What is Stagehand")

[Stagehand](https://github.com/browserbase/stagehand) is an AI-powered browser automation library from Browserbase. It allows you to control a browser using natural language commands like "click the login button" or "extract the product price". Under the hood, Stagehand uses large language models (OpenAI, Anthropic, or Google) to understand the page structure and execute your instructions.

## How StagehandCrawler works[​](#how-stagehandcrawler-works "Direct link to How StagehandCrawler works")

StagehandCrawler extends [`BrowserCrawler`](https://crawlee.dev/js/api/browser-crawler/class/BrowserCrawler.md) and enhances each page with AI-powered methods. Here's the architecture:

1. **Stagehand launches the browser** - When a new browser is needed, Stagehand initializes and launches a Chromium browser
2. **Playwright connects via CDP** - Crawlee connects Playwright to the same browser using Chrome DevTools Protocol (CDP)
3. **Pages are enhanced with AI methods** - Each page gets `act()`, `extract()`, `observe()`, and `agent()` methods
4. **BrowserPool manages scaling** - Crawlee's BrowserPool handles browser lifecycle, retries, and concurrency

```
┌─────────────────────────────────────────────────────────┐
│                    StagehandCrawler                      │
├─────────────────────────────────────────────────────────┤
│  BrowserPool (manages browser lifecycle & concurrency)   │
├─────────────────────────────────────────────────────────┤
│  Stagehand Instance                                      │
│  ├── Launches Chromium browser                          │
│  ├── Provides CDP endpoint                              │
│  └── Handles AI operations (act/extract/observe)        │
├─────────────────────────────────────────────────────────┤
│  Playwright (connected via CDP)                          │
│  └── Standard page operations (goto, click, type, etc.) │
└─────────────────────────────────────────────────────────┘
```

## Key features[​](#key-features "Direct link to Key features")

The enhanced page object provides four AI-powered methods:

### `page.act(instruction)` - Perform actions[​](#pageactinstruction---perform-actions "Direct link to pageactinstruction---perform-actions")

Execute actions on the page using natural language. See [Stagehand act() documentation](https://docs.stagehand.dev/reference/act) for more details.

```
await page.act('Click the "Add to Cart" button');
await page.act('Fill in the email field with test@example.com');
await page.act('Scroll down to load more products');
```

### `page.extract(instruction, schema)` - Extract structured data[​](#pageextractinstruction-schema---extract-structured-data "Direct link to pageextractinstruction-schema---extract-structured-data")

Extract data from the page using a Zod schema for type safety. See [Stagehand extract() documentation](https://docs.stagehand.dev/reference/extract) for more details.

```
import { z } from 'zod';

const productSchema = z.object({
    title: z.string(),
    price: z.number(),
    description: z.string(),
});

const product = await page.extract('Get the product details', productSchema);
// product is typed as { title: string, price: number, description: string }
```

### `page.observe()` - Discover page actions[​](#pageobserve---discover-page-actions "Direct link to pageobserve---discover-page-actions")

Analyze the page and get AI-suggested actions. This is useful for exploring unfamiliar pages or building adaptive scrapers. See [Stagehand observe() documentation](https://docs.stagehand.dev/reference/observe) for more details.

```
const actions = await page.observe();
// Returns available actions like:
// [
//   { action: 'click', element: 'Load More button', selector: '.load-more' },
//   { action: 'click', element: 'Next Page link', selector: 'a.pagination-next' },
//   { action: 'fill', element: 'Search input', selector: '#search' },
// ]

// Use observe to find pagination dynamically
for (const action of actions) {
    if (action.element?.toLowerCase().includes('next page')) {
        await page.act(`Click the ${action.element}`);
        break;
    }
}
```

### `page.agent(config)` - Autonomous agents[​](#pageagentconfig---autonomous-agents "Direct link to pageagentconfig---autonomous-agents")

Create an autonomous agent for complex multi-step workflows. Unlike `act()` which executes a single action, `agent()` can plan and execute multiple steps autonomously to achieve a goal. See [Stagehand agent() documentation](https://docs.stagehand.dev/reference/agent) for more details.

```
const agent = page.agent({ model: 'gpt-4.1-mini' });
const result = await agent.execute('Find the cheapest laptop and add it to cart');
```

**When to use `act()` vs `agent()`:**

* Use `act()` for single, discrete actions ("click this button", "fill this form")
* Use `agent()` for goals requiring multiple steps with decision-making ("find and purchase the cheapest item")

Note that `agent()` makes multiple LLM calls and can be slower and more expensive than sequential `act()` calls where you control the flow.

## Requirements[​](#requirements "Direct link to Requirements")

StagehandCrawler requires an API key for the AI model provider. The recommended way is to use the `apiKey` option:

```
const crawler = new StagehandCrawler({
    stagehandOptions: {
        model: 'openai/gpt-4.1-mini',
        apiKey: 'sk-...', // Your OpenAI API key
    },
});
```

Alternatively, you can use environment variables (used as fallback when `apiKey` is not provided):

* **OpenAI**: `OPENAI_API_KEY`
* **Anthropic**: `ANTHROPIC_API_KEY`
* **Google**: `GOOGLE_API_KEY`

## Limitations[​](#limitations "Direct link to Limitations")

Some Crawlee features work differently or are unavailable with StagehandCrawler:

### Chromium only[​](#chromium-only "Direct link to Chromium only")

Stagehand uses Chrome DevTools Protocol (CDP), so only Chromium browsers are supported. The `launcher` option is ignored - you cannot use Firefox or WebKit.

### Reduced fingerprinting control[​](#reduced-fingerprinting-control "Direct link to Reduced fingerprinting control")

Since Stagehand controls the browser launch process, Crawlee's advanced fingerprinting features are limited:

* **Browser fingerprints** - Basic fingerprinting (viewport, user-agent) is applied, but low-level browser properties cannot be modified
* **`launchOptions`** - Only a subset of Playwright launch options are passed through to Stagehand (`headless`, `args`, `executablePath`, `proxy`, `viewport`)
* **Browser context options** - Custom context configurations are not fully supported since Stagehand manages the browser context

Stagehand provides its own anti-detection measures, but you have less granular control compared to PlaywrightCrawler.

## When to use StagehandCrawler[​](#when-to-use-stagehandcrawler "Direct link to When to use StagehandCrawler")

**Use StagehandCrawler when:**

* Pages have complex, dynamic structures that are hard to scrape with selectors
* You need to interact with pages in ways that are difficult to express programmatically
* You want to quickly prototype scrapers without writing detailed selectors
* The target website frequently changes its structure

**Consider alternatives when:**

* You need maximum performance (use CheerioCrawler or PlaywrightCrawler)
* You need to minimize costs (LLM API calls add up)
* You need fine-grained browser control (use PlaywrightCrawler)
* You need Firefox or WebKit support (use PlaywrightCrawler)

## Basic example[​](#basic-example "Direct link to Basic example")

Here's a simple example that extracts code examples from the Crawlee website:

src/main.ts

```
import { StagehandCrawler } from '@crawlee/stagehand';
import { z } from 'zod';

const crawler = new StagehandCrawler({
    stagehandOptions: {
        env: 'LOCAL',
        model: 'openai/gpt-4.1-mini',
        verbose: 1,
    },
    async requestHandler({ page, request, log, pushData }) {
        log.info(`Processing ${request.url}`);

        // Use AI to extract the page title
        const title = await page.extract('Get the main heading of the page', z.string());

        // Use AI to click on a navigation element
        await page.act('Click on the Documentation link');

        // Extract structured data after navigation
        const navItems = await page.extract('Get all sidebar navigation items', z.array(z.string()));

        log.info(`Found ${navItems.length} navigation items`);

        await pushData({
            url: request.url,
            title,
            navItems,
        });
    },
});

await crawler.run(['https://crawlee.dev']);
```

## Data extraction example[​](#data-extraction-example "Direct link to Data extraction example")

Here's an example showing structured data extraction with Zod schemas:

src/main.ts

```
import { StagehandCrawler, Dataset } from '@crawlee/stagehand';
import { z } from 'zod';

// Define a schema for the data you want to extract
const ProductSchema = z.object({
    name: z.string(),
    price: z.number(),
    description: z.string(),
    inStock: z.boolean(),
});

const ProductListSchema = z.object({
    products: z.array(ProductSchema),
    totalCount: z.number(),
});

const crawler = new StagehandCrawler({
    stagehandOptions: {
        env: 'LOCAL',
        model: 'anthropic/claude-sonnet-4-20250514',
        verbose: 1,
    },
    maxRequestsPerCrawl: 10,
    async requestHandler({ page, request, log, enqueueLinks }) {
        log.info(`Scraping ${request.url}`);

        // Extract structured product data using AI
        const data = await page.extract(
            'Extract all products from this page including their names, prices, descriptions, and availability',
            ProductListSchema,
        );

        log.info(`Found ${data.products.length} products`);

        // Save each product to the dataset
        for (const product of data.products) {
            await Dataset.pushData({
                ...product,
                url: request.url,
                scrapedAt: new Date().toISOString(),
            });
        }

        // Use AI to find and click "Next page" if it exists
        try {
            await page.act('Click the next page button if available');
            // Enqueue the new URL after navigation
            await enqueueLinks({
                strategy: 'same-domain',
            });
        } catch {
            log.info('No more pages to scrape');
        }
    },
});

await crawler.run(['https://example-shop.com/products']);
```

## Configuration options[​](#configuration-options "Direct link to Configuration options")

### Stagehand options[​](#stagehand-options "Direct link to Stagehand options")

Configure the AI behavior through `stagehandOptions`:

```
const crawler = new StagehandCrawler({
    stagehandOptions: {
        // Environment: 'LOCAL' or 'BROWSERBASE'
        env: 'LOCAL',

        // AI model to use (e.g., 'openai/gpt-4.1-mini', 'anthropic/claude-sonnet-4-20250514')
        model: 'openai/gpt-4.1-mini',

        // API key for the LLM provider (can be overridden by environment variables)
        apiKey: process.env.OPENAI_API_KEY,

        // Logging verbosity: 0 (minimal), 1 (standard), 2 (debug)
        verbose: 1,

        // Enable automatic error recovery
        selfHeal: true,

        // Timeout for DOM to stabilize (ms)
        domSettleTimeout: 30000,
    },
});
```

### Environment variables[​](#environment-variables "Direct link to Environment variables")

Stagehand options can alternatively be set via environment variables. Programmatic options always take precedence over environment variables:

| Environment variable   | Option      | Notes                         |
| ---------------------- | ----------- | ----------------------------- |
| `OPENAI_API_KEY`       | `apiKey`    | Fallback for OpenAI models    |
| `ANTHROPIC_API_KEY`    | `apiKey`    | Fallback for Anthropic models |
| `GOOGLE_API_KEY`       | `apiKey`    | Fallback for Google models    |
| `STAGEHAND_ENV`        | `env`       |                               |
| `STAGEHAND_MODEL`      | `model`     |                               |
| `STAGEHAND_VERBOSE`    | `verbose`   |                               |
| `STAGEHAND_API_KEY`    | `apiKey`    | Browserbase API key           |
| `STAGEHAND_PROJECT_ID` | `projectId` | Browserbase project ID        |

## Using with Browserbase[​](#using-with-browserbase "Direct link to Using with Browserbase")

For cloud browser infrastructure, you can use [Browserbase](https://browserbase.com/):

```
const crawler = new StagehandCrawler({
    stagehandOptions: {
        env: 'BROWSERBASE',
        apiKey: process.env.BROWSERBASE_API_KEY,
        projectId: process.env.BROWSERBASE_PROJECT_ID,
        model: 'openai/gpt-4.1-mini',
    },
});
```

## Combining AI and standard methods[​](#combining-ai-and-standard-methods "Direct link to Combining AI and standard methods")

You can mix AI-powered methods with standard Playwright methods:

src/main.ts

```
import { StagehandCrawler } from '@crawlee/stagehand';
import { z } from 'zod';

const crawler = new StagehandCrawler({
    stagehandOptions: {
        model: 'openai/gpt-4.1-mini',
    },
    async requestHandler({ page, request, log, pushData }) {
        // Use standard Playwright navigation
        await page.goto(request.url);

        // Use AI to interact with the page
        await page.act('Accept the cookie consent banner');

        // Use standard Playwright for precise operations
        await page.waitForSelector('.product-list');

        // Use AI for complex extraction
        const products = await page.extract(
            'Get all product names and prices',
            z.array(
                z.object({
                    name: z.string(),
                    price: z.number(),
                }),
            ),
        );

        log.info(`Extracted ${products.length} products`);

        // Use standard Playwright for screenshots
        await page.screenshot({ path: 'products.png' });

        await pushData({ url: request.url, products });
    },
});

await crawler.run(['https://example.com/products']);
```

## Further reading[​](#further-reading "Direct link to Further reading")

* [Stagehand documentation](https://docs.stagehand.dev/)
* [Browserbase documentation](https://docs.browserbase.com/)
* [`StagehandCrawler` API reference](https://crawlee.dev/js/api/stagehand-crawler/class/StagehandCrawler.md)
