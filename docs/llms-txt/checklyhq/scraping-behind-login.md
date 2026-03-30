# Source: https://checklyhq.com/docs/learn/playwright/scraping-behind-login.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Scrape Data Behind a Login with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright can be particularly useful when scraping data accessible only behind a login wall. This article shows a practical example of such a case.

## Scraping expenses on Amazon

For our example, we will be logging in to our Amazon account and scraping the price off each order in the previous year, then adding them all up to show us our total Amazon expenditures over that period of time.

A combination of UI automation and scraping will allow us to first log in to the platform, and then to retrieve the information about all our orders.

```js scraping-example-purchases.js theme={null}
const { chromium } = require('playwright')
;(async () => {
  const currency = process.env.CURRENCY
  const amazonUrl = process.env.AMAZON_URL
  const amazonUser = process.env.AMAZON_USER
  const amazonPassword = process.env.AMAZON_PASSWORD

  const browser = await chromium.launch()
  const page = await browser.newPage()

  await page.goto(amazonUrl)

  await page.setViewportSize({ width: 1200, height: 1822 })

  await page.click(
    '#nav-signin-tooltip > .nav-action-button > .nav-action-inner'
  )

  await page.type('#ap_email', amazonUser)
  await page.click('#continue')
  await page.type('#ap_password', amazonPassword)

  await page.click('#signInSubmit')

  await page.click('#nav-link-accountList > .nav-long-width')

  await page.click(
    '.ya-card__whole-card-link > .a-box > .a-box-inner > .a-row > .a-column > div'
  )

  await page.click('#a-autoid-1-announce > .a-dropdown-prompt')

  await page.click('#orderFilter_2')

  let filteredPrices = []
  let prices = []

  await page.waitForSelector('.a-normal')
  const pages = await page.$$('.a-normal')

  for (const singlePage of pages) {
    await singlePage.waitForSelector('.a-last')
    prices = await singlePage.$$eval(
      '.a-column:nth-child(2) .a-color-secondary.value',
      (nodes) => nodes.map((n) => n.innerText)
    )

    filteredPrices = filteredPrices.concat(
      prices.filter((price) => price.includes(currency))
    )
    await singlePage.waitForSelector('li.a-last')
    await singlePage.click('li.a-last')
  }

  const cleanPrices = filteredPrices.map((x) => {
    return x.replace(',', '.').replace(/[^\d.,-]/g, '')
  })

  const totalExpense = cleanPrices.reduce(
    (a, b) => parseFloat(a) + parseFloat(b),
    0
  )
  console.log(`Total expense for the year: ${currency} ${totalExpense}`)

  await browser.close()
})()
```

<Note> This example is only intended for learning purposes. Always make sure the website you are planning to scrape allows such behaviour.</Note>

Run the above examples as follows, making sure to choose the right Amazon URL and currency:

```sh  theme={null}
CURRENCY=EUR AMAZON_URL=https://www.amazon.de AMAZON_USER=<YOUR_AMAZON_USERNAME> AMAZON_PASSWORD=<YOUR_AMAZON_PASSWORD> node scraping-example-purchases.js
```

```sh  theme={null}
SET CURRENCY=EUR
SET AMAZON_URL=https://www.amazon.de
SET AMAZON_USER=<YOUR_AMAZON_USERNAME>
SET AMAZON_PASSWORD=<YOUR_AMAZON_PASSWORD>
node scraping-example-purchases.js
```

> Under the hood, Amazon can change quite quickly. You might need to adjust the locators and/or flow slightly to have the script work for you.

> ⚠️ Websites might [restrict headless browser traffic](/learn/playwright/challenging-flows/) in order to protect their users from fraud. 2FA will also interfere with the script if enabled.

## Takeaways

1. We can scrape information available behind a login wall with Playwright.
2. Some websites might not allow scraping. Always make sure you check their terms of service beforehand.

## Further reading

1. [Basic scraping](/learn/playwright/web-scraping/) with Playwright

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).