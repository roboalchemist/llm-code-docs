# Source: https://posthog.com/docs/advanced/proxy/nextjs-middleware.md

# Next.js proxy file reverse proxy - Docs

**Before you start**

-   If you use a self-hosted proxy, PostHog can't help troubleshoot. Use [our managed reverse proxy](/docs/advanced/proxy/managed-reverse-proxy.md) if you want support.
-   Use domains matching your PostHog region: `us.i.posthog.com` for US, `eu.i.posthog.com` for EU.
-   Don't use obvious path names like `/analytics`, `/tracking`, `/telemetry`, or `/posthog`. Blockers will catch them. Use something unique to your app instead.

This guide shows you how to use [Next.js proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) (formerly middleware) as a reverse proxy for PostHog.

**Next.js 16 renamed middleware to proxy**

In Next.js 16, `middleware.js` was renamed to `proxy.js`. The functionality is identical, but the file and export names changed. If you're on Next.js 15 or earlier, use `middleware.js` and export `middleware` instead of `proxy`.

You can migrate existing middleware using: `npx @next/codemod@canary middleware-to-proxy .`

## How it works

Next.js proxy runs on the edge before a request reaches your pages. When a request matches your proxy path, it rewrites the request to PostHog's servers and returns the response under your domain.

Here's the request flow:

1.  User triggers an event in your app
2.  Request goes to your domain (e.g., `yourdomain.com/ph`)
3.  Next.js proxy intercepts the request before it reaches your pages
4.  Proxy rewrites the request URL to PostHog's servers
5.  PostHog processes the request and returns a response
6.  Proxy returns the response to the user under your domain

This works because the proxy runs server-side, so the browser only sees requests to your domain. Ad blockers that filter by domain won't block these requests.

## When to use proxy vs rewrites

Next.js offers two ways to proxy PostHog: [rewrites](/docs/advanced/proxy/nextjs.md) and proxy. Both work with the app router and pages router.

-   [**Rewrites:**](/docs/advanced/proxy/nextjs.md) Simpler configuration in `next.config.js`. Use this for most cases, especially on Vercel or self-hosted Next.js.
-   **Proxy:** More control over request handling. Use this when rewrites return `503` or `400` errors on your hosting platform, or when you need custom logic like header modification.

Try rewrites first. Use proxy if you encounter issues.

## Prerequisites

This guide works with any Next.js project using the app router or pages router. Requires Next.js 12.2 or later (use `middleware.js` for versions before 16, `proxy.js` for 16+).

## Setup

1.  1

    ## Create the proxy file

    Create a file named `proxy.js` (or `proxy.ts` for TypeScript) in your project root, at the same level as your `app` or `pages` folder:

    PostHog AI

    ### US

    ```javascript
    import { NextResponse } from 'next/server'
    export function proxy(request) {
      const url = request.nextUrl.clone()
      const hostname = url.pathname.startsWith('/ph/static/')
        ? 'us-assets.i.posthog.com'
        : 'us.i.posthog.com'
      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('host', hostname)
      url.protocol = 'https'
      url.hostname = hostname
      url.port = '443'
      url.pathname = url.pathname.replace(/^\/ph/, '')
      return NextResponse.rewrite(url, {
        headers: requestHeaders,
      })
    }
    export const config = {
      matcher: '/ph/:path*',
    }
    ```

    ### EU

    ```javascript
    import { NextResponse } from 'next/server'
    export function proxy(request) {
      const url = request.nextUrl.clone()
      const hostname = url.pathname.startsWith('/ph/static/')
        ? 'eu-assets.i.posthog.com'
        : 'eu.i.posthog.com'
      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('host', hostname)
      url.protocol = 'https'
      url.hostname = hostname
      url.port = '443'
      url.pathname = url.pathname.replace(/^\/ph/, '')
      return NextResponse.rewrite(url, {
        headers: requestHeaders,
      })
    }
    export const config = {
      matcher: '/ph/:path*',
    }
    ```

    Using Next.js 15 or earlier? Use middleware.js instead

    PostHog AI

    ### US

    ```javascript
    import { NextResponse } from 'next/server'
    export function middleware(request) {
      const url = request.nextUrl.clone()
      const hostname = url.pathname.startsWith('/ph/static/')
        ? 'us-assets.i.posthog.com'
        : 'us.i.posthog.com'
      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('host', hostname)
      url.protocol = 'https'
      url.hostname = hostname
      url.port = '443'
      url.pathname = url.pathname.replace(/^\/ph/, '')
      return NextResponse.rewrite(url, {
        headers: requestHeaders,
      })
    }
    export const config = {
      matcher: '/ph/:path*',
    }
    ```

    ### EU

    ```javascript
    import { NextResponse } from 'next/server'
    export function middleware(request) {
      const url = request.nextUrl.clone()
      const hostname = url.pathname.startsWith('/ph/static/')
        ? 'eu-assets.i.posthog.com'
        : 'eu.i.posthog.com'
      const requestHeaders = new Headers(request.headers)
      requestHeaders.set('host', hostname)
      url.protocol = 'https'
      url.hostname = hostname
      url.port = '443'
      url.pathname = url.pathname.replace(/^\/ph/, '')
      return NextResponse.rewrite(url, {
        headers: requestHeaders,
      })
    }
    export const config = {
      matcher: '/ph/:path*',
    }
    ```

    The only differences are the filename (`middleware.js`) and the exported function name (`middleware` instead of `proxy`).

    The proxy does the following:

    -   The `matcher` config tells Next.js to only run this proxy for requests starting with `/ph`
    -   It determines which PostHog host to use: the assets host for `/static/*` requests, the main host for everything else
    -   It sets the `host` header so PostHog knows how to route the request. Without this, you'll get 401 errors.
    -   It rewrites the URL to PostHog's domain and strips the `/ph` prefix

    See [Next.js proxy documentation](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) for more details.

