# Source: https://momentic.ai/docs/steps/drag-and-drop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Drag and drop

> Drag and drop elements across the page

This step allows you to drag an element from one location to another on the
page.

## Inputs

<ResponseField name="Element to drag" type="string" required>
  Description of the element where you are initiating drag.
</ResponseField>

<ResponseField name="Drag destination element" type="string" required>
  Description of the element where you are dropping the dragged element.
</ResponseField>

## Configs

<ResponseField name="Hover duration" type="number">
  Number of seconds to wait before dropping the element. This can be useful for
  ensuring that mouse and hover events are triggered before the drop completes.
</ResponseField>

<ResponseField name="Drag segments" type="number" default="5">
  Number of intermediate segments to use when dragging the mouse. Increasing
  this value sends more incremental move events, creating a smoother drag.
  Defaults to 5 segments if unset.
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