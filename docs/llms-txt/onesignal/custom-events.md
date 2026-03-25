# Source: https://documentation.onesignal.com/docs/en/custom-events.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom events

> Track user behavior with Custom Events and use them to trigger Journeys, control flow with Wait Until steps, and personalize messages in real time.

## What are Custom Events?

A Custom Event is a named user action (or inaction) that you send to OneSignal. You send events from your app, website, or external systems so you can trigger automation, control Journey flow, and personalize user experiences in real time.

**Examples include:**

* Completed onboarding
* Made a purchase
* Abandoned a cart
* Canceled a subscription
* Reached a new game level

**When OneSignal receives a Custom Event, you can:**

* Start a Journey
* Continue a Journey with a Wait Until step
* Exit users from a Journey
* Personalize messages using event properties
* Segment users by behavior (Early Access)

### When should you use Custom Events?

Use Custom Events when:

* Messaging should respond to real-time user behavior
* The data represents something that happened (not permanent state)
* You need event properties for personalization or Journey logic

Do not use Custom Events when:

* You want to store long-term user attributes (use Tags instead)

<Warning>
  Custom Events represent something that happened at a specific point in time. Unlike Tags, they do not permanently update the user's profile — they record behavior.

  See [Tags vs Custom Events](#tags-vs-custom-events) below for a detailed comparison.
</Warning>

### Custom Event structure

Custom Events include the following fields:

<ParamField body="name" type="string" required>
  The event name. Maximum `128` characters.
</ParamField>

<ParamField body="properties" type="object">
  Optional parameters that describe the event (for example: plan name, product ID, or price). These can be used for personalization and Journey flow control.
</ParamField>

<ParamField body="external_id" type="string">
  The user's External ID. A user identifier is required when using the [Create Custom Events API](/reference/create-custom-events). Either `external_id` or `onesignal_id` must be provided.
</ParamField>

<ParamField body="timestamp" type="string">
  The time the event occurred (or will occur), formatted as an ISO 8601 string. See [Create Custom Events API](/reference/create-custom-events).
</ParamField>

<ParamField body="idempotency_key" type="string">
  A unique UUID used to prevent duplicate event processing. See [Create Custom Events API](/reference/create-custom-events).
</ParamField>

<Warning>
  Event size limits:

* Maximum event payload: 2024 bytes
* Maximum request size (multiple events): 1 MB
</Warning>

***

## Send Custom Events to OneSignal

<Info>
  All events are treated the same for billing purposes, regardless of source.
</Info>

### API and SDKs

<Columns cols={2}>
  <Card title="Create Custom Events API" icon="server" href="/reference/create-custom-events">
    Send events from your backend.
  </Card>

  <Card title="Mobile/Web SDKs" icon="mobile" href="./mobile-sdk-reference#custom-events">
    Track events client-side.
  </Card>
</Columns>

Example Custom Event payload:

```json JSON theme={null}
{
  "events": [
    {
      "name": "purchase",
      "properties": {
        "item": "T-shirt",
        "size": "small",
        "color": "blue",
        "price": 24.99
      },
      "external_id": "user_12345",
      "timestamp": "2025-10-21T19:09:32.263Z",
      "idempotency_key": "123e4567-e89b-12d3-a456-426614174000"
    }
  ]
}
```

### Integrations

OneSignal connects to 25+ external data sources to import custom events — including data warehouses, databases, and streaming platforms — with no custom code required.

<Columns cols={3}>
  <Card title="Twilio Segment" icon="share-nodes" href="./segment-onesignal-integration">
    Route events and audiences between Segment and OneSignal.
  </Card>

  <Card title="Amplitude" icon="chart-line" href="./amplitude">
    Sync cohorts and import custom events from Amplitude.
  </Card>

  <Card title="Mixpanel" icon="chart-mixed" href="./mixpanel">
    Sync cohorts and import custom events from Mixpanel.
  </Card>

  <Card title="Snowflake" icon="snowflake" href="./snowflake">
    Import custom events from your Snowflake warehouse.
  </Card>

  <Card title="Google BigQuery" icon="database" href="./bigquery">
    Import custom events from BigQuery datasets.
  </Card>

  <Card title="Apache Kafka" icon="bolt" href="./kafka">
    Stream custom events from Kafka topics.
  </Card>
</Columns>

<Card title="Browse all custom event sources" icon="grid-2" href="./integrations#custom-event-sources">
  See the full list of databases, warehouses, and streaming platforms that import custom events into OneSignal.
</Card>

<Tip>
  **No developer resources?** Import custom events directly from a [Google Sheets](./google-sheets) spreadsheet — no code required. Add your event data to a sheet and OneSignal imports it automatically. Ideal for early experimentation or teams without engineering support.
</Tip>

### Verify events are received

After sending events, confirm they are reaching OneSignal in **Data > Custom Events**.

#### Event List tab

<Frame caption="Event List tab in OneSignal dashboard Data > Custom Events">
  <img src="https://mintcdn.com/onesignal/MWGmj5X1CnFliD-c/images/dashboard/event-list.png?fit=max&auto=format&n=MWGmj5X1CnFliD-c&q=85&s=2b9cae667bed4b54974326ffa0830907" width="3302" height="1888" data-path="images/dashboard/event-list.png" />
</Frame>

The Event List tab provides an overview of all Custom Events in your app, organized by event name.

For each event type, you can see:

* Total events ingested
* Most recent event (with full JSON payload and properties)
* Event source (SDK, API, or integration)
* Last occurrence timestamp

Select an event to open its detail view, where you can also update its retention period.

The detail view includes:

* **Source Breakdown**: Number of events ingested by source. Expand to view the latest event schema and the timestamp of the most recent event.
* **Activities**: The 10 most recent events, including source and timestamp. Expand any entry to inspect the full JSON payload.
* **Usage**: Where the event is currently used (Journeys or segments). Click directly into the associated Journey or segment to modify its settings.

#### Event Activity tab

<Frame caption="Event List tab in OneSignal dashboard Data > Custom Events">
  <img src="https://mintcdn.com/onesignal/MWGmj5X1CnFliD-c/images/dashboard/event-activity.png?fit=max&auto=format&n=MWGmj5X1CnFliD-c&q=85&s=8e355c907b598f1ac5a446e3536b9eea" width="3302" height="1888" data-path="images/dashboard/event-activity.png" />
</Frame>

The Event Activity tab provides a live feed of the most recent events ingested into your OneSignal app.

Use it to:

* Filter by event name, source, or external ID
* Inspect full JSON payloads
* Debug integration issues

<Warning> The feed does not auto-refresh. Refresh manually after sending new events. </Warning>

***

## Use Custom Events in OneSignal

After events are flowing into OneSignal, you can use them in the following ways:

### Trigger Journey entry and exit rules

Set a Custom Event as a Journey entry or exit rule to immediately add or remove users when the event occurs.

Example:

* `signup_completed` → Start onboarding or remove from a trial-encouragement Journey
* `purchase` → Send confirmation and cross-sell or remove from abandoned cart Journey

<Card title="Journey settings" icon="gear" href="./journeys-settings#entry-rules">
  Enter users into Journeys with Custom Events.
</Card>

### Control Journey flow (Wait Until)

Use a Wait Until step to hold users until a Custom Event occurs.

Example:

* Wait until `purchase` after `added_to_cart`

<Info> You can define an expiration window. If the user does not trigger the event in time, you can send a fallback message or exit the Journey. </Info>

<Card title="Journey Wait Until step" icon="stopwatch" href="./journeys-actions#wait-until">
  Hold users until a Custom Event occurs.
</Card>

### Personalize Journeys with event properties

Reference event properties using Liquid in your Journey templates.

Example:

```liquid Liquid theme={null}
Thanks for purchasing {{ journey.first_event.properties.item }}!
```

<Card title="Custom Event personalization" icon="bolt" href="./personalization-custom-event">
  Complete guide to using event properties to personalize Journeys.
</Card>

### Segment users with Custom Events

Create a segment based on the occurrence of a Custom Event.

<Note>
  Custom Event segmentation is in Early Access.

  To request access, email `support@onesignal.com` with:

* Your company name
* Your OneSignal App ID(s)
</Note>

<Warning>
  Current limitations:

* Not supported with Email Warm Up or A/B tests
* Cannot power Journeys
* Cannot be combined with other segment filters
</Warning>

<Card title="Segmentation" icon="filter" href="./segmentation">
  Complete guide to segmentation.
</Card>

***

## Plan availability and retention costs

Custom Events are available on all paid plans.

<Card title="Billing FAQ" icon="receipt" href="./billing-faq#event-related-billing">
  Learn about event retention and pricing.
</Card>

***

## Tags vs Custom Events

[Tags](/docs/en/add-user-data-tags) and [Custom Events](/docs/en/custom-events) are both ways to add data to your users. However, there are some key differences:

| Feature        |                      Tags                     |                                          Custom Events                                         |
| -------------- | :-------------------------------------------: | :--------------------------------------------------------------------------------------------: |
| Data usage     |        Segmentation and personalization       | Trigger Journeys without a Segment, Wait Until steps, personalization directly within Journeys |
| Data retention |                    Lifetime                   |        30+ days ([lifetime storage is available](/docs/en/billing-faq#streaming-events))       |
| Data format    |          Key-value strings or numbers         |                                              JSON                                              |
| Data source    | OneSignal SDK, API, or integrations (limited) |                               OneSignal SDK, API, or integrations                              |
| Data access    |    Segmentation and message personalization   |        Journeys and Journey-message-template personalization, Segmentation (Coming soon)       |

The key distinction between Tags and Custom Events is in their depth and use cases. Tags are properties of a user, such as Name, Account Status, or Location. Events are thing that the user has done, such as Purchasing an Item, Completing a Level, or Inviting a Friend. Both tags and events can be used for segmentation and personalization.

In practice, you will likely use both:

* Tags for user properties that are static and don't change often
* Custom Events for real-time scenarios, complex segmentation, and more sophisticated journey workflows

***

Built with [Mintlify](https://mintlify.com).
