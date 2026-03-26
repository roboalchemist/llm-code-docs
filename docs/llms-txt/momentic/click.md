# Source: https://momentic.ai/docs/steps/click.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Click

> Clicking on an element on the page

## Inputs

<ResponseField name="Description" type="string" required>
  Description of the element you want to interact with.
</ResponseField>

## Configs

<ResponseField name="Double click" type="boolean" default={false}>
  Double click on the element.
</ResponseField>

<ResponseField name="Right click" type="boolean" default={false}>
  Right click on the element.
</ResponseField>

<ResponseField name="Wait for download" type="boolean" default={false}>
  Wait for the click to initiate a download and for the download to complete. A
  handle to the downloaded file will be returned in the step output. Files
  should not exceed 10MB.
</ResponseField>

<ResponseField name="Download timeout" type="number">
  Number of milliseconds to wait for a download. Defaults to 30000ms if unset.
</ResponseField>

<ResponseField name="Click delay ms" type="number" default={25}>
  Number of milliseconds between each
  [mousedown](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event)
  and
  [mouseup](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event)
  event. Useful for UI handlers that require long presses or only listen to
  mousedown events.
</ResponseField>

<ResponseField name="Relative position" type="boolean" default="false">
  Specify where the click should occur relative to the top-left corner of the
  element.
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