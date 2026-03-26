# Source: https://momentic.ai/docs/auto-heal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto-healing

> Learn how Momentic makes tests reliable by automatically adjusting to changes in your app

## Natural language locators

During test execution, Momentic uses both traditional and AI-enhanced techniques
to determine whether the original element you targeted still exists on the page.

If the original element is not present, Momentic will attempt to locate a
replacement element on the page that still matches your original description.

If a reasonable result is found and the rest of the test passes, the new target
will be [cached](/step-cache) automatically.

## Smart waiting

Momentic intelligently waits for the page to stabilize before performing each
action. Smart waiting is designed to remove the need for users to add explicit
[Wait](/steps/wait) steps, which is a common source of flakiness.

While smart waiting, Momentic will periodically check if performing the next
step is possible. For example, while waiting for the page to stabilize for a
[Click](/steps/click) step, Momentic will periodically check if the element to
be clicked is present on the page and proceed if so.

The smart waiting timeout is set to 3 seconds by default and is configurable for
each test.

Inputs to smart waiting:

* Navigation events
* `load` events
* Page screenshots
* DOM changes (nodes added, removed, or updated)
* Same-origin requests


Built with [Mintlify](https://mintlify.com).