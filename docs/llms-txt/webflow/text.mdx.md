# Source: https://developers.webflow.com/code-components/reference/prop-types/text.mdx

***

title: Text
slug: reference/prop-types/text
description: Configure a Text property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/text](https://developers.webflow.com/code-components/reference/prop-types/text)'
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Text property to your component for designers to input plain text content.

## Syntax

```tsx
// Prop definition
props.Text({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: string,
})

// Prop value
string
```

### Prop Definition

Define the Text prop in your Webflow code component with a name. Optionally, you can add a default value, group, and tooltip text.

```tsx
props.Text({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: string,
})
```

<Tip>
  You can use `props.String` as an alias for the `props.Text` prop type.
</Tip>

#### Properties

* `name`: The name for the property.
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)
* `defaultValue`: Default value for all component instances. (optional)

#### Example

```tsx title={"MyComponent.Webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent, {
    name: "MyComponent",
    description: "A component with a Text property",
    props: {
        title: props.Text({
            name: "Title",
            group: "Content",
            defaultValue: "Hello World!"
        })
    }
});
```

### Prop Value

The Text prop provides a string value to your React component.

```tsx title="PropType.Text"
string
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/523987d0c97f665398ab5af2538991eef98a7caffee9aa3e5c2b9fd074e776f6/products/code-components/pages/reference/prop-types/assets/text.png" alt="Text property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
title?: string;
}

export const MyComponent = ({ title }: MyComponentProps) => {
return (
    <h1 className="title">
    {title}
    </h1>
);
}

```

## When to use

Use a Text prop when you want designers to:

* Input simple text content
* Set titles, labels, or descriptions

## Best practices

* Provide meaningful default values so the component renders when added to the canvas
* Use descriptive prop names
