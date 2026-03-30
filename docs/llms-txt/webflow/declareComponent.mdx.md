# Source: https://developers.webflow.com/code-components/reference/hooks/declareComponent.mdx

***

title: Define a code component
slug: reference/hooks/declareComponent
description: Use the declareComponent function to create a code component definition
hidden: false
max-toc-depth: 2
canonical-url: >-
[https://developers.webflow.com/code-components/reference/hooks/declareComponent](https://developers.webflow.com/code-components/reference/hooks/declareComponent)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

## `declareComponent(Component, data)`

The `declareComponent` function is used to create a code component declaration. See the [declare code component guide](/code-components/define-code-component) for more information.

## Syntax

```typescript
declareComponent(Component, data): void;
```

### Parameters

* **`Component`**: The React component to declare
* **`Data`**: An object with: Component metadata, prop definitions, and optional configurations

#### Data object

The `data` object is used to define the component's metadata, prop definitions, and optional configurations. It takes the following properties:

| Property       | Type   | Description                                                                                                                        |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `name`         | string | The name of the component                                                                                                          |
| `description?` | string | A description of the component (optional)                                                                                          |
| `group?`       | string | Group of the component in the component panel (optional)                                                                           |
| `props`        | object | Props for the user to edit in Webflow. See the [prop types reference](/code-components/reference/prop-types) for more information. |
| `options?`     | object | Optional configurations including applying tag selectors, and managing SSR.                                                        |

## Example

```tsx title={"Button.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { Button } from './Button';

// Declare the component
export default declareComponent(Button, {

  // Component metadata
  name: "Button",
  description: "A button component with a text and a style variant",
  group: "Interactive",

  // Prop definitions
  props: {
    text: props.Text({
        name: "Button Text",
        defaultValue: "Click me"
    }),
    variant: props.Variant({
        name: "Style",
        options: ["primary", "secondary"],
        defaultValue: "primary"
    }),
  },
  // Optional configuration
  options: {
    applyTagSelectors: true,
  },
});
```
