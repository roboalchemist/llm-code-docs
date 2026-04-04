# Source: https://documentation.onesignal.com/docs/en/quickstart-guide.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart guide

> Set up your OneSignal account, configure messaging channels, manage Users, and send your first message.

This guide walks through four stages to get you up and running with OneSignal. Complete them in order or jump to the section you need. If you haven't already, [create your account](https://onesignal.com) to get started.

1. [**Set up your account and messaging channels**](#set-up-your-account-and-messaging-channels) — create your app and configure at least one channel
2. [**Add and organize your Users**](#add-and-organize-your-users) — understand Users, Subscriptions, tags, and segments
3. [**Send messages**](#send-messages) — compose campaigns, personalize content, and build automated Journeys
4. [**Measure impact with analytics**](#measure-impact-with-analytics) — track delivery, engagement, and conversions

Watch a walkthrough of the platform, or skip ahead to the steps below.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/bH60T1PZg1c?si=0qtigm-eVcpl1bcl" title="OneSignal quickstart video walkthrough" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

***

## Set up your account and messaging channels

Your OneSignal App is where User and message data is stored. You can have multiple Apps in a single Organization for different projects, environments, or billing needs.

### OneSignal account

<Columns cols={2}>
  <Card title="Apps, Organizations, and accounts" icon="building" href="./apps-organizations">
    Your OneSignal App, Organization structure, and account settings.
  </Card>

  <Card title="Add team members" icon="user-plus" href="./manage-team-members">
    Invite collaborators and assign roles within your Organization.
  </Card>

  <Card title="Keys and IDs" icon="key" href="./keys-and-ids">
    Find your OneSignal App ID, Organization ID, and API keys.
  </Card>

  <Card title="Usage and billing" icon="credit-card" href="./billing-faq">
    Billing, invoices, and usage details.
  </Card>
</Columns>

### Messaging channels

OneSignal supports push notifications, in-app messages, email, SMS/MMS/RCS, and Live Activities. Choose your first channel and follow its setup guide — you can add more channels to the same app at any time.

<Tip>
  Email and SMS can be configured without writing code. Push notifications and in-app messages require SDK integration — [invite a developer](./manage-team-members) to your team if needed.
</Tip>

<Frame caption="Select a messaging channel in your OneSignal dashboard to begin setup.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/set-up-messaging-channels.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=bf38c40f30d3cc8e6c8ddc12224642ee" alt="OneSignal dashboard showing messaging channel setup options including push, email, SMS, and in-app" width="1690" height="868" data-path="images/dashboard/set-up-messaging-channels.png" />
</Frame>

<Columns cols={3}>
  <Card title="Email" icon="envelope" href="./email-setup">
    Transactional and marketing email configuration.
  </Card>

  <Card title="Mobile push" icon="mobile" href="./mobile-sdk-setup">
    iOS, Android, Huawei, and Amazon push setup.
  </Card>

  <Card title="Web push" icon="globe" href="./web-sdk-setup">
    Browser-based push notification setup.
  </Card>

  <Card title="In-app messages" icon="window-maximize" href="./in-app-messages-setup">
    Rich, interactive messages displayed within your app.
  </Card>

  <Card title="SMS" icon="comment-sms" href="./sms-messaging">
    Text messaging for time-sensitive alerts.
  </Card>

  <Card title="RCS" icon="message" href="./rcs-messaging">
    Rich messaging with branded content and read receipts on Android.
  </Card>

  <Card title="Live Activities" icon="tower-broadcast" href="./live-activities">
    Dynamic iOS lock screen updates. Similar capabilities available for Android.
  </Card>
</Columns>

<Note>
  After setting up push, configure [mobile push permission prompts](./prompt-for-push-permissions) or [web permission prompts](./permission-requests) to start collecting opt-ins from your Users.
</Note>

***

## Add and organize your Users

As users interact with your app, OneSignal assigns each a **OneSignal ID** (user ID) and **Subscription IDs** for each device, email address, or phone number. A single User can have multiple Subscriptions across channels. Users remain anonymous until you identify them with an [External ID](./users#external-id).

<Frame caption="OneSignal dashboard: Audience > Users">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/users-page.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=8992ef97cf3c9f336078f9dbf8a6374e" alt="OneSignal dashboard Users page showing a list of users with subscription details" width="2316" height="858" data-path="images/dashboard/users-page.png" />
</Frame>

<Columns cols={2}>
  <Card title="Users" icon="users" href="./users">
    Identified by External ID; can have multiple Subscriptions across channels.
  </Card>

  <Card title="Subscriptions" icon="address-book" href="./subscriptions">
    Email addresses, phone numbers, and devices that receive your messages.
  </Card>
</Columns>

### User properties

Store User data as **tags** (key-value pairs) and **custom events** (user actions). Tags power message personalization and segmentation.

Common tag examples:

* **Attributes**: `first_name`, `city`, `subscription_tier`
* **Behaviors**: `cart_abandoned`, `last_login_date`, `onboarding_complete`
* **Preferences**: `notification_frequency`, `theme_preference`

<Columns cols={2}>
  <Card title="Tags" icon="tags" href="./add-user-data-tags">
    Use tags for message personalization and advanced segmentation.
  </Card>

  <Card title="Custom events" icon="bolt" href="./custom-events">
    Trigger Journeys or wait-until actions based on User behavior.
  </Card>
</Columns>

### Segments and integrations

Segments are dynamic groups of Users defined by tags, behavior data, or message interactions. They update automatically as User data changes — for example, "Last session greater than a week" or "Added item to cart." Connect external platforms to enrich your segments with additional User data.

<Frame caption="Creating a segment with a User Tag filter.">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e1801ce-4667771-Segment_Picker_3_1.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=e27107ac0e1975e8cb63b3cbb02822ee" alt="OneSignal segment builder showing a User Tag filter configuration" width="883" height="471" data-path="images/docs/e1801ce-4667771-Segment_Picker_3_1.png" />
</Frame>

<Columns cols={2}>
  <Card title="Segments" icon="chart-pie" href="./segmentation">
    Create dynamic audience groups using tags and behavior data.
  </Card>

  <Card title="Integrations" icon="plug" href="./integrations">
    Import User data from external platforms to power segments and Journeys.
  </Card>
</Columns>

***

## Send messages

Design and send single-message campaigns or automated multi-step Journeys from the OneSignal dashboard. Each channel has its own composer with preview, targeting, and scheduling options.

<Tip>
  Before sending to your full audience, [set up test Subscriptions](./find-set-test-subscriptions) to verify your messages render and deliver correctly.
</Tip>

<Frame caption="Push notification composer in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/007d277-f8b3231-message_1.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=d8d2e386bfa2ff742bfc6d3e6583f4d2" alt="OneSignal push notification editor showing message content fields and preview" width="790" height="627" data-path="images/docs/007d277-f8b3231-message_1.png" />
</Frame>

<Columns cols={2}>
  <Card title="Push notifications" icon="bell" href="./push">
    Send to web, iOS, Android, Huawei, and Amazon devices.
  </Card>

  <Card title="Email" icon="envelope" href="./email-messaging">
    Compose and send transactional or marketing emails.
  </Card>

  <Card title="In-app messages" icon="window-maximize" href="./in-app-messages-setup">
    Trigger rich, interactive messages based on User behavior within your app.
  </Card>

  <Card title="SMS" icon="comment-sms" href="./sms-messaging">
    Send text messages for time-sensitive alerts and updates.
  </Card>

  <Card title="RCS" icon="message" href="./rcs-messaging">
    Send rich, branded messages with read receipts on Android.
  </Card>

  <Card title="Live Activities" icon="tower-broadcast" href="./live-activities">
    Deliver dynamic lock screen updates on iOS.
  </Card>
</Columns>

### Personalize your messages

Use tags, custom events, and dynamic data to tailor message content for each recipient. Create reusable templates to maintain consistency across campaigns.

<Columns cols={2}>
  <Card title="Message personalization" icon="wand-magic-sparkles" href="./message-personalization">
    Personalize content with Liquid syntax, tags, Data Feeds, and custom data.
  </Card>

  <Card title="Templates" icon="clone" href="./templates">
    Create reusable message templates for push, email, and SMS.
  </Card>
</Columns>

### Journeys

Journeys are automated, multi-step campaigns that respond to User behavior — such as onboarding sequences, abandoned cart reminders, and re-engagement flows.

<Frame caption="Example abandoned cart Journey in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/be3ec1a-e61fae7-settings_Journeys_1.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=6f266cd498ccc2884a0fde9d35d2fd49" alt="OneSignal Journey builder showing an abandoned cart automation flow" width="1105" height="745" data-path="images/docs/be3ec1a-e61fae7-settings_Journeys_1.png" />
</Frame>

<Columns cols={2}>
  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated, multi-step campaigns triggered by User behavior.
  </Card>

  <Card title="Journey examples" icon="book-open" href="./journeys-examples">
    Common patterns like onboarding, abandoned carts, and re-engagement.
  </Card>
</Columns>

### Send via API

Send messages programmatically for transactional use cases like order confirmations, OTPs, and billing alerts.

<Columns cols={2}>
  <Card title="Developer guides" icon="code" href="./developers">
    SDK and REST API documentation for engineering teams.
  </Card>

  <Card title="Transactional messages" icon="paper-plane" href="./transactional-messages">
    Send time-sensitive messages like OTPs, receipts, and shipping updates via API.
  </Card>
</Columns>

***

## Measure impact with analytics

Track message performance — including delivery, opens, clicks, and conversions — to understand what drives engagement and refine your strategy.

<Columns cols={2}>
  <Card title="Analytics overview" icon="chart-line" href="./analytics-overview">
    Review all analytics options available in OneSignal.
  </Card>

  <Card title="Event streams" icon="signal-stream" href="./event-streams">
    Stream message events like clicks, opens, and receives to your data warehouse in real time.
  </Card>

  <Card title="Export data" icon="file-export" href="./exporting-data">
    Export User and message data in CSV or API format.
  </Card>

  <Card title="Integrations" icon="plug" href="./integrations">
    Connect analytics platforms like Amplitude, Mixpanel, Segment, and more to OneSignal.
  </Card>

  <Card title="Conversion metrics" icon="arrow-trend-up" href="./conversion-metrics">
    Measure business impact like revenue and sign-ups with cross-channel last-touch attribution.
  </Card>

  <Card title="Goals" icon="bullseye" href="./goals">
    Set a target metric on a message or Journey and track progress on the delivery report.
  </Card>
</Columns>

***

## FAQ

### Do I need a developer to get started?

Not necessarily. Email and SMS channels can be configured without code. Push notifications and in-app messages require SDK integration, which may need a developer or AI assistant. You can [invite team members](./manage-team-members) with different roles at any time.

### Can I add more messaging channels later?

Yes. Add any combination of channels to the same OneSignal App. Each channel has its own setup guide — return to the [messaging channels](#messaging-channels) section to add a new one.

### What is the difference between a User and a Subscription?

A **User** represents one person, identified by an [External ID](./users#external-id). A **Subscription** is a specific channel endpoint — such as a device, email address, or phone number. One User can have multiple Subscriptions across different channels and devices.

### How long does initial setup take?

Email setup typically takes under 30 minutes if you have access to your domain DNS settings. SMS requires carrier registration, which can take a few days. Push notification setup depends on your app's platform and build process — plan for a few hours of developer time.

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
