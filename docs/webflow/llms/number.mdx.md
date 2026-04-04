# Source: https://developers.webflow.com/code-components/reference/prop-types/number.mdx

***

title: Number
slug: reference/prop-types/number
description: Configure a Number property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/number](https://developers.webflow.com/code-components/reference/prop-types/number)'
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Number property to your component so designers can input numeric values.

## Syntax

```tsx
// Prop definition
props.Number({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: number,
    min?: number,
    max?: number,
    decimals?: number,
})

// Prop value
number
```

### Prop definition

Define the Number prop in your Webflow code component with a name. Optionally, you can add a group, tooltip text, and a default value, as well as numeric constraints like min, max, and decimals.

```tsx
props.Number({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: number,
    min?: number,
    max?: number,
    decimals?: number,
})
```

#### Properties

* `name`: The name for the property.
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)
* `defaultValue`: Default value for all component instances. (optional)
* `min`: Minimum value allowed. (optional)
* `max`: Maximum value allowed. (optional)
* `decimals`: Maximum number of decimal places. (optional)

#### Example

```tsx title={"MyComponent.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent, {
    name: "MyComponent",
    description: "A component with a Number property",
    props: {
        count: props.Number({
            name: "Item Count",
            group: "Settings",
            defaultValue: 5,
            min: 1,
            max: 100,
            decimals: 0
        })
    }
});

```

### Prop value

The Number prop provides a numeric value to your React component.

```tsx title="PropType.Number"
number
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/e04f00d5f53fbbfd75c3b29788fad129e83b95e9c352e0cb9d4411fd7a40c5b1/products/code-components/pages/reference/prop-types/assets/number.png" alt="Number property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
count?: number;
}

export const MyComponent = ({ count }: MyComponentProps) => {
return (
    <div className="counter">
    <span>Count: {count}</span>
    </div>
);
}

```

## When to use

Use a Number prop when you want designers to:

* Set numeric values like counts, sizes, or durations
* Control values within specific ranges
* Provide sensible defaults for components
* Limit decimal precision for cleaner data

## Best practices

* Set appropriate min/max values for your use case
* Use decimals: 0 for whole numbers, 1-2 for currency/percentages
* Provide meaningful default values
* Consider the range designers will need
