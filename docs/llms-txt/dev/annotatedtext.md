# Source: https://dev.writer.com/components/annotatedtext.md

# Annotated Text

Shows text with annotations

<img src="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=78fb88811d7e3486ed8f72e02339ea92" data-og-width="1134" width="1134" data-og-height="186" height="186" data-path="framework/public/components/annotatedtext.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?w=280&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=56980ae7a8f8654c84b0a414172a7ed9 280w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?w=560&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=fb3c686ec2b2c30c052dbdead7a3a047 560w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?w=840&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=5018721c36762c7198eeb1668d1c4463 840w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?w=1100&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=43db995169cf9b7cc435ba62a8c0ac37 1100w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?w=1650&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=06e4019194d7c2a69ee37c7a3c1798d7 1650w, https://mintcdn.com/writer/mFPGVlLcGxKIh_Y1/framework/public/components/annotatedtext.png?w=2500&fit=max&auto=format&n=mFPGVlLcGxKIh_Y1&q=85&s=148efe3c1584781237183ef0eb5bc722 2500w" />

## Overview

The **Annotated Text** component displays text with visual annotations and highlights. It allows users to see text with embedded annotations that are color-coded to distinguish different types of content or sections.

Annotated text is essential for educational content, document review systems, and any interface where text needs visual distinction between different types of content. It provides a way to highlight important terms and sections without cluttering the main display.

## Common use cases

* **Educational content**: Provide explanations and definitions for complex terms
* **Document review**: Show comments, suggestions, and feedback on text
* **Code documentation**: Highlight and explain code snippets with annotations
* **Research papers**: Show citations, references, and additional context
* **Legal documents**: Display legal annotations and explanations

## How it works

1. **Text content**: Displays the main text content with embedded annotations
2. **Annotation markers**: Shows visual indicators for annotated sections
3. **Styling**: Customize appearance of annotations and text with colors and CSS classes

The component displays text with embedded annotations that are visually highlighted using color coding and styling to distinguish different types of content or sections.

## Configuration options

### Basic settings

* **Annotated text**: The main text with embedded annotation markers, must be a JSON string or a state reference to an array

### Advanced settings

* **Enable markdown**: Adds markdown support for automatically sanitizing unsafe elements
* **Enable copy buttons**: Adds a control bar with both copy text and JSON buttons
* **Rotate hue**: Rotates the hue of annotated text colors depending on the content of the string

### Styling options

* **Text color**: Set the color of the main text
* **Annotation colors**: Set colors for different annotation types
* **Custom CSS classes**: Apply additional styling

## Example

### Contract review and analysis

This example shows how to create a contract review interface with highlighted terms and clauses.

**Interface:**

* File input component for file upload
* Annotated text component for annotated contract content

**Annotated Text configuration:**

* **Annotated text**: JSON array containing contract text with embedded annotations in the format `["text", ["highlighted term", "label"], "more text"]`

## Best practices

1. **Clear annotations**: Make annotation content concise and informative
2. **Visual indicators**: Use clear visual cues to show where annotations exist
3. **Performance**: Limit the number of annotations to avoid overwhelming users
4. **Consistent styling**: Use consistent annotation styling throughout your interface
5. **Context relevance**: Ensure annotations provide relevant and helpful information

## Fields

<table className="componentFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th class="desc">Description</th>
    <th>Options</th>
  </thead>

  <tbody>
    <tr>
      <td>Annotated text</td>
      <td>Object</td>
      <td>Value array with text/annotations. Must be a JSON string or a state reference to an array.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Reference</td>
      <td>Color</td>
      <td>The colour to be used as reference for chroma and luminance, and as the starting point for hue rotation.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Seed value</td>
      <td>Number</td>
      <td>Choose a different value to reshuffle colours.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Rotate hue</td>
      <td>Boolean</td>
      <td>If active, rotates the hue depending on the content of the string. If turned off, the reference colour is always used.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable markdown</td>
      <td>Boolean</td>
      <td>If active, the output will be sanitized; unsafe elements will be removed.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable copy button</td>
      <td>Boolean</td>
      <td>Enable a copy button that lets users to copy the contents in this field to their clipboard</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Button</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Button text</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Primary text</td>
      <td>Color</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Custom CSS classes</td>
      <td>Text</td>
      <td>CSS classes, separated by spaces. You can define classes in custom stylesheets.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>
