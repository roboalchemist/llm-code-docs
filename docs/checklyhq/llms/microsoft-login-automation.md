# Source: https://checklyhq.com/docs/learn/playwright/microsoft-login-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Automate Microsoft Live Login with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright allows us to automate logging in to a Microsoft Online account.

## Steps

1. We start at `https://login.microsoftonline.com/`
2. We provide the username and password, injected by using environment variables
3. We are redirected to the main account page

```ts ms-account-login.spec.ts theme={null}
import { test } from '@playwright/test'

test('test', async ({ page }) => {
  await page.goto('https://login.microsoftonline.com/')

  await page.getByRole('heading', { name: 'Sign in' }).click()
  await page.getByPlaceholder('Email address, phone number').fill(process.env.MS_USERNAME)
  await page.getByRole('button', { name: 'Next' }).click()

  await page.getByTestId('i0118').fill(process.env.MS_PASSWORD)
  await page.getByTestId('textButtonContainer').getByRole('button', { name: 'Sign in' }).click()
  await page.getByTestId('checkboxField').check()
  await page.getByLabel('Stay signed in?').click()
})
```

Run this example as follows. Replace the username and password placeholder with your own credentials.

```sh  theme={null}
MS_USER=username MS_PWD=password npx playwright test ms-account-login.spec.ts
```

```sh  theme={null}
SET MS_USER=username
SET MS_PWD=password
npx playwright test ms-account-login.spec.ts
```

> This example does not work when you have 2-factor authentication enabled, and you might trigger a recaptcha check.

## Takeaways

1. Use environment variables to inject secrets.
2. Wait for the navigation as you are redirected to Microsoft.
3. Wait for the navigation as you are redirected back to the start site.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).