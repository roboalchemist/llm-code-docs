# Source: https://developers.webflow.com/designer/reference/element-properties-methods.mdx

***

title: Element properties & methods
slug: designer/reference/element-properties-methods
description: >-
Learn about element properties and their related methods in the Webflow
Designer API
hidden: false
'og:title': 'Webflow Designer API: Element Properties & Methods'
'og:description': >-
Elements have properties that determine what functionality they support. Learn
how to use property-based methods to manipulate elements.
---------------------------------------------------------

Elements in Webflow have properties that determine what functionality they support. These properties are boolean flags that indicate whether an element can have certain features like children, styles, or text content. Each property unlocks a set of related methods that you can use to manipulate the element.

## Core element properties

All elements have a set of core properties that determine what actions you can perform on them:

| Property           | Description                                         | Examples of Elements with Property |
| :----------------- | :-------------------------------------------------- | :--------------------------------- |
| `children`         | Whether the element can contain child elements      | `DivBlock`, `Section`, `Container` |
| `customAttributes` | Whether the element can have custom HTML attributes | Most elements                      |
| `styles`           | Whether the element can have styles applied         | Most elements                      |
| `textContent`      | Whether the element can contain direct text content | `Paragraph`, `Heading`             |
| `appConnections`   | Whether the element can connect with external apps  | `Image`, `FormForm`                |

## Checking element properties

Before using property-based methods, you should always check if the element has the required property:

```typescript
const element = await Webflow.getSelectedElement();

// Check if element can have children
if (element?.children) {
  // Safe to use children-related methods
  await element.append(Webflow.elementPresets.Paragraph);
}

// Check if element can have styles
if (element?.styles) {
  // Safe to use style-related methods
  await element.setStyles([myStyle]);
}
```

## Property-based methods

Each element property unlocks specific functionality that you can use in your Designer Extension:

<CardGroup>
  <Card
    title="Children"
    href="/designer/reference/elements/children"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Scalability.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Scalability.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Methods for adding, retrieving, and managing child elements.
  </Card>

  <Card
    title="Styles"
    href="/designer/reference/elements/styles"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Styles.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Styles.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Methods for applying and managing styles on elements.
  </Card>

  <Card
    title="Text Content"
    href="/designer/reference/elements/text-content"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Typography.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Typography.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Methods for setting and manipulating text content.
  </Card>

  <Card
    title="Custom Attributes"
    href="/designer/reference/elements/custom-attributes"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/CodeBrackets.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/CodeBrackets.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Methods for working with custom HTML attributes.
  </Card>

  <Card
    title="App Connections"
    href="/designer/reference/app-intents-and-connections"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Sync.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Sync.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Methods for connecting elements with external apps.
  </Card>
</CardGroup>

## Best practices

1. **Always check properties before using methods**:
   ```typescript
   if (element?.styles) {
     // Now it's safe to use style methods
     await element.setStyles([myStyle]);
   }
   ```

2. **Combine property and type checks when needed**:
   ```typescript
   if (element.type === "Paragraph" && element.textContent) {
     await element.setTextContent("New paragraph text");
   }
   ```

3. **Handle missing properties gracefully**:
   ```typescript
   try {
     if (!element.children) {
       console.log("This element doesn't support child elements");
       return;
     }

     await element.append(Webflow.elementPresets.Paragraph);
   } catch (error) {
     console.error("Error adding child element:", error);
   }
   ```
