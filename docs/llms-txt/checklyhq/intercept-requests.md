# Source: https://checklyhq.com/docs/learn/playwright/intercept-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Intercept Requests in Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

When we browse the web, a series of HTTP requests and responses are exchanged between our browser and the pages we are visiting. There are scenarios in which it is useful to monitor or manipulate this traffic.

## Request interception

Request interception enables us to observe which requests and responses are being exchanged as part of our script's execution. For example, this is how we could print them out when we load our [test website](https://danube-web.shop/):

```ts title="request-interception-read.spec.ts" theme={null}
// Example code for request interception
import { test, expect } from '@playwright/test';

test('intercept requests', async ({ page }) => {
  // Listen for all requests
  page.on('request', request => {
    console.log('Request:', request.url());
  });

  // Listen for all responses
  page.on('response', response => {
    console.log('Response:', response.url(), response.status());
  });

  await page.goto('https://danube-web.shop/');
});
```

We might want to intervene and filter the outgoing requests. For example, when [scraping web pages](/learn/playwright/web-scraping/), we might want to block unnecessary elements from loading in order to speed up the procedure and lower bandwidth usage.

```ts title="request-interception-block.spec.ts" theme={null}
// Example code for blocking requests
import { test, expect } from '@playwright/test';

test('block image requests', async ({ page }) => {
  // Block image requests
  await page.route('**/*', route => {
    if (route.request().resourceType() === 'image') {
      route.abort();
    } else {
      route.continue();
    }
  });

  await page.goto('https://danube-web.shop/');
});
```

As a result, you will see the website logo not being loaded.

<img src="https://mintcdn.com/checkly-422f444a/PFNKka5JJJWLiGJ7/images/samples/images/request-interception-image.png?fit=max&auto=format&n=PFNKka5JJJWLiGJ7&q=85&s=c6f1960b7627f07abaccae3d6ab35f94" alt="test site without images" width="1200" height="800" data-path="images/samples/images/request-interception-image.png" />

Similarly, switching the `resourceType` to `stylesheet` would result in the target website loading without any CSS styling.

<img src="https://mintcdn.com/checkly-422f444a/PFNKka5JJJWLiGJ7/images/samples/images/request-interception-css.png?fit=max&auto=format&n=PFNKka5JJJWLiGJ7&q=85&s=17c9e1829cf6b45c15f67a85586f5c18" alt="test site without css" width="1200" height="800" data-path="images/samples/images/request-interception-css.png" />

## Response interception

Isolating one or more software components from their dependencies makes them easier to test. We can do so by substituting interactions with such dependencies with simulated, simplified ones. This is also known as *stubbing*.

Playwright makes it easy for us, as for every request we can intercept we also can stub a response.

Every time we load it, our test website is sending a request to its backend to fetch a list of best selling books. For our example, we are going to intercept this response and modify it to return a single book we define on the fly.

```ts title="response-interception.spec.ts" theme={null}
// Example code for response interception
import { test, expect } from '@playwright/test';

test('intercept and modify response', async ({ page }) => {
  // Intercept API calls and return custom data
  await page.route('**/api/best-sellers', route => {
    const customResponse = {
      books: [
        {
          title: 'Custom Book Title',
          author: 'Custom Author',
          genre: 'Custom Genre',
          price: '$19.99',
          rating: '4.5 stars'
        }
      ]
    };

    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify(customResponse)
    });
  });

  await page.goto('https://danube-web.shop/');
});
```

Here is what the homepage will look like with our stubbed response:

<img src="https://mintcdn.com/checkly-422f444a/PFNKka5JJJWLiGJ7/images/samples/images/response-interception.png?fit=max&auto=format&n=PFNKka5JJJWLiGJ7&q=85&s=12b68b829bd04596134e1dad2d5580fd" alt="test site with stubbed response" width="1200" height="800" data-path="images/samples/images/response-interception.png" />

Run the above examples as follows:

```bash  theme={null}
npx playwright test request-interception.ts
```

## Takeaways

1. Playwright gives us control over outgoing HTTP requests.
2. Playwright can easily stub HTTP responses.

## Avoid Network Interception in Synthetic Monitoring

Network interception is valuable if your primary goal is to test a frontend application in isolation. However, if you want to test your application end-to-end or [use Playwright for synthetic production monitoring with Checkly](/detect/synthetic-monitoring/playwright-checks/overview) you should avoid network interception as much as possible.

The goal of end-to-end testing and synthetic monitoring is to test the entire stack ranging from the backend systems to the last third-party JavaScript snippet being loaded in the frontend.

* You won't learn about your image CDN's downtime if your tests block image requests to save bandwidth.
* You will never learn about your flaky checkout API flow if you mock all the `/order` requests.
* You won't be notified when a tracking script breaks your page layout if you block third-parties in your tests.

Investing in fully end-to-end testing and monitoring can be challenging but it'll provide you the safety net you're aiming for.

## Further reading

1. Official documentation on this topic from [Playwright](https://playwright.dev/docs/network).
2. [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) by Martin Fowler.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).