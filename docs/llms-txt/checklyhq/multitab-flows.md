# Source: https://checklyhq.com/docs/learn/playwright/multitab-flows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Handling Multiple Tabs with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright enables us to control multiple browser tabs, albeit in different ways.

## Opening tabs directly

If we are looking to open brand new tabs with which to interact, the setup is rather straightforward.

```ts multitab-open.spec.ts theme={null}
import { test } from '@playwright/test'

test('open multiple tabs', async ({ browser }) => {
  const context = await browser.newContext()

  const pageOne = await context.newPage()
  const pageTwo = await context.newPage()

  await pageOne.goto('https://www.checklyhq.com/')
  await pageTwo.goto('https://playwright.dev/')

  await pageOne.screenshot({ path: 'screenshot-tab-one.png' })
  await pageTwo.screenshot({ path: 'screenshot-tab-two.png' })

  await browser.close()
})

```

## Handling links that open a new tab

Controlling tabs that are opened after a click on an element on the page can be trickier. Let's explore this through an example:

* Navigating to `https://checklyhq.com/docs`.
* Opening a new tab by clicking the link to the Checkly YouTube channel which opens in a new tab.

By allowing us to wait for the creation of a child tab with `page.waitForEvent`, Playwright enables us to "catch" it following a click on an element with `target="_blank"`, and then seamlessly interact with any of the currently open tabs.

```ts multitab-flows.spec.ts theme={null}
import { test } from '@playwright/test'

test('open multiple tabs', async ({ browser }) => {
  const context = await browser.newContext()
  const page = await context.newPage()

  await page.goto('https://www.checklyhq.com/docs/')

  const [newPage] = await Promise.all([
    context.waitForEvent('page'),
    await page.getByRole('link', { name: 'Checkly on Youtube' }).click()
  ])

  await page.screenshot({ path: 'screenshot-tab-old.png' })
  await newPage.screenshot({ path: 'screenshot-tab-new.png' })

  await browser.close()
})

```

## Further reading

1. Official documentation on [Playwright's multi-tab scenarios](https://playwright.dev/docs/multi-pages)

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).