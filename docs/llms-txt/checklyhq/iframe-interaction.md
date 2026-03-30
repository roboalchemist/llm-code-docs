# Source: https://checklyhq.com/docs/learn/playwright/iframe-interaction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Handle iFrames in Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright enables us to access and interact with iframes.

## Locate an iframe and its elements

To access iframe elements, locate the iframe and query the DOM elements as if you're in the page context.

```ts iframe-access.spec.ts theme={null}
import { test } from '@playwright/test'

test('access iframe content', async ({ page }) => {
  await page.goto('https://your-page-with-an-iframe.com')
  const header = await page.frameLocator('iframe').locator('h1')
  console.log(await header.innerText())
})

```

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>

## Further reading

1. [Playwright's "Frames documentation"](https://playwright.dev/docs/frames)


Built with [Mintlify](https://mintlify.com).