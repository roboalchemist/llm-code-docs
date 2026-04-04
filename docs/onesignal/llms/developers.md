# Source: https://documentation.onesignal.com/docs/en/developers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Developers

> Developer guide to integrating OneSignal: SDK setup, API reference, User identity, and testing across mobile and web.

This guide helps developers integrate OneSignal into mobile and web applications. Follow the sections in order for a first-time setup, or jump to the area you need.

1. [**Get started**](#get-started) — access your OneSignal App and find your API keys
2. [**Set up messaging channels**](#set-up-messaging-channels) — install the SDK and configure channels
3. [**SDK and API reference**](#sdk-and-api-reference) — detailed method, class, and endpoint documentation
4. [**Users and identity**](#users-and-identity) — identify Users, manage Subscriptions, and secure access
5. [**Testing and debugging**](#testing-and-debugging) — verify your integration before going live
6. [**Webhooks and events**](#webhooks-and-events) — receive message events server-side

***

## Get started

If your team already has a OneSignal account, ask an admin to [invite you](./manage-team-members) to the Organization. Otherwise, [create an account](https://onesignal.com) to get started.

Your OneSignal App is where User and message data lives. Each App has its own App ID, API keys, and messaging channels. You can have multiple Apps in a single Organization for different projects or environments.

<Columns cols={2}>
  <Card title="Apps, Organizations, and accounts" icon="building" href="./apps-organizations">
    How Apps, Organizations, and accounts relate to each other.
  </Card>

  <Card title="Keys and IDs" icon="key" href="./keys-and-ids">
    Find your App ID, REST API key, and Organization ID for authentication.
  </Card>

  <Card title="Add team members" icon="user-plus" href="./manage-team-members">
    Invite developers and assign roles within your Organization.
  </Card>

  <Card title="Usage and billing" icon="credit-card" href="./billing-faq">
    Billing, invoices, and usage details.
  </Card>
</Columns>

***

## Set up messaging channels

Install the OneSignal SDK to create and track user engagement for your platforms. Each message channel has its own setup guide covering credentials, SDK initialization, and tutorials.

<Columns cols={3}>
  <Card title="Mobile SDK setup" icon="mobile" href="./mobile-sdk-setup">
    SDK setup for iOS, Android, Huawei, and Amazon. Enables push notifications, in-app messages, and Live Activities.
  </Card>

  <Card title="Web push" icon="globe" href="./web-sdk-setup">
    Web SDK installation and browser push notification setup.
  </Card>

  <Card title="Email" icon="envelope" href="./email-setup">
    Email channel configuration and sender domain verification.
  </Card>

  <Card title="In-app messages" icon="window-maximize" href="./in-app-messages-setup">
    Display rich, interactive messages within your mobile app.
  </Card>

  <Card title="SMS" icon="comment-sms" href="./sms-messaging">
    SMS channel setup and carrier registration.
  </Card>

  <Card title="RCS" icon="message" href="./rcs-messaging">
    Rich messaging with branded content and read receipts.
  </Card>

  <Card title="Live Activities" icon="tower-broadcast" href="./live-activities">
    Dynamic iOS lock screen updates. Similar capabilities available for Android.
  </Card>

  <Card title="Mobile push prompts" icon="bell" href="./prompt-for-push-permissions">
    Configure opt-in prompts to collect push Subscriptions on mobile.
  </Card>

  <Card title="Web push prompts" icon="bell-on" href="./permission-requests">
    Configure opt-in prompts to collect push Subscriptions on web.
  </Card>
</Columns>

***

## SDK and API reference

Detailed documentation for client SDKs, server SDKs, and the REST API.

<Columns cols={2}>
  <Card title="Mobile SDK reference" icon="mobile" href="./mobile-sdk-reference">
    Methods, classes, and event hooks for iOS, Android, and cross-platform SDKs.
  </Card>

  <Card title="Web SDK reference" icon="globe" href="./web-sdk-reference">
    Initialization, User management, Subscription methods, and custom triggers.
  </Card>

  <Card title="Server SDK reference" icon="server" href="./server-sdk-reference">
    Install and configure server SDKs for Node.js, Python, Java, Go, PHP, Ruby, C#, and Rust.
  </Card>

  <Card title="REST API overview" icon="code" href="/reference/rest-api-overview">
    Endpoints, authentication, rate limits, and request/response formats.
  </Card>

  <Card title="Transactional messages" icon="paper-plane" href="./transactional-messages">
    Send OTPs, receipts, and time-sensitive alerts via API with personalized data.
  </Card>

  <Card title="Server SDKs on GitHub" icon="github" href="https://github.com/OneSignal/sdks#server-sdks">
    Source code and examples for all server SDK libraries.
  </Card>
</Columns>

***

## Users and identity

OneSignal assigns each person a **OneSignal ID** and tracks their devices, email addresses, and phone numbers as **Subscriptions**. Users are anonymous until you call `login` with an **External ID** to identify them. Identifying Users unifies their Subscriptions across channels and devices.

<Columns cols={2}>
  <Card title="Users" icon="users" href="./users">
    User model, External ID, anonymous vs. identified Users, and login/logout.
  </Card>

  <Card title="Subscriptions" icon="address-book" href="./subscriptions">
    Devices, email addresses, and phone numbers that receive your messages.
  </Card>

  <Card title="Identity verification" icon="shield-halved" href="./identity-verification">
    Require server-generated JWTs to prevent User impersonation.
  </Card>

  <Card title="Aliases" icon="fingerprint" href="./aliases">
    Map custom identifiers to Users for cross-platform tracking and integrations.
  </Card>

  <Card title="Tags" icon="tags" href="./add-user-data-tags">
    Set key-value data on Users for personalization and segmentation.
  </Card>

  <Card title="Custom events" icon="bolt" href="./custom-events">
    Track User actions to trigger Journeys or power analytics.
  </Card>
</Columns>

***

## Testing and debugging

Verify your integration works before sending to your full audience.

<Tip>
  Always test with [test Subscriptions](./find-set-test-subscriptions) first. This lets you verify delivery, rendering, and deep links without affecting real Users.
</Tip>

<Columns cols={2}>
  <Card title="Test Subscriptions" icon="vial" href="./find-set-test-subscriptions">
    Find and configure test Subscriptions for push, email, and SMS.
  </Card>

  <Card title="Debug logs" icon="bug" href="./capturing-a-debug-log">
    Capture verbose SDK logs from mobile apps for troubleshooting.
  </Card>

  <Card title="Mobile troubleshooting" icon="mobile" href="./mobile-troubleshooting">
    Resolve common push delivery, APNS, and in-app messaging issues.
  </Card>

  <Card title="Web troubleshooting" icon="globe" href="./troubleshooting-web-push">
    Fix service worker, browser compatibility, and web push issues.
  </Card>
</Columns>

***

## Webhooks and events

Receive message events server-side for analytics, automation, or syncing with external systems.

<Columns cols={2}>
  <Card title="Event Streams" icon="signal-stream" href="./event-streams">
    Stream clicks, opens, receives, and other message events to your data warehouse in real time.
  </Card>

  <Card title="Journey webhooks" icon="route" href="./journeys-webhook">
    Send HTTP requests to your server from Journey steps.
  </Card>

  <Card title="Web push webhooks" icon="link" href="./webhooks">
    HTTP callbacks for web push display, click, and dismiss events.
  </Card>
</Columns>

***

## FAQ

### How do I authenticate REST API requests?

Include your REST API key in the `Authorization` header as a bearer token: `Authorization: Key YOUR_REST_API_KEY`. Find your key in **Settings > Keys and IDs** in the OneSignal dashboard. See [Keys and IDs](./keys-and-ids) for details.

### What is the difference between client SDKs and server SDKs?

**Client SDKs** (mobile and web) run in your app on the User's device. They handle Subscription registration, permission prompts, in-app messages, and User identification via `login`. **Server SDKs** run on your backend and call the REST API to send messages, manage Users, and export data.

### How do I identify Users across devices?

Call `OneSignal.login("your_external_id")` on each device after the User signs in. OneSignal merges all Subscriptions with the same External ID under a single User. See [Users](./users#external-id) for implementation details.

### Do I need to set up identity verification?

Identity verification is optional but strongly recommended for production apps. Without it, any client can call `login` with an arbitrary External ID. Enabling [identity verification](./identity-verification) requires updating the OneSignal SDK to use a server-generated JWT, preventing impersonation.

***

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

Built with [Mintlify](https://mintlify.com).
