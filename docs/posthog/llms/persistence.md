# Source: https://posthog.com/docs/libraries/js/persistence.md

# JavaScript web persistence and cookies - Docs

For PostHog to work optimally, we store a small amount of information about the user on the user's browser. This ensures we identify users properly if they navigate away from your site and come back later.

The information we store includes:

-   Their `distinct_id`
-   Session ID & Device ID
-   Active & enabled feature flags
-   Any super properties you have defined
-   Some PostHog configuration options (e.g. whether session recording is enabled)

By default, we store all this information in both a `cookie` and `localStorage`, which means PostHog can identify your users across subdomains. By default, the name of the cookie PostHog sets is `ph_<project_api_key>_posthog` and it expires after `365` days.

If you want to change how PostHog stores this information, you can do so with the `persistence` configuration option:

-   `persistence: "localStorage+cookie"` (default): Limited things are stored in the cookie such as the distinctID and the sessionID, and everything else in the browser's [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

-   `persistence: "cookie"` : Stores all data in a cookie.

-   `persistence: "localStorage"`: Stores everything in `localStorage`.

-   `persistence: "sessionStorage"`: Stores everything in `sessionStorage`.

-   `persistence: "memory"`: Stores everything in page memory, which means data is only persisted for the duration of the page view.

To change `persistence` values without reinitializing PostHog, you can use the `posthog.set_config()` method. This enables you to switch from memory to cookies to better comply with privacy regulations.

Web

PostHog AI

```javascript
const handleCookieConsent = (consent) => {
  posthog.set_config({ persistence: consent === 'yes' ? 'localStorage+cookie' : 'memory' });
  localStorage.setItem('cookie_consent', consent);
};
```

## Cookie-persisted properties

When using `localStorage+cookie` persistence (the default), most properties are stored in `localStorage` while only essential values like `distinct_id` and session ID go in the cookie. Since `localStorage` doesn't work across subdomains but cookies do, you can use the `cookie_persisted_properties` configuration option to specify additional properties that should be stored in the cross-subdomain cookie.

This is useful when you need specific properties to be available across subdomains. For example, you might want to track which products a user has shown interest in on your marketing site and use that data to personalize their onboarding experience on your app subdomain.

JavaScript

PostHog AI

```javascript
posthog.init('<ph_project_token>', {
    api_host: 'https://us.i.posthog.com',
    persistence: 'localStorage+cookie',
    cookie_persisted_properties: ['user_preferences', 'signup_source'],
})
```

You can then set these properties using `posthog.register()`:

JavaScript

PostHog AI

```javascript
// Store a property that will persist in the cookie
posthog.register({ signup_source: 'product-page' })
// Later, read it back (works across subdomains)
const source = posthog.get_property('signup_source')
```

### Example: tracking user interests across subdomains

Here's an example of tracking which products a user has viewed on a marketing site, then using that data for personalized onboarding on an app subdomain (like we do!):

JavaScript

PostHog AI

```javascript
// On marketing site (e.g., example.com)
posthog.init('<ph_project_token>', {
    api_host: 'https://us.i.posthog.com',
    persistence: 'localStorage+cookie',
    cookie_persisted_properties: ['product_interests'],
})
// When user visits a product page
function trackProductInterest(productSlug) {
    const currentInterests = posthog.get_property('product_interests') || []
    if (!currentInterests.includes(productSlug)) {
        currentInterests.push(productSlug)
    }
    posthog.register({ product_interests: currentInterests })
}
// On app subdomain (e.g., app.example.com)
// The property is automatically available because it's in the cross-subdomain cookie
const interests = posthog.get_property('product_interests') || []
// interests = ["analytics", "session-replay", ...]
```

> **Warning: Cookie size limits**
>
> Cookies have a maximum size of approximately 4KB. If your `cookie_persisted_properties` store large arrays or complex objects, you may exceed this limit, which can cause:
>
> -   Properties being silently truncated or not stored
> -   `431 Request Header Fields Too Large` errors from your server
> -   Unexpected behavior when reading properties
>
> Keep cookie-persisted values small (short strings, small arrays of IDs). For larger data, consider using `localStorage` persistence and a different cross-subdomain strategy, or store the data server-side.

## Persistence caveats

-   Be aware that `localStorage` and `sessionStorage` can't be used across subdomains. If you have multiple sites on the same domain, you may want to consider a `cookie` option or make sure to set all super properties across each subdomain.

-   Due to the size limitation of cookies you may run into `431 Request Header Fields Too Large` errors (e.g. if you have a lot of feature flags). In that case, use `localStorage+cookie`.

-   If you don't want PostHog to store anything on the user's browser (e.g. if you want to rely on your own identification mechanism only or want completely anonymous users), you can set `disable_persistence: true` in PostHog's config. If you do this, remember to call [`posthog.identify`](/docs/libraries/js/features.md#identifying-users) **every time** your app loads. If you don't, every page refresh is treated as a new and different user.

-   For browser extensions, use `localStorage`, `sessionStorage`, or `memory`. Each extension context may initialize its own PostHog instance. These contexts don't share storage so the instances don't know about each other. Since `browser.storage` and `chrome.storage` APIs are not supported for data persistence, you'll need to provide your own shared `distinct_id` during each initialization to ensure events are sent under the same identifier. See the [browser extension documentation](/docs/advanced/browser-extension.md) for more details.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better