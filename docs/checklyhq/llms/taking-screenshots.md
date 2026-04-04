# Source: https://checklyhq.com/docs/learn/playwright/taking-screenshots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Playwright Screenshots - How to Take and  Automate Screenshots

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Headless browsers are fully capable of taking screenshots, which is very useful in troubleshooting failures or faulty scripts. Using additional libraries and tools, it is also possible to automate visual comparisons.

## Generating and saving screenshots

The `page.screenshot` command allows us to save one or more screenshots of the current page to a specified path. Without any additional options, the size of the screenshot depends on the viewport size:

```ts basic-screenshot.spec.ts theme={null}
import { test } from '@playwright/test'

test('take a screenshot', async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 800 })
  await page.goto('https://danube-web.shop/')
  await page.screenshot({ path: 'my_screenshot.png' })
})

```

## Full page screenshots

Adding the `fullPage: true` option allows for the capture of full page screenshots, overriding the `height` parameter specified for our viewport:

```js  theme={null}
await page.screenshot({ path: 'my_screenshot.png', fullPage: true })
```

## Clipped screenshots

Having our screenshot limited to a smaller portion of the viewport is also possible. All we need to do is specify the coordinates of the top left corner of the screenshot, plus `width` and `height`. We then pass these options to:

```ts basic-screenshot-clipped.spec.ts theme={null}
import { test } from '@playwright/test'

test('take a clipped screenshot', async ({ page }) => {
  const options = {
    path: 'clipped_screenshot.png',
    fullPage: false,
    clip: {
      x: 5,
      y: 60,
      width: 240,
      height: 40
    }
  }

  await page.setViewportSize({ width: 1280, height: 800 })
  await page.goto('https://danube-web.shop/')
  await page.screenshot(options)
})

```

The above examples can be run as follows:

```sh  theme={null}
npx playwright test basic-screenshots.spec.ts
```

## Visual regression testing

Playwright can be used to take screenshots of a page and compare them with a reference image. This is useful for visual
regression testing, where we can detect changes in the UI that may have been introduced by code changes.

The `expect(page).toMatchSnapshot()` command is used to take a screenshot and compare it with a reference image. If the images are different, the test will fail.

```ts visual-regression.spec.ts theme={null}
import { test, expect } from '@playwright/test'

test('visual regression', async ({ page }) => {
  await page.goto('https://danube-web.shop/')
  const screenshot = await page.screenshot()
  expect(screenshot).toMatchSnapshot('danube-web-shop.png')
})
```

## Further reading

1. Official documentation for taking screenshots with [Playwright](https://playwright.dev/docs/verification?_highlight=screenshot#screenshots)
2. Blog post from baseweb.design on the whys and hows of [visual regression testing](https://baseweb.design/blog/visual-regression-testing/)
3. Blog post from Gideon Pyzer looking at different visual [regression testing tools](https://gideonpyzer.dev/blog/2018/06/25/visual-regression-testing/)

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).