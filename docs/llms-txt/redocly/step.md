# Source: https://redocly.com/docs/realm/content/markdoc-tags/code-walkthrough/step.md

# Step tag

Use the `step` tag to define and organize the individual procedures of a walkthrough.
A code walkthrough primarily consists of a series of steps with their corresponding code snippets that may be further refined into [chunks](/docs/realm/content/markdoc-tags/code-walkthrough#chunk-annotations).

## Attributes

| Attribute | Type | Description |
|  --- | --- | --- |
| id | string | **REQUIRED.** Unique identifier for the code step.
Controls the highlighting behavior in a chunk's `steps` field. |
| heading | string | The header of the code step. |
| when | [Conditions object](#conditions-object) | Conditions for when the step is visible. |
| unless | [Conditions object](#conditions-object) | Conditions for when the step **is not** be visible. |


## Conditions object

Provide conditions for when to display certain UI elements such as toggles or inputs.
You can also add conditions for when to display content such as steps or code sample files when a filter is selected.

| Attribute | Type | Description |
|  --- | --- | --- |
| *{toggle id}* | boolean | True if toggle is enabled. |
| *{filter id}* | string | [string] | A single or list of filter `id`s. |
| *{input id}* | string | [string] | A single or list of input `id`s. |


## Chunk annotations

Chunk annotations ("chunks") are single-line comments you add to code example files to control the highlighting behavior of a code-walkthrough.
Each chunk has an opening and closing annotation, wrapping sections of code.

The exact comment syntax varies between languages, but the chunk syntax remains the same, as in the following examples:

HTML

```html index.html
<head>
  <!-- @chunk {"steps": ["add-script"]} -->
  <script src="script.js"></script>
  <!-- @chunk-end -->
</head>
```

JavaScript
These comment patterns apply to all JavaScript-based files, such as TypeScript and React.


```javascript script.js
// @chunk {"steps": ["select-dom"]}
const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');
// @chunk-end
```

CSS

```css styles.css
/* @chunk {"steps": ["body-defaults"]} */
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
}
/* @chunk-end */
```

Python

```python main.py
# @chunk {"steps": ["app-setup"]}
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
PORT = 5000
# @chunk-end
```

Java

```java Calculator.java
// @chunk {"steps": ["calculator-class"]}
public class CalculatorApplication {

    public static void main(String[] args) {
        SpringApplication.run(CalculatorApplication.class, args);
    }
}
// @chunk-end
```

### Chunk attributes

Each chunk requires either a [step `id`](/docs/realm/content/markdoc-tags/code-walkthrough/step), or a `when` or `unless` condition with a [filter](/docs/realm/content/markdoc-tags/code-walkthrough#filter-object), [toggle](/docs/realm/content/markdoc-tags/code-walkthrough/toggle) or [input id](/docs/realm/content/markdoc-tags/code-walkthrough/input).
The code that is wrapped within a set of chunk annotations is highlighted when the corresponding content in the `step` tags is selected or when the `input` or `toggle` tag condition is met in a code walkthrough.

If you have the same step `id` in two chunks in separate files, selecting the content in the `step` tags for the step `id`, highlights the first file from the list.

| Attribute | Type | Description |
|  --- | --- | --- |
| steps | array | A list of step `id`s that activate the chunk's highlighting. |
| when | [Conditions object](#conditions-object) | Conditions for when the code snippet wrapped in a chunk can be **revealed** with a filter or toggle. |
| unless | [Conditions object](#conditions-object) | Conditions for when the code snippet wrapped in a chunk can be **hidden** with a filter or toggle. |


### Nested chunks

You can nest chunks inside each other to highlight a larger section along with smaller subsections inside them.


```html index.html
<!-- @chunk {"steps": ["hello-world-html", "create-html-file"]} -->
<!DOCTYPE html>
<html lang="en">
  <!-- @chunk {"steps": ["html-head"]} -->
  <head>
    <meta charset="UTF-8">
    <title>Hello World Page</title>
    <!-- @chunk {"steps": ["link-stylesheet"]} -->
    <link rel="stylesheet" href="styles.css">
    <!-- @chunk-end -->
  </head>
  <!-- @chunk-end -->
  <body>
    <p>Hello world.</p>
  </body>
</html>
<!-- @chunk-end -->
```

Using indentation can help organize your chunks and ensure they're all closed.

### Conditional chunks

Similar to the step tag, you can define `when` and `unless` conditions that control the visibility of code snippets wrapped in chunks in the code panel.
Conditions are evaluated against the code walkthrough filters, toggles, and inputs.

The following example includes content that is revealed when "npm" is selected in a "client" filter and different content is displayed when "pip" is selected in the same filter:

Markdown file

```markdoc code-walkthrough.md
{% toggle id="testimonial" label="Add testimonials" when={ "filetype": "React" } %}
{% slot "description" %}
Add testimonials to your landing page.
{% /slot %}

{% step id="step-2b" heading="Add a testimonial" %}
Add a testimonial section to your page using the highlighted code.
{% /step %}
{% /toggle %}
```

Code file

```typescript landing.page.tsx
// @chunk {"steps": ["step-2b"], "unless": {"testimonial": false}}
    <TestimonialsSection>
        <TestimonialQuote>
        "I was able to set up my travel plans in minutes!"
        </TestimonialQuote>
        <p>- Train Travel API user</p>
    </TestimonialsSection>
// @chunk-end
```

## Examples

The following examples demonstrate the `step` tag configurations only.
Other content and configuration is abstracted out.
Line breaks have been added for readability.

### Basic steps


```markdoc Step tag syntax
{% code-walkthrough ... %}

  ## Create HTML Structure

  {% step id="create-html" heading="Create HTML File" %}
    Set up your basic HTML structure in `index.html` with a display and buttons.
  {% /step %}

  ## Add Calculator Display

  {% step id="add-display" heading="Add Calculator Display" %}
    In `index.html`, add a `<div>` for the calculator display.
  {% /step %}

  {% step id="add-css" heading="Add CSS Styles" %}
    Apply styles in `styles.css` to make your calculator look clean and functional.
  {% /step %}

{% /code-walkthrough %}
```

### Conditional steps


```markdoc When attribute syntax
{% code-walkthrough ... %}
  {% step
    id="create-html"
    heading="Create index.html"
    when={ "client": ["HTML"] } // add toggle, input
  %}
    Create `index.html` file with a display and buttons.
  {% /step %}

  {% step
    id="create-react"
    heading="Create App.js"
    when={ "client": "React" }
  %}
    Create `App.js` file with display logic and buttons.
  {% /step %}
{% /code-walkthrough %}
```


```markdoc Unless attribute syntax
{% code-walkthrough ... %}
  {% step
    id="test-client"
    heading="Test Client Calculations"
    unless={ "server": ["Spring (Java)", "Python"] }
  %}
    Test calculator in client application by entering calculations and verifying output.
  {% /step %}

  {% step
    id="test-server"
    heading="Test Server Calculations"
    unless={ "client": "React" }
  %}
    Test the **server-side** calculations by sending requests and verifying responses.
  {% /step %}
{% /code-walkthrough %}
```

## Resources

- Learn how to use Markdoc to create interactive code guides in [Create code walkthrough](/docs/realm/content/markdoc-tags/code-walkthrough/create-code-walkthrough) how-to documentation.
- Control the highlighting behavior of code examples with [chunk annotations](/docs/realm/content/markdoc-tags/code-walkthrough#chunk-annotations).