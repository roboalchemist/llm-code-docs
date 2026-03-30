# Source: https://posthog.com/docs/libraries/next-js/posthog-next.md

# Next.js: @posthog/next - Docs

**Pre-release**

`@posthog/next` is currently in pre-release. The API may change before the stable release. For production apps, see the [standard Next.js setup guide](/docs/libraries/next-js.md).

`@posthog/next` is a unified package for integrating PostHog into your Next.js app. It provides a simplified interface that handles common patterns out of the box:

-   **Synchronized identity across client and server**, so both sides share the same user automatically
-   **Server-side feature flag bootstrapping** so hooks return real values immediately with no flicker
-   **Eager client initialization** ensures PostHog is always available when your components render
-   **Built-in API proxy** that routes SDK traffic through your domain to avoid ad blockers
-   **Automatic event flushing** with no manual `shutdown()` or `flush()` calls needed

This guide covers both the App Router and Pages Router. You'll need a PostHog instance ([Cloud](https://app.posthog.com/signup) or [self-hosted](/docs/self-host.md)) and a Next.js 13.0.0+ application.

1.  1

    ## Install @posthog/next

    Required

    PostHog AI

    ### npm

    ```bash
    npm install --save @posthog/next
    ```

    ### Yarn

    ```bash
    yarn add @posthog/next
    ```

    ### pnpm

    ```bash
    pnpm add @posthog/next
    ```

    ### Bun

    ```bash
    bun add @posthog/next
    ```

