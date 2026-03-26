# Source: https://momentic.ai/docs/prompting/finding-elements.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Finding elements

> Guide to targeting elements reliably with Momentic's AI

Momentic's AI is trained to understand HTML, the accessibility tree, and
screenshots. Use a combination of these three modalities to describe the
elements you want to interact with.

## Accessibility attributes

<Tip>
  Leveraging accessibility attributes such as `aria-roles`, `aria-labels`, and
  alt text is an existing [best practice](https://playwright.dev/docs/locators)
  in testing. If your app is not accessible, we recommend adding these
  attributes to improve UX and comply with [ADA
  standards](https://www.uschamber.com/co/run/technology/ada-website-accessibility-compliance).
</Tip>

The accessibility tree is how screen readers and other assistive technologies
navigate web pages. As such, the best descriptions reference elements using
their accessibility attributes.

We recommend mentioning the desired element's
[accessibility role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)
in the description, such as "the submit **button**", "the homepage **link**",
"the password **input**", "the 'People' **tab**", or "the **combobox** for
selecting a month".

If you are unsure what attributes to use, you can use
[Chrome Dev Tools](https://developer.chrome.com/blog/full-accessibility-tree#full_accessibility_tree_in_devtools)
to find out.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/a11y-tree-chrome-devtools.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=c828c3a8d4315064049ea015cdef0827" width="2000" height="1178" data-path="images/a11y-tree-chrome-devtools.png" />
</Frame>

## HTML content and attributes

If the desired element contains text content, you can also include a subset or
summary of the text in your description. For example, the "the **'Welcome'**
header" or "the text area containing **'Lorem Ipsum'**".

Momentic's AI also looks at certain high-signal HTML attributes. Values that are
flagged as auto-generated, sensitive, or lengthy are ignored.

<Accordion title="Included HTML attributes">
  ```
  id
  value
  type
  class
  height
  width
  target
  title
  href
  src
  alt
  role
  headers
  scope
  checked
  required
  action

  min
  max
  minlength
  maxlength
  multiple
  pattern
  placeholder
  accept
  contenteditable

  data-value
  data-testid
  data-cy
  data-test-id
  data-test
  data-role
  data-type
  data-key
  data-action
  data-hidden

  data-handleid
  data-handlepos

  data-col-index
  data-row-index
  data-row
  data-col
  ```
</Accordion>

## Typos

Momentic's agents are tuned for helpfulness and will tolerate minor spelling,
casing, and punctuation mismatches. For example, our agent will allow you to a
describe an element like `<button>Sign in</button>` as "the logging in button",
"the sign on button", or even "the signin button".

If you would like to ensure an exact match, you can wrap the desired content in
single quotes and explicitly prompt the agent to disallow any differences in the
element description. For example, "the 'Sign in' button. don't allow any typos".
Alternatively, you can use an [Element Check step](/steps/element-check) to
deterministically validate requirements for the element.

If single quotes are not provided, Momentic's AI will try to use the context
available on the page, as well as past executions, to infer the correct element.

## Visual information

<Warning>
  Momentic's AI can access HTML and a11y tree for the **entire page**, not just
  the current visible viewport. However, it can only access visual information
  from the current visible viewport as it relies on a screenshot of the page.
</Warning>

Momentic's AI is trained to understand visual information like colors, shapes,
sizes, and positions. For example, you can say "the **red** 'Cancel' button",
"the **thumbs up** icon", or "the **hamburger menu** beside the logo".

Due to image quality constraints, we recommend against relying on visual
information alone to identify elements smaller than 12x12 pixels. Vision-based
descriptions are also less reliable when the element is embedded among many
visually similar elements (e.g. a toolbar full of small icons).

## Positional cues

Wen there are multiple instances of the same element (e.g. a data table or
list), you will need to disambiguate which instance you want to interact with.

### Absolute locations

You can provide absolute cues such as "...**at the top** of the page" or
"...**in the bottom right corner**".

### Relative locations

You can provide relative cues such as "...**below** the 'Introduction' header"
or "...**beside** the 'Back' button".

Use the **inside** keyword to specify the parent element of another element. For
example, "the 'Submit' button **inside** the user dialog".

Use the **closest** keyword to specify the closest element to another element.
For example, "the **closest** 'Submit' button to the 'Username' input".

### Ordering

<Warning>
  Since the order of elements on the page can change, make sure to turn off
  [caching](/step-cache). This will ensure Momentic's AI will always target the
  correct element
</Warning>

Use the **nth** keyword to specify the position of an element in a list. For
example, "the **second** 'Submit' button".

## Dynamic elements

<Warning>
  Since the target element will change every time, make sure to turn off
  [caching](/step-cache). This will ensure Momentic's AI will always target the
  correct element
</Warning>

You can target random and dynamic elements with natural language descriptions.
For example, "a **random** card" or "**today's** date in the calendar"

## Examples

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/locator-reference.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=1a101ad2d9cd3df0b50a31410cf87b38" width="2517" height="1266" data-path="images/locator-reference.png" />
</Frame>

Putting it all together, here are some examples of how to describe the labelled
elements in the screenshot above:

1. "the avatar picture on the top left corner"
2. "the home link in the sidebar"
3. "the 'Amount' filter menu"
4. "the notification bell icon to the right of the green button"
5. "the third outgoing transaction card in the list"

## Troubleshooting

* **Dynamic elements**: If you use **nth** or dynamic elements in a description,
  make sure to turn off [caching](/step-cache). This will ensure Momentic's AI
  will always target the correct element.
* **Hidden elements**: Momentic's AI will ignore elements that are explicitly
  marked as `aria-hidden` (or are part of sub-trees that are hidden), not
  attached to the DOM, or have no bounding box.
* **Multiple matches**: If Momentic's AI finds multiple elements that match your
  description, it will select the first one in the DOM order. If you want to
  target a specific instance, use positional cues like **nth**, **closest**, or
  **inside**.


Built with [Mintlify](https://mintlify.com).