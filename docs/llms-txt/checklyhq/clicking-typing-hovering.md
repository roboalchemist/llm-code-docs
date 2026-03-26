# Source: https://checklyhq.com/docs/learn/playwright/clicking-typing-hovering.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Click, Type, and Hover with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Users normally access most website functionality through clicks, keystrokes etc. Playwright allows us to replicate these events by referencing elements on the page using [User-first Selectors](https://www.checklyhq.com/blog/playwright-user-first-selectors/).

## Clicking

Clicking is the default way of selecting and activating elements on web pages, and will appear very often in most headless scripts.

```ts basic-click.spec.ts theme={null}
import { test, expect } from '@playwright/test'

test('can click log in', async ({ page }) => {
 await page.goto('https://danube-web.shop/')
 await page.getByRole('button', { name: 'Log in' }).click()
})
```

## Hovering

A popular pattern among web pages is exposing additional information or functionality when the user hovers the mouse cursor over a specific item. Examples include, menus, previews and dialogs containing extra information on the item.

```ts basic-hover.spec.ts theme={null}
import { test, expect } from '@playwright/test'

test('hover over sign in', async ({ page }) => {
 await page.goto('https://danube-web.shop/')
 await page.getByRole('button', { name: 'Log in' }).click()
 await page.getByRole('button', { name: 'Sign In' }).hover()
});
```

*Note that in this example we're not asserting anything, since our web example doesn't do any element updates on hover.*

## Focussing

Focussing on specific UI elements allows the user to interact with them without clicks. It can also result in a proactive reaction from the webapp, such as displaying suggestions.

```ts basic-focus.spec.ts theme={null}
import { test, expect } from '@playwright/test'

test('Focus on email field', async ({ page }) => {
 await page.goto('https://danube-web.shop/')
 await page.getByRole('button', { name: 'Log in' }).click()
 await page.getByPlaceholder('Email').focus()
});
```

## Typing

We can simulate typing on a real keyboard using `page.type()`:

```ts basic-type.spec.ts theme={null}
 import { test, expect } from '@playwright/test'

test('testAlpha', async ({ page }) => {
  await page.goto('https://danube-web.shop/')
  await page.getByRole('textbox').focus()
  await page.getByRole('textbox').fill('catcher')
  await page.getByRole('button', { name: 'Search' }).click()
  await expect(page.locator('#app-content')).toContainText('Rye')
});
```

Single key presses can also be executed. For example, to press the Enter key:

* Playwright: `await page.press('Enter')`

Key presses can also be sent to a specific element:

`await (await page.$('input[type="text"]')).press('Enter')`

We can also hold down and release one or more keys, possibly combining them to use keyboard shortcuts:

```ts  theme={null}
await page.keyboard.down('Control')
await page.keyboard.press('V')
await page.keyboard.up('Control')
```

You can run (from the terminal) the above examples as follows:

```sh  theme={null}
npx playwright test basic-click-type.ts
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

1. The related official documentation of [Playwright](https://playwright.dev/docs/input#mouse-click)
2. [Finding effective selectors](/learn/playwright/selectors/)


Built with [Mintlify](https://mintlify.com).