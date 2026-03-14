# Source: https://documentation.onesignal.com/reference/rest-api-overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# REST API Overview

> Learn about OneSignal's REST API capabilities, security requirements, rate limits, retries, and how to send notifications, manage users, apps, and segments programmatically.

Our REST API follows the [REST architecture](https://en.wikipedia.org/wiki/Representational_state_transfer) and provides programmatic access to OneSignal’s core messaging and user features. Use the API to send push notifications, emails, and SMS, manage users, subscriptions, segments, export data, and configure apps.

***

## Requirements

**General**

* **HTTPS required**: All API requests must use HTTPS with **TLS 1.2 or higher** on port `443`.
* **Network access**: Firewalls or proxies must allow **outbound traffic** to `https://api.onesignal.com` on port `443`.
* **DNS TTL**: Clients must respect OneSignal’s DNS **TTL of 300 seconds** to avoid stale IP resolution.

**Incoming Traffic to OneSignal (API & SDK Requests)**

All incoming API traffic—whether from your backend, our SDKs, or the dashboard—passes through **Cloudflare**, which serves as our global edge network.

* You may see Cloudflare IP addresses in logs.
* Cloudflare IPs may change over time.
* If you maintain a strict firewall, use Cloudflare’s official IP ranges: [https://www.cloudflare.com/ips/](https://www.cloudflare.com/ips/)

<Warning>
  We do not recommend allowlisting specific Cloudflare IPs, as they may change without notice.
</Warning>

**Outgoing Traffic from OneSignal (Webhooks & Event Streams)**

For features where OneSignal sends HTTP requests to your servers (such as webhooks or event streams), traffic originates from OneSignal infrastructure running on Google Cloud Platform (GCP) in the `europe-west4` region (Groningen, Netherlands).

* Allow inbound traffic from `https://api.onesignal.com`, **or**
* Use GCP’s maintained IP range list and filter by `europe-west4` region: [https://www.gstatic.com/ipranges/cloud.json](https://www.gstatic.com/ipranges/cloud.json)

<Note>We support [IP allowlisting](/docs/en/keys-and-ids) with REST API keys.</Note>

***

### Platform-specific network requirements

#### FCM (Google Android and Chrome push)

* Required ports: `5228`, `443`, `5229`, and `5230`
* No IP allow-listing needed
* More info: [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall)

#### APNs (Apple iOS, iPadOS, Safari push)

* Required ports: `5223`, `443`, and `2197`
* Recommended servers:
  * Sandbox: `api.sandbox.push.apple.com:443`
  * Production: `api.push.apple.com:443`
  * IP range: `17.0.0.0/8`
* More info:
  * [Apple Support](https://support.apple.com/en-us/102266)
  * [APNs Developer Docs](https://developer.apple.com/documentation/usernotifications/sending-notification-requests-to-apns?language=objc)

***

## Core API capabilities

### Send messages

See our [Create Message guide](/reference/create-message) to get started. Programmatically send:

<Columns cols={2}>
  <Card title="Push Notifications" href="/reference/push-notification" arrow={true}>
    Send push notifications to apps and websites.
  </Card>

  <Card title="Email" href="/reference/email" arrow={true}>
    Send transactional and promotional emails.
  </Card>

  <Card title="SMS" href="/reference/sms" arrow={true}>
    Send SMS or MMS messages globally.
  </Card>

  <Card title="Live Activities" href="/reference/start-live-activity" arrow={true}>
    Send Live Activity updates to iOS devices.
  </Card>
</Columns>

#### Supported features

Below are common supported features for each platform. See our overview docs for each platform's supported features:

* [Push overview](/docs/en/push)
* [Email overview](/docs/en/email-messaging)
* [SMS overview](/docs/en/sms-messaging)
* [Live Activities overview](/docs/en/live-activities)

<Columns cols={2}>
  <Card title="Message Personalization" href="/docs/en/message-personalization" arrow={true}>
    Add dynamic content to personalize messages for each user.
  </Card>

  <Card title="Multi-Language Messaging" href="/docs/en/multi-language-messaging" arrow={true}>
    Send push notifications in multiple languages.
  </Card>

  <Card title="Throttling" href="/docs/en/throttling" arrow={true}>
    Control push notification delivery speed.
  </Card>

  <Card title="Frequency Capping" href="/docs/en/frequency-capping" arrow={true}>
    Limit the number of push notifications per user.
  </Card>

  <Card title="Data & background notifications" href="/docs/en/data-notifications" arrow={true}>
    Send data-only notifications for background tasks.
  </Card>
</Columns>

***

### Manage templates

[Templates](/docs/en/templates) are reusable push, email, and SMS messages that simplify development and improve consistency.

<Columns cols={2}>
  <Card title="Create template" href="/reference/create-template" arrow={true}>
    Create a reusable template.
  </Card>

  <Card title="Update template" href="/reference/update-template" arrow={true}>
    Update a template.
  </Card>

  <Card title="View templates" href="/reference/view-templates" arrow={true}>
    View all templates.
  </Card>

  <Card title="Delete template" href="/reference/delete-template" arrow={true}>
    Delete a template.
  </Card>
</Columns>

***

### Manage users and subscriptions

See our [Users](/docs/en/users) and [Subscriptions](/docs/en/subscriptions) guides for more details.

<Columns cols={2}>
  <Card title="Create user" href="/reference/create-user" arrow={true}>
    Create a user with optional aliases and subscriptions.
  </Card>

  <Card title="View user" href="/reference/view-user" arrow={true}>
    View user details.
  </Card>

  <Card title="Update user" href="/reference/update-user" arrow={true}>
    Update a user.
  </Card>

  <Card title="Delete user" href="/reference/delete-user" arrow={true}>
    Delete a user.
  </Card>
</Columns>

### Manage segments

[Segments](/docs/en/segmentation) help group users by filters.

<Columns cols={2}>
  <Card title="Create Segments" href="/reference/create-segments" arrow={true}>
    Create a segment.
  </Card>

  <Card title="Delete Segments" href="/reference/delete-segments" arrow={true}>
    Delete a segment.
  </Card>
</Columns>

<Note>
  You can also target users dynamically using [filters](/reference/create-message#filters) without creating persistent segments.
</Note>

***

### Export data

For analytics breakdowns, see [Analytics overview](/docs/en/analytics-overview).

<Columns cols={2}>
  <Card title="Export CSV of subscriptions" href="/reference/csv-export" arrow={true}>
    Export all user and subscription data.
  </Card>

  <Card title="Export CSV of events" href="/reference/export-csv-of-events" arrow={true}>
    Export events like sent, received, and clicked.
  </Card>

  <Card title="View messages" href="/reference/view-messages" arrow={true}>
    View message details and analytics.
  </Card>

  <Card title="View message" href="/reference/view-message" arrow={true}>
    View individual message details.
  </Card>
</Columns>

***

### Manage apps & keys

OneSignal allows you to group platforms (mobile apps, websites) under a single App ID. See [Apps, orgs, & accounts](/docs/en/apps-organizations).

<Columns cols={2}>
  <Card title="Create an app" href="/reference/create-an-app" arrow={true}>
    Create an app.
  </Card>

  <Card title="Update an app" href="/reference/update-an-app" arrow={true}>
    Update an app.
  </Card>

  <Card title="View single app" href="/reference/view-an-app" arrow={true}>
    View a single app.
  </Card>

  <Card title="View multiple apps" href="/reference/view-apps" arrow={true}>
    View all apps.
  </Card>
</Columns>

**API key management**

See [Keys & IDs](/docs/en/keys-and-ids) for more details.

<Columns cols={2}>
  <Card title="Create API key" href="/reference/create-api-key" arrow={true}>
    Create an API key.
  </Card>

  <Card title="View API keys" href="/reference/view-api-keys" arrow={true}>
    View all API keys.
  </Card>

  <Card title="Delete API key" href="/reference/delete-api-key" arrow={true}>
    Delete an API key.
  </Card>

  <Card title="Update API key" href="/reference/update-api-key" arrow={true}>
    Update an API key.
  </Card>
</Columns>

***

## Error handling and retries

Our APIs may return temporary errors such as `429` (rate limited), `5xx` (server errors), or timeouts. When this happens, the request may still be processing.

If you retry failed requests, always use an `idempotency_key` and follow the recommended retry delays to avoid duplicate messages or accidental app disablement.

See [Rate limits and error handling](/reference/rate-limits) for retry strategies, error definitions, and recovery steps.

***

## FAQ

### What is the timeout for API responses?

* Default: **100 seconds**
* If you're unsure whether a request completed, use an [`idempotency_key`](/reference/idempotent-notification-requests) to safely retry.
* See [Rate limits and error handling](/reference/rate-limits) for more details.

### Do I need to download or renew certificates to call the OneSignal API?

No, you do not need to manually download or renew certificates to call the OneSignal API.

Our API uses HTTPS with a publicly trusted TLS certificate managed by Cloudflare. These edge certificates are renewed automatically by Cloudflare and trusted by all major browsers, operating systems, and runtimes. No extra action is needed unless your environment has special trust or pinning rules.

**Why you might be seeing frequent certificate changes**

If your network or middleware is configured to pin a specific leaf certificate (the one shown during the TLS handshake), you will see it expire and rotate every few months. This is normal — Cloudflare rotates these certificates for security. Most clients trust the public root and intermediate Certificate Authorities (CAs) instead, which avoids any impact when the leaf cert changes.

**Recommended approach**

* **Best practice**: Trust the root and intermediate CAs in the chain instead of the rotating leaf certificate. This allows certificate rotation without breaking your connection.
* **If you must pin a certificate**: Pin the public key (SPKI) of the CA or use a backup key set, not the exact leaf certificate.

**Workaround: Fetching the current certificate**

If your process requires the active leaf certificate, you can retrieve it directly from our API endpoint:

```bash  theme={null}
SERVERNAME=api.onesignal.com
echo -n | openssl s_client -connect $SERVERNAME:443 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /tmp/${SERVERNAME}_current.pem
```

To retrieve the full certificate chain, add the `-showcerts` flag to `openssl s_client` and capture all certificates printed.

**More information**

Cloudflare’s documentation explains how their SSL/TLS certificates work and why they rotate:

* [Cloudflare SSL/TLS documentation](https://developers.cloudflare.com/ssl/get-started/)
* [Cloudflare Edge Certificates documentation](https://developers.cloudflare.com/ssl/edge-certificates/)

***

Built with [Mintlify](https://mintlify.com).
