# Source: https://developers.webflow.com/code-components/define-code-component.mdx

***

title: Define a code component
slug: define-code-component
description: Learn about the structure and purpose of code component definition files
hidden: false
max-toc-depth: 3
subtitle: 'Learn how to map React components to Webflow with component definition files. '
canonical-url: '[https://developers.webflow.com/code-components/define-code-component](https://developers.webflow.com/code-components/define-code-component)'
-------------------------------------------------------------------------------------------------------------------------------------------------------------

A code component definition is a file that tells Webflow how to use your React component on the Webflow canvas. It defines which properties designers can configure and how they’ll appear in the designer.

Every code component definition is a `.webflow.tsx` file that uses the `declareComponent` function to define the component.

<CodeBlocks>
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

  ```tsx title={"Button.tsx"}
  import React from 'react';
  import styles from './Button.module.css';

  interface ButtonProps {
    text: string;
    variant: 'primary' | 'secondary';
  }

  export const Button: React.FC<ButtonProps> = ({ text, variant }) => {
    return (
      <button
        className={`${styles.button} ${styles[variant]}`}
        type="button"
      >
        {text}
      </button>
    );
  };
  ```
</CodeBlocks>

## File structure and naming

Code component definition files follow specific extension and naming patterns:

* **File extension**: `.webflow.tsx` or `.webflow.ts`
* **Naming pattern**: `ComponentName.webflow.tsx` (where `ComponentName` matches your React component)
* **Location**: Typically alongside your React component file

If you have specific naming needs, you can [configure this pattern in `webflow.json`.](/code-components/installation)  It's recommended to create your code component file alongside your React component, adding `.webflow` to the name. For example, `Button.webflow.tsx` for `Button.tsx`.

<Warning title="File names are the unique identifier of your code component">
  Renaming a definition file creates a new component and removes the old one from your library. If designers are already using the old component in their projects, those instances will break and need to be manually replaced.
</Warning>

## Imports

Every code component definition file needs to import your React component, Webflow functions, and any styles you want to apply to the component.

```tsx title={"Button.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { props } from '@webflow/data-types';
import { Button } from './Button';

```

<Note title="Importing styles">
  To apply global styles or integrate CSS-in-JS libraries, configure a global decorators file with [component decorators](#component-decorators).
</Note>

## Declare component

The `declareComponent` function creates a code component definition. It takes two arguments: the React component and a configuration object.

```tsx title={"Button.webflow.tsx"}
import { declareComponent } from '@webflow/react';
import { Button } from './Button';
import { styledComponentsShadowDomDecorator } from "@webflow/styled-components-utils";
import { props } from '@webflow/data-types';

// Declare the component
export default declareComponent(Button, {

  // Component metadata
  name: "Button",
  description: "A button component with a text and a style variant",
  group: "Interactive",
  decorators: [styledComponentsShadowDomDecorator],
  props: {
    text: props.Text({
      name: "Button Text",
      defaultValue: "Click me"
    }),
  },
});
```

* **`name`**: The name designers see in the component panel
* **`description?`**: Description to provide context for the component's purpose (optional)
* **`group?`**: Organize components into groups in the component panel (optional)
* **`props?`**: Object defining the props of the component (optional)
* **`decorators?`**: Array of decorators to apply to the component (optional)
* **`options?`**: Object defining the options of the component (optional)

## Prop definitions

The `props` object defines which properties of your React component a designer can edit in Webflow. Declare a prop for each editable property in your React component and provide metadata that will appear in the designer. To see a list of all available prop types and their configuration options, see the [prop types reference. →](/code-components/reference/prop-types)

The below examples show a React component, its corresponding code component definition file, and how it appears in Webflow.

<Tabs>
  <Tab title="React component">
    This React component expects a `buttonText` property, and a `variant` property.

    ```tsx title={"Button.tsx"}
    import React from 'react';
    import styles from './Button.module.css';

    interface ButtonProps {
      text: string;
      variant: 'primary' | 'secondary';
    }

    export const Button: React.FC<ButtonProps> = ({ text, variant }) => {
      return (
        <button
          className={`${styles.button} ${styles[variant]}`}
          type="button"
        >
          {text}
        </button>
      );
    };
    ```
  </Tab>

  <Tab title="Code component">
    This code component definition file declares a `buttonText` and `variant` prop for the `Button` component.

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
    });
    ```
  </Tab>

  <Tab title="Component in Webflow">
    Once shared with designers, the component will appear in the component panel. And can be added to a page with editable props.

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/3c51c1cf23c2277a83f4c864587594d1e6498a20b24cb4051a821a7ad88c8d4c/products/code-components/pages/guides/assets/button.png" alt="Webflow props" />
      </Frame>
    </div>
  </Tab>
</Tabs>

See more examples in the [prop types reference. →](/code-components/reference/prop-types)

## Component decorators

Decorators are functions that wrap your React component with providers or other wrapper components. Use them to provide context like themes, internationalization, or feature flags, or to integrate CSS-in-JS libraries. For CSS-in-JS setup, see the [frameworks and libraries guide](/code-components/frameworks-and-libraries).

### Global styles

To apply global styles across all components, import your CSS in a global decorators file and reference it in `webflow.json`:

<CodeBlocks>
  ```ts title={"globals.ts"}
  import "./globals.css";


  ```

  ```css title={"globals.css"}
  :root {
    --primary-color: #007bff;
    --font-family: system-ui, sans-serif;
  }


  ```
</CodeBlocks>

```json title="webflow.json"
{
  "library": {
    "globals": "./src/globals.ts"
  }
}
```

### Custom decorators

Create a custom decorator when you need to wrap components with additional behavior. A decorator is a higher-order component that takes a component and returns a wrapped version. This example wraps a data-fetching component with an error boundary to handle API failures gracefully:

<CodeBlocks>
  ```tsx title={"ErrorBoundary.tsx"}
  // Custom error boundary component that catches JavaScript errors in child components and displays a fallback UI

  import React, { Component, ErrorInfo, ReactNode } from "react";

  interface Props {
    children: ReactNode;
  }

  interface State {
    hasError: boolean;
  }

  // Catches JavaScript errors in child components and displays a fallback UI
  class ErrorBoundary extends Component<Props, State> {
    state: State = { hasError: false };

    static getDerivedStateFromError(): State {
      return { hasError: true };
    }

    componentDidCatch(error: Error, info: ErrorInfo) {
      console.error("Component error:", error, info);
    }

    render() {
      if (this.state.hasError) {
        return <div>Something went wrong. Please refresh the page.</div>;
      }
      return this.props.children;
    }
  }

  // Decorator that wraps any component with error handling
  export const errorBoundaryDecorator = <P extends object>(
    Component: React.ComponentType<P>
  ): React.ComponentType<P> => {
    return (props: P) => (
      <ErrorBoundary>
        <Component {...props} />
      </ErrorBoundary>
    );
  };

  ```

  ```tsx title={"UserCard.tsx"}
  import React, { useEffect, useState } from "react";

  interface User {
    name: string;
    email: string;
  }

  interface UserCardProps {
    userId: string;
  }

  // Displays user data from an external API
  export const UserCard: React.FC<UserCardProps> = ({ userId }) => {
    const [user, setUser] = useState<User | null>(null);

    useEffect(() => {
      fetch(`https://api.example.com/users/${userId}`)
        .then((res) => res.json() as Promise<User>)
        .then((data) => setUser(data));
    }, [userId]);

    if (!user) return <div>Loading...</div>;

    return (
      <div>
        <h3>{user.name}</h3>
        <p>{user.email}</p>
      </div>
    );
  };


  ```

  ```tsx title={"UserCard.webflow.tsx"}
  import { declareComponent } from "@webflow/react";
  import { props } from "@webflow/data-types";
  import { UserCard } from "./UserCard";
  import { errorBoundaryDecorator } from "./ErrorBoundary";

  // Wrap with error boundary to gracefully handle API failures
  export default declareComponent(UserCard, {
    name: "User Card",
    decorators: [errorBoundaryDecorator], // Apply the error boundary decorator to the component
    props: {
      userId: props.Text({
        name: "User ID",
        defaultValue: "123",
      }),
    },
  });


  ```
</CodeBlocks>

To apply decorators globally, export a `decorators` array from your  decorators file:

```typescript title="src/globals.ts"
import "./globals.css";
import { errorBoundaryDecorator } from "./ErrorBoundary";

