# Source: https://developers.webflow.com/code-components/reference/prop-types/visibility.mdx

***

title: Visibility
slug: reference/prop-types/visibility
description: Configure a Visibility property for a code component
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/visibility](https://developers.webflow.com/code-components/reference/prop-types/visibility)'
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Visibility property to your component to choose whether to show or hide elements in Webflow.

## Syntax

```tsx
// Prop definition
props.Visibility({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: boolean,
})

// Prop value
boolean
```

### Prop definition

Define the Visibility prop in your Webflow code component with a name. Optionally, you can add a group, tooltip text, and a default value.

```tsx
props.Visibility({
    name: string,
    group?: string,
    tooltip?: string,
    defaultValue?: boolean,
})
```

#### Properties

* `name`: The name for the property.
* `group`: The group for this property. (optional)
* `tooltip`: The tooltip for the property. (optional)
* `defaultValue`: Default visibility state. (optional)

#### Example

```tsx title={"MyComponent.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { MyComponent } from "./MyComponent";

export default declareComponent(MyComponent, {
    name: "MyComponent",
    description: "A component with a Visibility property",
    props: {
        isVisible: props.Visibility({
            name: "Show Element",
            group: "Display",
            defaultValue: true
        })
    }
});
```

### Prop value

The Visibility prop provides a `boolean` value to your React component.

```tsx title="PropType.Visibility"
boolean
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
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/9b7b102b642ca7093522bcf31663a7936e1b21a30580e6dca96cea526fd310af/products/code-components/pages/reference/prop-types/assets/visibility.png" alt="Visibility property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Example

```tsx title={"MyComponent.tsx"}
import React from "react";

interface MyComponentProps {
isVisible?: boolean;
}

export const MyComponent = ({ isVisible }: MyComponentProps) => {
if (!isVisible) return null;

return (
    <div className="element">
    This element is visible
    </div>
);
}
```

```

## When to use

Use a Visibility prop when you want designers to:
- Show or hide elements conditionally
- Control component display states
- Create toggled content
- Build conditional layouts

## Best practices
- Provide sensible default values
- Handle hidden states gracefully
- Consider accessibility implications
```
