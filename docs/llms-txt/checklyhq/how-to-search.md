# Source: https://checklyhq.com/docs/learn/playwright/how-to-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to search with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Searching a website is an everyday action for most internet users. For most services, the speed at which their customers are able to get to the products they are looking for is directly tied to revenue. To enable that, a performant and reliable search function is needed.

## Steps

The example below, which is running against our [test webshop](https://danube-web.shop/), shows how we can verify the correctness of a search's result from an end-to-end perspective. In short, we will:

1. Enter a known search term
2. Firstly, assert the expected number of results is being shown
3. If the previous point is true, assert that all expected search results are shown

```ts title="search.spec.ts" theme={null}
// Example code for testing search functionality
import { test, expect } from '@playwright/test';

test('search functionality', async ({ page }) => {
  await page.goto('https://danube-web.shop/');

  // Enter search term
  await page.fill('#search-input', 'book');
  await page.click('#search-button');

  // Assert expected number of results
  await expect(page.locator('.search-result')).toHaveCount(4);

  // Assert all expected search results are shown
  await expect(page.locator('.search-result')).toContainText([
    'Haben oder haben',
    'Parry Hotter',
    'Laughterhouse-Five',
    'To Mock a Killingbird'
  ]);
});
```

Run this example as follows:

```sh  theme={null}
npx playwright test search.spec.ts
```

<Note> When testing search on large sets of data, you might additionally need to handle result pagination, together with the possibility of duplicate results.</Note>

Listing search terms and their corresponding expected results in a file could be helpful for additional, more thorough testing. The contents of the file would be then used to drive the searches and comparisons. An example could look like the following JSON:

```json  theme={null}
[
    {
        "search": "pen",
        "results": [
            "red pen",
            "blue pen",
            "fountain pen"
        ]
    },
    {
        "search": "pencil",
        "results": [
            "short pencil",
            "pencil sharpener",
            "pencil case"
        ]
    }
]
```

## Takeaways

1. Moving test data to a separate file can help when running more thorough comparisons.
2. Assertion libraries help us cleanly verify multiple constraints in our test.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).