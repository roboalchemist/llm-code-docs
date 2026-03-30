# Source: https://developers.webflow.com/flowkit/v1.0.0/variables/typography.mdx

***

title: Typography
slug: variables/typography
description: >-
The typography system provides consistent text styling using variables to
control size, spacing, and hierarchy.
hidden: null
'og:title': Flowkit - Typography
'og:description': >-
The typography system provides consistent text styling using variables to
control size, spacing, and hierarchy.
-------------------------------------

The typography system provides consistent text styling using variables to control size, spacing, and hierarchy.

The base typography variables define the fundamental text properties used throughout the project. These variables are inherited by the default <span class="sg-selector sg-tag">Paragraph</span>, <span class="sg-selector sg-tag">Text</span> elements, and <span class="sg-selector sg-tag">Body</span> tag.

| Base Typography Variable                                    | Property                       |
| ----------------------------------------------------------- | ------------------------------ |
| <span class="sg-selector sg-var">Base Font</span>           | Font Family                    |
| <span class="sg-selector sg-var">Base Font Size</span>      | Font Size (1rem)               |
| <span class="sg-selector sg-var">Base Font Weight</span>    | Font Weight                    |
| <span class="sg-selector sg-var">Base Letter Spacing</span> | Letter Spacing                 |
| <span class="sg-selector sg-var">Base Line Height</span>    | Line Height                    |
| <span class="sg-selector sg-var">Base Margin Bottom</span>  | Margin Bottom (using em units) |

<Note title="Note">
  In the Webflow Variables panel, these variables appear exactly as shown in the 

  **Properties**

   column above.
  In the Styles panel, purple color indicates that the property is linked to a variable.
</Note>

<img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/49589594e89a8159b3bc32a0430db0f02f145fd3b669898f9337e094a4320cde/products/flowkit/pages/v1/typography/flowkit_typography.webp" alt="Styles panel with linked variables" />

***

## Font Family

Font family is applied to text element through the variable. To update the font, make changes in the Variables panel.

| Font Variables                                       | Usage                                                                                                                                                                 |
| ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span class="sg-selector sg-var">Heading Font</span> | <span class="sg-selector sg-tag">All H1-H6 Heading</span> and <span class="sg-selector sg-class">H1-H6 Heading</span> heading selectors                               |
| <span class="sg-selector sg-var">Body Font</span>    | <span class="sg-selector sg-tag">Body</span> tag, <span class="sg-selector sg-tag">All Paragraph</span> tag, default text, text links                                 |
| <span class="sg-selector sg-var">Button Font</span>  | <span class="sg-selector sg-tag">Button</span> tag, <span class="sg-selector sg-class">Button</span> class, <span class="sg-selector sg-class">Tag</span> class, etc. |

***

## Headings

Headings tags and classes are sharing the same varables. It helps keep them sync and manage style through the variables panel.

Here’s how variables are applied to the <span class="sg-selector sg-class">H1 Heading</span> and <span class="sg-selector sg-tag">All H1 Heading</span> tag:

<img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/2298b57e51eba10d32f803fd21cbd5c2795450cafc3788325f76769c87f82e54/products/flowkit/pages/v1/typography/flowkit_heading.webp" alt="Styles panel with linked variables" />

Each heading level has its own responsive variables for different breakpoints, following the same pattern.

<Note title="Subheading">
  For consistency across the site, Flowkit uses the <span class="sg-selector sg-class">Subheading</span> class to accompany headings.
  It works with any text element and automatically inherits its color, applying a transparent tint:
</Note>

***

## Paragraph

Similar to headings, <span class="sg-selector sg-tag">All Paragraphs</span> selector, <span class="sg-selector sg-class">Paragraph</span> class, and its size variations properties controlled through related text variables.

Available paragraph sizes:

* <span class="sg-selector sg-tag">
    All Paragraphs
  </span>
* <span class="sg-selector sg-class">Paragraph</span> (default)
* <span class="sg-selector sg-class">
    Paragraph SM
  </span>
* <span class="sg-selector sg-class">
    Paragraph LG
  </span>
* <span class="sg-selector sg-class">
    Paragraph XL
  </span>
* <span class="sg-selector sg-class">
    Paragraph XXL
  </span>

***

## Default Spacing

Headings and paragraphs have default bottom spacing applied via variables.
For example, the <span class="sg-selector sg-class">H1 Heading</span> and <span class="sg-selector sg-tag">All H1 Heading</span> use the variable <span class="sg-selector sg-var">H1 Margin Bottom</span>
The same pattern applies to paragraphs using <span class="sg-selector sg-var">Base Margin Bottom</span>.

To override this spacing, use a margin utility class such as:
<span class="sg-selector sg-class">\[Utility] Margin Bottom 0</span>

See the full list of margin utilities [here](/flowkit/reference/utilities#margin).

***

## Utility classes

Also check how to use utility classes to override the default behavior of typography classes:

* [Text Color Modifiers](/flowkit/reference/utilities#text-color)
* [Text Alignment Modifiers](/flowkit/reference/utilities#text-alignment)

***

## Best Practices

* **Use variables for consistency** — Modify variables when possible instead of creating custom styles.
* **Choose appropriate sizes** — Use <span class="sg-selector sg-class">Paragraph SM</span> for small text, <span class="sg-selector sg-class">Paragraph LG</span> / <span class="sg-selector sg-class">XL</span> / <span class="sg-selector sg-class">XXL</span> for emphasis.
* **Maintain readability** — Ensure text remains readable at all screen sizes.
* **Preserve hierarchy** — Maintain clear distinction between headings and paragraph text.
* **Semantic order** — Keep the hierarchy in tag usage (e.g., `h1` > `h2` > `h3` > `p`).
* **One H1 tag per page** — Only one <code>h1</code> tag per page. If you need multiple visually styled H1s, apply the <span class="sg-selector sg-class">H1 Heading</span> class instead.
