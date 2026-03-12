# Source: https://documentation.onesignal.com/docs/en/web-push-setup-faq.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web push FAQ

> Complete guide to OneSignal Web Push Notifications setup, requirements, browser compatibility, domain changes, and troubleshooting common issues for developers and website owners.

## Web push requirements

Your website must meet all of the following for Web Push to work:

**Browser APIs required**

* [Notification API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)
* [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)
* [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)

**Security & connection**

* ✅ HTTPS only (with valid SSL certificate)
* ✅ OneSignal's [service worker](./onesignal-service-worker) installed
* ✅ Browser must reach:
  * Browser push servers (e.g., FCM, Mozilla)
  * `api.onesignal.com`

**User state**

* ✅ Notification permission granted by user
* ❌ Not in Incognito/Private/Guest mode
* ❌ Site data not cleared (deletes subscriptions)

<Warning>Clearing browser data (cookies, site storage) automatically unsubscribes users from push notifications.</Warning>

### iOS/iPadOS requirements

To receive push on iOS or iPadOS:

* iOS 16.4+ or iPadOS 16.4+
* Site must be added to home screen and opened from there
* Valid `manifest.json` file with required fields
* Users must accept notification permissions after opening as web app

<Card title="iOS web push setup" href="./web-push-for-ios">
  Follow Apple-specific steps to enable web push on iPhones and iPads running iOS 16.4+.
</Card>

### Browser compatibility

Users may see [web permission prompts](/docs/en/permission-requests) but cannot subscribe to push notifications in incognito, private, or guest browser modes.

