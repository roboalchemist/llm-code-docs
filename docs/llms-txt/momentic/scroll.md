# Source: https://momentic.ai/docs/steps/scroll.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scroll

> Scroll the page

Scroll up, down, left, or right by a specified amount.

## Inputs

<ResponseField name="Pixels to scroll" type="number">
  Number of pixels to scroll the page. Positive values scroll down, negative
  values scroll up. If omitted, scrolls the full height of the viewport for
  vertical directions and the full width for horizontal directions.
</ResponseField>

<ResponseField name="Element to hover when scrolling" type="string">
  Description of the element you want to interact with.
</ResponseField>

## Configs

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