# Source: https://checklyhq.com/docs/learn/playwright/navigation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Use Playwright to Navigate and Interact with Web Pages

> Learn how to navigate web pages and implement effective waiting mechanisms. A guide ideal for developers looking to refine their automation scripts.

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Every script that we will write will almost certainly do three key things:

1. Navigating to some web page
2. Waiting for something
3. Possibly getting a timeout 😐

## Navigating

Initial navigation to any page can happen in multiple ways.

* Whenever your code does a `page.goto()`, or a `page.click()` on a link, you explicitly trigger a navigation.
* The webpage you are on can also trigger a navigation by executing `location.href= 'https://example.com'` or using the
  `history.pushState()` API.

In the example below we trigger two navigations:

1. The initial load of the page.
2. A navigation to the shopping cart by clicking a link

```ts basic-browser-navigation.spec.ts theme={null}
import { test } from '@playwright/test'

test('basic navigation', async ({ page }) => {
  await page.goto('https://danube-web.shop/')
  await page.click('#cart')
})

```

Run this example as follows:

```bash  theme={null}
npx playwright test basic-browser-navigation.spec.ts
```

## Waiting

Waiting for something to happen is a crucial part of any automation script. In most cases, this is handled automatically
by Playwright. For example, when you click a button, Playwright will wait for that button to be clickable before it actually clicks it.

In the example below, we type an email address into an input field on a login modal. Playwright's `fill` method comes with
built-in waiting functionality.

```ts basic-browser-waiting.spec.ts theme={null}
import { test } from '@playwright/test'

test('basic built-in waiting', async ({ page }) => {
  await page.goto('https://danube-web.shop/')
  await page.getByRole('button', { name: 'Log in' }).click()
  await page.getByPlaceholder('Email').click()
  await page.getByPlaceholder('Email').fill('test@test.com')
})

```

Run this example as follows:

```bash  theme={null}
npx playwright test basic-browser-waiting.spec.ts
```

Playwright actions perform so-called [actionability checks](https://playwright.dev/docs/actionability#introduction) before interacting with DOM elements.

If you call `click()` on a locator, Playwright will ensure that:

* your locator resolves to exactly one element.
* the matching element is visible.
* the matching element is stable.
* the matching element can receive events and is not covered or obscured by other elements.
* the matching element is enabled.

Playwright's auto-waiting and actionability checks allow you to focus on the end-to-end test flow without worrying when and if elements become visible. Playwright evaluates this for you.

## Timeouts

The `page.waitForNavigation()` method — but also similar methods like `page.reload()` and `page.goBack()` — all take some
options that determine "how" it should wait and what the timeout limits are.

These options come in two flavors:

**1. Hard timeout**

The time in milliseconds passed as the `timeout` property e.g.
`page.waitForNavigation({ timeout: 2000 })`. We do not recommend
using this if you do not explicitly need to.

**2a. DOM event based**

These two options are directly related to the events your browser emits when it has reached a certain loading stage.

* `load`: This is the `page.goto()` default and very strict: your whole page including all dependent resources, i.e. images, scripts, css etc.
* `domcontentloaded`: less strict: when your HTML has loaded.

**2b. Heuristic based**

This option is based on the heuristic that if (almost) all network connections your browser has are no longer active,
your page has probably finished loading.

* `networkidle`: consider navigation to be finished when there are no more than 0 network connections for at least 500 ms.

<Warning>Relying on `networkidle` is discouraged because it slows down your end-to-end tests. It's recommended to rely on auto-waiting and application state to evaluate when a page is ready.</Warning>

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>

## Further reading

1. [Waits and Timeouts](/learn/playwright/waits-and-timeouts/)
2. [Playwright general navigation docs](https://playwright.dev/docs/navigations)
3. [Playwright auto waiting](/learn/playwright/interaction/waits/)


Built with [Mintlify](https://mintlify.com).