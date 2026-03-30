# Source: https://developers.webflow.com/code-components/frameworks-and-libraries.mdx

***

title: Frameworks and libraries
slug: frameworks-and-libraries
description: Learn how to use frameworks and libraries with code components.
hidden: false
subtitle: Learn how to use CSS frameworks and component libraries with code components.
canonical-url: '[https://developers.webflow.com/code-components/frameworks-and-libraries](https://developers.webflow.com/code-components/frameworks-and-libraries)'
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Code Components work with a wide range of styling approaches, including CSS preprocessors, utility frameworks, and component/style libraries.

Because Code Components render inside a [Shadow DOM](/code-components/component-architecture#shadow-dom-and-react-roots), some tools that inject styles into the global `document.head` need additional configuration to scope styles correctly. Webflow provides utilities for popular CSS-in-JS libraries (e.g. Emotion, styled-components) so they can inject styles directly into the Shadow Root.

Most setups just require a small addition to your [webpack configuration](/code-components/webpack-configuration-overrides) and an import in your component. For CSS-in-JS solutions, you’ll wrap your components in a Shadow DOM provider.

## CSS frameworks

<Accordion title="Tailwind CSS">
  To use Tailwind CSS with your code components, configure PostCSS to process Tailwind classes:

  <Steps>
    <Step title="Install Tailwind CSS">
      Install Tailwind CSS and its PostCSS plugin:

      ```bash
      npm install tailwindcss @tailwindcss/postcss postcss
      ```
    </Step>

    <Step title="Configure PostCSS">
      Add the Tailwind PostCSS plugin to your `postcss.config.mjs` file:

      ```mjs title={"postcss.config.mjs"}
      const config = {
        plugins: {
          "@tailwindcss/postcss": {},
        },
      };

      export default config;

      ```
    </Step>

    <Step title="Create Tailwind styles">
      Create a CSS file that imports Tailwind:

      ```css title={"globals.css"}
      @import "tailwindcss";

      ```
    </Step>

    <Step title="Configure global decorators">
      Create a global decorators file that imports your Tailwind CSS:

      ```ts title={"globals.ts"}
      import "./globals.css";


      ```

      Then reference it in your `webflow.json`:

      ```json title="webflow.json"
      {
        "library": {
          "globals": "./src/globals.ts"
        }
      }
      ```
    </Step>

    <Step title="Use Tailwind classes">
      Write your React components using Tailwind utility classes. The global styles are automatically applied to all components:

      <CodeBlocks>
        ```tsx title={"Badge.tsx"}
        import * as React from "react";

        interface BadgeProps {
          text: string;
          variant: 'Light' | 'Dark';
        }

        export const Badge = ({ text, variant }: BadgeProps) => (
          <span
            className={`inline-block rounded-full px-3 py-1 text-sm font-medium ${
              variant === 'Light'
                ? 'bg-gray-100 text-gray-800'
                : 'bg-gray-800 text-white'
            }`}
          >
            {text}
          </span>
        );
        ```

        ```tsx title={"Badge.webflow.tsx"}
        import { Badge } from "./Badge";
        import { props } from "@webflow/data-types";
        import { declareComponent } from "@webflow/react";

        export default declareComponent(Badge, {
          name: "Badge",
          props: {
            text: props.Text({
              name: "Text",
              defaultValue: "Hello World",
            }),
            variant: props.Variant({
              name: "Variant",
              options: ["Light", "Dark"],
              defaultValue: "Light",
            }),
          },
        });

        ```
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

<Accordion title="styled-components">
  To use styled-components with code components, install the `@webflow/styled-components-utils` package and configure a global decorator to inject styles into the Shadow DOM.

  <Steps>
    <Step title="Install the styled-components utility library">
      Install the utility library:

      ```bash
      npm i @webflow/styled-components-utils
      ```

      <Tip>
        This package requires the following peer dependencies:

        ```bash
        npm i styled-components react react-dom
        ```
      </Tip>
    </Step>

    <Step title="Configure global decorators">
      Create a global decorators file that exports the styled-components decorator:

      ```ts title={"globals.ts"}
      import { styledComponentsShadowDomDecorator } from "@webflow/styled-components-utils";

      export const decorators = [styledComponentsShadowDomDecorator];


      ```

      Then reference it in your `webflow.json`:

      ```json title="webflow.json"
      {
        "library": {
          "globals": "./src/globals.ts"
        }
      }
      ```
    </Step>

    <Step title="Use styled-components in your component">
      Write your React component using styled-components. The global decorator automatically wraps all components:

      <CodeBlocks>
        ```tsx title={"Button.tsx"}
        import React from "react";
        import styled from "styled-components";

        const StyledButton = styled.button`
          background-color: #007bff;
        `;

        interface ButtonProps {
          buttonText: string;
        }

        export const Button = ({ buttonText }: ButtonProps) => {
          return <StyledButton>{buttonText}</StyledButton>;
        };

        ```

        ```tsx title={"Button.webflow.tsx"}
        import { declareComponent } from "@webflow/react";
        import { props } from "@webflow/data-types";
        import { Button } from "./Button";

        export default declareComponent(Button, {
          name: "Button",
          props: {
            buttonText: props.Text({
              name: "Button Text",
              defaultValue: "Click me",
            }),
          },
        });

        ```
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

<Accordion title="Emotion">
  To use Emotion with code components, install the [`@webflow/emotion-utils`](https://www.npmjs.com/package/@webflow/emotion-utils?activeTab=readme) package and configure a global decorator to inject styles into the Shadow DOM.

  <Steps>
    <Step title="Install the Emotion utility library">
      In your terminal, run the following command to install the Emotion utility package:

      ```bash
      npm i @webflow/emotion-utils
      ```

      <Tip>
        This package requires the following peer dependencies:

        ```bash
        npm i @emotion/cache @emotion/react react react-dom
        ```
      </Tip>
    </Step>

    <Step title="Configure global decorators">
      Create a global decorators file that exports the Emotion decorator:

      ```ts title={"globals.ts"}
      import { emotionShadowDomDecorator } from "@webflow/emotion-utils";

      export const decorators = [emotionShadowDomDecorator];


      ```

      Then reference it in your `webflow.json`:

      ```json title="webflow.json"
      {
        "library": {
          "globals": "./src/globals.ts"
        }
      }
      ```
    </Step>

    <Step title="Use Emotion in your component">
      Write your React component using Emotion. The global decorator automatically wraps all components:

      <CodeBlocks>
        ```tsx title={"Button.tsx"}
        import React from "react";
        import styled from "@emotion/styled";

        const StyledButton = styled.button`
          background-color: #007bff;
        `;

        interface ButtonProps {
          buttonText: string;
        }

        export const Button = ({ buttonText }: ButtonProps) => {
          return <StyledButton>{buttonText}</StyledButton>;
        };

        ```

        ```tsx title={"Button.webflow.tsx"}
        import { declareComponent } from "@webflow/react";
        import { props } from "@webflow/data-types";
        import { Button } from "./Button";

        export default declareComponent(Button, {
          name: "Button",
          props: {
            buttonText: props.Text({
              name: "Button Text",
              defaultValue: "Click me",
            }),
          },
        });

        ```
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

## Component libraries

<Accordion title="Material UI">
  Material UI uses Emotion for styling. Install the [`@webflow/emotion-utils`](https://www.npmjs.com/package/@webflow/emotion-utils?activeTab=readme) package and configure a global decorator to inject styles into the Shadow DOM.

  <Steps>
    <Step title="Install the Emotion utility library">
      In your terminal, run the following command to install the Emotion utility package:

      ```bash
      npm i @webflow/emotion-utils
      ```

      <Tip>
        This package requires the following peer dependencies:

        ```bash
        npm i @mui/material @emotion/react @emotion/cache
        ```
      </Tip>
    </Step>

    <Step title="Configure global decorators">
      Create a globals file that exports the Emotion decorator:

      ```ts title={"globals.ts"}
      import { emotionShadowDomDecorator } from "@webflow/emotion-utils";

      export const decorators = [emotionShadowDomDecorator];


      ```

      Then reference it in your `webflow.json`:

      ```json title="webflow.json"
      {
        "library": {
          "globals": "./src/globals.ts"
        }
      }
      ```
    </Step>

    <Step title="Use Material UI in your component">
      Write your React component using Material UI. The global decorator automatically wraps all components:

      <CodeBlocks>
        ```tsx title={"Button.tsx"}
        import React from "react";
        import { Button } from "@mui/material";

        interface ButtonProps {
          children: React.ReactNode;
          variant?: "text" | "outlined" | "contained";
          color?: "primary" | "secondary" | "error" | "info" | "success" | "warning";
          onClick?: () => void;
        }

        export const CustomButton = ({
          children,
          variant = "contained",
          color = "primary",
          onClick,
        }: ButtonProps) => {
          return (
            <Button variant={variant} color={color} onClick={onClick}>
              {children}
            </Button>
          );
        };

        ```

        ```tsx title={"Button.webflow.tsx"}
        import { declareComponent } from "@webflow/react";
        import { props } from "@webflow/data-types";
        import { CustomButton } from "./Button";

        export default declareComponent(CustomButton, {
          name: "Button",
          description: "A simple button component",
          group: "Forms",
          props: {
            children: props.Text({
              name: "Button Text",
              defaultValue: "Click me"
            }),
            variant: props.Variant({
              name: "Style",
              options: ["text", "outlined", "contained"],
              defaultValue: "contained"
            }),
            color: props.Variant({
              name: "Color",
              options: ["primary", "secondary", "error", "info", "success", "warning"],
              defaultValue: "primary"
            })
          },
        });
        ```
      </CodeBlocks>
    </Step>
  </Steps>
</Accordion>

<Accordion title="Shadcn/UI">
  Shadcn/UI is a component library built on Tailwind CSS that provides pre-built, accessible React components. It works with code components but requires path alias configuration. Follow these steps after setting up Tailwind CSS:

  <Steps>
    <Step title="Configure path aliases">
      Shadcn/UI uses path aliases that need to be configured in your webpack setup. Add this to your webpack configuration:

      ```js title={"webpack.webflow.js"}
      module.exports = {
          resolve: {
              alias: {
                  "@": process.cwd(), // Maps @ to your project root
              },
          },
      };

      ```

      For detailed webpack configuration options, see the [bundling and import guide](/code-components/bundling-and-import).
    </Step>
  </Steps>
</Accordion>

## Preprocessors & post-processing

<Accordion title="Sass">
  Configure your project to use Sass with the following steps:

  <Steps>
    <Step title="Install the Sass loaders">
      Install the loaders as development dependencies:

      ```bash
      npm install --save-dev sass sass-loader
      ```
    </Step>

    <Step title="Create a custom webpack configuration">
      Create a `webpack.webflow.js` file to customize the webpack configuration to use the Sass loader:

      ```js title={"webpack.webflow.js"}
      module.exports = {
      module: {
              rules: (currentRules) => {
              const currentCSSRule = currentRules.find(
                  (rule) =>
                  rule.test instanceof RegExp &&
                  rule.test.test("test.css") &&
                  Array.isArray(rule.use)
              );
              return [
                  ...currentRules,
                  {
                  test: /\.scss$/,
                  use: [...currentCSSRule.use, "sass-loader"],
                  },
              ];
              },
          }
      }
      ```
    </Step>

    <Step title="Update your Webflow configuration">
      Update your `webflow.json` file to use the custom webpack configuration:

      ```json title={"webflow.json"}
      {
          "library": {
            "name": "React Components Library",
            "components": ["./src/**/*.webflow.@(js|jsx|mjs|ts|tsx)"],
            "bundleConfig": "./webpack.webflow.js"
          }
        }

      ```
    </Step>

    <Step title="Use Sass in your code component">
      Import Sass in your code component definition file:

      ```tsx title="src/components/Button.webflow.tsx"
      import '../styles/button.scss';

      // Declare the component
      ```
    </Step>
  </Steps>
</Accordion>

<Accordion title="Less">
  Configure your project to use Less with the following steps:

  <Steps>
    <Step title="Install the Less loaders">
      Install the loaders as development dependencies:

      ```bash
      npm install --save-dev less less-loader
      ```
    </Step>

    <Step title="Create a custom webpack configuration">
      Create a `webpack.webflow.js` file to customize the webpack configuration to use the Sass loader:

      ```js title={"webpack.webflow.js"}
      // webpack.webflow.js
      module.exports = {
          module: {
            rules: (currentRules) => {
              const currentCSSRule = currentRules.find(
                (rule) =>
                  rule.test instanceof RegExp &&
                  rule.test.test("test.css") &&
                  Array.isArray(rule.use)
              );

              return [
                ...currentRules,
                {
                  test: /\.less$/i,
                  use: [...currentCSSRule.use, "less-loader"],
                },
              ];
            },
          },
        };

      ```
    </Step>

    <Step title="Update your Webflow configuration">
      Update your `webflow.json` file to use the custom webpack configuration:

      ```json title={"webflow.json"}
      {
          "library": {
            "name": "React Components Library",
            "components": ["./src/**/*.webflow.@(js|jsx|mjs|ts|tsx)"],
            "bundleConfig": "./webpack.webflow.js"
          }
        }

      ```
    </Step>

    <Step title="Use less in your code component">
      Import less in your code component definition file:

      ```tsx title="src/components/Button.webflow.tsx"
      import '../styles/button.less';

      // Declare the component
      ```
    </Step>
  </Steps>
</Accordion>

Learn about additional configuration options in the [bundling and import guide](/code-components/bundling-and-import).

## Next steps

* [Declare your code component](/code-components/define-code-component)
* [Style your React component](/code-components/styling-components)
* [Deploy your code component](/code-components/bundling-and-import)

## Troubleshooting

<Accordion title="Errors when sharing to Webflow">
  If you're getting errors when sharing to Webflow, try the following:

  * Ensure you've installed the Webflow CLI locally within the project. If you have a global installation, try running the command with `npx` to ensure the correct version is being used.
</Accordion>
