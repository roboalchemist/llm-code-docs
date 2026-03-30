# Source: https://developers.webflow.com/devlink/usage/framework-guides.mdx

***

title: Framework Guides
slug: devlink/usage/framework-guides
description: >-
Guides for integrating DevLink with various frameworks, including Next.js,
Remix, Gatsby, and Vite/CRA.
subtitle: >-
Use exported components with various frameworks, including Next.js, Remix, and
Gatsby.
-------

Exported components are designed to be framework-agnostic, but each framework has its own conventions and best practices for integration. This guide provides specific considerations for popular React frameworks.

Regardless of the framework you're using, follow these patterns to successfully integrate DevLink:

<CardGroup cols={2}>
  <Card
    title="Import paths"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Folder.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Folder.svg" alt="" className="block dark:hidden" />
      </>
    }
  >
    Ensure your import paths correctly resolve to your DevLink directory. Adjust import paths based on your project structure (for example, `@/DevLink`, `~/DevLink`, or relative paths).
  </Card>

  <Card
    title="SSR compatibility"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DeveloperToolsSDK.svg" alt="" className="hidden dark:block" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DeveloperToolsSDK.svg" alt="" className="block dark:hidden" />
    </>
  }
  >
    DevLink components are fully compatible with server-side rendering. Just make sure to wrap your application with DevLinkProvider at the root level.
  </Card>

  <Card
    title="Dedupe styles"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Styles.svg" alt="" className="hidden dark:block" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Styles.svg" alt="" className="block dark:hidden" />
    </>
  }
  >
    Some frameworks may need configuration to prevent duplicate CSS imports. Use each framework's recommended approach for CSS management.
  </Card>

  <Card
    title="Type support"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Code.svg" alt="" className="hidden dark:block" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Code.svg" alt="" className="block dark:hidden" />
    </>
  }
  >
    DevLink generates type definitions for each Webflow component. Ensure your `tsconfig.json` includes the DevLink directory `*.ts` files.
  </Card>
</CardGroup>

## React Server Components

Exported components, which often rely on client-side JavaScript for interactions and styling, may not work directly with React Server Components (RSC). To use Webflow components in your React application, it's recommended to:

* Use exported Webflow components only within client components.
* Mark the React component consuming the exported Webflow component as a **client component** by adding the `"use client"` directive to the component file.
* Make sure the `DevLinkProvider` is in a client-side context (e.g., within a `layout.tsx` file marked as a client component) to enable all interactions.

```jsx title="ClientComponent.tsx"
"use client";

import { MyDevLinkComponent } from '@/devlink';

export default function ClientComponent() {
  return <MyDevLinkComponent />;
}
```

## Next.js

Next.js, with its server-side rendering (SSR) and static site generation (SSG) capabilities, requires some changes when integrating client-side DevLink components and interactions.

### Styles and interactions

To support interactions, your application must be wrapped with the `DevLinkProvider` component.

