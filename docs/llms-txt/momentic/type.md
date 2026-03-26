# Source: https://momentic.ai/docs/steps/type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Type

> Typing text into an input field

Type the specified text into an element.

## Inputs

<ResponseField name="Value" type="string" required>
  The text you want to type into the input field.
</ResponseField>

<ResponseField name="Element to type into" type="string" required>
  Description of the element you want to interact with.
</ResponseField>

## Configs

<ResponseField name="Replace content" type="string" default="Only inputs and textareas">
  Choose when the typed content should replace the existing content.

  * `Only inputs and textareas`: Only replace content in input and textarea
    elements.
  * `Never`: Never replace existing content.
  * `Always`: Always replace existing content, regardless of element type (useful
    custom `contenteditable` elements).
</ResponseField>

<ResponseField name="Press enter" type="boolean" default={false}>
  Press the Enter key after typing the text.
</ResponseField>

<ResponseField name="Key press delay" type="number" default={0}>
  Amount of milliseconds to wait after each key press. This is useful for
  triggering on-press event handlers such as autocomplete.
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