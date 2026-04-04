# Source: https://checklyhq.com/docs/learn/playwright/generating-pdfs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Generate PDFs with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Playwright can be used to create PDFs from webpages. This opens up interesting automation scenarios for tasks such as archiving, generating invoices, writing manuals, books and more.

This article introduces this functionality and shows how we can customise the PDF to fit our needs.

## Generating a PDF file

After loading a page, we use the `page.pdf()` command to convert it to a PDF.

```ts title="pdf-minimal.spec.ts" theme={null}
// Example code for generating a minimal PDF
import { test, expect } from '@playwright/test';

test('generate PDF', async ({ page }) => {
  await page.goto('https://example.com');
  await page.pdf({ path: 'example.pdf' });
});
```

Note that we need to pass the `path` option to have the PDF file actually saved to disk.

<Note> This feature is currently only supported in Chromium headless in Playwright.</Note>

## Tweaking the result

It is important to take a quick look at the official docs for `page.pdf()` from [Playwright](https://playwright.dev/docs/api/class-page#page-pdf), as it is almost certain that we will want to tweak the appearance of our page in the resulting PDF.

In certain cases, our webpage might look significantly different in our PDF compared to our browser. Depending on the case, it can pay off to experiment with the following:

1. We might need to set option `printBackground` to true in case graphical components appear to be missing in the generated PDF.
2. By default, `page.pdf()` will generate a PDF with adjusted colors for printing. Setting the CSS property `-webkit-print-color-adjust: exact` will force rendering of the original colors.
3. Calling `page.emulateMedia('screen')` changes the CSS media type of the page.
4. Setting either `width` and `height` or `format` to the appropriate value might be needed for the page to be displayed optimally.

## Customising header and footer

We can also have custom headers and footers added to our pages, displaying values such as title, page number and more. Let's see how this looks on your [favourite website](https://www.checklyhq.com/):

```ts title="pdf-hd.spec.ts" theme={null}
// Example code for generating a PDF with header and footer
import { test, expect } from '@playwright/test';

test('generate PDF with header and footer', async ({ page }) => {
  await page.goto('https://www.checklyhq.com/docs/');
  await page.pdf({
    path: 'checkly-with-header-footer.pdf',
    format: 'A4',
    displayHeaderFooter: true,
    headerTemplate: '<div class="header-content">Custom Header</div>',
    footerTemplate: '<div class="footer-content">Custom Footer</div>',
    margin: {
      top: '100px',
      bottom: '100px',
      left: '50px',
      right: '50px'
    }
  });
});
```

Change `headerTemplate` and `footerTemplate` to include more complex templates like these ones below.

**template-header.html**

```html  theme={null}
<html>
  <head>
    <style type="text/css">
      #header {
        padding: 0;
      }
      .content {
        width: 100%;
        background-color: #777;
        color: white;
        padding: 5px;
        -webkit-print-color-adjust: exact;
        vertical-align: middle;
        font-size: 15px;
        margin-top: 0;
        display: inline-block;
      }
      .title {
        font-weight: bold;
      }
      .date {
        text-align:right;
      }
    </style>
  </head>
  <body>
    <div class="content">
        <span class="title"></span> -
        <span class="date"></span>
        <span class="url"></div>
    </div>
  </body>
</html>
```

**template-footer.html**

```html  theme={null}
<html>
  <head>
    <style type="text/css">
      #footer {
        padding: 0;
      }
      .content-footer {
        width: 100%;
        background-color: #777;
        color: white;
        padding: 5px;
        -webkit-print-color-adjust: exact;
        vertical-align: middle;
        font-size: 15px;
        margin-top: 0;
        display: inline-block;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="content-footer">
      Page <span class="pageNumber"></span> of <span class="totalPages"></span>
    </div>
  </body>
</html>
```

Then, the first page of the generated PDF looks as follows:

<img src="https://mintcdn.com/checkly-422f444a/oRctcItr3u0Uxv5E/images/samples/images/pdf-generation-hd.png?fit=max&auto=format&n=oRctcItr3u0Uxv5E&q=85&s=333fca306d05dcbc70a8794ec9d3e21c" alt="generated pdf example" width="1058" height="1488" data-path="images/samples/images/pdf-generation-hd.png" />

Run the above examples as follows:

```bash  theme={null}
npx playwright test generate-pdf.ts
```

## Further considerations

We can easily transform existing web pages into PDF format, just as we have shown in our example. An even more interesting use case is about generating a brand new document: now we can use our existing HTML and CSS skills to produce high-quality PDFs, often eliminating the need for LaTeX or similar tools.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).