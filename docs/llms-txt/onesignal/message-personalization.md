# Source: https://documentation.onesignal.com/docs/en/message-personalization.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Personalization

> Choose the right personalization method in OneSignal. Compare Properties, Custom Events, API custom_data, Data Feeds, and CSV uploads to send dynamic messages using Liquid syntax.

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/71gtwxKWlN8?si=mlgmP6eE3652r_cX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

Personalization lets you send messages that include dynamic data — such as a user's name, cart items, account balance, booking details, or a one-time password.

This guide helps you choose the right personalization method based on:

* Where your data lives
* Whether it should persist
* How the message is triggered

***

## How personalization works

Personalization in OneSignal has two parts:

1. **Liquid syntax** – defines how values render in your message
2. **A data source** – determines where the value comes from

At send time, OneSignal resolves your Liquid variables using the selected data source.

<Info>
  Liquid controls formatting and logic (variables, loops, conditionals). The data source determines what values are available.
</Info>

**Example:**

```liquid Liquid theme={null}
Hi {{ user.tags.first_name }},

Your verification code is {{ message.custom_data.otp }}.
```

* `user.tags.first_name` is a stored property
* `message.custom_data.otp` is passed via the API `custom_data` field

***

## Data source comparison

If you need to…

* Reuse stored user data → [Properties](#properties)
* Personalize inside a Journey based on behavior → [Custom Events](#custom-events)
* Send one-time or sensitive values → [API `custom_data`](#api-custom_data)
* Fetch live backend data at delivery → [Data Feeds](#data-feeds)
* Upload bulk personalization via dashboard → [Dynamic Content CSV](#dynamic-content-csv)

<Warning>
  **Common mistakes to avoid**

* Using Properties (Tags) for one-time values like OTPs or verification codes
* Expecting `custom_data` to be available in Journeys or future messages
* Assuming Custom Event properties are available outside of the event triggered Journey entry or a Wait Until step
* Using Data Feeds for static data that rarely changes
</Warning>

***

## Data sources

### Data feeds

[Data Feeds](./data-feeds) call your API at send time and inject the response into your message.

**When to use Data Feeds:**

* You need the latest value at delivery
* The data lives in your backend
* The value may change between sends

<Card title="Data feeds" icon="cloud-arrow-up" href="./data-feeds">
  Pull real-time backend data into messages at send time.
</Card>

***

### Custom Events

[Custom Events](./custom-events) can personalize messages inside [Journeys](./journeys-overview) using event properties.

When an event **starts a Journey** or **matches a Wait Until condition**, OneSignal stores that event so its properties can be referenced in message templates using Liquid.

**When to use Custom Events:**

* Event triggered messages with Journeys
* The message should reflect event-specific data

<Warning> Only events that trigger Journey entry or a Wait Until step are stored for personalization. Events sent outside those moments are not available to Journey messages. </Warning>

<Card title="Custom Event personalization" icon="bolt" href="./personalization-custom-event">
  Complete guide to using event properties to personalize Journeys.
</Card>

***

### Properties

Properties include user tags, External ID, subscription data, and app-level fields.

They are:

* Persistent
* Reusable
* Available across messages, templates, [Journey webhooks](./journeys-webhook), and [Event Streams](./event-streams).

**Use Properties when:**

* The value exists in OneSignal
* The value is persistent
* You reuse it across campaigns

<Card title="Personalize with Properties" icon="tag" href="./personalization-properties-and-tags">
  Learn how to reference stored persistent property data.
</Card>

***

### API `custom_data`

The `custom_data` field in the [Create Message API](/reference/create-message) lets you send message-specific values from your backend.

This data:

* Exists only for the current request
* Is not stored in OneSignal
* Is not available in Journeys

**Use `custom_data` when:**

* Sending one-time or sensitive values (OTP, secure links)
* Passing arrays (cart items, order lines, leaderboard scores)
* Sending transactional or API-triggered messages

<Card title="Personalize with API custom_data" icon="code" href="./personalization-api-custom-data">
  Learn how to pass transient personalization data.
</Card>

***

### Dynamic Content CSV

Upload a CSV file into the OneSignal dashboard and reference its values using Liquid.

**Use CSV when:**

* Customizing differnt sections of a bulk campaign for each recipient
* Translations or custom data for each recipient is exportable to a CSV file
* You do not want to use the API

<Card title="Dynamic Content CSV" icon="file-csv" href="./dynamic-content">
  Personalize dashboard campaigns using CSV uploads.
</Card>

***

## Detailed guides

Use the guides below for step-by-step implementation details and advanced examples.

<Columns cols={2}>
  <Card title="Using Liquid syntax" icon="droplet" href="./using-liquid-syntax">
    Learn how to insert dynamic data into messages using Liquid. Covers variables, conditionals, loops, filters, formatting, and common personalization patterns.
  </Card>

  <Card title="Data feeds" icon="cloud-arrow-up" href="./data-feeds">
    Pull real-time data from your own APIs at send time. Use Data Feeds when message content depends on live backend values like balances, availability, or pricing.
  </Card>

  <Card title="Custom Events personalization" icon="bolt" href="./personalization-custom-event">
    Personalize Journey messages using event properties captured when users enter or progress through a Journey. Ideal for behavioral and event-driven workflows.
  </Card>

  <Card title="Properties & Tags" icon="tag" href="./personalization-properties-and-tags">
    Use stored user, subscription, message, and app properties to personalize content across messages, templates, Journey webhooks, and Event Streams.
  </Card>

  <Card title="API custom_data" icon="code" href="./personalization-api-custom-data">
    Pass per-message and transient data from your backend using the Create Message API. Best for OTPs, carts, arrays, and bulk transactional personalization.
  </Card>

  <Card title="Dynamic Content CSV" icon="file-csv" href="./dynamic-content">
    Upload CSV files in the dashboard to personalize campaigns at scale. Each row maps to a recipient and can be referenced using Liquid.
  </Card>
</Columns>

### Tutorials

These guides show how to implement personalization in practice.

<Columns cols={2}>
  <Card title="Verification, Magic Link, & OTP" icon="key" href="./example-verification-magic-link-otp">
    Send secure verification messages using one-time passwords, magic links, or custom URLs with API-driven personalization.
  </Card>

  <Card title="Abandoned cart Journey" icon="cart-shopping" href="./abandoned-cart">
    Build an automated Journey that detects cart activity, waits for inactivity, sends a personalized reminder, and exits users immediately after purchase.
  </Card>

  <Card title="Booking confirmations" icon="calendar" href="./booking-confirmations">
    Send booking confirmation and recovery messages using Custom Events, Journeys, and Data Feeds based on real-time reservation status.
  </Card>

  <Card title="Transactional messages" icon="receipt" href="./transactional-messages">
    Learn how to send receipts, alerts, confirmations, and other transactional messages across channels using APIs and automation.
  </Card>

  <Card title="In-app personalization examples" icon="mobile" href="./example-tag-substitution">
    See practical examples of using tags and properties to personalize in-app messages for different users and segments.
  </Card>
</Columns>

***

Built with [Mintlify](https://mintlify.com).
