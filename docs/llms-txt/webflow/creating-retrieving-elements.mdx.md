# Source: https://developers.webflow.com/designer/reference/creating-retrieving-elements.mdx

***

title: Creating & Retrieving Elements
slug: designer/reference/creating-retrieving-elements
description: >-
Learn how to create, select, and manipulate elements in the Webflow Designer
using the Designer API
hidden: false
hide-nav-links: true
'og:title': 'Webflow Designer API: Creating & Retrieving Elements'
'og:description': >-
Methods for creating, selecting, and manipulating elements in the Webflow
Designer canvas
---------------

Managing elements is a core aspect of working with the Webflow Designer API. This section covers methods for creating new elements, selecting existing ones, and managing their placement in the element hierarchy.

<video autoplay loop muted>
  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_Get%20Selected%20Element.webm" type="video/webm" />

   Your browser doesn't support HTML video.
</video>

## Element selection

Before manipulating elements on the canvas, you typically need to select them. The Designer API provides methods to get references to existing elements:

```typescript
// Get the currently selected element
const selectedElement = await webflow.getSelectedElement();

// Get all elements on the page
const allElements = await webflow.getAllElements();

// Programmatically select an element
await webflow.setSelectedElement(elementToSelect);

// Get element children and select the first child
if (selectedElement?.children) {
  const children = await selectedElement.children;
  await webflow.setSelectedElement(children[0]);
}
```

## Adding elements to the Canvas

When adding elements to your design, you need to consider their placement within the [element hierarchy](https://university.webflow.com/lesson/element-hierarchy?topics=getting-started). The Designer API provides several methods for inserting elements precisely where you need them. Including:

| Method                                                      | Description                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------- |
| [`before()`](/designer/reference/insert-element-before)     | Insert a new element before the target element.                |
| [`after()`](/designer/reference/insert-element-after)       | Insert a new element after the target element.                 |
| [`prepend()`](/designer/reference/prepend)                  | Insert a new element as the first child of the target element. |
| [`append()`](/designer/reference/append)                    | Insert a new element as the last child of the target element.  |
| [`elementBuilder()`](/designer/reference/bulk-add-elements) | Add multiple elements at once with a hierarchical structure.   |

### Element presets

The Designer API uses Element Presets to specify which type of element to create. Each preset corresponds to a unique element type in Webflow. Some [element types include their own properties and methods](/designer/reference/element-types-methods).

For a complete list of available presets, refer to the [Element Presets](/designer/reference/element-presets) documentation. These presets can be used with any of the element creation methods shown below.

<Warning title="Use custom DOM elements when presets aren't available">
  Not all element types are supported through presets. If a preset isn't
  available for the element you want to create, you can use the [custom DOM
  element](/designer/reference/dom-element) method to create a custom element.
</Warning>

### Inserting elements next to existing elements

To position an element alongside existing elements:

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement();

if (selectedElement) {
  // Insert a div after the selected element
  const newDivAfter = await selectedElement.after(
    webflow.elementPresets.DivBlock
  );

  // Insert a div before the selected element
  const newDivBefore = await selectedElement.before(
    webflow.elementPresets.DivBlock
  );
}
```

<Note title="Parent elements">
  If the selected element has a parent element, the new element created using
  `before()` or `after()` will also be a child element of the same parent.
</Note>

### Nesting elements within parent elements

To create parent-child relationships by nesting elements:

```typescript
// Get Selected Element
const parentElement = await webflow.getSelectedElement();

// Check if element supports child elements
if (parentElement?.children) {
  // Add element as first child (prepend)
  const firstChild = await parentElement.prepend(
    webflow.elementPresets.DivBlock
  );

  // Add element as last child (append)
  const lastChild = await parentElement.append(
    webflow.elementPresets.Paragraph
  );
}
```

### Bulk adding elements

For more complex structures, you can create multiple elements at once using [element builder](/designer/reference/bulk-add-elements):

```typescript maxLines=10
// Create an element structure using elementBuilder
const selectedElement = await webflow.getSelectedElement();

// Create a section element as the root
const section = webflow.elementBuilder(webflow.elementPresets.DOM);
section.setTag("section");

// Add a container child element
const container = section.append(webflow.elementPresets.DOM);
container.setTag("div");
container.setAttribute("class", "container");

// Add heading and paragraph to the container
const heading = container.append(webflow.elementPresets.DOM);
heading.setTag("h2");

const paragraph = container.append(webflow.elementPresets.DOM);
paragraph.setTag("p");

// Add the entire structure to the canvas in one operation
if (selectedElement?.children) {
  await selectedElement.append(section);

  // After adding to canvas, find elements and set text content
  const elements = await webflow.getAllElements();

  // Find the heading and paragraph elements by their IDs
  const headingEl = elements.find((el) => el.id.element === heading.id);
  const paragraphEl = elements.find((el) => el.id.element === paragraph.id);

  // Set text content on the elements
  if (headingEl) await headingEl.setTextContent("Hello World");
  if (paragraphEl)
    await paragraphEl.setTextContent("Created with element builder");
}
```

## Removing elements

To remove an element from the canvas:

```typescript
// Get Selected Element
const elementToRemove = await webflow.getSelectedElement();

if (elementToRemove) {
  // Remove the element
  await elementToRemove.remove();
}
```

## Methods

The Elements API offers the following methods for element creation and manipulation:

<CardGroup>
  <Card title="Get selected element" href="/designer/reference/get-selected-element">
    Retrieve the currently selected element in the Designer.
  </Card>

  <Card title="Set selected element" href="/designer/reference/set-selected-element">
    Programmatically select an element in the Designer.
  </Card>

  <Card title="Get all elements" href="/designer/reference/get-all-elements">
    Retrieve all elements on the current page.
  </Card>

  <Card title="Insert element before" href="/designer/reference/insert-element-before">
    Insert a new element before the target element.
  </Card>

  <Card title="Insert element after" href="/designer/reference/insert-element-after">
    Insert a new element after the target element.
  </Card>

  <Card title="Prepend" href="/designer/reference/prepend">
    Insert a new element as the first child of the target element.
  </Card>

  <Card title="Append" href="/designer/reference/append">
    Insert a new element as the last child of the target element.
  </Card>

  <Card title="Bulk add elements" href="/designer/reference/bulk-add-elements">
    Add multiple elements at once with a hierarchical structure.
  </Card>

  <Card title="Remove element" href="/designer/reference/remove-element">
    Remove an element from the canvas.
  </Card>
</CardGroup>

{" "}
