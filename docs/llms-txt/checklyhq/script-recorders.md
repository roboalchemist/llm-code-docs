# Source: https://checklyhq.com/docs/learn/playwright/script-recorders.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Script Recorders with Playwright

<Tip>
  If you're using Playwright for end-to-end testing, you should check out [Playwright Check Suites](/detect/synthetic-monitoring/playwright-checks/overview) and start testing in production.
</Tip>

With Playwright, writing scripts manually is not the only option. Since browser automation became possible, there have always been tools trying to simplify script creation. Such instruments aim to help users with little or no scripting skills use automation tools, while also saving more expert users time when creating brand new scripts.

Recorders can be used to quickly generate code for a scenario, saving time users would otherwise have to spend inspecting the various pages to find valid selectors. When creating multiple scripts, this adds up to a noticeable amount of time saved.

## How to record automation scripts with Playwright

### Record Playwright scripts with `codegen`

Playwright provides multiple ways to record browser automation scripts. The recommended approach is to leverage [the built-in `codegen` command](https://playwright.dev/docs/codegen-intro#running-codegen).

<img src="https://mintcdn.com/checkly-422f444a/PFNKka5JJJWLiGJ7/images/samples/images/playwright-codegen.jpg?fit=max&auto=format&n=PFNKka5JJJWLiGJ7&q=85&s=6bc0616f17606ac7089cfaa9af3f7af6" alt="Playwright codegen example" width="1200" height="709" data-path="images/samples/images/playwright-codegen.jpg" />

> Pro tip: if you're using [the Playwright VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright#record-new-tests), you can also record and run scripts in your editor.

## Using recorders effectively

Regardless of your chosen approach, you will want to inspect the output scripts to make sure they are doing what you need them to in the fastest and most reliable way possible.

Double-check the newly created scripts and tweak it when necessary, especially keeping an eye out for:

1. Selectors, which should be in line with common [best practices](/learn/playwright/selectors/).
2. [Waits](/learn/playwright/navigation/), which should ensure the right element is present and/or ready for interaction at the right time; also, make sure you get rid of unnecessary waits.
3. Any sort of needless duplication.

## Takeaways

1. Recorders are a powerful tool to speed up script creation.
2. Recorded scripts should always be inspected and possibly tweaked to ensure correctness and efficiency.
3. Script maintenance is still required after scripts have been recorded.

## Further reading

1. [Playwright Codegen](https://playwright.dev/docs/codegen-intro#running-codegen) documentation.

<div className="relative rounded-lg p-6 my-4 bg-gradient-to-b from-[#0c449a] to-[#062047] text-white">
  <div className="text-xl font-bold text-balance mb-1">
    Bugs don't stop at CI/CD. Why would Playwright? <img className="my-auto inline-block w-8 h-8 align-middle -mt-1" src="https://mintcdn.com/checkly-422f444a/EbiaOE1oHX_3_YEg/images/icons/playwright.svg?fit=max&auto=format&n=EbiaOE1oHX_3_YEg&q=85&s=7a281b91e55b4aa6c01bbb63be50402c" alt="Playwright logo" noZoom width="256" height="192" data-path="images/icons/playwright.svg" />
  </div>

  <div className="text-slate-200">
    <a href="https://app.checklyhq.com/signup" target="_blank" className="text-inherit before:content-[''] before:absolute before:inset-0">Sign up</a> and start using Playwright for end-to-end monitoring with Checkly.
  </div>
</div>


Built with [Mintlify](https://mintlify.com).