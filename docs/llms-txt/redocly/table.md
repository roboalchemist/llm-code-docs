# Source: https://redocly.com/docs/realm/content/markdoc-tags/table.md

# Source: https://redocly.com/learn/markdoc/tags/table.md

# Table Tag [](/learn/markdoc/tags/tag-library#redocly-tag-badge)

The table tag enables you to create tables using a list-based syntax that allows for injection of rich content, like bulleted lists and code samples.
You can also add tables using HTML syntax, but the table tag allows for richer content and is easier to format.

## Syntax and usage

Use the table tag to add tables with rich content to your documentation.

Example syntax:


```markdown
{% table %}

- Option
- Type
- Description

---

- hide
- boolean
- Disables breadcrumb links in the project when set to `true`.\
  Default value: `false`

---

- prefixItems
- [[Breadcrumb object](#breadcrumb-object)]
- A list of breadcrumb links to always be displayed first.

{% /table %}
```

## Attributes

| Option | Type | Description |
|  --- | --- | --- |
| `width` | string | Sets the width of the table row. |
| `align` | string | Sets the text alignment to either `center`, `left`, or `right`.
Default value: `left` |
| `colspan` | number | Sets the column and row span. |


## Examples

The following examples illustrate using rich text in Markdoc tables:

### Example table with bullets

| Type | Description  | Example |
|  --- | --- | --- |
| Sentiment
 | - Includes a question or statement with a thumbs-up and thumbs-down icon.
- This is the default feedback form and displays without configuration.
- Users can express either a positive or negative reaction to the page.

 | ![Sentiment feedback form](/assets/sentiment-01.f8a903c27b0b56a445801013247ea297132c63cbd326864a21df4664001786d2.409f0d4d.png)
 |
| Mood
 | - Includes a question or statement with a smiling-face, neutral-face, and frowning-face icon.
- Users can express a positive, negative, or neutral review of the page.

 | ![Mood feedback form](/assets/mood-01.be1f8847fd9315efb8322fade1af86b352336a7192392215487f431baad59b82.d96f5373.png)
 |
| Rating
 | - Includes a question or statement with five star icons.
- Users can rate a page from one to five stars.

 | ![Rating feedback form](/assets/rating-01.db9ba0181d0b5757b96e0d4151e3be10c94e41be0829e82c3b7d0f626e76f499.d96f5373.png)
 |
| Scale
 | - Includes a question or statement, left-hand side and right-hand side text labels, and buttons for numbers 1 - 10.
- Users can rate a page from one to ten.

 | ![Scale feedback form](/assets/scale-01.911fba40b3203a5efe97ed2c76feb860f8a6081c3d7c6ac50c1efd386253359c.d96f5373.png)
 |
| Comment
 | - Includes a text label and text input.
- Users can use the text field to express their thoughts about the page in a free-form way.

 | ![Comment feedback form](/assets/comment-01.98a6a8629ad72d83abbacdbdf7b9609eba966b55cbb912b4f7d739d5b4445d8e.d96f5373.png)
 |


**Example table with bullets syntax:**


```markdown
{% table %}

- Type
- Description {% width="40%" %}
- Example

---

- Sentiment

- - Includes a question or statement with a thumbs-up and thumbs-down icon.
  - This is the default feedback form and displays without configuration.
  - Users can express either a positive or negative reaction to the page.

- ![Sentiment feedback form](../images/sentiment-01.png)

---

- Mood

- - Includes a question or statement with a smiling-face, neutral-face, and frowning-face icon.
  - Users can express a positive, negative, or neutral review of the page.

- ![Mood feedback form](../images/mood-01.png)

---

- Rating

- - Includes a question or statement with five star icons.
  - Users can rate a page from one to five stars.

- ![Rating feedback form](../images/rating-01.png)

---

- Scale

- - Includes a question or statement, left-hand side and right-hand side text labels, and buttons for numbers 1 - 10.
  - Users can rate a page from one to ten.

- ![Scale feedback form](../images/scale-01.png)

---

- Comment

- - Includes a text label and text input.
  - Users can use the text field to express their thoughts about the page in a free-form way.

- ![Comment feedback form](../images/comment-01.png)

{% /table %}
```

### Example table with code samples

| Option | Type | Description |
|  --- | --- | --- |
| languages | [language object] | **REQUIRED.**
Array of language objects, one per language.
The samples are displayed in the order that they are listed.
Default array value is:
```javascript
[
  { lang: curl },
  { lang: JavaScript },
  { lang: Node.js },
  { lang: Python },
  { lang: Java },
  { lang: C# },
  { lang: PHP },
  { lang: Go },
  { lang: Ruby },
  { lang: R },
  { lang: Payload }
]
```
 |
| skipOptionalParameters | boolean | Excludes optional parameters (cookies, headers, query params) from the generated code samples.
Defaults to `false`. |


**Example table with code sample syntax:**


```markdown
{% table %}

* Option
* Type
* Description

---

* languages
* [language object]
* **REQUIRED.**
  Array of language objects, one per language.
  The samples are displayed in the order that they are listed.
  Default array value is:
  ```javascript
  [
    { lang: curl },
    { lang: JavaScript },
    { lang: Node.js },
    { lang: Python },
    { lang: Java },
    { lang: C# },
    { lang: PHP },
    { lang: Go },
    { lang: Ruby },
    { lang: R },
    { lang: Payload }
  ]
  ```
---

* skipOptionalParameters
* boolean
* Excludes optional parameters (cookies, headers, query params) from the generated code samples.
  Defaults to `false`.

{% /table %}
```

### Example table without headings

| 
| Row 1 Cell 1 | Row 1 Cell 2 |
| Row 2 Cell 1 | Row 2 cell 2 |


**Example table without headings syntax:**


```markdown
{% table %}
---
* Row 1 Cell 1
* Row 1 Cell 2
---
* Row 2 Cell 1
* Row 2 cell 2
{% /table %}
```

## Best practices

Tables are especially useful for displaying complex data in an organized way.

**Do not use tables for layout**

It is best to use CSS for styling if you need to place items side-by-side on the page, not tables.

**Use a list if only one column**

If you only have a single column, a list is probably a better way to display the information.

**Include an introductory sentence**

Introduce tables with an explanatory sentence that describes the significance of the table.