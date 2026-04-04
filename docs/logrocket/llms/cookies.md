# Source: https://docs.logrocket.com/reference/cookies.md

# Cookies

The LogRocket SDK uses first-party cookies to properly stitch together sessions. These cookies are not visible to our backend, and are only accessible by the clientside SDK while a session is being recorded.

The LogRocket SDK creates cookies with the following prefixes:

`_lr_tabs_`is used for session persistence, by default containing unidentifiable information about the current session. In conjunction with the `_lr_hb_` cookie, this cookie detects if a LogRocket session with the same appID is active in another tab, preventing multiple tabs from spawning multiple sessions. This cookie also holds Conditional Recording rules, telling the SDK what conditions to look for when triggering sessions.

`_lr_hb_`is used for cross-tab activity checking and contains a single timestamp that is periodically updated.

By default these cookies do not contain any identifiable information. They do not record user's IP address or device ID or other identifiable information. These cookies are necessary for LogRocket's basic functionality, and cannot be disabled.

### Additional Configuration

If needed, it is possible to include user identity information in the `_lr_tabs_` session persistence cookie by setting the `persistUserIdInfo` configuration setting to `true` when initializing LogRocket. The main reason to do this is to enable user identity information to be persisted within a LogRocket session while a user navigates between web applications on different subdomains (i.e. from `www.mystore.com` to `checkout.mystore.com`). This type of situation is common if you are running a [headless Shopify store](https://www.shopify.com/plus/solutions/headless-commerce), and still want to maintain user identity information when [capturing checkout activity](https://docs.logrocket.com/docs/shopify-capture-app) on a different subdomain.