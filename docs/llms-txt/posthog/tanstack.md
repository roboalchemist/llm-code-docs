# Source: https://posthog.com/docs/web-analytics/installation/tanstack.md

# TanStack Start web analytics installation - Docs

1.  1

    ## Install the package

    Required

    Install the PostHog JavaScript library using your package manager:

    PostHog AI

    ### npm

    ```bash
    npm install posthog-js
    ```

    ### yarn

    ```bash
    yarn add posthog-js
    ```

    ### pnpm

    ```bash
    pnpm add posthog-js
    ```

2.  2

    ## Add environment variables

    Required

    Add your PostHog API key and host to your environment variables:

    .env

    PostHog AI

    ```bash
    VITE_PUBLIC_POSTHOG_KEY=<ph_project_token>
    VITE_PUBLIC_POSTHOG_HOST=https://us.i.posthog.com
    ```

3.  3

    ## Initialize PostHog

    Required

    Wrap your app with the `PostHogProvider` component at the root of your application (such as `main.tsx`):

    main.tsx

    PostHog AI

    ```jsx
    import { StrictMode } from 'react'
    import { createRoot } from 'react-dom/client'
    import './index.css'
    import App from './App.jsx'
    import { PostHogProvider } from 'posthog-js/react'
    const options = {
      api_host: import.meta.env.VITE_PUBLIC_POSTHOG_HOST,
      defaults: '2026-01-30',
    } as const
    createRoot(document.getElementById('root')).render(
      <StrictMode>
        <PostHogProvider apiKey={import.meta.env.VITE_PUBLIC_POSTHOG_KEY} options={options}>
          <App />
        </PostHogProvider>
      </StrictMode>
    )
    ```

    **defaults option**

    The `defaults` option automatically configures PostHog with recommended settings for new projects. See [SDK defaults](/docs/libraries/js.md#sdk-defaults) for details.

4.  4

    ## Send events

    Click around and view a couple pages to generate some events. PostHog automatically captures pageviews, clicks, and other interactions for you.

    If you'd like, you can also manually capture custom events:

    JavaScript

    PostHog AI

    ```javascript
    posthog.capture('my_custom_event', { property: 'value' })
    ```

5.  5

    ## Next steps

    Recommended

    After installing PostHog and ensuring [autocapture](/docs/data/autocapture.md) is enabled, head to your [web analytics dashboard](/docs/web-analytics/dashboard.md) to see your data. And then check out our [getting started](/docs/web-analytics/getting-started.md) guide.

    > **PostHog tip:** Web analytics works with [anonymous events](/docs/data/anonymous-vs-identified-events.md). This means if you are primarily using PostHog for web analytics, it can be significantly cheaper for you.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better