<Accordion title="Browser compatibility by operating system">
  | Browser                                                                          | Windows | macOS | Android | iOS |
  | -------------------------------------------------------------------------------- | ------- | ----- | ------- | --- |
  | [Chrome](https://en.wikipedia.org/wiki/Google_Chrome)                            | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Firefox](https://en.wikipedia.org/wiki/Firefox)                                 | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Safari 10+](https://en.wikipedia.org/wiki/Safari_\(web_browser\))               | ❌       | ✅     | ❌       | ✅ ¹ |
  | [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge)                   | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Opera](https://en.wikipedia.org/wiki/Opera_\(web_browser\)) ²                   | ✅       | ✅     | ✅       | ✅ ¹ |
  | [Samsung Internet](https://en.wikipedia.org/wiki/Samsung_Internet_for_Android) ² | ❌       | ❌     | ✅       | ✅ ¹ |
  | [Yandex](https://en.wikipedia.org/wiki/Yandex_Browser) ²                         | ✅       | ✅     | ✅       | ✅ ¹ |
  | [UC Browser](https://en.wikipedia.org/wiki/UC_Browser) ²                         | ✅       | ❌     | ✅       | ✅ ¹ |
  | [Internet Explorer](https://en.wikipedia.org/wiki/Internet_Explorer)             | ❌       | ❌     | ❌       | ❌   |
  | [DuckDuckGo](https://en.wikipedia.org/wiki/DuckDuckGo)                           | ❌       | ❌     | ❌       | ❌   |

  <Info>
    ¹ iOS requires web app installation (see [iOS web push setup](/docs/en/web-push-for-ios))

    ² Chromium-based browsers appear as "Chrome" in OneSignal analytics
  </Info>
</Accordion>

***

## Domain changes & migration

### Understanding browser origin policy

Browsers tie web push subscriptions to a specific [origin (domain/site URL)](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) for security reasons. **You cannot transfer subscribers between different origins** - this is a browser limitation, not a OneSignal restriction.

**Different origins include:**

* HTTP vs HTTPS (e.g., `http://mysite.com` → `https://mysite.com`)
* www vs non-www (e.g., `www.mysite.com` vs `mysite.com`)
* Different domains/subdomains (e.g., `domain1.com` vs `domain2.com` or `sub1.domain.com` vs `sub2.domain.com`)

### Migration options

When changing your site's origin, choose one of these approaches:

<Tabs>
  <Tab title="New OneSignal App (Recommended)">
    **Best for**: Most domain changes, especially when you want a clean migration

    1. **Create new OneSignal App** for your new domain
    2. **Dual-send strategy**: Continue sending from old app, but set "Launch URL" to your new domain
    3. **Gradual transition**:
       * High-frequency senders (1+ notifications/day): 2 weeks transition
       * Medium-frequency senders (2+ notifications/week): 2 months transition
    4. **Migration notifications**: Send 1-2 messages like "We've moved! Visit our new site to stay updated" at the beginning and end of transition

    <Warning> Sending identical messages from both apps will create duplicate notifications for users subscribed to both.</Warning>
  </Tab>

  <Tab title="Update App & Delete Old Subscribers">
    **Best for**: When you need to keep the same OneSignal App ID

    1. Use [Update an app](/reference/update-an-app) API with:
       * `name`: Your app/site name
       * `chrome_web_origin`: New site URL
       * `chrome_web_default_notification_icon`: Icon image URL

    2. **Delete old subscribers** to prevent duplicates:
       * Create segment: "Device Type is Web Push"
       * [Delete all users in segment](./delete-users)
  </Tab>
</Tabs>

### HTTP to HTTPS upgrade

Upgrading from HTTP to HTTPS creates a new origin. Follow the domain migration steps above since browsers treat HTTPS sites as completely separate from their HTTP versions.

***

## Multiple sites & subdomains

### Single app limitations

Due to browser same-origin policy, you **can not** use one OneSignal App for multiple origins like:

* `https://mysite.com` and `https://www.mysite.com`
* `https://main.com` and `https://shop.main.com`

### Solutions for multiple origins

<Tabs>
  <Tab title="Single Origin Strategy">
    * Subscribe users only on your main domain
    * Redirect users from other origins to main domain for subscription
    * Redirect back to original page after subscription
  </Tab>

  <Tab title="Separate Apps">
    * Create individual OneSignal Apps for each origin
    * Accept that users may receive duplicate notifications if subscribed to multiple sites
  </Tab>
</Tabs>

***

### Language support scenarios

<Tabs>
  <Tab title="Same Origin (Recommended)">
    * URLs like `https://mysite.com/en/` or `https://mysite.com/es/`
    * Use single OneSignal App
    * Follow [multi-language prompts guide](./permission-requests#faq)
    * Implement [Language & Localization](./multi-language-messaging)
  </Tab>

  <Tab title="Different Origins">
    * URLs like `https://en.mysite.com` or `https://es.mysite.com`
    * Requires separate OneSignal Apps for each subdomain
  </Tab>
</Tabs>

***

## Advanced configuration

### Multiple OneSignal apps on same site

* **Not recommended** - causes subscription conflicts.
* **What happens**: OneSignal auto-resubscribes users to the most recently visited App ID, causing subscribers to bounce between apps and creating many unsubscribed devices.
* **Better approach**: Use [Data Tags](./add-user-data-tags) to segment users within a single app.

### Subfolder sites

Web push operates at the origin level. For sites in subfolders (e.g., `https://example.com/blog`), use the main origin (`https://example.com`) for setup.

### Self-hosting SDK files

**Strongly discouraged**. Browser push specifications change frequently, and OneSignal updates files immediately to maintain compatibility. Use OneSignal's CDN URLs from your Web Push Settings instead.

### Custom init code

Custom `init` code only works with [Custom Code Setup](./web-push-custom-code-setup).

**Typical Setup or Website Builder users**: Custom init code will be ignored by the OneSignal SDK. If you need to delay initialization, use the [privacy methods](./web-sdk-reference#privacy).

***

## Development & testing

### Local environment testing

See [Web SDK setup > Local testing](./web-sdk-setup#local-testing) for complete local testing setup.

### Service worker integration

OneSignal can work alongside existing service workers and PWAs. See [Integrating Multiple Service Workers](./onesignal-service-worker) for implementation details.

***

## Push spam

Push notifications are not designed to be used for advertisments, spamming users, or deceptive campaigns.

If your app is detected as sending spam notifications, browsers may send your users a "Spam warning" notification.

Avoid sending notifications that:

* Are not relevant to the users
* Use words like "Ads" or link to a page that is not related to the app
* Are not from a trusted source (e.g. a brand you are not associated with)

<Warning>
  See [Fighting Unwanted Notifications with Machine Learning in Chrome](https://blog.chromium.org/2025/05/fighting-unwanted-notifications-with.html) for more information.
</Warning>

If your app is being flagged as spam, you can:

* Review your notification content and remove anything that may be considered spam. This includes:
  * The words "Ads" or "Ad" in the title or body
  * Links to pages that are not related to the app
  * Links to pages that are not from a trusted source (e.g. a brand you are not associated with)
* Continue sending and monitor further reports.

***

## Troubleshooting

### Update deployment timing

* **Service Worker files**: 24-hour cache
* **Web SDK**: 3-day cache

Plan accordingly when deploying critical updates.

### macOS Chrome notification issues

For macOS Chrome users, ensure notifications are enabled for **both**:

1. **Google Chrome** app (Apple Menu > Settings > Notifications)
2. **Google Chrome Helper** app

Without both enabled, notifications won't appear in the notification center.

### Next steps after setup

1. **Test thoroughly** across your supported browsers and devices
2. **Implement proper error handling** for permission requests
3. **Set up analytics** to monitor subscription rates
4. **Plan your notification strategy** to avoid user fatigue
5. **Consider A/B testing** your permission request timing and messaging

### Common migration gotchas

* **Browser data clearing** unsubscribes users automatically
* **Duplicate notifications** during dual-app transitions
* **iOS requires web app installation** before push works
* **Private/Incognito modes** never support push notifications
* **Service workers must be accessible** at your site's root or configured subdirectory

***

## Next steps

* [Web SDK setup](./web-sdk-setup)
* [Web SDK reference](./web-sdk-reference)

***

Built with [Mintlify](https://mintlify.com).
