# Source: https://developers.webflow.com/code-components/reference/prop-types/link.mdx

***

title: Link
slug: reference/prop-types/link
description: Configure a Link property for a code component
max-toc-depth: 3
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/link](https://developers.webflow.com/code-components/reference/prop-types/link)'
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add a Link property to your component so designers can create clickable links with full control over URL, target behavior, and preload settings.

## Syntax

```tsx
// Prop definition
props.Link({
    name: string,
    group?: string,
    tooltip?: string,
})

// Prop value
{
    href: string,
    target?: "_self" | "_blank" | string,
    preload?: "prerender" | "prefetch" | "none" | string,
}
```

### Prop definition

Define the Link prop in your Webflow code component with a name. Optionally, you can add a group and tooltip text.

```tsx
props.Link({
    name: string,
    group?: string,
    tooltip?: string,
})
```

#### Properties

* `name`: The name for the property.
* `group`: The group for this property (optional).
* `tooltip`: The tooltip for this property (optional).

### Prop value

The Link prop value provides an object to your React component with the following properties:

```tsx title="PropType.Link"
{
    href: string,
    target?: "_self" | "_blank" | string,
    preload?: "prerender" | "prefetch" | "none" | string,
}
```

<div>
  <div>
    #### Properties returned to the React component

    * `href`: The URL destination.
    * `target`: How the link opens (optional).
    * `preload`: Preload behavior (optional).
  </div>

  <div>
    #### Webflow properties panel

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/efa18be417a6ff044fe6eff73048c955739914bfa61685c867eeff54ab43dfbc/products/code-components/pages/reference/prop-types/assets/link.png" alt="Link property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

#### Examples

<Tabs>
  <Tab title="Direct mapping">
    Define a Link property in your Webflow component, that directly maps to a link property in your React component. If your React component expects a `href` and `target` property, see the [prop mapping](#prop-mapping) example below.

    <CodeBlocks>
      ```tsx title={"Button.webflow.tsx"}
      import { declareComponent } from '@webflow/react';
      import { props } from '@webflow/data-types';
      import { Button } from "./Button";

      export default declareComponent(Button, {
      name: "Button",
      description: "A Button component with a Link property",
      props: {
          link: props.Link({
              name: "Button Link",
              group: "Navigation"
          }),
          text: props.Text({
              name: "Button Text",
              group: "Navigation"
          })
      }
      });

      ```

      ```tsx title={"Button.tsx"}
      import React from "react";

      export interface ButtonProps {
          text?: string;
          link?: {
              href: string;
              target?: "_self" | "_blank" | string;
              preload?: "prerender" | "prefetch" | "none" | string;
          };
      }

          export const Button = ({ text, link }: ButtonProps) => {
          if (!link) return null;

          return (
              <a
              href={link.href}
              target={link.target}
              rel={link.target === "_blank" ? "noopener noreferrer" : undefined}
              >
              {text}
              </a>
          );
      }
      ```
    </CodeBlocks>
  </Tab>

  <Tab title="Prop mapping">
    This example shows how to define a Link property in your Webflow component, with a wrapper to map the link property to the `href` and `target` properties in your React component.

    <CodeBlocks>
      ```tsx title={"Button.webflow.tsx"}
      import { props, PropType, PropValues } from "@webflow/data-types";
      import { declareComponent } from "@webflow/react";
      import React from "react";
      import { Button, ButtonProps } from "./Button";

      // Remove href and target from the props to prevent conflicts
      type WebflowButtonProps = {
        link: PropValues[PropType.Link];
      } & Omit<ButtonProps, "href" | "target">; // Remove buttonText from the props

      // Wrapper that destructures the object returned from `props.Link` and passes the href and target to the button component as expected.
      const WebflowButton = ({
        link: { href, target },
        ...props
      }: WebflowButtonProps) => {
        return <Button href={href} target={target} {...props} />;
      };

      // Component declaration for Webflow
      export default declareComponent(WebflowButton, {
        name: "Button",
        props: {
          text: props.Text({
            name: "Text",
            defaultValue: "Lorem ipsum",
          }),
          link: props.Link({ name: "Link" }),
        },
      });

      ```

      ```tsx title={"Button.tsx"}
      import React from "react";

      export interface ButtonProps {
          text?: string;
          href?: string;
          target?: "_self" | "_blank" | string;
      }

      export const Button = ({ text, href, target }: ButtonProps) => {
          if (!href) return null;

          return (
              <a
              href={href}
              target={target}
              rel={target === "_blank" ? "noopener noreferrer" : undefined}
              >
              {text}
              </a>
          );
      }
      ```
    </CodeBlocks>
  </Tab>
</Tabs>

## When to use

Use a Link prop when you want designers to:

* Set URLs for buttons or text links
* Control link behavior (same tab vs new tab)
* Create navigation components

## Best practices

* Handle missing links gracefully
* Add proper rel attributes for security
* Consider accessibility for link text
