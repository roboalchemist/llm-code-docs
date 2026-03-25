# Source: https://posthog.com/docs/web-analytics/installation/remix.md

# Source: https://posthog.com/docs/session-replay/installation/remix.md

# Source: https://posthog.com/docs/experiments/installation/remix.md

# Source: https://posthog.com/docs/advanced/proxy/remix.md

# Source: https://posthog.com/docs/libraries/remix.md

# Remix - Docs

PostHog makes it easy to get data about traffic and usage of your [Remix](https://remix.run/) app. Integrating PostHog into your site enables analytics about user behavior, custom events capture, session recordings, feature flags, and more.

**Using Remix V3?**

Remix V3 is now React Router V7 framework mode. Please refer to the [React Router V7 framework mode](/docs/libraries/react-router/react-router-v7-framework-mode.md) guide instead for instructions on how to integrate PostHog.

This guide walks you through integrating PostHog into your Remix app using the [JavaScript Web SDK](/docs/libraries/js.md).

## Installation

Install `posthog-js` and `@posthog/react`:

Terminal

PostHog AI

```bash
npm install --save posthog-js @posthog/react
```

Start by setting `posthog-js` and `@posthog/react` as external packages in your `vite.config.ts` file.

TypeScript

PostHog AI

```typescript
// vite.config.ts
// ... imports and rest of config
export default defineConfig({
  plugins: [
    remix({
      future: {
        v3_fetcherPersist: true,
        v3_relativeSplatPath: true,
        v3_throwAbortReason: true,
        v3_singleFetch: true,
        v3_lazyRouteDiscovery: true,
      },
    }),
    tsconfigPaths(),
  ],
  ssr: {
    noExternal: ["posthog-js", "@posthog/react"],
  },
});
```

Next, create a `provider.tsx` file in the `app` folder. In it, set up the PostHog provider to initialize after hydration. You'll need both your API key and instance address (you can find these in your [project settings](https://us.posthog.com/project/settings)).

TypeScript

PostHog AI

```typescript
// app/provider.tsx
import { useEffect, useState } from "react";
import posthog from "posthog-js";
import { PostHogProvider } from "@posthog/react";
export function PHProvider({ children }: { children: React.ReactNode }) {
  const [hydrated, setHydrated] = useState(false);
  useEffect(() => {
    posthog.init("<ph_project_token>", {
      api_host: "https://us.i.posthog.com",
      defaults: "2026-01-30",
    });
    setHydrated(true);
  }, []);
  if (!hydrated) return <>{children}</>;
  return <PostHogProvider client={posthog}>{children}</PostHogProvider>;
}
```

Finally, import the `PHProvider` component in your `app/root.tsx` file and use it to wrap your app.

TypeScript

PostHog AI

```typescript
// app/root.tsx
// ... imports
import { PHProvider } from "./provider";
// ... links, meta, etc.
export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        <PHProvider>
          {children}
          <ScrollRestoration />
          <Scripts />
        </PHProvider>
      </body>
    </html>
  );
}
export default function App() {
  return <Outlet />;
}
```

When you run your app now, PostHog will automatically capture events and pageviews. You can also use the other features of PostHog by importing and using the `usePostHog` hook in your components.

## Identifying users

> **Identifying users is required.** Call `posthog.identify('your-user-id')` after login to link events to a known user. This is what connects frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), and [error tracking](/docs/error-tracking.md) to the same person — and lets backend events link back too.
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

Set up a reverse proxy (recommended)

We recommend [setting up a reverse proxy](/docs/advanced/proxy.md), so that events are less likely to be intercepted by tracking blockers.

We have our [own managed reverse proxy service](/docs/advanced/proxy/managed-reverse-proxy.md), which is free for all PostHog Cloud users, routes through our infrastructure, and makes setting up your proxy easy.

If you don't want to use our managed service then there are several other options for creating a reverse proxy, including using [Cloudflare](/docs/advanced/proxy/cloudflare.md), [AWS Cloudfront](/docs/advanced/proxy/cloudfront.md), and [Vercel](/docs/advanced/proxy/vercel.md).

Grouping products in one project (recommended)

If you have multiple customer-facing products (e.g. a marketing website + mobile app + web app), it's best to install PostHog on them all and [group them in one project](/docs/settings/projects.md).

This makes it possible to track users across their entire journey (e.g. from visiting your marketing website to signing up for your product), or how they use your product across multiple platforms.

Add IPs to Firewall/WAF allowlists (recommended)

For certain features like [heatmaps](/docs/toolbar/heatmaps.md), your Web Application Firewall (WAF) may be blocking PostHog’s requests to your site. Add these IP addresses to your WAF allowlist or rules to let PostHog access your site.

**EU**: `3.75.65.221`, `18.197.246.42`, `3.120.223.253`

**US**: `44.205.89.55`, `52.4.194.122`, `44.208.188.173`

These are public, stable IPs used by PostHog services (e.g., Celery tasks for snapshots).

## Next steps

For any technical questions for how to integrate specific PostHog features into Remix (such as analytics, feature flags, A/B testing, surveys, etc.), have a look at our [JavaScript Web SDK docs](/docs/libraries/js/features.md) and [React](/docs/libraries/react.md) docs.

Alternatively, the following tutorials can help you get started:

-   [How to set up Remix analytics, feature flags, and more](/tutorials/remix-analytics.md)
-   [How to set up A/B tests in Remix](/tutorials/remix-ab-tests.md)
-   [How to set up surveys in Remix](/tutorials/remix-surveys.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better