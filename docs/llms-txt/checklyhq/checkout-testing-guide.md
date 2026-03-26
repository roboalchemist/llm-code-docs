# Source: https://checklyhq.com/docs/learn/playwright/checkout-testing-guide.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Mastering E2E Checkout Testing Using Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Another key website flow that needs to be closely monitored is any sort of checkout. You want to be 100% sure your users are able to pay for goods or services you might be offering, at any given time.

## Steps

Checkout procedures can vary dramatically depending on what is being bought or sold. A few constants will be:

1. a shopping basket page / section, in cases where multiple items can be bought - this is normally where the checkout procedure starts
2. a page to enter or edit billing and, where applicable, shipping information
3. a summary to review all the different parameters of the purchase

Modelled on the above structure is the following example running against our test website. We will add a few products to the shopping cart, then proceed until the summary screen shows up and verify that the transaction has been confirmed. Here we can get creative and, for example, iterate through a number of products to fill the cart:

```ts checkout.spec.ts theme={null}
import { test } from '@playwright/test'

const productsNumber: number = parseInt(<string>process.env.PRODUCTS_NUMBER) || 3

test('checkout', async ({ page }) => {
  await page.goto('https://danube-web.shop/')

  for (let i = 1; i <= productsNumber; i++) {
    await page.click(`.preview:nth-child(${i}) > .preview-author`)
    await page.getByRole('button', { name: 'Add to cart' }).click()
    await page.click('#logo')
  }

  await page.locator('#cart').click()
  await page.getByRole('button', { name: 'Checkout' }).click()

  await page.getByPlaceholder('Name', { exact: true }).fill('Max')
  await page.getByPlaceholder('Surname', { exact: true }).fill('Mustermann')
  await page.getByPlaceholder('Address').fill('Charlottenstr. 57')
  await page.getByPlaceholder('Zipcode').fill('10117')
  await page.getByPlaceholder('City').fill('Berlin')
  await page.getByPlaceholder('Company (optional)').fill('Firma GmbH')
  await page.getByLabel('as soon as possible').check()
  await page.getByRole('button', { name: 'Buy' }).click()
})
```

Run this example as follows:

```sh  theme={null}
PRODUCTS_NUMBER=3 npx playwright test checkout.spec.ts
```

```sh  theme={null}
SET PRODUCTS_NUMBER=3
npx playwright test checkout.spec.ts
```

Note: In some cases, users will need to [log in](/learn/playwright/login-automation/) before they can proceed to a purchase. When users are allowed to buy both with and without having a pre-existing account on the platform, it might be worthwhile to test both flows separately.

## Limitations

Checkout is a peculiar flow: unlike Login and others, it almost always involves an actual exchange of currency. This is usually not an issue in pre-production environments, as payment providers are not yet involved or are set up in sandbox/test mode. For Production, low-value transactions can be performed with low frequency and immediately voided after the test has been completed.

## Takeaways

1. Checkout flows will vary depending on what is being purchased.
2. Remember to check different flows (e.g. with and without login) if needed.
3. Additional care is needed on production systems as real transactions will take place.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).