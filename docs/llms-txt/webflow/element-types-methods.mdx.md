# Source: https://developers.webflow.com/designer/reference/element-types-methods.mdx

***

title: Element Types & Methods
slug: designer/reference/element-types-methods
description: >-
Learn about different element types and their specific methods in the Webflow
Designer API
hidden: false
'og:title': 'Webflow Designer API: Element Types & Methods'
'og:description': >-
Each element type in Webflow has specific methods based on its functionality.
Learn how to use type-specific methods to manipulate different elements.
------------------------------------------------------------------------

Each element in Webflow has a specific type that determines its functionality and available methods. While all elements share some [common properties](/designer/reference/element-properties-methods), each element type also has specialized methods that allow you to manipulate that element's unique characteristics.

## Identifying element types

You can identify an element's type using the `element.type` property:

```typescript
const element = await Webflow.getSelectedElement();
console.log(element.type); // "DOM", "String", "Image", etc.
```

## Element presets

To add a specific element type to the canvas, you can use the [`webflow.elementPresets` object](/designer/reference/element-presets), which contains a set of presets for different element types available in the designer.

```typescript
const element = await webflow.elementPresets.DOM;
await webflow.addElement(element);
```

## Element type methods

Different element types have unique methods tailored to their functionality. Always check an element's type before applying type-specific methods.

<CardGroup>
  <Card
    title="DOM Elements"
    href="/designer/reference/dom-element"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/CodeBrackets.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/CodeBrackets.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Customize HTML elements with methods for HTML tags and attributes.
  </Card>

  <Card
    title="Strings"
    href="/designer/reference/string-element"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Typography.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Typography.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Work with text content and manipulate their text values.
  </Card>

  <Card
    title="Images"
    href="/designer/reference/image-element"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Image.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Image.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Manage images and alt text.
  </Card>

  <Card
    title="Headings"
    href="/designer/reference/heading-element"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/TypographyDetails.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/TypographyDetails.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Modify heading levels and heading content.
  </Card>

  <Card
    title="Links"
    href="/designer/reference/link-element"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/SiteWWW.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/SiteWWW.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Configure links with methods for URLs, targets, and link settings.
  </Card>

  <Card
    title="Forms"
    href="/designer/reference/forms"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Test.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Test.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Create and configure forms and form field settings.
  </Card>

  <Card
    title="Components"
    href="/designer/reference/component-element"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Components.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Components.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Get components definitions from a component instance.
  </Card>
</CardGroup>

## Best Practices for Element Type Methods

1. **Always check element type before applying type-specific methods**:
   ```typescript
   if (element.type === "Image") {
     // Now it's safe to use Image methods
     await element.setAltText("Description");
   }
   ```

2. **Handle multiple element types with type guards**:
   ```typescript
   function handleElement(element) {
     switch(element.type) {
       case "String":
         return element.getText();
       case "Image":
         return element.getAsset();
       default:
         return null;
     }
   }
   ```

3. **Combine property and type checks for maximum safety**:
   ```typescript
   if (element.type === "DOM" && element.children) {
     // Safe to use DOM methods and children methods
     await element.setTag("div");
     await element.append(Webflow.elementPresets.Paragraph);
   }
   ```
