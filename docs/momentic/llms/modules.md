# Source: https://momentic.ai/docs/modules.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Modules

<Warning>
  Editing a module will update all tests that use it. This allows you to
  maintain a single source of truth for your test logic, making it easier to
  manage and update.
</Warning>

Modules are reusable steps that can be shared across multiple tests. This is
particularly useful for complex workflows or when you need to perform the same
actions in different tests.

## Parameters

Parameters allow you to pass different values to the module when you use it in a
test. This way, you can use the same module with different inputs without
duplicating steps.

Parameter keys are strings and parameter values are any valid JavaScript value,
including strings, numbers, booleans, and objects.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/modules/parameters.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=6bf3ee826e0ff9476907a54154f25f19" width="1186" height="520" data-path="images/modules/parameters.png" />
</Frame>

## Caching

By default, modules are not cached, meaning they will always execute. However,
you can enable caching to speed up test execution by skipping steps that have
already been completed.

The return value of the module will be cached, allowing you to use it in
subsequent steps. The return value of a module is the return value of the last
step.

Make sure to configure the cache key and expiry.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/modules/cache-settings.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=ef8845112431d6d84a23aa2a0bc3d977" width="1198" height="456" data-path="images/modules/cache-settings.png" />
</Frame>

### Authentication

<Info>
  Make sure the authenticated session expiry time is longer than the cache
  expiry time. If the session expires, the module will need to be re-executed.
</Info>

<Info>
  Make sure the last step of the module is validating the authentication state
  (e.g. by checking if the user is logged in or if a specific element is
  present). This ensures that the module is only cached when the authentication
  state is valid.
</Info>

If your module is performing authentication logic, you can enable the **Treat as
auth module** option. This will automatically save and restore the
authentication state between test runs, allowing you to reuse the same
authentication session without having to log in again.

Values stored:

* [Cookies](https://playwright.dev/docs/api/class-browsercontext#browser-context-cookies)
* `localStorage`
* [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)


Built with [Mintlify](https://mintlify.com).