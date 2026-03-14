# Source: https://documentation.onesignal.com/docs/en/database-dmp-crm-integration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data warehouse, DMP, & CRM integration

> Integrate your CRM, database, or DMP with OneSignal to trigger personalized, real-time notifications and sync user messaging data at scale.

Connecting OneSignal to your internal systems like a data warehouse, CRM, or data management platform (DMP) unlocks powerful capabilities for real-time, personalized, and scalable messaging. Whether you're using Salesforce, a custom user system, or another platform, integration enables you to:

* Send personalized, time-sensitive messages using live data
* Sync user attributes and message data between systems
* Use your internal system as the source of truth while leveraging OneSignal's messaging infrastructure

This guide walks through common use cases, integration methods, and setup best practices.

<Frame caption="Database integration">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3a0f52f88c855832e2f2185aa456925c300ed7c2d13446f52802cbda474c3570-Screenshot_2024-10-08_at_15.27.28.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=4887fb763f121365fbdf803e3b298d3b" width="747" height="537" data-path="images/docs/3a0f52f88c855832e2f2185aa456925c300ed7c2d13446f52802cbda474c3570-Screenshot_2024-10-08_at_15.27.28.png" />
</Frame>

***

## Benefits of database integration

**Personalized messaging at scale**

Use data from your internal systems to [personalize messages](./message-personalization) in real-time:

* Add [Tags](./add-user-data-tags) to store user attributes in OneSignal for segmentation or content personalization.
* Pass `custom_data` in the [Create message](/reference/create-message) API to personalize without storing data permanently.

**Trigger time-sensitive messages**

Send messages instantly when key events occur in your system, such as:

* Orders placed
* Subscription renewals or expirations
* Milestone achievements
* Trigger using:
  * [Create message](/reference/create-message) API with aliases or filters to reach the right users at the right time.
  * [Journeys](./journeys-overview) via [Custom Events](./custom-events)

**Unified user identity with External ID and aliases**

OneSignal supports `external_id` as a stable cross-platform user ID and up to 10 custom aliases per user (e.g., `crm_id`, `facebook_id`).

***

## Data flow

### User identity structure

Use `external_id` as your primary user identifier across systems. You can attach other aliases or identifiers for flexibility. If no global user ID exists, OneSignal/Subscription IDs can be used but require extra handling, as they are anonymous until linked.

See [Users](./users) and [Subscriptions](./subscriptions) for more information.

### Send user data to OneSignal

Use our REST API to create and update users in real time. We also support [CSV import](./import) for bulk onboarding or updates.

* [Create user](/reference/create-user)
* [Create Subscription by alias](/reference/create-subscription)
* [Update user](/reference/update-user) for tag-only updates

### Export data from OneSignal

To retrieve data from OneSignal:

* Use [Event Streams](./event-streams) for real-time delivery and engagement events
* Access static exports via:
  * [Export subscriptions CSV](/reference/csv-export)
  * [View messages API](/reference/view-messages)

### Send custom events to OneSignal

Send [Custom Events](./custom-events) to trigger [Journeys](./journeys-overview) by syncing data from your warehouse directly to OneSignal.

**Supported Integrations**

OneSignal integrates with many sources to sync custom events. See [Custom Events](./custom-events#supported-integrations) for a list of supported integrations.

**Getting started**

1. Navigate to **Data > Integrations** in your OneSignal dashboard.
2. Look for the **Sync data from your favorite data warehouse** banner.
3. Click **Sync Data** to access the configuration for data ingestion.

<Frame caption="Sync data from your data warehouse">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/integrations/sync-data.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=32d8eb13b13549ba3806a6e68a4a76f1" width="2464" height="858" data-path="images/integrations/sync-data.png" />
</Frame>

#### 1. Connect your data source

If you don’t see a data warehouse listed, or if you have questions about how to set up an integration - please let us know by emailing `integrations@onesignal.com`. We’re currently taking requests to expand our integration offerings.

#### 2. Create your sync

* Click **Add Sync**
* Select **Any Warehouse Table**
* Choose your connected data source
* Select your schema and table
  * For Google Sheets: Use the table dropdown to select specific sheets within your document.

#### 3. Configure your destination

* Select OneSignal as connection
* Choose **Custom Event** as object type
* Keep **Create Only** as sync behavior
* Map your identifier column to OneSignal External IDs

#### 4. Choose Your Data Fields

* Select which columns to sync to OneSignal:
  * Supported types: Text, numbers, booleans, dates, times
  * Usage: These fields become available for journey segmentation
  * Recommendation: Sync only the fields you'll use for targeting

#### 5. Test and Deploy

* Test your sync to verify data flows correctly
* Add a descriptive label (can't be changed later)
* Set your trigger: Manual, scheduled, or sequential. We recommend selecting sequential for ingesting custom events.

<Check>
  What Happens Next?

  Your custom events will appear in OneSignal's events index, ready to use in journeys based on user behavior and data from your warehouse.
  Each sync option has specific details needed to connect to your account - please reach out to us at [integrations@onesignal.com](mailto:integrations@onesignal.com) with any questions about individual settings.
</Check>

***

## Where should data live: OneSignal or your database?

Decide based on the data's purpose:

### What to store in OneSignal

<AccordionGroup>
  <Accordion title="Store data used directly for messaging">
    Store data used directly for messaging:

    * `external_id` and aliases
    * Emails (for email messaging)
    * Phone numbers (for SMS)
    * Lightweight user attributes as [Tags](./add-user-data-tags)

    For richer personalization, avoid storing full profiles—inject dynamic fields at send time using `custom_data`.
  </Accordion>

  <Accordion title="What to keep in your own systems">
    ### What to keep in your own systems

    Keep data unrelated to messaging (e.g., full user profiles, transaction logs) in your own systems for performance, privacy, and control. Archive message history from OneSignal for long-term analytics or compliance.
  </Accordion>
</AccordionGroup>

***

## Triggering messages from your database

You can trigger messages using two approaches—choose one or both based on your use case.

<Tabs>
  <Tab title="API">
    Use the [Create message](/reference/create-message) API for immediate, transactional messaging.

    Target users via:

    * `external_id`
    * Aliases (e.g., `crm_id`)
    * Email or phone number

    Best for:

    * [Transactional messages](./transactional-messages) (e.g., receipts, alerts)
    * Time-sensitive or personalized notifications
    * Targeting individuals or groups (up to 20,000 users per call)

    You can also schedule messages using the `send_after` parameter.
  </Tab>

  <Tab title="Tags and Journeys">
    Use [Tags](./add-user-data-tags) to build dynamic user segments.

    Send messages by:

    * Targeting segments or filters via the API
    * Manual sends through the dashboard
    * Automated messaging using [Journeys](./journeys-overview)

    Best for:

    * Marketing campaigns (promotions, re-engagement)
    * Scheduled or lifecycle messages
    * Empowering non-technical teams to run campaigns
  </Tab>

  <Tab title="Custom Events and Journeys">
    If you followed [Send custom events to OneSignal](#send-custom-events-to-onesignal), you can trigger [Journeys](./journeys-overview) by syncing data from your warehouse directly to OneSignal.

    See [Custom Events](./custom-events) for more information.
  </Tab>
</Tabs>

***

Built with [Mintlify](https://mintlify.com).
