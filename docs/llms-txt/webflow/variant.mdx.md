# Source: https://developers.webflow.com/code-components/reference/prop-types/variant.mdx

***

title: Variant
slug: reference/prop-types/variant
description: Configure a Variant property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/variant](https://developers.webflow.com/code-components/reference/prop-types/variant)'
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Variant property to your component for designers to choose from a predefined list of options.

## Syntax

```tsx
// Prop definition
props.Variant({
    name: string,
    options: string[],
    group?: string,
    tooltip?: string,
    defaultValue?: string,
})

// Prop value
string
```

### Prop Definition

Define the Variant prop in your Webflow code component with a name and list of options. Optionally, you can add a group, tooltip text, and a default value that matches one of the pre-defined options.

```tsx
props.Variant({
    name: string,
    options: string[],
    group?: string,
    tooltip?: string,
    defaultValue?: string,
})
```

#### Properties

* `name`: The name for the property.
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)
* `options`: Array of available variant options.
* `defaultValue`: Default selected option. (optional)

#### Example

```tsx title={"MyComponent.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent, {
    name: "MyComponent",
    description: "A component with a Variant property",
    props: {
        style: props.Variant({
            name: "Button Style",
            group: "Style",
            options: ["Primary", "Secondary", "Tertiary"],
            defaultValue: "Primary"
        })
    }
});
```

### Prop Value

The Variant prop provides a string value representing the selected option to your React component.

```tsx title="PropType.Variant"
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/46b3b9ebd245d3ef0a174be1b5d5651381db000b008210b1a91f4afeeeafdc59/products/code-components/pages/reference/prop-types/assets/variant.png" alt="Variant property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
    style?: "Primary" | "Secondary" | "Tertiary";
}

export const MyComponent = ({ style }: MyComponentProps) => {
    return (
        <button className={`button button--${style?.toLowerCase()}`}>
        Click me
        </button>
    );
}
```

## When to use

Use a Variant prop when you want designers to:

* Choose from predefined visual styles
* Switch between component variations / themes
* Control component appearance

## Best practices

* Use clear, descriptive option names
* Provide a sensible default value
* Keep options list manageable
