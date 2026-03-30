# Source: https://posthog.com/docs/web-analytics/installation/ai-wizard.md

# Source: https://posthog.com/docs/product-analytics/installation/ai-wizard.md

# Source: https://posthog.com/docs/ai-engineering/ai-wizard.md

# AI wizard - Docs

The PostHog wizard automatically installs and instruments PostHog into your application codebase using AI. It's an agentic CLI tool that handles the entire PostHog integration process on your behalf.

Set up the PostHog platform in minutes, with a single command.

`npx @posthog/wizard@latest`

When it's done, your project is onboarded with:

-   [Product Analytics](/docs/product-analytics.md)
-   [Session Replay](/docs/session-replay.md)
-   [Error Tracking](/docs/error-tracking.md)
-   [Web Analytics](/docs/web-analytics.md)
-   [Feature Flags](/docs/feature-flags.md)
-   [Experiments](/docs/experiments.md)
-   [LLM Analytics](/docs/llm-analytics.md)
-   [Logs](/docs/logs.md)

## How it works

Running the wizard automatically:

1.  Authenticates your PostHog account
2.  Installs the relevant **PostHog SDKs**
3.  Scans your codebase and app architecture
4.  Creates **custom events** based on real product flows
5.  Configures `.env` file with your project credentials
6.  Writes code and instruments the PostHog SDKs **client-side** and **server-side**
7.  Generates **insights** and **dashboards** in the PostHog app
8.  Optionally installs the [PostHog MCP server](/docs/model-context-protocol.md) for your AI agent

The AI wizard integrating both the JS Web SDK and Node SDK into a Next.js application

## AI wizard installation

Install PostHog in minutes with our wizard by running this command in your project directory:

`npx @posthog/wizard@latest`

[Learn more](/wizard.md)

Wait for it to finish and test the setup once the wizard is complete.

## Frameworks and languages

The wizard supports the following frameworks and languages:

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Android_robot_bec2fb7318.svg)Android (Kotlin)](/docs/libraries/android.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/angular.svg)Angular](/docs/libraries/angular.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/astro_icon_dark_23a13977ad.svg)Astro](/docs/libraries/astro.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/django.svg)Django](/docs/libraries/django.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/python.svg)FastAPI](https://github.com/PostHog/wizard)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/flask.svg)Flask](/docs/libraries/flask.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/laravel.svg)Laravel](/docs/libraries/laravel.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nextjs.svg)Next.js](/docs/libraries/next-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nuxt.svg)Nuxt](/docs/libraries/nuxt.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/python.svg)Python](/docs/libraries/python.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React Native](/docs/libraries/react-native.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React](/docs/libraries/react.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ruby.svg)Ruby](/docs/libraries/ruby.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/rails_581d31c82d.svg)Ruby on Rails](/docs/libraries/rails.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/rr_logo_light_970950178e.svg)React Router](/docs/libraries/react-router.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/svelte.svg)SvelteKit](/docs/libraries/svelte.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ios.svg)Swift (iOS/macOS)](/docs/libraries/ios.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/logo_color_600_391d28faae.png)TanStack Start](https://github.com/PostHog/wizard)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/vue.svg)Vue](/docs/libraries/vue-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/elixir.svg)ElixirComing soon](/docs/libraries/elixir.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/flutter.svg)FlutterComing soon](/docs/libraries/flutter.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/go.svg)GoComing soon](/docs/libraries/go.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/java.svg)JavaComing soon](/docs/libraries/java.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/rust.svg)RustComing soon](/docs/libraries/rust.md)

We've got more on the way.

Check out the wizard's [GitHub repo](https://github.com/PostHog/wizard) for more details.

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

We think flows like the AI wizard are pretty cool and the future of developer experience. The AI wizard is our recommended and default method for [installing PostHog](/docs/getting-started/install?tab=wizard.md) and getting started.

If you have any feedback or requests, we would love to hear from you. Feel free to comment on this page or open an issue on [GitHub](https://github.com/PostHog/wizard/issues).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better