2.  2

    ## Add your environment variables

    Required

    Add these to your `.env.local` file and to your hosting provider (e.g. Vercel, Netlify, AWS). You can find your project token in your [project settings](https://app.posthog.com/project/settings).

    .env.local

    PostHog AI

    ```shell
    NEXT_PUBLIC_POSTHOG_KEY=<ph_project_api_key>
    NEXT_PUBLIC_POSTHOG_HOST=https://us.i.posthog.com
    ```

    `NEXT_PUBLIC_POSTHOG_HOST` is optional and defaults to `https://us.i.posthog.com`.

3.  3

    ## Add the middleware

    Recommended

    The middleware seeds an identity cookie on first visit so client and server share the same user, and optionally proxies API requests through your domain.

    middleware.ts

    PostHog AI

    ```typescript
    import { postHogMiddleware } from '@posthog/next'
    export default postHogMiddleware({ proxy: true })
    export const config = {
        matcher: ['/((?!_next/static|_next/image|favicon.ico).*)'],
    }
    ```

    Setting `proxy: true` routes PostHog API calls through your domain at `/ingest`, which helps avoid ad blockers. You can customize the path prefix by passing `proxy: { pathPrefix: '/analytics' }` instead.

    > **Note:** Middleware requires a server runtime and is not available with `output: 'export'` (fully static sites). If you can't use middleware, you can set up a [reverse proxy](/docs/advanced/proxy.md) separately to route traffic through your domain.

4.  4

    ## Wrap your app with PostHogProvider

    Required

    ## App router

    Add `PostHogProvider` and `PostHogPageView` to your root layout:

    app/layout.tsx

    PostHog AI

    ```jsx
    import { PostHogProvider, PostHogPageView } from '@posthog/next'
    export default function RootLayout({ children }: { children: React.ReactNode }) {
        return (
            <html lang="en">
                <body>
                    <PostHogProvider clientOptions={{ api_host: '/ingest' }} bootstrapFlags>
                        <PostHogPageView />
                        {children}
                    </PostHogProvider>
                </body>
            </html>
        )
    }
    ```

    `PostHogProvider` is a React Server Component. When `bootstrapFlags` is enabled, it evaluates feature flags server-side and passes the results to the client so hooks return real values immediately.

    > **Note:** Enabling `bootstrapFlags` opts the route into dynamic rendering (incompatible with static generation / ISR). Without it, the provider does not call any dynamic Next.js APIs and is safe for static pages.

    ## Pages router

    Add `PostHogProvider` and `PostHogPageView` to your `_app`:

    pages/\_app.tsx

    PostHog AI

    ```jsx
    import type { AppProps } from 'next/app'
    import { PostHogProvider, PostHogPageView } from '@posthog/next/pages'
    export default function App({ Component, pageProps }: AppProps) {
        return (
            <PostHogProvider
                apiKey={process.env.NEXT_PUBLIC_POSTHOG_KEY!}
                clientOptions={{ api_host: '/ingest' }}
            >
                <PostHogPageView />
                <Component {...pageProps} />
            </PostHogProvider>
        )
    }
    ```

    > **Note:** For the Pages Router, import from `@posthog/next/pages` instead of `@posthog/next`.

5.  ## Verify events are captured

    Checkpoint

    *Confirm that you can see events in your PostHog project*

    Visit your app and click around. Within a minute or two, you should see `$pageview` and [autocaptured](/docs/product-analytics/autocapture.md) events (like clicks) appear in the [activity tab](https://app.posthog.com/activity/explore).

6.  5

    ## Access PostHog in client components

    Required

    All hooks must be used in client components (`'use client'`).

    **Capture events:**

    TSX

    PostHog AI

    ```jsx
    'use client'
    import { usePostHog } from '@posthog/next'
    export function TrackButton() {
        const posthog = usePostHog()
        return <button onClick={() => posthog.capture('button_clicked')}>Track</button>
    }
    ```

    **Feature Flags:**

    TSX

    PostHog AI

    ```jsx
    'use client'
    import { useFeatureFlag } from '@posthog/next'
    export function MyComponent() {
        const flag = useFeatureFlag('new-feature')
        return flag?.enabled ? <NewFeature /> : <OldFeature />
    }
    ```

    **Conditional rendering with `PostHogFeature`:**

    TSX

    PostHog AI

    ```jsx
    'use client'
    import { PostHogFeature } from '@posthog/next'
    export function NewBanner() {
        return (
            <PostHogFeature flag="show-banner" match={true}>
                <div>New feature available!</div>
            </PostHogFeature>
        )
    }
    ```

    You can also read [the full `posthog-js` documentation](/docs/libraries/js/features.md) for all the usable functions.

7.  6

    ## Identify your user

    Recommended

    Call `posthog.identify()` on the client after login to link events to a known user. This connects event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), and [Error Tracking](/docs/error-tracking.md) to the same person across client and server.

    TSX

    PostHog AI

    ```jsx
    'use client'
    import { usePostHog } from '@posthog/next'
    export function LoginButton() {
        const posthog = usePostHog()
        const handleLogin = async () => {
            const user = await signIn()
            posthog.identify(user.id, {
                email: user.email,
                name: user.name,
            })
        }
        return <button onClick={handleLogin}>Log in</button>
    }
    ```

    See our guide on [identifying users](/docs/getting-started/identify-users.md) for more details.

8.  7

    ## Use PostHog on the server

    Recommended

    ## App router

    Use `getPostHog()` in server components, route handlers, and server actions to capture events and evaluate feature flags. The client is automatically scoped to the current user via the identity cookie set by the middleware.

    TSX

    PostHog AI

    ```jsx
    import { getPostHog } from '@posthog/next'
    export default async function DashboardPage() {
        const posthog = await getPostHog()
        const flags = await posthog.getAllFlags()
        posthog.capture({ event: 'dashboard_viewed' })
        return (
            <div>{flags['new-dashboard'] ? <NewDashboard /> : <OldDashboard />}</div>
        )
    }
    ```

    > **Note:** `getPostHog()` calls `cookies()` internally, which opts the route into dynamic rendering. Pages using it cannot be statically generated.

    **Event flushing:** On Vercel, `@posthog/next` auto-detects [`waitUntil`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#waituntil) from `@vercel/functions` so events are flushed after the response is sent without blocking it. No manual `shutdown()` call is needed. In other environments, you can pass a custom `waitUntil` via `serverOptions` on the `PostHogProvider`, or events will be batched and flushed normally.

    ## Pages router

    Use `getServerSidePostHog` inside `getServerSideProps` to capture events and evaluate feature flags for the current user:

    pages/dashboard.tsx

    PostHog AI

    ```jsx
    import type { GetServerSideProps } from 'next'
    import { getServerSidePostHog } from '@posthog/next/pages'
    export const getServerSideProps: GetServerSideProps = async (ctx) => {
        const posthog = await getServerSidePostHog(ctx)
        const flags = await posthog.getAllFlags()
        posthog.capture({ event: 'dashboard_viewed' })
        return { props: { showNewDashboard: flags['new-dashboard'] ?? false } }
    }
    ```

    To bootstrap feature flags and eliminate flicker on page load, pass the flag data through `pageProps`:

    pages/dashboard.tsx

    PostHog AI

    ```jsx
    export const getServerSideProps: GetServerSideProps = async (ctx) => {
        const posthog = await getServerSidePostHog(ctx)
        const bootstrap = await posthog.getAllFlagsAndPayloads()
        return { props: { posthogBootstrap: bootstrap } }
    }
    ```

    **Event flushing:** On Vercel, `@posthog/next` auto-detects [`waitUntil`](https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package#waituntil) from `@vercel/functions` so events are flushed after the response is sent without blocking it. No manual `shutdown()` call is needed. In other environments, you can pass a custom `waitUntil` via `serverOptions` on the `PostHogProvider`, or events will be batched and flushed normally.

    Then wire the bootstrap data into the provider:

    pages/\_app.tsx

    PostHog AI

    ```jsx
    import type { AppProps } from 'next/app'
    import { PostHogProvider, PostHogPageView } from '@posthog/next/pages'
    export default function App({ Component, pageProps }: AppProps) {
        return (
            <PostHogProvider
                apiKey={process.env.NEXT_PUBLIC_POSTHOG_KEY!}
                clientOptions={{ api_host: '/ingest' }}
                bootstrap={pageProps.posthogBootstrap}
            >
                <PostHogPageView />
                <Component {...pageProps} />
            </PostHogProvider>
        )
    }
    ```

9.  8

    ## Further reading

    Recommended

    -   [How to set up Next.js analytics, Feature Flags, and more](/tutorials/nextjs-analytics.md)
    -   [How to set up Next.js A/B tests](/tutorials/nextjs-ab-tests.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better