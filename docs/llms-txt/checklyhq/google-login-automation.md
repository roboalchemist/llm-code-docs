# Source: https://checklyhq.com/docs/learn/playwright/google-login-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Automate Google Login with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Social login using your personal Google or Google Gsuite account is a common use case for many login scenarios.

## Steps

1. We start at a site that offers Google as an authentication provider. In this case we use [Stack Overflow](https://stackoverflow.com/).
2. We fetch the login page and click the "Login with Google" button.
3. We are redirect to Google.
4. We provide the username and password, injected by using environment variables.
5. We are redirected back to the starting.

```ts google-login.spec.ts theme={null}
import { test } from '@playwright/test'

test('Google login', async ({ page }) => {
  await page.goto('https://stackoverflow.com/users/login')

  await page.getByRole('button', { name: 'Log in with Google' }).click()
  await page.getByLabel('Email or phone').fill(process.env.GOOGLE_USER)
  await page.getByRole('button', { name: 'Next' }).click()

  await page.getByLabel('Enter your password').fill(process.env.GOOGLE_PWD)
  await page.getByRole('button', { name: 'Next' }).click()
  await page.getByRole('button', { name: 'Continue' }).click()
})

```

Run this example as follows. Replace the username and password placeholder with your own credentials.

```sh  theme={null}
GOOGLE_USER=username GOOGLE_PWD=password npx playwright test google-login.spec.ts
```

```sh  theme={null}
SET GOOGLE_USER=username
SET GOOGLE_PWD=password
npx playwright test google-login.spec.ts
```

<Note> This example does not work when you have 2-factor authentication enabled, and you might trigger a recaptcha check.</Note>

## Takeaways

1. Use environment variables to inject secrets.
2. Waiting for the navigation as you are redirected to Google is done automatically.
3. Waiting for the navigation as you are redirected back to the start site is done automatically.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).