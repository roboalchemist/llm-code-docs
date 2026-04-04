# Source: https://developers.webflow.com/designer/reference/bulk-add-elements.mdx

***

title: Bulk Add Elements
slug: designer/reference/bulk-add-elements
description: Create complex element structures efficiently with the element builder API
hidden: false
'og:title': 'Webflow Designer API: Bulk Add Elements'
'og:description': >-
Learn how to create complex element structures efficiently with the element
builder API
-----------

## `webflow.elementBuilder(preset)`

Construct complex element structures before adding them to a page. This method is optimized for bulk creation of elements, and is particularly useful when working with SVG graphics or nested element groups like a navigation menu. This approach is more efficient than creating and adding elements one at a time, especially for complex designs.

<Warning title="Current Limitations">
  Currently, only DOM elements can be created with the element builder.
</Warning>

### Syntax

```typescript
webflow.elementBuilder(elementPreset: webflow.elementPresets.DOM): BuilderElement
```

### Parameters

* **preset**: The DOM element preset from the Webflow presets. Currently, only DOM elements are supported.

### Returns

**BuilderElement**

A builder element object designed for creating and manipulating hierarchical structures. This object has these methods:

* `append()`: Add a child element to this builder element
* `setTag()`: Set the HTML tag for this DOM element
* `setAttribute()`: Set an attribute on this DOM element
* `setTextContent()`: Set the text within this DOM element
* `setStyles()`: Set styles on this DOM element

## How to use the element builder

<Steps>
  <Step>
    **Get the parent element** <br />
    Use `webflow.getSelectedElement()` to select the parent element. This is where your new structure will be added.
  </Step>

  <Step>
    **Create a builder element** <br />
    Use `webflow.elementBuilder(webflow.elementPresets.DOM)` to create a builder element.
  </Step>

  <Step>
    **Configure the builder element** <br />
    Use the builder element to configure the tags, attributes, and styles of the new structure.
  </Step>

  <Step>
    **Add child elements** <br />
    Use `append()` to add child elements to the builder element. Configure them with tags, attributes, and styles.
  </Step>

  <Step>
    **Add the complete structure to your page** <br />
    Use `append()` on the parent element to add the complete structure to your page.
  </Step>
</Steps>

### Examples

