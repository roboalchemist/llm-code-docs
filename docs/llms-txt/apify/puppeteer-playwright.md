# Source: https://docs.apify.com/academy/puppeteer-playwright.md

# Puppeteer and Playwright course

**Learn in-depth how to use two of the most popular Node.js libraries for controlling a headless browser - Puppeteer and Playwright.**

***

https://pptr.dev/ and https://playwright.dev/ are libraries that allow you to automate browsing. Based on your instructions, they can open a browser window, load a website, click on links, etc. They can also do this *headlessly*, i.e., in a way that the browser window isn't visible, which is faster.

Both packages were developed by the same team and are very similar, which is why we have combined the Puppeteer course and the Playwright course into one super-course that shows code examples for both technologies. The two differ in only small ways, and those will always be highlighted in the examples.

> Each lesson's activity will contain examples for both libraries, but we recommend using Playwright, as it is newer and has more features and better https://playwright.dev/docs/intro

## Advantages of using a headless browser

When automating a headless browser, you can do a whole lot more in comparison to making HTTP requests for static content. In fact, you can programmatically do pretty much anything a human could do with a browser, such as clicking elements, taking screenshots, typing into text areas, etc.

Additionally, since the requests aren't static, https://docs.apify.com/academy/concepts/dynamic-pages.md can be rendered and interacted with (or, data from the dynamic content can be scraped). Turn on the https://playwright.dev/docs/api/class-testoptions#test-options-headless (`headless: false`) to see exactly what the browser is doing.

Browsers can also be effective for https://docs.apify.com/academy/anti-scraping.md, especially if the website is running https://docs.apify.com/academy/anti-scraping/techniques/browser-challenges.md.

## Disadvantages of headless browsers

Browsers are slow and expensive to run. In the follow-up courses, the Apify Academy will show you how to scrape websites without a browser. Every website can potentially be reverse-engineered into a series of quick and cheap HTTP calls, but it might require significant effort and specialized knowledge.

## Setup

For this course, we'll be jumping right into the features of these awesome libraries and expecting you to already have an environment set up. Here's how we set up our environment:

1. Make sure you've installed https://nodejs.org/en/
2. Create a new folder called **puppeteer-playwright** (or whatever you want to call it)
3. Run the command `npm init -y` within your new folder to automatically initialize the project
4. Add `"type": "module"` to the **package.json** file
5. Create a new file named **index.js**
6. Install the library you're going to be using during this course:

* Install Playwright
* Install Puppeteer


```
npm install playwright
```



```
npm install puppeteer
```


> For a more in-depth guide on how to set up the basic environment we'll be using in this tutorial, check out the https://docs.apify.com/academy/web-scraping-for-beginners/data-extraction/computer-preparation.md lesson in the **Web scraping basics for JavaScript devs** course

## Course overview

1. https://docs.apify.com/academy/puppeteer-playwright/browser.md

2. https://docs.apify.com/academy/puppeteer-playwright/page.md

   * https://docs.apify.com/academy/puppeteer-playwright/page/interacting-with-a-page.md
   * https://docs.apify.com/academy/puppeteer-playwright/page/waiting.md
   * https://docs.apify.com/academy/puppeteer-playwright/page/page-methods.md

3. https://docs.apify.com/academy/puppeteer-playwright/executing-scripts.md

   * https://docs.apify.com/academy/puppeteer-playwright/executing-scripts/injecting-code.md
   * https://docs.apify.com/academy/puppeteer-playwright/executing-scripts/collecting-data.md

4. https://docs.apify.com/academy/puppeteer-playwright/reading-intercepting-requests.md

5. https://docs.apify.com/academy/puppeteer-playwright/proxies.md

6. https://docs.apify.com/academy/puppeteer-playwright/browser-contexts.md

7. https://docs.apify.com/academy/puppeteer-playwright/common-use-cases.md

## First up

In the https://docs.apify.com/academy/puppeteer-playwright/browser.md of this course, we'll be learning a bit about how to create and use the **Browser** object.
