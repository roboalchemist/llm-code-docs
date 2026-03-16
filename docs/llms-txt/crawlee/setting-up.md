# Source: https://crawlee.dev/js/docs/introduction/setting-up.md

# Setting up

Copy for LLM

To run Crawlee on your own computer, you need to meet the following pre-requisites first:

1. Have **Node.js version 16.0** (Visit [Node.js website](https://nodejs.org/en/download/) to download or use [fnm](https://github.com/Schniz/fnm)) or higher installed.
2. Have **NPM** installed, or use other package manager of your choice.

If not certain, confirm the prerequisites by running:

```
node -v
```

```
npm -v
```

## Creating a new project[​](#creating-a-new-project "Direct link to Creating a new project")

The fastest and best way to create new projects with Crawlee is to use the [Crawlee CLI](https://www.npmjs.com/package/@crawlee/cli). You can use the `npx` utility to download and run the CLI - it is embedded in the `crawlee` package:

```
npx crawlee create my-crawler
```

A prompt will be shown, asking you to select a template. Crawlee is written in TypeScript so if you're familiar with it, choosing a TypeScript template will give you better code completion and static type checking, but feel free to use JavaScript as well. Functionally they're identical.

Let's choose the first template called **Getting started example**. The command will create a new directory in your current working directory, called **my-crawler**, add a **package.json** to this folder and install all the necessary dependencies. It will also add example source code that you can immediately run.

Let's try that!

```
cd my-crawler
npm start
```

You will see log messages in the terminal as Crawlee boots up and starts scraping the Crawlee website.

```
INFO  PlaywrightCrawler: Starting the crawl
INFO  PlaywrightCrawler: Title of https://crawlee.dev/ is 'Crawlee · Build reliable crawlers. Fast. | Crawlee'
INFO  PlaywrightCrawler: Title of https://crawlee.dev/js/docs/examples is 'Examples | Crawlee'
INFO  PlaywrightCrawler: Title of https://crawlee.dev/js/api/core is '@crawlee/core | API | Crawlee'
INFO  PlaywrightCrawler: Title of https://crawlee.dev/js/api/core/changelog is 'Changelog | API | Crawlee'
INFO  PlaywrightCrawler: Title of https://crawlee.dev/js/docs/quick-start is 'Quick Start | Crawlee'
```

You can always terminate the crawl with a keypress in the terminal:

```
CTRL+C
```

### Running headful browsers[​](#running-headful-browsers "Direct link to Running headful browsers")

Browsers controlled by Playwright run headless (without a visible window). You can switch to headful by uncommenting the `headless: false` option in the crawler's constructor. This is useful in the development phase when you want to see what's going on in the browser.

```
// Uncomment this option to see the browser window.
headless: false
```

When you run the example again, after a second a Chromium browser window will open. In the window, you'll see quickly changing pages as the crawler does its job.

note

For the sake of this show off, we've slowed down the crawler, but rest assured, it's blazing fast in real world usage.

![An image showing off Crawlee scraping the Crawlee website using Puppeteer/Playwright and Chromium](/img/chrome-scrape-light.gif)![An image showing off Crawlee scraping the Crawlee website using Puppeteer/Playwright and Chromium](/img/chrome-scrape-dark.gif)

## Next steps[​](#next-steps "Direct link to Next steps")

Next, you will see how to create a very simple crawler and explain Crawlee components while building it.