2.  2

    ## Configure trailing slash handling

    Add `skipTrailingSlashRedirect` to your `next.config.js`:

    JavaScript

    PostHog AI

    ```javascript
    // next.config.js
    const nextConfig = {
      skipTrailingSlashRedirect: true,
    }
    module.exports = nextConfig
    ```

    PostHog's API endpoints use trailing slashes (like `/e/`). Without this setting, Next.js redirects these requests by removing the trailing slash, which breaks event capture.

3.  3

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

4.  4

    ## Deploy your changes

    Commit and push your changes. The proxy activates once deployed.

    In development, restart your dev server after creating the proxy file. Next.js doesn't hot-reload proxy changes.

5.  ## Verify your setup

    Checkpoint

    Confirm events are flowing through your proxy:

    1.  Open your browser's developer tools and go to the **Network** tab
    2.  Navigate to your site or trigger an event
    3.  Look for requests to your domain with your proxy path (e.g., `yourdomain.com/ph`)
    4.  Verify the response status is `200 OK`
    5.  Check the [PostHog app](https://app.posthog.com) to confirm events appear in your activity feed

    If you see errors, check [troubleshooting](#troubleshooting) below.

## Troubleshooting

### Proxy not running

If requests to your proxy path return 404 or don't get proxied:

1.  Verify your `proxy.js` (or `middleware.js` for Next.js <16) file is in the project root (same level as `app` or `pages`), not inside those folders
2.  Check that the `matcher` pattern matches your proxy path
3.  Restart your dev server after creating or modifying the proxy file

### Using with Clerk or other auth solutions

If you're using Clerk or similar auth solutions, handle PostHog routes before authentication. Add the proxy logic to your `beforeAuth` function and exclude the proxy path from auth:

PostHog AI

### US

```javascript
export default authMiddleware({
  beforeAuth(req) {
    if (req.nextUrl.pathname.startsWith('/ph')) {
      const url = req.nextUrl.clone()
      const hostname = url.pathname.startsWith('/ph/static/')
        ? 'us-assets.i.posthog.com'
        : 'us.i.posthog.com'
      const requestHeaders = new Headers(req.headers)
      requestHeaders.set('host', hostname)
      url.protocol = 'https'
      url.hostname = hostname
      url.port = '443'
      url.pathname = url.pathname.replace(/^\/ph/, '')
      return NextResponse.rewrite(url, {
        headers: requestHeaders,
      })
    }
  },
  ignoredRoutes: ['/ph(.*)'],
})
```

### EU

```javascript
export default authMiddleware({
  beforeAuth(req) {
    if (req.nextUrl.pathname.startsWith('/ph')) {
      const url = req.nextUrl.clone()
      const hostname = url.pathname.startsWith('/ph/static/')
        ? 'eu-assets.i.posthog.com'
        : 'eu.i.posthog.com'
      const requestHeaders = new Headers(req.headers)
      requestHeaders.set('host', hostname)
      url.protocol = 'https'
      url.hostname = hostname
      url.port = '443'
      url.pathname = url.pathname.replace(/^\/ph/, '')
      return NextResponse.rewrite(url, {
        headers: requestHeaders,
      })
    }
  },
  ignoredRoutes: ['/ph(.*)'],
})
```

### Cookies being forwarded to PostHog

By default, the proxy forwards all headers including cookies to PostHog. If you don't want to forward authentication cookies, delete them from the request:

JavaScript

PostHog AI

```javascript
const requestHeaders = new Headers(request.headers)
requestHeaders.set('host', hostname)
requestHeaders.delete('cookie')
```

Alternatively, configure PostHog to use `localStorage` instead of cookies:

JavaScript

PostHog AI

```javascript
posthog.init(process.env.NEXT_PUBLIC_POSTHOG_TOKEN, {
  api_host: '/ph',
  persistence: 'localStorage'
})
```

### 503 or 400 errors persist

If proxy doesn't resolve the errors, your hosting platform may be incompatible with Next.js proxying. Try:

1.  A platform-specific proxy like [Netlify redirects](/docs/advanced/proxy/netlify.md) or [Vercel rewrites](/docs/advanced/proxy/vercel.md)
2.  [PostHog's managed reverse proxy](/docs/advanced/proxy/managed-reverse-proxy.md)
3.  Self-hosting Next.js where you control the infrastructure

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better