# Source: https://developers.webflow.com/data/docs/webflow-v1-api-deprecation-notice.mdx

***

title: Webflow v1 API Deprecation Notice
slug: data/docs/webflow-v1-api-deprecation-notice
hidden: false
-------------

As part of Webflow's ongoing commitment to enhancing your developer experience, we're transitioning from the v1 APIs to the more advanced v2 APIs. This document outlines the deprecation timeline for v1 Apps, APIs, and Webhooks, and provides guidance on managing a smooth transition to v2. We recommend starting your migration as soon as possible to ensure uninterrupted service for your integrations.

## Key changes

1. **API Site Tokens:**
   * **Webflow has discontinued creation of v1 API Site Tokens.**<br />
     For new integrations or updates, developers should use v2 API Site Tokens.

     <Note>
       API Tokens are distinct from [auth tokens](/data/reference/oauth-app) generated via Webflow Apps.
     </Note>

   * See the [v2 migration guide](/data/docs/migrating-to-v2#migrating-to-v2-site-tokens-webhooks-and-v2-apps) for more on migrating to v2 API Site Tokens

2. **Webhooks:**
   * **Webflow will no longer support manual creation of v1 Webhooks.**<br />
     To continue receiving real-time notifications via webhooks, [register v2 webhooks](/data/docs/working-with-webhooks).
   * See the [v2 migration guide](/data/docs/migrating-to-v2#migrating-to-v2-site-tokens-webhooks-and-v2-apps) for more on migrating to v2 Webhooks

3. **App Registrations:**
   * **Webflow no longer accepts App submissions for new v1 Apps.**<br />
     To create new applications or update your existing v1 Apps to v2, use the [v2 App registration process](/data/docs/migrating-to-v2#building-v2-apps).
   * **Integrations/automations created by v1 Apps will stop receiving maintenance and support after <span>March 31, 2025</span>.**<br />
     See the [v2 migration guide](/data/docs/migrating-to-v2#migrating-to-v2-site-tokens-webhooks-and-v2-apps) for more on migrating to v2 Apps

## Important dates

* **<span>August 1, 2024</span>**: De-listing of Marketplace Apps that are still reliant on v1 (non-scoped) authorization.
* **<span>March 31, 2025</span>**: Deprecation date for the v1 API. While the v1 API may continue to function after this date, it will no longer receive maintenance, updates, or support. We recommend completing your migration to v2 before this date to ensure uninterrupted service.

Transitioning to the v2 API ensures that developers have access to the latest features, enhanced security, and improved performance. We understand the challenges that come with such transitions, and are committed to supporting the Webflow developer community every step of the way.

For any queries or support migrating to v2 APIs, Apps, and Webhooks, reach out to [developers@webflow.com](mailto:developers@webflow.com). For other support matters, please reach out to Webflow's [support team](https://support.webflow.com/).
