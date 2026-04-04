# Source: https://developers.webflow.com/code-components/reference/prop-types/image.mdx

***

title: Image
slug: reference/prop-types/image
description: Configure an Image property for a code component
max-toc-depth: 3
hidden: false
canonical-url: '[https://developers.webflow.com/code-components/reference/prop-types/image](https://developers.webflow.com/code-components/reference/prop-types/image)'
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Add an Image property to your component so designers can select images from their Webflow asset library.

## Syntax

```tsx
// Prop definition
props.Image({
    name: string,
    group?: string,
    tooltip?: string,
})

// Props returned to the React component
{
    src: string;
    alt?: string;
}
```

### Prop definition

Define the Image prop in your Webflow code component with a name. Optionally, you can add a group and tooltip text.

```tsx
props.Image({
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

The Image prop provides both the image URL and alt text to your React component, making it easy to display dynamic images with proper accessibility.

```tsx title="PropType.Image"
{
    src: string;
    alt?: string;
}
```

<div>
  <div>
    #### Properties returned to the React component

    * `src`: The source URL of the image.
    * `alt`: The alt text for the image (optional).
  </div>

  <div>
    #### Webflow properties panel

    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/34b3c448d91a85db2e2a34a9bd1b82d1b5d4f05f4e64e7a54fa53a00a10a7000/products/code-components/pages/reference/prop-types/assets/image.png" alt="Image property in the Webflow panel" />
      </Frame>
    </div>
  </div>
</div>

### Examples

<Tabs>
  <Tab title="Direct mapping">
    Define an Image property in your Webflow component, that directly maps to an image property in your React component.

    <CodeBlocks>
      ```tsx title={"Hero.webflow.tsx"}
      import { declareComponent } from '@webflow/react';
      import { props } from '@webflow/data-types';
      import { Hero } from "./Hero";

      export default declareComponent(Hero, {
          name: "Hero",
          description: "A Hero component with an Image property",
          props: {
              image: props.Image({
                  name: "Hero Image",
                  group: "Content"
              })
          }
      });

      ```

      ```tsx title={"Hero.tsx"}
      import React from "react";

      interface HeroProps {
      image?: {
          src: string;
          alt?: string;
      };
      }

      export const Hero = ({ image }: HeroProps) => {
      if (!image) return null;

      return (
          <div className="image-container">
          <img
              src={image.src}
              alt={image.alt || ""}
              className="component-image"
          />
          </div>
      );
      }

      ```
    </CodeBlocks>
  </Tab>

  <Tab title="Prop mapping">
    This example shows how to define an Image property in your Webflow component, with a wrapper to map the image property to the `src` and `alt` properties in your React component.

    <CodeBlocks>
      ```tsx title={"Hero.webflow.tsx"}
      import { props, PropType, PropValues } from "@webflow/data-types";
      import { declareComponent } from "@webflow/react";
      import React from "react";
      import { Hero, HeroProps } from "./Hero";


      // Declare type for the Webflow wrapper props
      type HeroWebflowComponentProps = {
        image: PropValues[PropType.Image]; // Imapge prop uses the Webflow Image prop type
      } & Omit<HeroProps, "src" | "alt">; // Remove src and alt from the props to prevent conflicts

      // Wrapper that destructures the object returned from `props.Image` and passes the src and alt to the image component as expected.
      const HeroWebflowComponent = ({
        image: { src, alt },
        ...props
      }: HeroWebflowComponentProps) => {
        return <Hero src={src} alt={alt} {...props} />;
      };

      // Component declaration for Webflow
      export default declareComponent(HeroWebflowComponent, {
        name: "Hero",
        props: {
          image: props.Image({ name: "Image" }),
        },
      });

      ```

      ```tsx title={"Hero.tsx"}
      import React from "react";

      export interface HeroProps {
          src?: string;
          alt?: string;
      }

      export const Hero = ({ src, alt }: HeroProps) => {
      if (!src) return null;

      return (
          <div className="image-container">
          <img
              src={src}
              alt={alt || ""}
              className="component-image"
          />
          </div>
      );
      }

      ```
    </CodeBlocks>
  </Tab>
</Tabs>

## When to use

Use an Image prop when you want designers to:

* Select images from their asset library
* Change images without touching code
* Set alt text for accessibility

## Best practices

* Handle missing images
* Use alt text for accessibility
* Consider responsive design needs
