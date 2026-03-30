# Source: https://posthog.com/docs/libraries/gatsby.md

# Gatsby - Docs

> This [library](https://github.com/posthog/gatsby-plugin-posthog) was built by the community. Thanks to [Ritesh Kadmawala](https://github.com/kgritesh) for building it.

Gatsby behaves like a single-page app which means to track `$pageview` events special care is needed. This integration takes care of that.

## Install

Terminal

PostHog AI

```bash
yarn add gatsby-plugin-posthog
```

or

Terminal

PostHog AI

```bash
npm install --save gatsby-plugin-posthog
```

## How to use

JavaScript

PostHog AI

```javascript
// In your gatsby-config.js
module.exports = {
  plugins: [
    {
      resolve: `gatsby-plugin-posthog`,
      options: {
        // Specify the API key for your PostHog Project (required)
        apiKey: "<ph_project_token>",
        // Specify the app host if self-hosting (optional, default: https://us.i.posthog.com)
        apiHost: "https://us.i.posthog.com",
        // Puts tracking script in the head instead of the body (optional, default: true)
        head: true,
        // Enable posthog analytics tracking during development (optional, default: false)
        isEnabledDevMode: true
      },
    },
  ],
}
```

This will automatically start tracking pageviews, clicks and more.

In your code you can access posthog via `window.posthog`.

For more instructions, see [browser JS library](/docs/integrate/client/js.md).

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

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better