export const decorators = [errorBoundaryDecorator];
```

<Note title="Styling components">
  Code components render in Shadow DOM, encapsulating them from the rest of the page, which impacts several CSS capabilities.

  [Learn more about styling components →](/code-components/styling-components).
</Note>

## Options

The `options` object is used to configure the component for more advanced use cases. Options accepts the following properties:

| Option              | Type    | Default | Description                                      |
| ------------------- | ------- | ------- | ------------------------------------------------ |
| `applyTagSelectors` | boolean | `false` | Whether to apply tag selectors to the component. |
| `ssr`               | boolean | `true`  | Whether to disable server-side rendering.        |

### Tag selectors

Styles targeting a tag selector (for example, `h1`, `p`, `button`) can be automatically provided to the Shadow DOM with the `applyTagSelectors` option. This is helpful for styling components with CSS selectors.

[See more about styling components in the styling documentation. →](/code-components/styling-components)

### Server-side rendering (SSR)

By default, Webflow will load your component on the server. This means that the component will be rendered on the server, but the DOM will be hydrated on the client-side. This is helpful for improving the performance of your component.

You can disable this behavior by setting `ssr` to `false`.

## Best practices

<Accordion title="File naming and organization">
  * **Use consistent naming**: `ComponentName.webflow.tsx` for all code component definitions
  * **Keep code component definitions close**: Place `.webflow.tsx` files next to their React components
</Accordion>

<Accordion title="Component metadata">
  * **Use clear names**: Make it obvious what the component does
  * **Add descriptions**: Help designers understand the component's purpose
  * **Group logically**: Use groups to organize components in the panel
</Accordion>

<Accordion title="Prop definitions">
  * **Provide helpful defaults**: Make components work immediately when added
  * **Use descriptive names**: The `name` property appears in the designer
  * **Group related props**: Consider how props will appear together in the designer
</Accordion>

<Accordion title="Global styles">
  Import CSS once in a global decorators file rather than in each component. This keeps your component definitions clean and ensures consistent styling:

  ```typescript title="src/globals.ts"
  import "./globals.css";
  ```

  Then reference your global decorators file in `webflow.json`:

  ```json title="webflow.json"
  {
    "library": {
      "globals": "./src/globals.ts"
    }
  }
  ```
</Accordion>

## Next steps

Now that you understand code component definitions, you can:

* **[Understand styling](/code-components/styling-components)** - Learn about how to style your components.
* **[Explore prop types](/code-components/reference/prop-types)** - Learn about all available prop types
* **[Configure bundling](/code-components/bundling-and-import)** - Set up your build process
* **[Importing your components](/code-components/bundling-and-import)** - Share your components with designers and other developers
