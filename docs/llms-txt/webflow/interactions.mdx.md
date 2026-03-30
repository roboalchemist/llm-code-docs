# Source: https://developers.webflow.com/devlink/docs/component-export/design-guidelines/interactions.mdx

***

title: Interactions
description: Principles for interactions in Webflow to ensure clean export
subtitle: Principles for interactions in Webflow to ensure clean export
-----------------------------------------------------------------------

[Webflow interactions](/devlink/docs/component-export/design-guidelines/interactions) are JavaScript-powered animations and transitions. Most interactions are supported in Exported Components. See the \[#page-interactions] section for more details on specific limitations.

## Enabling interactions

To enable interactions in your Exported Components, you need to wrap your application in the `DevLinkProvider` component.

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

### Page interactions

Webflow components support [page triggers](https://help.webflow.com/hc/en-us/articles/33961357722643-Triggers-and-animations#page-triggers) with a limitation: DevLink only exports the first page interaction. If a component uses multiple page interactions across different pages, DevLink will only export the first one.

### GSAP-powered interactions

<Warning title="GSAP-powered interactions aren't supported in Exported Components.">
  GSAP-powered interactions aren't supported in Exported Components.
</Warning>
