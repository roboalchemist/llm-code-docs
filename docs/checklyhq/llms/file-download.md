# Source: https://checklyhq.com/docs/learn/playwright/file-download.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Download Files with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Websites might expose files for users to download and then access from their local machine. Common cases are downloading tickets, receipts and itineraries.

## Steps

This example runs against our [test webshop](https://danube-web.shop/) and proceeds to download a receipt for a previous purchase. It includes the following steps:

1. Logging in to the website
2. Navigating to the account page
3. Downloading a linked file

We will check that the downloaded file is as expected by comparing it to a [fixture file](/learn/playwright/handling-test-data/) in our final assertion.

We can approach this scenario in different ways. One possibility is to perform the first two steps, then [extract](/learn/playwright/web-scraping/)
the `href` value and use it to retrieve the file with a `GET` request (performed with [axios](https://github.com/axios/axios), for example).

```ts title="file-download.spec.ts" theme={null}
// Example code for file download using HTTP request
import { test, expect } from '@playwright/test';
import axios from 'axios';
import fs from 'fs';

test('download file with HTTP request', async ({ page }) => {
  // Login to the website
  await page.goto('https://danube-web.shop/login');
  await page.fill('#email', process.env.USER_EMAIL!);
  await page.fill('#password', process.env.USER_PASSWORD!);
  await page.click('#login-button');

  // Navigate to account page
  await page.goto('https://danube-web.shop/account');

  // Extract download link
  const downloadLink = await page.getAttribute('a[href*="receipt"]', 'href');

  // Download file using HTTP request
  const response = await axios.get(downloadLink, { responseType: 'stream' });
  const downloadPath = './downloaded-receipt.pdf';
  const writer = fs.createWriteStream(downloadPath);
  response.data.pipe(writer);

  await new Promise((resolve, reject) => {
    writer.on('finish', resolve);
    writer.on('error', reject);
  });

  // Compare with fixture file
  const downloadedFile = fs.readFileSync(downloadPath);
  const fixtureFile = fs.readFileSync('./fixtures/expected-receipt.pdf');
  expect(downloadedFile).toEqual(fixtureFile);
});
```

We could also click the link directly and wait for the download event, then proceed with the comparison.
Note that in this case, we need to enable downloads in the browser context before proceeding.

```ts title="file-download-alt.spec.ts" theme={null}
// Example code for file download using Playwright's download event
import { test, expect } from '@playwright/test';
import fs from 'fs';

test('download file with download event', async ({ page }) => {
  // Login to the website
  await page.goto('https://danube-web.shop/login');
  await page.fill('#email', process.env.USER_EMAIL!);
  await page.fill('#password', process.env.USER_PASSWORD!);
  await page.click('#login-button');

  // Navigate to account page
  await page.goto('https://danube-web.shop/account');

  // Wait for download event when clicking the link
  const downloadPromise = page.waitForEvent('download');
  await page.click('a[href*="receipt"]');
  const download = await downloadPromise;

  // Save the downloaded file
  const downloadPath = './downloaded-receipt.pdf';
  await download.saveAs(downloadPath);

  // Compare with fixture file
  const downloadedFile = fs.readFileSync(downloadPath);
  const fixtureFile = fs.readFileSync('./fixtures/expected-receipt.pdf');
  expect(downloadedFile).toEqual(fixtureFile);
});
```

Both examples can be run as follows:

**macOS/Linux:**

```bash  theme={null}
USER_EMAIL=user@email.com USER_PASSWORD=supersecure1 npx playwright test file-download.spec.ts
```

**Windows:**

```bash  theme={null}
SET USER_EMAIL=user@email.com
SET USER_PASSWORD=supersecure1
npx playwright test file-download.spec.ts
```

## Takeaways

1. Use environment variables to inject secrets.
2. Compare the expected file with the newly downloaded one.
3. There is more than one way to download a file within our script.

## Further reading

1. [Playwright's](https://playwright.dev/#version=v1.3.0\&path=docs%2Fapi.md\&q=class-download) documentation on downloading files.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).