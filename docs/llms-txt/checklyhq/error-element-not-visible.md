# Source: https://checklyhq.com/docs/learn/playwright/error-element-not-visible.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Fix "Element Not Visible" Error in Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Knowing that an element is included in the DOM might not be enough for us to properly interact with it: its state also determines whether our action will be able to go through.

Example error message:

```sh  theme={null}
ERROR - UserScript page.waitForSelector: Timeout 30000ms exceeded.
waiting for selector ".contact-form > .form-control" to be visible
  selector resolved to hidden <element>
```

## Possible causes

* **Obvious possible cause:** the element is set to hidden while it shouldn't. Something is wrong with the element itself.
* **Not-so-obvious possible cause:** a different element is hiding the target element without our knowledge.

## How to avoid confusion

Either walk through the execution in headful mode or take screenshots before and after the instruction that has raised the error - this will help you verify whether the application state actually is the one you expect.

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