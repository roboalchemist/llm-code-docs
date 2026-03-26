# Source: https://checklyhq.com/docs/learn/playwright/testing-file-uploads.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Test File Uploads with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Most services allow users to upload files to their accounts. This can be a profile picture, a document, or any other type of file.
Testing this functionality is crucial to ensure that users can upload files without any issues. In this example, we will
show you how to test file uploads using Playwright.

## Steps

Account properties to verify can run the gamut from simple text to connected third party services. In this example, we
will focus on a popular case: changing a profile image by uploading one of our own.

On our [test site](https://danube-web.shop/), such a test could look as follows:

```ts title="file-upload.ts" theme={null}
// Example code for testing file uploads
import { test, expect } from '@playwright/test';

test('upload profile image', async ({ page }) => {
  // Login to the website
  await page.goto('https://danube-web.shop/login');
  await page.fill('#email', process.env.USER_EMAIL!);
  await page.fill('#password', process.env.USER_PASSWORD!);
  await page.click('#login-button');

  // Navigate to profile page
  await page.goto('https://danube-web.shop/profile');

  // Upload file
  await page.setInputFiles('input[type="file"]', process.env.FILE_PATH!);
  await page.click('#upload-button');

  // Verify upload success
  await expect(page.locator('#upload-success')).toBeVisible();
  await expect(page.locator('#upload-success')).toContainText('Upload successful');
});
```

**macOS/Linux:**

```sh  theme={null}
USER_EMAIL=user@email.com USER_PASSWORD=supersecure1 FILE_PATH=file.jpg npx playwright test file-upload.ts
```

**Windows:**

```sh  theme={null}
SET USER_EMAIL=user@email.com
SET USER_PASSWORD=supersecure1
SET FILE_PATH=file.jpg
npx playwright test file-upload.ts
```

Here, we are simply checking for a message giving us feedback on the status of the upload. Depending on the website we are testing, it might be possible to also download the profile image afterwards to run a comparison locally for a more robust check.

## Takeaways

1. Use environment variables to inject secrets.
2. Use `setInputFiles` (Playwright) to upload the file.
3. If possible, download the file from the platform and compare it with the one that was just uploaded.

## Further reading

1. Official documentation from [Playwright](https://playwright.dev/docs/input#upload-files)

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).