<Tabs>
  <Tab title="Create a navigation menu">
    This example shows how to use element builder to create a navigation menu:

    <CodeBlock>
      ```typescript
      async function createNavMenu() {
        // Start by creating some styles that will be applied to the nav container.
        const navStyle = await webflow.createStyle('navContainer');
        await navStyle.setProperties({
          'display': 'flex',
          'row-gap': '20px',
          'padding-left': '15px',
          'padding-right': '15px',
          'padding-top': '15px',
          'padding-bottom': '15px',
          'background-color': '#f5f5f5',
          'border-radius': '8px'
        });

        const navItemStyle = await webflow.createStyle('navItem');
        await navItemStyle.setProperties({
          'color': '#333',
          'text-decoration': 'none',
          'padding-left': '12px',
          'padding-right': '12px',
          'padding-top': '8px',
          'padding-bottom': '8px',
          'border-radius': '4px',
          'font-weight': '500'
        });

        // Get the selected element as the container
        const selectedElement = await webflow.getSelectedElement();

        // Create a nav container
        const navMenu = webflow.elementBuilder(webflow.elementPresets.DOM);
        navMenu.setTag('nav');
        navMenu.setStyles([navStyle]);

        // Menu items to add
        const menuItems = ['Home', 'About', 'Services', 'Portfolio', 'Contact'];

        // Create all menu items at once and store references for later
        const menuItemRefs = [];
        menuItems.forEach(itemText => {
          const item = navMenu.append(webflow.elementPresets.DOM);
          item.setTag('a');
          item.setAttribute('href', '#');
          item.setTextContent(itemText);
          item.setStyles([navItemStyle]);
          // Store reference to set text later
          menuItemRefs.push(item);
        });

        // Add the entire menu to the canvas in one operation
        if (selectedElement?.children) {
          await selectedElement.append(navMenu);
          console.log('Navigation structure with 5 items created in one operation');
        }
      }
      ```
    </CodeBlock>
  </Tab>

  <Tab title="SVG with multiple paths">
    This example shows how to create a nested SVG structure:

    <CodeBlock>
      ```typescript
      async function webflowRainbow() {
        // Get the selected element as the container
        const selectedElement = await webflow.getSelectedElement();

        // Create an SVG builder element
        const svgBuilder = webflow.elementBuilder(webflow.elementPresets.DOM);
        svgBuilder.setTag('svg');
        svgBuilder.setAttribute('viewBox', '0 0 100 100');
        svgBuilder.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
        svgBuilder.setAttribute('width', '200');
        svgBuilder.setAttribute('height', '200');

        // Create rainbow circular background with multiple circles
        const backgroundElements = [];
        const rainbowColors = [
          'hsl(0, 90%, 55%)',    // Red
          'hsl(30, 90%, 55%)',   // Orange
          'hsl(60, 90%, 55%)',   // Yellow
          'hsl(120, 90%, 55%)',  // Green
          'hsl(240, 90%, 55%)',  // Blue
          'hsl(270, 90%, 55%)',  // Indigo
          'hsl(300, 90%, 55%)'   // Violet
        ];

        for (let i = 0; i < 7; i++) {
          const circle = svgBuilder.append(webflow.elementPresets.DOM);
          circle.setTag('circle');
          circle.setAttribute('cx', '50');
          circle.setAttribute('cy', '50');
          circle.setAttribute('r', `${46 - (i * 3)}`);
          circle.setAttribute('fill', 'none');
          circle.setAttribute('stroke', rainbowColors[i]);
          circle.setAttribute('stroke-width', '2.5');
          circle.setAttribute('opacity', '0.9');
          backgroundElements.push(circle);
        }

        // Create the central background circle
        const centralCircle = svgBuilder.append(webflow.elementPresets.DOM);
        centralCircle.setTag('circle');
        centralCircle.setAttribute('cx', '50');
        centralCircle.setAttribute('cy', '50');
        centralCircle.setAttribute('r', '32');
        centralCircle.setAttribute('fill', 'white');

        // Create the "Webflow" logo
        const logoPath = svgBuilder.append(webflow.elementPresets.DOM);
        logoPath.setTag('path');
        logoPath.setAttribute('d', 'M61.3811 14L43.0716 49.7933H25.8737L33.5362 34.959H33.1924C26.8709 43.1653 17.439 48.5674 4 49.7933V35.1643C4 35.1643 12.5972 34.6565 17.6513 29.3429H4V14.0003H19.3426V26.6194L19.687 26.6179L25.9565 14.0003H37.5597V26.5393L37.9041 26.5388L44.4089 14H61.3811Z');
        logoPath.setAttribute('fill', '#146EF5');
        logoPath.setAttribute('fill-rule', 'evenodd');
        logoPath.setAttribute('clip-rule', 'evenodd');
        logoPath.setAttribute('transform', 'translate(30.5, 30.5) scale(0.7)');

        // Add the entire SVG structure to the canvas in one operation
        if (selectedElement?.children) {
          await selectedElement.append(svgBuilder);
          console.log('webflow logo created successfully');
        }
      }
      ```
    </CodeBlock>
  </Tab>
</Tabs>

## When to use element builder

The element builder is particularly useful for:

* **Complex Element Structures**: When creating hierarchies with many nested elements
* **SVG Creation**: Perfect for building SVG graphics with many path, circle, or other elements
* **Repeating Patterns**: When you need to create many similar elements
* **Performance**: More efficient than adding elements one-by-one to the canvas

## Best practices

* **Build Complete Structures**: Create your entire element structure before adding it to the canvas
* **Set Properties**: Configure tags, attributes, styles, and text content on builder elements before appending
* **Track References**: If you need to modify elements after adding to canvas, store references to them
* **Batch Operations**: Use `Promise.all` for batch operations when modifying multiple elements
