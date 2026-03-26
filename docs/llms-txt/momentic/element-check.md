# Source: https://momentic.ai/docs/steps/element-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Element check

> Assert on a specific element

This step asserts on a specific element's content, attributes, or state.

When a usable cached target exists, `ELEMENT_CHECK` retries with cache-only
resolution during the timeout window. If those retries still fail, it performs
one final AI locate attempt after the timeout window elapses.

Assertion types:

* **Content**: Verify the text content of an element.
* **Attribute**: Verify the value of an attribute on an element.
* **State**:Verify the state of an element, such as whether it is visible or
  enabled.

## Inputs

<ResponseField name="Description" type="string" required>
  Description of the element you want to assert on.
</ResponseField>

## Configs

<ResponseField name="Timeout" type="number">
  The maximum number of seconds to wait for the check to be true. If it becomes
  true at any point during that window, the step passes. The step may continue
  running for a bit longer due to the latency of the final check, which starts
  when the timeout is reached.
</ResponseField>

<ResponseField name="Disable stability checks" type="boolean" default={false}>
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean" default={false}>
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean" default={false}>
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


Built with [Mintlify](https://mintlify.com).