# Source: https://checklyhq.com/docs/learn/playwright/testing-coupons.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Test Coupons and Discounts with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Webshops and subscription-based services often offer discounts through coupon codes. Applying a valid coupon code during checkout might reduce the price of one, several, or all items in the shopping cart.

## Steps

While discount coupons will be applied in different ways depending on the service or shop they are relevant to, in most cases:

1. Having selected one or more products will be a prerequisite for applying the coupon
2. Entering a valid coupon will result in visible feedback, i.e. a reduction of the previous product/cart price

The following example, running against our [test site](https://danube-web.shop/), will add a variable number of items to the cart, then proceed to compare the total price before and after applying the coupon. The coupon is reducing the price of the whole shopping cart by 20%, therefore we will be asserting that the discounted price is reduced by the right amount. For this step we have chosen [Chai](https://www.chaijs.com/api/assert/), but any solid assertion library will do.

```js coupon.js theme={null}
const assert = require('chai').assert
const { chromium } = require('playwright')
const productsNumber = process.env.PRODUCTS_NUMBER || 3

;(async () => {
  const browser = await chromium.launch()
  const page = await browser.newPage()

  await page.goto('https://danube-web.shop/')

  for (let i = 1; i <= productsNumber; i++) {
    await page.click(`.preview:nth-child(${i}) > .preview-author`)
    await page.click('.detail-wrapper > .call-to-action')
    await page.click('#logo')
  }

  await page.click('#cart')

  await page.waitForSelector('#total-price')
  const price = await page.$eval('#total-price', (e) => e.innerText)

  await page.click('.cart > label')
  await page.click('#coupon')
  await page.type('#coupon', 'COUPON2020')
  await page.click('.cart > div > button')

  const expectedDiscountedPrice = price * 0.8
  const discountedPrice = await page.$eval('#total-price', (e) => e.innerText)
  assert.equal(discountedPrice, expectedDiscountedPrice)

  await browser.close()
})()

```

Run this example as follows:

```sh  theme={null}
PRODUCTS_NUMBER=3 node coupon.js
```

```sh  theme={null}
SET PRODUCTS_NUMBER=3
node coupon.js
```

## Takeaways

1. We can simply verify that coupons are accepted, or also check that they command the right discount.
2. Assertion libraries are useful when non-trivial [assertions](https://www.checklyhq.com/docs/api-checks/assertions/) are required.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).