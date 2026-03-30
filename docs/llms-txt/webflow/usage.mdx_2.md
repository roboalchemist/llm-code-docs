# Source: https://developers.webflow.com/devlink/docs/component-export/usage.mdx

***

title: Using Exported Components
description: >-
Guides for React developers on how to import, configure, and extend Exported
Components in their applications.
---------------------------------

Once you've exported your components, you can use them in your React project. This section provides guides for integrating Exported Components with various frameworks, styling and theming, data and state integration, and best practices for usage.

## Using Exported Components

<Steps>
  <Step title="Apply Webflow's design system globally">
    To apply Webflow's design system globally, import the `global.css` file at the root of your application.

    ```tsx title="app/layout.tsx"
    import { DevLinkProvider } from '@/devlink/DevLinkProvider';
    import '@/devlink/global.css';
    ```
  </Step>

  <Step title="Wrap your application in the DevLinkProvider component">
    Wrap your application in the `DevLinkProvider` component to ensure all exported components have access to Webflow interactions.

    ```tsx title="app/layout.tsx"
    import { DevLinkProvider } from '@/devlink/DevLinkProvider';
    import '@/devlink/global.css';

    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode;
    }) {
      return (
        <html lang="en">
          <body>
          {/* Wrap your application in the DevLinkProvider component */}
            <DevLinkProvider>
              {children}
            </DevLinkProvider>
          </body>
        </html>
      );
    }
    ```
  </Step>

  <Step title="Use the DevLink alias">
    To import the components and styles into your React project, you can use the DevLink alias. To set up the alias, update the paths in `tsconfig.json` to the correct location of your DevLink components.

    ```json title="tsconfig.json"
    {
      "compilerOptions": {
        "paths": {
          "@/*": ["./src/*"],
          "@/devlink": ["./devlink"],
          "@/devlink/*": ["./devlink/*"]
        }
      }
    }
    ```
  </Step>

  <Step title="Use the exported components">
    Now you can import and use your Webflow components in your application. This particular example uses three components exported from Webflow via DevLink: `Hero`, `Card`, and `Button`.

    You can use them in your application:

    ```tsx title="app/page.tsx"
    import { Button } from '@/devlink/Button';
    import { Card } from '@/devlink/Card';
    import { Hero } from '@/devlink/Hero';

    export default function Home() {
      return (
        <main>
          <Hero />
          <Card />
          <Button />
        </main>
      );
    }
    ```

    <Note title="Always include the component name in the import">
      Always include the component name in the import. For example, `import { Hero } from '@/devlink/Hero';` instead of `import { Hero } from '@/devlink';`.
    </Note>
  </Step>
</Steps>

## Learn more

<CardGroup cols={2}>
  <Card
    title="Getting Started"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CirclePlay.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CirclePlay.svg" alt="" className="light-icon" />
      </>
    }
    href="/devlink/docs/quick-start/quick-start-component-export"
  >
    How to setup DevLink and export components to a React project.
  </Card>

  <Card
    title="Framework Guides"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/ComponentsCode.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/ComponentsCode.svg" alt="" className="light-icon" />
      </>
    }
    href="/devlink/usage/framework-guides"
  >
    Specific guides for integrating DevLink with various frameworks, including Next.js (App Router & Pages Router), Remix, Gatsby, and Vite/CRA.
  </Card>

  <Card
    title="Styling and Theming Overrides"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Styles.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Styles.svg" alt="" className="light-icon" />
      </>
    }
    href="/devlink/usage/styling-and-theming-overrides"
  >
    How to override DevLink component styles using CSS Modules, global CSS imports, reusing Webflow classes, targeting namespaced selectors, and advanced configuration.
  </Card>

  <Card
    title="Troubleshooting DevLink"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Troubleshooting.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Troubleshooting.svg" alt="" className="light-icon" />
      </>
    }
    href="/devlink/docs/component-export/usage/troubleshooting"
  >
    Solutions for common issues encountered when working with DevLink, including authentication, component sync, styling, interactions, and framework-specific problems.
  </Card>
</CardGroup>
