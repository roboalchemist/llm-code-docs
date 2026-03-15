# Source: https://posthog.com/docs/web-analytics/installation/docusaurus.md

# Source: https://posthog.com/docs/libraries/docusaurus.md

# Docusaurus - Docs

To easily track your Docusaurus site, you can install the [PostHog plugin](https://github.com/PostHog/posthog-docusaurus). This enables you to autocapture pageviews, clicks, session replays, as well as use the other features of PostHog such as [surveys](/docs/surveys.md).

## Install

Once you have your Docusaurus site set up, install the PostHog plugin:

Terminal

PostHog AI

```bash
npm install --save posthog-docusaurus
```

or

Terminal

PostHog AI

```bash
yarn add posthog-docusaurus
```

Next, add it to your Docusaurus config with your project token and instance address, both of which you can find in [your project settings](https://us.posthog.com/settings/project).

JavaScript

PostHog AI

```javascript
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      "posthog-docusaurus",
      {
        apiKey: "<ph_project_token>",
        appUrl: "https://us.i.posthog.com", // optional, defaults to "https://us.i.posthog.com"
        enableInDevelopment: false, // optional
      },
    ],
  ],
};
```

Run your site again to see events autocaptured by PostHog.

> **Note:**You can pass additional PostHog [config options](/docs/libraries/js/config.md) to the plugin, but they are passed through `JSON.stringify()`, so functions (such as `before_send`) are not supported.

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