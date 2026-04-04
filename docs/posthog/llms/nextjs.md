# Source: https://posthog.com/docs/web-analytics/installation/nextjs.md

# Source: https://posthog.com/docs/session-replay/installation/nextjs.md

# Source: https://posthog.com/docs/logs/installation/nextjs.md

# Source: https://posthog.com/docs/experiments/installation/nextjs.md

# Source: https://posthog.com/docs/error-tracking/upload-source-maps/nextjs.md

# Source: https://posthog.com/docs/error-tracking/installation/nextjs.md

# Source: https://posthog.com/docs/advanced/proxy/nextjs.md

# Next.js rewrites reverse proxy - Docs

**Before you start**

-   If you use a self-hosted proxy, PostHog can't help troubleshoot. Use [our managed reverse proxy](/docs/advanced/proxy/managed-reverse-proxy.md) if you want support.
-   Use domains matching your PostHog region: `us.i.posthog.com` for US, `eu.i.posthog.com` for EU.
-   Don't use obvious path names like `/analytics`, `/tracking`, `/telemetry`, or `/posthog`. Blockers will catch them. Use something unique to your app instead.

This guide shows you how to use [Next.js rewrites](https://nextjs.org/docs/app/api-reference/next-config-js/rewrites) as a reverse proxy for PostHog.

## How it works

Next.js rewrites map incoming request paths to different destinations. When you add PostHog rewrites, Next.js fetches content from PostHog's servers and returns it under your domain.

Here's the request flow:

1.  User triggers an event in your app
2.  Request goes to your domain (e.g., `yourdomain.com/ph`)
3.  Next.js matches the request against your rewrite rules
4.  Next.js fetches the response from PostHog's servers
5.  Next.js returns PostHog's response under your domain

This works because the rewrite happens server-side, so the browser only sees requests to your domain. Ad blockers that filter by domain won't block these requests.

**Hosting compatibility**

Rewrites work best when self-hosting Next.js or using Vercel. Some hosting platforms modify headers during rewrites, causing `503` or `400` errors.

If you encounter issues, try [Next.js proxy](/docs/advanced/proxy/nextjs-middleware.md) (formerly middleware) or a platform-specific proxy like [Netlify](/docs/advanced/proxy/netlify.md).

## Prerequisites

This guide works with any Next.js project using the app router or pages router.

## Setup

1.  1

    ## Add rewrites to next.config.js

    Add a `rewrites()` function and the `skipTrailingSlashRedirect` option to your `next.config.js`:

    JavaScript

    PostHog AI

    ```javascript
    // next.config.js
    const nextConfig = {
      async rewrites() {
        return [
          {
            source: '/ph/static/:path*',
            destination: 'https://us-assets.i.posthog.com/static/:path*',
          },
          {
            source: '/ph/:path*',
            destination: 'https://us.i.posthog.com/:path*',
          },
        ]
      },
      skipTrailingSlashRedirect: true,
    }
    module.exports = nextConfig
    ```

    Replace `us` with `eu` for EU region.

    Here's what each part does:

    -   The first rewrite routes static asset requests to PostHog's asset server. This serves the JavaScript SDK and other static files.
    -   The second rewrite routes all other requests to PostHog's main API. This handles event capture, feature flags, and session recordings.
    -   `skipTrailingSlashRedirect` prevents Next.js from redirecting URLs with trailing slashes. PostHog's API uses trailing slashes (like `/e/`), and without this setting, Next.js would redirect them and break event capture.

    The static rewrite must come first. Next.js evaluates rewrites in order, so if the catch-all rule came first, it would match `/ph/static/*` before the static-specific rule.

    See [Next.js rewrites documentation](https://nextjs.org/docs/app/api-reference/next-config-js/rewrites) for more details.

2.  2

    ## Update your PostHog SDK

    In your application code, update your PostHog initialization to use your proxy path:

    PostHog AI

    ### US

    ```javascript
    posthog.init(process.env.NEXT_PUBLIC_POSTHOG_TOKEN, {
      api_host: '/ph',
      ui_host: 'https://us.posthog.com'
    })
    ```

    ### EU

    ```javascript
    posthog.init(process.env.NEXT_PUBLIC_POSTHOG_TOKEN, {
      api_host: '/ph',
      ui_host: 'https://eu.posthog.com'
    })
    ```

    The `api_host` tells the SDK where to send events. Using a relative path ensures requests go to your domain. The `ui_host` must point to PostHog's actual domain so features like the toolbar link correctly.

3.  3

    ## Deploy your changes

    Commit and push your changes. Restart your dev server if testing locally, as Next.js doesn't hot-reload config changes.

4.  ## Verify your setup

    Checkpoint

    Confirm events are flowing through your proxy:

    1.  Open your browser's developer tools and go to the **Network** tab
    2.  Navigate to your site or trigger an event
    3.  Look for requests to your domain with your proxy path (e.g., `yourdomain.com/ph`)
    4.  Verify the response status is `200 OK`
    5.  Check the [PostHog app](https://app.posthog.com) to confirm events appear in your activity feed

    If you see errors, check [troubleshooting](#troubleshooting) below.

## Troubleshooting

### 503 or 400 errors

Some hosting platforms modify headers during rewrites, breaking the proxy. This commonly happens with Heroku and Netlify.

Solutions:

1.  Use [Next.js proxy](/docs/advanced/proxy/nextjs-middleware.md) (formerly middleware) for more control over the request
2.  Use a platform-specific proxy like [Netlify redirects](/docs/advanced/proxy/netlify.md)
3.  Self-host Next.js or use Vercel

### Rewrites not working

If requests to your proxy path return 404:

1.  Verify your `next.config.js` is in the project root
2.  Restart your dev server after changing the config
3.  Check the rewrite order: static assets rule must come before the catch-all

### Trailing slash conflicts with SEO

The `skipTrailingSlashRedirect` setting is required for PostHog API requests but can cause SEO issues if pages become accessible at both `/page` and `/page/`.

Solutions:

1.  Handle trailing slash redirects in [Next.js middleware](https://nextjs.org/docs/app/building-your-application/routing/middleware) for non-PostHog routes
2.  Use `<link rel="canonical">` to specify the preferred URL for search engines
3.  Ensure your sitemap only includes one URL format

### 401 errors or "No project token provided"

If you see authentication errors and have verified your project token is correct, this usually indicates a region mismatch. Ensure the domains in your rewrites match your PostHog project's region (`us` or `eu`).

Some hosting platforms also strip the request body during rewrites, losing the project token. If this happens, use [Next.js proxy](/docs/advanced/proxy/nextjs-middleware.md) instead.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better