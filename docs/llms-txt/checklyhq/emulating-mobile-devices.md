# Source: https://checklyhq.com/docs/learn/playwright/emulating-mobile-devices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to emulate mobile devices with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright controls headless desktop browsers that can also emulate mobile devices. And while device emulation can't replace testing on mobile devices entirely, it's a practical and quick-to-setup approach to testing mobile scenarios.

Device emulation is well suited to test if your site behaves correctly across multiple viewport sizes and correctly handles `user-agent` strings. But if your site relies on device-specific browser features, an iPhone emulation running in a Chromium browser might lead to false positives.

This guide explains how to define viewport sizes, device pixel ratio and  `user-agent` strings using Playwright.

## Defining the user agent string

If your site parses the user agent string to serve a different experience to mobile users, define the `userAgent` in your automation scripts.

```ts emulate-mobile.spec.ts theme={null}
import { test } from '@playwright/test'

test.use({
  userAgent:
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/16.0 Mobile/14E304 Safari/602.1',
})

test('emulate iPhone SE', async ({ page }) => {
  await page.goto("https://danube-web.shop/")

  // perform your tests
})
```

## Defining viewport size and pixel density

If your site follows responsive web design practices and renders elements depending on device viewport size, define a mobile viewport and pixel density.

```ts emulate-mobile-viewport.spec.ts theme={null}
const { test } = require('@playwright/test')

test.use({
  viewport: {
    width: 320,
    height: 568
  },
  deviceScaleFactor: 2
})

test('emulate iPhone SE', async ({ page }) => {
  await page.goto('https://danube-web.shop/')

  // perform your tests
})
```

### Use built-in device registries

Playwright includes a built-in device registry to access mobile device characteristics quickly.

* [Playwright devices](https://playwright.dev/docs/emulation#devices)

Leverage the pre-defined devices to emulate mobile devices.

```ts emulate-mobile-builtin.spec.ts theme={null}
import { test, devices } from '@playwright/test'
const iPhone = devices['iPhone SE']

test.use({
  ...iPhone,
})

test('emulate iPhone SE', async ({ page }) => {
  await page.goto('https://danube-web.shop/')

  // perform your tests
})
```

## Further reading

1. [Measuring page performance](/learn/playwright/performance/)
2. [Playwright's emulation documentation](https://playwright.dev/docs/emulation)

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).