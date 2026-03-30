# Source: https://developers.webflow.com/code-components/reference/prop-types/id.mdx

***

title: ID
slug: reference/prop-types/id
description: Configure an ID property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/id](https://developers.webflow.com/code-components/reference/prop-types/id)'
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Add an ID property to your component so designers can set unique identifiers on HTML elements.

The ID prop creates a text input for element IDs, making it easy to target elements with CSS or JavaScript.

## Syntax

```tsx
// Prop definition
props.Id({
    name: string,
    group?: string,
    tooltip?: string,
})

// Prop value
string
```

### Prop definition

Define the ID prop in your Webflow code component with a name. Optionally, you can add a group and tooltip text.

```tsx
props.Id({
    name: string,
    group?: string,
    tooltip?: string,
})
```

#### Properties

* `name`: The name for the property.
* `group`: The group for this property (optional).
* `tooltip`: The tooltip for this property (optional).

#### Example

```tsx title={"MyComponent.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent,    {
    name: "MyComponent",
    description: "A component with an ID property",
    props: {
        id: props.Id({
            name: "Element ID",
            group: "Info"
        })
    }
});
```

### Prop value

The ID prop provides a string to your React component:

```tsx title="PropType.Id"
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/ac1bd8660e095d93d30bffb6bd0110b6a24b5162317aab3f60a734d1f494bdc6/products/code-components/pages/reference/prop-types/assets/id.png" alt="ID property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
id?: string;
}

export const MyComponent = ({ id }: MyComponentProps) => {
return (
    <div id={id}>
    {/* Component content */}
    </div>
);
}
```

## When to use

Use an ID prop when you want designers to:

* Set unique identifiers for CSS targeting
* Connect form labels to inputs
* Enable JavaScript interactions
