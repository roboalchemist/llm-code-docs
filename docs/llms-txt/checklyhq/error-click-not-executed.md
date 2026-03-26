# Source: https://checklyhq.com/docs/learn/playwright/error-click-not-executed.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Fix the "Click Not Executed" Error in Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

In certain situations, it might look as if no click is happening in the browser even if our script specifies it.

For example: our Playwright script is supposed to run a `page.click('#btn-login')` but seems to ignore the click and just proceed with the next instruction. This can result in an `Element not found error` or similar.

## Possible causes

* **Not-so-obvious:** the element we are trying to click is on the page, but is not the one receiving the click; there might be another element somewhere else on the page that is receiving it instead. The instruction itself does not raise any error, as it is in fact being executed correctly.

## How to avoid confusion

Try querying for the element in the browser console during inspection. If a `document.querySelectorAll('mySelector')` (or simply `$$('mySelector')`) returns more than one element, you want to come up with a more precise selector which references only the specific element you are looking to click.

Unless you know for certain, do not assume that the page you are automating follows best practices. For example: IDs are unique in valid HTML, but a page can be made up of invalid HTML and still work! So if you are struggling with a click seemingly not going through and your selector is based on an ID, check whether the page contains duplicated IDs. The Chrome DevTools console will also alert you:

<img src="https://mintcdn.com/checkly-422f444a/PFNKka5JJJWLiGJ7/images/samples/images/errors-ids-console.png?fit=max&auto=format&n=PFNKka5JJJWLiGJ7&q=85&s=ff03c165b816004755031d090ca95a5d" alt="chrome devtools console showing alert for duplicated id" width="1150" height="506" data-path="images/samples/images/errors-ids-console.png" />

If you are running Playwright 1.14 or newer, you can also enable [strict mode](https://playwright.dev/docs/release-notes#version-114) to have it throw an error in case your selector matches more than one element on the page: `await page.click('mySelector', { strict: true });`

> Note that this list neither is nor aims to be complete: additional possible causes most likely exist for this error.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).