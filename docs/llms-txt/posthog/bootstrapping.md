# Source: https://posthog.com/docs/feature-flags/bootstrapping.md

# Client-side bootstrapping - Docs

> **Note:** Bootstrapping feature flags is only available in our [JavaScript web](/docs/libraries/js.md) and [React Native](/docs/libraries/react-native.md) SDKs.

Since there is a delay between initializing PostHog and fetching feature flags, feature flags are not always available immediately. This makes them unusable if you want to do something like redirecting a user to a different page based on a feature flag.

To have your feature flags available immediately, you can initialize PostHog with precomputed values until it has had a chance to fetch them. This is called bootstrapping. After the SDK fetches feature flags from PostHog, it will use those flag values instead of bootstrapped ones.

To bootstrap PostHog with feature flags, use the `bootstrap` key in the initialization config and add feature flag values to it:

PostHog AI

### Web

```javascript
posthog.init('<ph_project_token>', {
    api_host: 'https://us.i.posthog.com',
    defaults: '2026-01-30',
    bootstrap: {
        featureFlags: {
            'flag-1': true,
            'variant-flag': 'control',
            'other-flag': false,
        },
    },
})
```

### React Native

```jsx
// App.(js|ts)
import { usePostHog, PostHogProvider } from 'posthog-react-native'
export function MyApp() {
    return (
        <PostHogProvider apiKey="<ph_project_token>" options={{
            // usually 'https://us.i.posthog.com' or 'https://eu.i.posthog.com'
            host: 'https://us.i.posthog.com',
            bootstrap: {
                featureFlags: {
                    'flag-1': true,
                    'variant-flag': 'control',
                    'other-flag': false
                }
            }
        }}>
            <MyComponent />
        </PostHogProvider>
    )
}
```

## Setting the correct flag values

To ensure you are bootstrapping PostHog with the correct flag values, we recommend fetching the flags values from your server alongside the page load request, and then passing them to your frontend.

You can do this by:

1.  When receiving a frontend request, fetch all the feature flags for the user on the backend by calling [`getAllFlags()`](/docs/feature-flags/adding-feature-flag-code?tab=Node.js.md#fetching-all-flags-for-a-user).
2.  Return the frontend request with the flags values in the response.
3.  On the frontend, get the flag values from the response and add them to the `bootstrap` key in the PostHog initialization.

> **Tip:** to ensure your request is as quick as possible, use [local evaluation](/docs/feature-flags/local-evaluation.md) on your server.

### Bootstrapping in single-page apps

In environments where `posthog.init` only runs once during a session (for example, SPAs like Next.js using `instrumentation-client`), you have two options:

-   **Server-side pre-evaluation**: Evaluate flags before the app renders, then pass the values into your app and add them to `bootstrap` or use them directly.
-   **Client-side pre-evaluation**: Evaluate the flag in an earlier page/state than the one where you need the value, then store and reuse it immediately when required.

Both approaches avoid flicker and achieve the same outcome as bootstrapping, as long as you use the same `distinct_id` across client and server.

## Bootstrapping with a distinct ID

The `bootstrap` object has four optional arguments: `distinctID`, `isIdentifiedID`, `sessionID`, and `featureFlags`.

-   `distinctID` enables you to set distinct ID of the user during PostHog's initialization. This is useful when you want to ensure the distinct ID on your frontend is the same as the distinct ID that you called `getAllFlags()` with on your server. It is **strongly recommended** to include it.

> **Note:** The only case where you don't want to include `distinctID` is when your user has an existing PostHog session and you have not yet called [`identify()`](/docs/product-analytics/identify.md) at any point in time to link the anonymous session ID with their identified ID. In this case, bootstrapping `distinctID` will cause PostHog to drop the anonymous session ID and the two sessions will not be linked.

-   `isIdentifiedID` ensures that the `distinctID` is treated as an [identified ID](/docs/product-analytics/identify.md) in the library. This is helpful as it warns you when you try to do something wrong with this ID, like calling identify again with a different ID. Set this to `true` if you're using a unique ID such as `email` or a database ID. Set this to `false` if you're generating a random anonymous ID.

-   `sessionID` enables you to connect sessions across domains. This enables you get an accurate session count and complete session replays. To get the session ID, call `posthog.get_session_id()`.

-   `featureFlags` enables flag values to be available as soon as PostHog loads. Call `posthog.getAllFlags()` (or equivalent method) in your backend and pass the values to your frontend in the `bootstrap` object.

PostHog AI

### Web

```javascript
posthog.init('<ph_project_token>', {
    api_host: 'https://us.i.posthog.com',
    defaults: '2026-01-30',
    bootstrap: {
        distinctID: 'distinct_id_of_your_user',
        isIdentifiedID: true,
        sessionID: 'session_id_of_user_session',
        featureFlags: {
            'flag-1': true,
            'variant-flag': 'control',
            'other-flag': false,
        },
    },
})
```

### React Native

```jsx
// App.(js|ts)
import { usePostHog, PostHogProvider } from 'posthog-react-native'
export function MyApp() {
    return (
        <PostHogProvider apiKey="<ph_project_token>" options={{
            // usually 'https://us.i.posthog.com' or 'https://eu.i.posthog.com'
            host: 'https://us.i.posthog.com',
            bootstrap: {
                distinctId: 'distinct_id_of_your_user',
                isIdentifiedId: true,
                featureFlags: {
                    'flag-1': true,
                    'variant-flag': 'control',
                    'other-flag': false
                }
            }
        }}>
            <MyComponent />
        </PostHogProvider>
    )
}
```

## Overriding feature flags

Bootstrapped feature flag values are temporary and are disregarded after PostHog fetches flag values. If you are trying to override feature flag values in a persistent manner, some PostHog SDKs support overriding flags:

PostHog AI

### Node.js

```javascript
posthog.overrideFeatureFlag('my-feature-flag', true)
```

### Web

```javascript
posthog.featureFlags.overrideFeatureFlags({flags: {'my-feature-flag': 'variant-1', 'other-feature': true}})
// you can also override feature flag payloads
posthog.featureFlags.overrideFeatureFlags({flags: {'my-feature-flag': 'variant-1'}, payloads: {'my-feature-flag': {someData: true}}})
```

## Examples

-   [How to bootstrap feature flags in React and Express](/tutorials/bootstrap-feature-flags-react.md)
-   [How to use Next.js middleware to bootstrap feature flags](/tutorials/nextjs-bootstrap-flags.md)
-   [How to set up Next.js A/B tests](/tutorials/nextjs-ab-tests.md)
-   [How to set up cross-domain tracking](/tutorials/cross-domain-tracking.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better