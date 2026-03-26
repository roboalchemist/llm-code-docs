# Source: https://momentic.ai/docs/ai-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI configuration

> Customize AI behavior in your tests

Momentic uses a variety of agents, each specialized for a specific task within
end-to-end testing. Currently, the following agents can be configured by users:

| Name                                  | Description                                                                                                                                                                                                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Locator (`locator`)                   | Locates elements on the page based on a natural language description. This agent is used for all interactive commands that target elements, such as [Click](/steps/click) and [Type](/steps/type) steps. This agent is also used to resolve elements in [Element check](/steps/element-check) steps. |
| Assertion (`assertion`)               | Evaluates the truthiness of natural language statements based on an instantaneous snapshot of the page. This agent is used to power [AI check](/steps/ai-check) steps.                                                                                                                               |
| Visual Assertion (`visual-assertion`) | Evaluates the truthiness of natural language statements purely based on a screenshot of the current viewport.                                                                                                                                                                                        |
| Text Extraction (`text-extraction`)   | Extracts text from the page based on a natural language description. This agent powers [AI extract](/steps/ai-extract) steps.                                                                                                                                                                        |

Momentic exposes the ability to choose the versions of these agents so that
users can upgrade at their own cadence and test upgrades before applying them.

## Locator

### v1

* Uses older 2024 models.
* Interprets the user's criteria more leniently and will attempt to find a
  candidate element that fulfills the same function as what the user describes.

### v2

* Uses early 2025 models.
* Places a strong emphasis on respecting relative positioning criteria (e.g.
  "the link in the header", "the X icon in the modal"), and will fail if it
  cannot find the reference element.
* Strongly respects single-quoted text (e.g. "the 'Submit' button") and will
  reject candidate elements that do not contain that exact text.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.
* Generates smarter caches:
  * Element attributes: if a prompt specifically refers to certain attributes
    such as text content or position, those will be stored and required to
    remain the same across runs.
  * Relative elements: if a prompt refers to other elements on the page, those
    will also be included in the cache to ensure that any meaningful changes
    result in the cache busting.
* Writes better explanations of its reasoning for choosing elements.

## Assertion

### v1

* Uses older 2024 models.
* Interprets assertion criteria more leniently and will attempt to evaluate
  whether or not an assertion is "overall true" or "overall false".

### v2

* Uses early 2025 models.
* Displays superior understanding of sorted order, visual positioning, and
  relative positioning criteria (e.g. "The button in the modal is enabled").
* Strongly respects single-quoted text (e.g. "element with title='hello world'")
  and will fail the assertion if there is no element that contains that provided
  text.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.

## Visual Assertion

### v1

* Uses older 2024 models.
* Faster, returning results in an average of 3 seconds.
* More lenient when evaluating user criteria against the page state,
  specifically for assertions about color.

### v2

* Uses early 2025 models.
* Slower than V1 but perceives small visual details more accurately.
* Far stronger on logical reasoning, negated assertions, and assertions about
  elements in containers.
* Strongly respects the term "exactly" and single quotes around text terms. Will
  fail the assertion if it not unambiguously true when these modifiers are
  provided.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.

## Text Extraction

### v1

* Uses older 2024 models.

### v2

* Uses early 2025 models.
* Adheres to the provided JSON schema more consistently and will throw an error
  if the extracted data does not conform to the schema.
* Tuned to understand the `pattern` JSON schema option specifically.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.
* Improved ability to handle complex JSON schemas, including nested objects and
  arrays.
* Better at following user instructions for processing or transforming data
  before returning it.


Built with [Mintlify](https://mintlify.com).