# Source: https://checklyhq.com/docs/learn/playwright/login-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Automate Login with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

When automating key site transactions, we inevitably stumble into login scenarios. In most cases, users need to be able to access accounts on a platform to get any value out of it. If they suddenly become unable to do so, we need to be informed as quickly as possible.

## Steps

In its simplest form, a login procedure requires the user to:

1. Navigate to the login form
2. Fill in a username/email field
3. Fill in a password field
4. Click a button to finalise the login

At the end of our test, we need to check if our login procedure has been successful. For example, we could verify that an element is shown that we know only appears for logged-in users.

On our [test site](https://danube-web.shop/) this could look like the following:

```ts login.spec.ts theme={null}
import { test, expect } from '@playwright/test'

test('Login', async ({ page }) => {
  await page.goto('https://danube-web.shop/')

  await page.getByRole('button', { name: 'Log in' }).click()
  await page.getByPlaceholder('Email').fill(process.env.USER_EMAIL)
  await page.getByPlaceholder('Password').fill(process.env.USER_PASSWORD)
  await page.getByRole('button', { name: 'Sign In' }).click()

  await expect(page.getByText('Welcome back, user@email.com')).toBeVisible()
})
```

Run this example as follows. Replace the username and password placeholder with your own credentials.

**macOS/Linux:**

```bash  theme={null}
USER_EMAIL=user@email.com USER_PASSWORD=supersecure1 npx playwright test login.spec.ts
```

**Windows:**

```bash  theme={null}
SET USER_EMAIL=user@email.com
SET USER_PASSWORD=supersecure1
npx playwright test login.spec.ts
```

## Takeaways

1. Use environment variables to inject secrets.
2. You might need to wait for the navigation as you are redirected to the login screen/modal.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).