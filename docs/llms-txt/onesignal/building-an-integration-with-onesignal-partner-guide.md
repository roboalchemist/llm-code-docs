# Source: https://documentation.onesignal.com/docs/en/building-an-integration-with-onesignal-partner-guide.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building an Integration with OneSignal: Partner Guide

> Everything you need to know about building your own OneSignal integration

Integrating your platform with OneSignal unlocks powerful opportunities for mutual customers, driving enhanced user engagement and value. This guide outlines the benefits, integration options, and steps to successfully join our partner ecosystem.

## Benefits of Integrating with OneSignal

As a OneSignal partner, you'll gain valuable benefits aligned with your integration success and engagement:

* **Visibility and Recognition:** Showcase your integration through a verified listing in the OneSignal Partner Directory, with opportunities for increased exposure and "featured" listings as your partnership grows.
* **Enhanced Collaboration:** Participate in joint co-marketing activities, co-selling initiatives, and access comprehensive training to maximize integration adoption.
* **Strategic Support:** Gain direct access to our dedicated support and technical teams, with additional levels of support unlocked based on partnership milestones.
* **Growth Opportunities:** Access progressively advanced partner benefits such as dedicated documentation pages, enterprise sandbox accounts, and prioritized marketing opportunities as you expand your customer base and reach specific partnership milestones.

***

## Getting Started

To start developing your integration, simply create a free account at onesignal.com. If you'd like to join our partner program or require access to premium features for integration development and testing, please reach out through [partners.onesignal.com](https://partners.onesignal.com) or contact us via email at `bd@onesignal.com`.

### Requirement: `OneSignal-Usage` Header

To join the partner program, you must include the `OneSignal-Usage` header in all API requests. This header allows OneSignal to identify your integration, provide better support, and track adoption across mutual customers.

**Format:**

```
OneSignal-Usage: <YourCompany> | Partner Integration
```

Replace `<YourCompany>` with your company or platform name. For example, if your company is Acme, use `Acme | Partner Integration`.

<Note>
  **Common mistake:** Using only your company name (e.g., `Acme`) without the ` | Partner Integration` suffix. The full format with the suffix and exact spacing is required.
</Note>

### Verify Your Integration

Once your integration is ready, complete the [Partner Validation Request form](https://form.asana.com/?k=SHmysllCA1c9RVCtynG8Zg\&d=780103692902078) to open a request ticket with our Partnerships team.

Verification formally recognizes your integration on OneSignal's side, enabling full access to all the advantages of our Integration Partner Program.

We’re excited to collaborate and help your integration succeed!

***

## Common Integration Use Cases

Here are primary ways to integrate with OneSignal, each offering unique opportunities to enhance customer experience and drive mutual growth:

### 1. Trigger Notifications (Push, Email, SMS)

Allow customers to seamlessly manage notifications directly from your platform, enhancing customer engagement across multiple channels.

[Push, Email, SMS Integration Documentation](/reference/create-message)

### 2. Email Template Management

Facilitate streamlined email marketing by syncing and managing email templates within OneSignal.

[Email Template API Documentation](/reference/create-template)

### 3. User Creation and Management

Automate user onboarding by directly creating and managing users and devices in OneSignal, simplifying user management. It is important to understand how a User is defined within OneSignal, and the one-to-many relationship a User has with devices (defined as “subscriptions”). [See our Guide to Understanding Users in OneSignal](./users).

[Create User Documentation](/reference/create-user)

[Create Alias Documentation](/reference/create-alias)

### 4. Sync User Atrributes

Enable targeted messaging by syncing valuable user data (location, preferences, behavior) directly with OneSignal.

[Update User Attributes Documentation](/reference/update-user)

### 5. Capture Event Streams

Capture valuable real-time user engagement data (notifications, interactions, email opens) for enhanced analytics and actionable insights.

[Event Stream Documentation](./event-streams)

### 6. Send Custom Events

Custom Events let you send important user actions to OneSignal to be used for real time Journeys triggers, delays, segmentation, and personalization.

[Custom Events Documentation](./custom-events)

### 7. Platform Embedding

Offer seamless integration to your customers by embedding OneSignal directly within your platform, simplifying customer onboarding with unique App IDs.

[Platform Embedding Documentation](./developers)

***

Built with [Mintlify](https://mintlify.com).
