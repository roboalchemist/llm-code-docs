# Source: https://developers.webflow.com/code-components/reference/prop-types/slot.mdx

***

title: Slot
slug: reference/prop-types/slot
description: Configure a Slot property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/slot](https://developers.webflow.com/code-components/reference/prop-types/slot)'
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Slot property to your component so designers can insert any child component

## Syntax

```tsx
// Prop definition
props.Slot({
    name: string,
    group?: string,
    tooltip?: string,
})

// Prop value
ReactNode
```

### Prop definition

Define the Slot prop in your Webflow code component with a name. Optionally, you can add a group and tooltip text.

```tsx
props.Slot({
    name: string,
    group?: string,
    tooltip?: string,
})
```

<Tip>
  You can use `props.Children` as an alias for the `props.Slot` prop type.
</Tip>

#### Properties

* `name`: The name for the property.
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)

#### Example

```tsx title={"MyComponent.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent, {
    name: "MyComponent",
    description: "A component with a Slot property",
    props: {
        children: props.Slot({
            name: "Content",
            group: "Content"
        })
    }
});

```

### Prop value

The Slot prop provides child components to your React component as a single `ReactNode` object.

```tsx title="PropType.Slot"
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/8b2b448950fc5ebc7ccded33ce24ac1cbe0612a150a53fbf5b51e3dcdc1fad11/products/code-components/pages/reference/prop-types/assets/slot.png" alt="Slot property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
children?: React.ReactNode;
}

export const MyComponent = ({ children }: MyComponentProps) => {
return (
    <div className="container">
    {children}
    </div>
);
}

```

## When to use

Use a Slot prop when you want designers to:

* Insert child components
* Create flexible layout containers
* Build wrapper components

## Best practices

* Handle missing children gracefully
* Consider layout and spacing for child content
* Test with various component types
