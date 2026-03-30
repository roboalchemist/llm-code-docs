# Source: https://developers.webflow.com/code-components/reference/prop-types/text-node.mdx

***

title: Text Node
slug: reference/prop-types/text-node
description: Configure a Text Node property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/text-node](https://developers.webflow.com/code-components/reference/prop-types/text-node)'
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Text Node property to your component. In the Webflow designer, designers can edit the text content of the component on the canvas or via the properties panel.

## Syntax

```tsx
// Prop definition
props.TextNode({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: string,
    multiline?: boolean,
})

// Prop value
ReactNode
```

### Prop definition

Define the Text Node prop in your Webflow code component with a name. Optionally, you can add a group and tooltip text.

```tsx
props.TextNode({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: string,
    multiline?: boolean,
})
```

#### Properties

* `name`: The name for the property.
* `multiline`: Whether the property allows multiple lines of text. (optional)
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)
* `defaultValue`: Default value for all component instances. (optional)

#### Example

```tsx title={"InfoSection.webflow.tsx"}
import { declareComponent } from "@webflow/react";
import { props } from "@webflow/data-types";
import { InfoSection } from "./InfoSection";

export default declareComponent(InfoSection, {
  name: "Info Section",
  description: "A component with a Text Node property",
  props: {
    title: props.TextNode({
      name: "Title",
      group: "Content",
      defaultValue: "Hello World",
    }),
    description: props.TextNode({
      name: "Description",
      multiline: true,
      group: "Content",
      defaultValue: "This is my first Webflow Code Component",
    }),
  },
});

```

### Prop value

The Text Node prop provides formatted HTML content to your React component as a `ReactNode`.

```tsx
ReactNode
```

<div>
  <div>
    #### Properties

    * `n/a`
  </div>

  <div>
    #### Webflow properties panel

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/ca6b827c54df038d715bf193972ff729315317b440205a51b54c45b47a5ffff9/products/code-components/pages/reference/prop-types/assets/text-node.png" alt="Text Node property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"InfoSection.tsx"}
import React from "react";

interface InfoSectionProps {
  title: React.ReactNode;
  description: React.ReactNode;
}

export const InfoSection = ({ title, description }: InfoSectionProps) => {
  return (
    <>
      <h2>{title}</h2>
      <p>{description}</p>
    </>
  );
};

```

## When to use

Use a Text Node prop when you want designers to:

* Edit text content in the webflow editor
* Create text content with HTML markup
* Add structured content like headings and lists

## Best practices

* Provide meaningful default values so the component renders when added to the canvas
* Handle missing content gracefully
* Consider content styling and layout
* Test with various HTML structures
