# Source: https://checklyhq.com/docs/learn/playwright/error-target-closed.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Fix "Target Closed" Error in Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

Our script can return the sometimes cryptic "Target closed" error. Knowing that the "target" is normally our browser, the [context](https://playwright.dev/docs/core-concepts#browser-contexts) or tab that our script is controlling can help us close in on the cause of the issue.

Example error message:

```sh  theme={null}
UnhandledPromiseRejectionWarning: Error: Protocol error: Target closed
```

## Possible causes

* **Obvious possible cause:** the browser, context or tab is being closed at the wrong time in the script.
* **Not-so-obvious possible cause:** promises are not being handled correctly, e.g.:

1. Forgetting an `await` so that the `browser.close()` executes before your command has terminated.
2. [Wrong foreach usage](https://github.com/babel/babel/issues/909): [forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) expects a synchronous function, so use a [for-of loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) if you are using `await`.

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