# Source: https://developers.webflow.com/code-components/reference/prop-types/rich-text.mdx

***

title: Rich Text
slug: reference/prop-types/rich-text
description: Configure a Rich Text property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/rich-text](https://developers.webflow.com/code-components/reference/prop-types/rich-text)'
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Rich Text property to your component so designers can create formatted content with HTML markup.

## Syntax

```tsx
// Prop definition
props.RichText({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: string,
})

// Prop value
ReactNode
```

### Prop definition

Define the Rich Text prop in your Webflow code component with a name. Optionally, you can add a group and tooltip text.

```tsx
props.RichText({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: string,
})
```

#### Properties

* `name`: The name for the property.
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)
* `defaultValue`: Default value for all component instances. (optional)

#### Example

```tsx title={"MyComponent.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent, {
    name: "MyComponent",
    description: "A component with a Rich Text property",
    props: {
        content: props.RichText({
            name: "Content",
            group: "Content"
        })
    }
});

```

### Prop value

The Rich Text prop provides formatted HTML content to your React component as a `ReactNode`.

```tsx title="PropType.RichText"
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/f74e012d1228098c4cc8bbe57887ce669374e58afc4608dd58db3a7c8af69644/products/code-components/pages/reference/prop-types/assets/rich-text.png" alt="Rich Text property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
content?: React.ReactNode;
}

export const MyComponent = ({ content }: MyComponentProps) => {
return (
    <div className="content-wrapper">
    {content}
    </div>
);
}

```

## When to use

Use a Rich Text prop when you want designers to:

* Create formatted content with bold, italic, links
* Add structured content like headings and lists
* Include HTML markup in their content

## Best practices

* Provide meaningful default values so the component renders when added to the canvas
* Handle missing content gracefully
* Consider content styling and layout
* Test with various HTML structures
