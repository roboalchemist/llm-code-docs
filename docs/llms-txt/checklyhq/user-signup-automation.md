# Source: https://checklyhq.com/docs/learn/playwright/user-signup-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automating User Signup with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Signups are key transactions in most web platforms, and therefore prime targets for automation.

Oftentimes, registering an account is where we will find longer forms asking the user to answer a variety of questions. Luckily, Playwright is quick enough to blaze through these in seconds.

## Steps

The flow will often match the following:

1. Navigate to the signup form.
2. Fill in all text fields, check all boxes etc.
3. Submit the form by clicking a button.

We will likely want to also check that some change occurred in the UI to confirm that the registration worked.

```ts signup.spec.ts theme={null}
import { test, expect } from '@playwright/test'

test('Sign up', async ({ page }) => {
  await page.goto('https://danube-web.shop/')

  await page.getByRole('button', { name: 'Sign up' }).click()
  await page.getByPlaceholder('Name', { exact: true }).fill('John')
  await page.getByPlaceholder('Surname').fill('Doe')
  await page.getByPlaceholder('Email').fill('user@email.com')
  await page.getByPlaceholder('Password').fill('supersecure1')

  await page.getByPlaceholder('Company (optional)').fill('Test Inc.')
  await page.getByLabel('Myself').check()
  await page.getByLabel('I would like to receive').check()
  await page.getByLabel('I have read and accept the').check()

  await page.getByRole('button', { name: 'Register' }).click()
  await expect(page.getByText('Welcome back, user@email.com')).toBeVisible()
})
```

Run this example as follows:

```sh  theme={null}
USER_EMAIL=user@email.com USER_PASSWORD=supersecure1 npx playwright test signup.spec.ts
```

```sh  theme={null}
SET USER_EMAIL=user@email.com
SET USER_PASSWORD=supersecure1
npx playwright signup.spec.ts
```

The normal signup flow might include asking the user to confirm their email address right away by navigating to a URL
included in an automated email. Reliably replicating the steps needed to achieve that is not trivial.

A possible solution to the issue is having the system under test distinguish between test sessions and normal user sessions,
and skip the verification step for test sessions. A way to achieve this would be to check for a specific user agent ID
which could be set as part of our test:

```js  theme={null}
await page.setUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 TEST_ID/<MY_SECRET>');
```

## Takeaways

1. Use environment variables to inject secrets.
2. You might need to go through additional steps in case email confirmation or similar is required.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).