# Source: https://checklyhq.com/docs/learn/playwright/error-wait-not-respected.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Fix "Wait Not Respected" Error in Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Our script might sometimes look as if it were not honoring the waits we are specifying, instead proceeding and potentially running into an error on the next instruction.

For example: we are waiting for an element, e.g. with `page.waitForSelector`, but the script immediately proceeds to the next instruction. This can result in an [element not found error](#element-not-found) or similar on the following step in our script.

## Possible causes

* **Not-so-obvious possible cause:** the element we are waiting for is already in the DOM, possibly not visible in our inspection but already matching our `state` requirements.

## How to avoid confusion

Try querying for the element in the browser console during inspection. If the element is found, inspect its attributes (e.g. `visibility`) and ensure they match your expectations.

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