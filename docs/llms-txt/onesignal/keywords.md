# Source: https://documentation.onesignal.com/docs/en/keywords.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS keywords

> Learn how to use SMS Keywords in OneSignal to drive two-way engagement, personalize subscriber experiences, and increase conversions through automatic message replies and tagging.

<Frame caption="Keyword Usage Example">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/02584c1443f3b08f3d0543fc6ef2fd65a9cfc2e73036c8441d3b45c70dcbb2c1-Keywords_Documentation.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=95fef53b96860862908da52b51850190" width="2568" height="1483" data-path="images/docs/02584c1443f3b08f3d0543fc6ef2fd65a9cfc2e73036c8441d3b45c70dcbb2c1-Keywords_Documentation.png" />
</Frame>

## Overview

SMS Keywords enable two-way engagement by allowing subscribers to text specific words or phrases and receive automated responses. They support personalization, accessibility, and higher conversion rates by driving meaningful interactions and letting you tag, segment, and follow up with engaged users.

***

## Setup

Manage and create SMS Keywords by navigating to **Settings > Platforms > SMS Settings > Keywords**.

1. Click “Add a keyword.”
2. Enter the keyword you want subscribers to text in.
3. Choose the audience behavior:
   * **Anyone**: Sends the same reply to all users, regardless of subscription status.
   * **Segment by subscription status**: Send different replies to subscribed and unsubscribed users.
4. Select a reply template: This will be the auto-reply message users receive when they text the keyword.
5. Tag the user: Assign a tag when a user sends the keyword (e.g., preference = acorn), enabling future segmentation.

<Frame caption="How to add a keyword">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0bd33c69e076ea7818f7bb4b5aec45ca7587f7c546cc44f698e3038ecd3801aa-Screenshot_2025-02-03_at_8.47.02_AM.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=6c61e363ed832952b533357ca3979910" width="3446" height="1736" data-path="images/docs/0bd33c69e076ea7818f7bb4b5aec45ca7587f7c546cc44f698e3038ecd3801aa-Screenshot_2025-02-03_at_8.47.02_AM.png" />
</Frame>

<Warning>
  To ensure Keywords work properly, each **SMS Sender** must be configured to sync incoming message replies.
  Go to **SMS Settings > Senders** and click **Setup Replies**.
  ❗ Note: Alpha-numeric senders cannot receive replies and do not support keyword functionality.
</Warning>

***

## Measuring keyword engagement

To track how many times a keyword is triggered:

* Visit your **Templates** section.
* Check the analytics for the template tied to your keyword reply.

For example, if the acorn template shows 300 sends, the acorn keyword was triggered 300 times.

<Frame caption="See templates for keyword engagement">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e2999343da97b3412f257ab267f347fa7297c1cf565faf14a68a1a761f356033-Templates.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=fc284ece6d8fac4622d2c2f826f85249" width="1722" height="861" data-path="images/docs/e2999343da97b3412f257ab267f347fa7297c1cf565faf14a68a1a761f356033-Templates.png" />
</Frame>

***

## Build a segment based on keyword engagement

Create targeted campaigns based on users who responded with specific keywords.

1. Go to Segments
2. Use the User Tag filter
3. Enter the tag you assigned when setting up the keyword (e.g., preference = acorn)
4. Save and use this segment in your campaigns and journeys

This helps you send relevant messages to highly engaged users.

***

## Set an auto-responder for unrecognized keywords

If a subscriber sends a keyword that hasn’t been defined, you can automatically send a fallback reply. Use this to:

* Redirect users to customer support
* Collect their intent
* Notify your team for follow-up

<Frame caption="Settings for adding an auto-responder">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a50f5f85d152807827a109cc362f413e7409e1b799e910fed7d7012f9b1840ed-Screenshot_2025-02-03_at_8.53.32_AM.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=3bfe1c97ece7c221e90504e6097c266c" width="3438" height="1730" data-path="images/docs/a50f5f85d152807827a109cc362f413e7409e1b799e910fed7d7012f9b1840ed-Screenshot_2025-02-03_at_8.53.32_AM.png" />
</Frame>

To configure an auto-responder:

1. Go to Settings > SMS > Auto-Responder
2. Click Add Auto-Responder
3. Select a reply template
4. (Optional) Tag the user upon reply to enable future segmentation or alerting

***

## Keywords vs. consent management keywords

Regular Keywords are for engagement and segmentation.
Consent Management Keywords (e.g., `START`, `STOP`, `HELP`) are reserved for subscription management and compliance purposes.

Learn more about [Consent Management Keywords](./sms-consent-keyword-management).

***

Built with [Mintlify](https://mintlify.com).