<Tabs>
  <Tab title="App Router">
    When using the Next.js App Router in versions 13 and higher, you’ll need to:

    * Import and set up the `DevLinkProvider` in your root `layout.tsx` file
    * Import global styles from DevLink

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
            <DevLinkProvider>
              {children}
            </DevLinkProvider>
          </body>
        </html>
      );
    }
    ```

    <Note title="React Server Components">
      The Next.js App Router uses React Server Components by default. For exported Webflow components that rely on client-side JavaScript for interactions and styling, you may need to add the `"use client"` directive at the top of your component files.
    </Note>
  </Tab>

  <Tab title="Pages Router">
    When using the Next.js Pages Router, you’ll need to:

    * Import and set up the `DevLinkProvider` in your `_app.tsx` file
    * Import global styles from DevLink

    ```tsx title="pages/_app.tsx"
    import { DevLinkProvider } from '@/devlink/DevLinkProvider';
    import '@/devlink/global.css';
    import type { AppProps } from 'next/app';
    export default function App({ Component, pageProps }: AppProps) {
      return (
        <DevLinkProvider>
          <Component {...pageProps} />
        </DevLinkProvider>
      );
    }
    ```
  </Tab>
</Tabs>

### Links and Images

Some frameworks like Next.js provide their own Link and Image components for use in applications. You can choose to override DevLink’s builtin Link and Image components with the ones from Next.js by passing a custom component to the `renderLink` and/or `renderImage` props of the `<DevLinkProvider>` component.

<Steps>
  <Step title="Update the Next.js Configuration">
    Update the Next.js configuration to ensure Image components work with external URLs.

    ```tsx title="next.config.ts"
    const nextConfig = {
      images: {
        remotePatterns: [
          {
            protocol: "https",
            hostname: "uploads-ssl.webflow.com",
          },
        ],
      },
    };
    module.exports = nextConfig;
    ```
  </Step>

  <Step title="Create custom components">
    Create custom components that will wrap the Next.js Link and/or Image components:

    ```tsx title="renderers.tsx" maxLines=10
      "use client";

      import Image from "next/image";
      import Link from "next/link";
      import { RenderLink, RenderImage } from "@/devlink";

      export const LinkRenderer: RenderLink = ({
        href,
        className,
        children,
        ...props,
      }) => (
        <Link href={href} className={className} {...props}>
          {children}
        </Link>
      );

      export const ImageRenderer: RenderImage = ({
        src,
        alt,
        height,
        width,
        loading,
        className,
        ...props,
      }) => {
        const imgProps = {
          loading,
          className,
          src: typeof src === "string" ? src : "",
          alt: alt || "",
          width: width === "auto" ? undefined : (width as number),
          height: height === "auto" ? undefined : (height as number),
          // Note: this will fill the image to its parent element container
          // so you'll need to style the parent container with the desired size.
          fill: width === "auto" || height === "auto",
          ...props,
        };

        return <Image {...imgProps} />;
      };

    ```
  </Step>

  <Step title="Configure the DevLinkProvider">
    In `layout.tsx`, pass the custom components to the `renderLink` and/or `renderImage` props of the `<DevLinkProvider>` component.

    ```tsx title="layout.tsx"
    import "@/devlink/global.css";
    import { DevLinkProvider } from "@/devlink/DevLinkProvider";
    import { LinkRenderer, ImageRenderer } from "@/components/renderers"; // Custom components
    export default function RootLayout({
      children,
    }: {
      children: React.ReactNode;
    }) {
      return (
        <html lang="en">
          <body>
            <DevLinkProvider renderLink={LinkRenderer} renderImage={ImageRenderer}>
              {children}
            </DevLinkProvider>
          </body>
        </html>
      );
    }
    ```
  </Step>
</Steps>

## Remix

Remix is a full-stack web framework that prioritizes web standards and performance. When using DevLink with Remix:

* **Client-side rendering**: Make sure that components relying on DevLink's JavaScript interactions are rendered client-side. You may need to use `useEffect` or other client-side hydration techniques for dynamic content.
* **Styling**: Import the DevLink `global.css` within your root `app/root.tsx` or a relevant stylesheet. Address any CSS conflicts with Remix's default styles or your custom CSS.
* **Data loading**: Integrate DevLink components with Remix's data loading mechanisms (e.g., `loader` functions) by passing fetched data as props to your DevLink-wrapped components.

**Example**

<CodeBlocks>
  ```tsx title="app/root.tsx"
  import {
    Links,
    LiveReload,
    Meta,
    Outlet,
    Scripts,
    ScrollRestoration
  } from "@remix-run/react";
  import { DevLinkProvider } from '~/devlink/DevLinkProvider';
  import styles from '~/devlink/global.css';

  // Import styles using the links export
  export const links = () => [
    { rel: "stylesheet", href: styles }
  ];

  export default function App() {
    return (
      <html lang="en">
        <head>
          <Meta />
          <Links />
        </head>
        <body>
        {/* Wrap the Outlet with the DevLinkProvider */}
          <DevLinkProvider>
            <Outlet />
          </DevLinkProvider>
          <ScrollRestoration />
          <Scripts />
          <LiveReload />
        </body>
      </html>
    );
  }
  ```

  ```tsx title="app/routes/_index.tsx"
  =import { json, type LoaderFunctionArgs } from "@remix-run/node";
  import { useLoaderData } from "@remix-run/react";
  import { ProductGrid } from "~/devlink/ProductGrid";
  // or import a purely presentational DevLink component if it doesn't require browser-only APIs
  // import { ProductGrid } from "~/devlink/ProductGrid";

  export async function loader({ request }: LoaderFunctionArgs) {
    // Fetch whatever your DevLink component needs
    const res = await fetch(`${process.env.API_BASE_URL}/products`, {
      headers: { accept: "application/json" },
    });
    if (!res.ok) {
      // Let Remix’s error boundaries handle failures cleanly
      throw new Response("Failed to load products", { status: res.status });
    }
    const products = await res.json();
    return json({ products });
  }

  export default function IndexRoute() {
    const { products } = useLoaderData<typeof loader>();

    // If your DevLink component can render on the server without touching the DOM,
    // you can pass props directly to it. If it needs the browser, use the “Client” wrapper.
    return (
      <main>
        <h1>Products</h1>
        <ProductGrid products={products} />
      </main>
    );
  }

  ```
</CodeBlocks>

## Gatsby

Gatsby is a static site generator for React. You can use DevLink components inside your Gatsby project for both static and interactive content. Follow the steps below to integrate DevLink.

### Static and interactive components

* **Static components** are purely presentational and work seamlessly with Gatsby’s static generation.
* **Interactive components** rely on `window`, animations, or JavaScript APIs and need to be hydrated on the client. Use `useEffect` or a mounted state guard to avoid hydration mismatches.

**Example**

```tsx title="/src/components/DevLinkInteractiveClient.tsx"
import { useEffect, useState } from "react";
import { DevLinkInteractive } from "../devlink/DevLinkInteractive";

export function DevLinkInteractiveClient(props: any) {
  const [ready, setReady] = useState(false);
  useEffect(() => setReady(true), []);
  if (!ready) return null; // Prevents SSR mismatch
  return <DevLinkInteractive {...props} />;
}
```

### Styling

Import DevLink’s global stylesheet so your components render with the expected styles. You can do this in either:

* `gatsby-browser.tsx` to apply styles on the client, or
* A shared layout component to ensure styles are included during SSR.

### DevLinkProvider

To give all routes access to DevLink, wrap your app root element with `DevLinkProvider`. Add the wrapper to both `gatsby-browser.tsx` and `gatsby-ssr.tsx`.

<CodeBlocks>
  ```tsx title="gatsby-browser.tsx"
  import React from "react";
  import { DevLinkProvider } from "./src/devlink/DevLinkProvider";
  import "./src/devlink/global.css"; // Option A: import global styles here

  export const wrapRootElement = ({ element }: { element: React.ReactNode }) => (
    <DevLinkProvider>{element}</DevLinkProvider>
  );
  ```

  ```tsx title="gatsby-ssr.tsx"
  import React from "react";
  import { DevLinkProvider } from "./src/devlink/DevLinkProvider";

  export const wrapRootElement = ({ element }: { element: React.ReactNode }) => (
    <DevLinkProvider>{element}</DevLinkProvider>
  );
  ```
</CodeBlocks>
