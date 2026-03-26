# Source: https://momentic.ai/docs/prompting/writing-assertions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Writing assertions

> Guide to asserting on complex application state with Momentic's AI

Momentic's AI is trained to understand HTML, the accessibility tree, and
screenshots. Use a combination of these three modalities to verify assertions.
Read more [here](/prompting/writing-assertions).

## Best practices

* **Keep assertions short and specific**. Break down complex assertions into
  smaller, manageable parts. This helps the AI understand your intentions. We
  recommend using no more than 20 words.
* **Provide useful context**. To avoid misinterpretations, include information
  such as a specific part of the page the AI should focus on or the element you
  are looking for. Explain any non-standard terminology.
* **Avoid ambiguity and subjectivity**: Minimize "grey area" when formulating
  your assertion - the answer to your assertion should be clearly true or false
  given the page state. If your assertion is highly nuanced, explicitly state
  the criteria you want the AI to use. For example, you can say "the textbox
  contains the exact value 'heading1'" rather than "textbox has heading".

## Examples

Here are some good examples of how to write assertions using
[AI check](/steps/ai-check):

| Category                          | Example                                                      |
| --------------------------------- | ------------------------------------------------------------ |
| Presence (or absence) of text     | A congratulations message is shown in the modal              |
| Presence (or absence) of elements | The page shows 3 search results                              |
| Logical statements                | The publish date of this article is more than 30 days ago    |
| Page state                        | There is no error message present on the page                |
| Color                             | The buy button is blue                                       |
| Layout                            | The 'XL' button is the largest button in the submission form |
| Images & video                    | There is a LinkedIn icon on the page                         |

Here are some poorly crafted assertions that are likely to be flaky,
misunderstood, or incorrect:

| Category                               | Bad example                                                                              | Alternative                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Malformed assertion                    | Search results                                                                           | There are search results displayed on the main body                          |
| Ambiguous assertion                    | The order of the results is correct                                                      | The search results are sorted by date                                        |
| Multiple focuses in a single assertion | The logo is blue, the page shows 4 results, and the last result is more than 30 days old | Split into 3 separate assertions                                             |
| Assertion contains an action           | Wait for the results to appear                                                           | Use a wait step if necessary, and then assert that the results have appeared |
| Assertion about imperceivable details  | The color of line divider is #ff5733                                                     | The color of the divider looks red                                           |
| Subjective assertion                   | The page looks well designed                                                             | No text in the table overflows its cell                                      |
| Assertion depends on changes over time | The video plays a 10-second advertisement for an insurance product                       | N/A                                                                          |

## Pre-trained behavior

The assertion agent is pre-trained to follow specific thought patterns to ensure
AI safety, testing consistency, and ease of interaction. Momentic has carefully
tuned the following behaviors.

### Typos

The agent is trained to tolerate and auto-heal minor typos. For example, if you
write "the username is `john@@gmail.com`" but the actual username is
`john@gmail.com`, the AI will pass the assertion since the test author likely
typed an extra `@`.

If your test genuinely relies such on a small difference, explicitly instruct
the agent to *not* to allow any changes and place the desired text in single
quotes. For example, "the username is exactly 'john@@gmail.com'. do not allow
any typos or casing differences".

If you are auto-generating test data, we recommend creating long, distinct
values using JavaScript functions like `crypto.randomUUID()` or
`faker.word.words(3)` so that assertions are unambiguous. Singular words like
`faker.animal.type()` are especially prone to collision.

### Visual criteria

Visual criteria is always verified using the screenshot. The assertion agent is
not allowed to infer the visual state using HTML attributes or CSS properties.
If a described element is not visible in the screenshot (e.g. because it is
hidden, covered, or out of the current viewport), the assertion will be
evaluated as false. Examples of visual criteria include color, size, position,
and shape.

### Vacuously true statements are disallowed

Momentic's agent will fail any assertion that is vacuously true. For example,
suppose the test asserts that the "submit button is not blue" but there is no
submit button on the page at all. Even though this statement is technically
true, the original test author likely intended a button to be present and so
Momentic errs on the side of caution and fails the assertion in this case.

The same line of reasoning applies to dependent elements. For example, if a test
asserts that "the X icon in the modal is active" but there is no modal present
at all, the assertion will be evaluated as false.

### Counts are evaluated exactly

If the assertion states that a certain number of objects are present, the agent
will evaluate the assertion as false if the actual number of objects does not
exactly match the expected number. This includes the case where the actual count
is greater than the expected count.

For example, if the assertion states that "the page shows 3 search results",
Momentic will fail the assertion if there are zero, two, or four search results
on the page.

#### Limited real-world knowledge

Our agent does not have access to up-to-date real-world knowledge such as the
news or the current date. In addition, the agent is also trained to focus on the
current page state. You can pass the agent dynamic context using `{{}}`
[expressions](/javascript#expressions), but we recommend using a
[JavaScript](/steps/javascript) step to evaluate assertions that do not depend
on the page state (e.g. mathematical calculations).

## Data visualizations

You can also assert on SVG or canvas-based data visualizations rendered by
libraries such as [D3](https://d3js.org/),
[Hicharts](https://www.highcharts.com/), [Recharts](https://recharts.org/en-US),
and more.

To improve accuracy, use the following guidelines:

* Maximize or expand your graph so that it takes up a majority of the screen. If
  your charting library does not have this functionality, you can try setting
  `document.body.style.zoom` manually using [JavaScript](/javascript).
* Provide clear labels and units for all axes. Include grid lines when possible.
* For interactive visualizations, use [Click](/steps/click) or
  [Hover](/steps/hover) steps to show tooltips and labels before making
  assertions.

## Troubleshooting

* **Assertions with actions**: The assertion agent cannot execute actions (e.g.,
  "expand the dropdown", "wait for the page to load") and will not be able to
  understand such queries. Instead, split the action and assertion into separate
  steps.
* **Assertions over time**: The AI does not support assertions that evaluate
  changes over time (e.g., "after 5 seconds, a popup appears", "the table has
  shifted upwards"). Instead, use a [Wait](/steps/wait) step to pause the test
  and then check for the expected post-condition.
* **Assertions on small visual details**: Due to resolution downscaling
  performed by AI providers, the AI may not be able to perceive small visual
  details such as exact hex codes, colors of indicator dots, colors of thin font
  faces, and shapes of SVGs smaller than 12px. We recommend keeping assertions
  general enough to avoid these edge cases.
* **Complex math**: The AI may struggle with complex mathematical calculations
  (e.g., "the average slope of the graph is 31.4"). Instead, simplify the
  assertion to a more straightforward comparison (e.g., "the graph shows an
  upward trend").
* **Complex conditionals**: The AI may not handle complex conditional logic well
  (e.g., "if the user is logged in, check that their profile photo is visible;
  otherwise, check that there is a Google icon on the page"). Instead, break it
  down into simpler assertions that do not rely on conditional logic.


Built with [Mintlify](https://mintlify.com).