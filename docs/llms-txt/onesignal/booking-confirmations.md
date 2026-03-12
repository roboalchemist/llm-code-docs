# Source: https://documentation.onesignal.com/docs/en/booking-confirmations.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Booking confirmations

> Use custom events, Journeys, and Data Feeds to send booking confirmation or recovery emails based on real-time booking status.

## Overview

In this tutorial, you will set up a common booking workflow:

* Send a booking confirmation email after a user completes a booking.
* Send a recovery email if a user starts a booking but does not complete it in time.

By the end, you will have:

* Two Custom Events (`booking_started`, `booking_complete`)
* One Journey that branches on completion vs abandonment
* A booking Data Feed for confirmation details
* An optional coupon Data Feed for recovery incentives

This guide focuses on configuring OneSignal. Your booking system and backend can be implemented in any language or framework.

### Setup flow

1. Your app tracks a `booking_started` [custom event](./custom-events).
2. This enters the user into a Journey.
3. The Journey waits for a `booking_complete` event and if not received in time, it sends follow-up reminders.
4. If the booking completes, OneSignal calls a booking Data Feed at send time and sends a confirmation email with the latest booking details.
5. If the booking does not complete within the wait window, the Journey follows the expiration path and sends a recovery email.

***

## Setup

### Prerequisites

Before you begin, make sure you have:

* A OneSignal app with the [**Email**](./email-setup) channel enabled
* A backend endpoint that can return booking and/or coupon data as JSON
* A stable user identifier shared between your app, backend, and OneSignal's [External ID](./users#external-id)
* Access to [Custom Events](./custom-events)

### 1. Track booking events

Track the following Custom Events. These can be from your app (using our SDK) or from your backend (using our REST API).

**Event names:**

* `booking_started` — when the user begins the booking flow
* `booking_complete` — when the booking is successfully completed

<Tabs>
  <Tab title="App - Mobile and Web">
    Use the `trackEvent()` method on our [Mobile SDK](./mobile-sdk-reference) and/or [Web SDK](./web-sdk-reference) to send custom events directly from your app/website.

    ```js Example theme={null}
    OneSignal.User.trackEvent("booking_started");
    OneSignal.User.trackEvent("booking_complete");
    ```
  </Tab>

  <Tab title="Server Side">
    If you are tracking events from your backend, use the [Create Custom Events API](/reference/create-custom-events) to send events to OneSignal.

    ```bash  theme={null}
    curl --request POST \
      --url https://api.onesignal.com/apps/{app_id}/custom_events \
      --header 'Authorization: Key YOUR_APP_API_KEY' \
      --header 'Content-Type: application/json' \
      --data '{
        "events": [
          {
            "name": "booking_started",
            "external_id": "user123",
            "properties": {}
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

<Note>
  Use the same user identity when tracking events and when returning data from
  your backend. Mismatched IDs are the most common cause of missing
  personalization.
</Note>

### 2. Create Data Feed aliases

In OneSignal, go to **Settings > Data Feeds** and create the following aliases.

**Booking Data Feed:**
Use this feed to pull the latest booking details at send time.

* **Alias:** `booking_data`
* **Method:** GET
* **URL:**

```liquid Example endpoint theme={null}
https://your-domain.com/datafeed/booking?user_id={{subscription.external_id}}
```

Example response:

```json JSON theme={null}
{
  "first_name": "Sam",
  "last_booking": {
    "service_type": "Consultation",
    "booking_date": "January 22, 2026",
    "booking_time": "2:00 PM",
    "price": 45
  }
}
```

**Coupon Data Feed (optional):**

Use this optional feed if you want to include a coupon code in your recovery email.

* **Alias:** `coupon`
* **Method:** GET
* **URL:**

```liquid Example endpoint theme={null}
https://your-domain.com/datafeed/coupon?user_id={{subscription.external_id}}
```

Example response:

```json JSON theme={null}
{
  "first_name": "Sam",
  "code": "PROMO8F3K2",
  "discount_text": "10%",
  "expires_in_hours": 2,
  "deep_link": "https://your-domain.com/checkout?coupon=PROMO8F3K2"
}
```

<Warning>
  Secure your Data Feed endpoints. In production, send an API key in request headers (for example `x-api-key`) and configure that header in **Settings > Data Feeds** instead of embedding secrets in the URL.
</Warning>

### 3. Create email templates

#### Booking confirmation email

**Subject:**

```text  theme={null}
Your booking details
```

**Body:**

```liquid  theme={null}
Hi {{ data_feed.booking_data.first_name | default: "there" }},

Thanks for your booking! Here are your appointment details:

Service: {{ data_feed.booking_data.last_booking.service_type }}
Date: {{ data_feed.booking_data.last_booking.booking_date }}
Time: {{ data_feed.booking_data.last_booking.booking_time }}
Price: ${{ data_feed.booking_data.last_booking.price }}

We look forward to seeing you!
```

#### Booking recovery email

**Subject:**

```text  theme={null}
Complete your booking and save
```

**Body:**

<Tabs>
  <Tab title="Using a Coupon Data Feed">
    ```liquid  theme={null}
    Hi {{ data_feed.coupon.first_name | default: "there" }},

    Finish your booking in the next {{ data_feed.coupon.expires_in_hours }} hours and save
    {{ data_feed.coupon.discount_text }} with this code:

    {{ data_feed.coupon.code }}

    Use it here:
    {{ data_feed.coupon.deep_link }}
    ```
  </Tab>

  <Tab title="Without a Coupon Data Feed">
    ```text  theme={null}
    Hi there,

    You have not completed your booking yet!

    Complete it now to save on your next appointment.

    Use this link to complete your booking:
    [Insert deep link here]
    ```
  </Tab>
</Tabs>

<Note>
  Always include `default` filters in Liquid to prevent blank content if a Data
  Feed field is missing.
</Note>

### 4. Build the Journey

1. In OneSignal, go to **Messages > Journeys > Create Journey**

2. Set the **Entry Trigger** to:
   * **Custom Event:** `booking_started`

3. Add a **Wait Until** step:
   * **Condition:** Custom Event occurs
   * **Event name:** `booking_complete`
   * **Maximum wait time:** 10 minutes
   * Enable the expiration path

4. Configure the branches:
   * **Completed:** Send booking confirmation email
     * **Data Feed:** `booking_data`
   * **Expired:** Send recovery email
     * **Data Feed:** `coupon`

<Info>
  The expiration branch allows you to handle abandonment without additional
  logic in your app. See: - [Journey settings](./journeys-settings) - for
  details on Custom Event entry and exit rules - [Journeys
  actions](./journeys-actions) - for details on Wait Until steps and expiration
  branches
</Info>

### 5. Test and verify

#### Verify events

Trigger the custom events from your app or backend and confirm.

In OneSignal, go to **Analytics > Custom Events** and confirm you see:

* `booking_started` events appear for your External ID
* `booking_complete` events appear for your External ID

#### Verify Data Feeds

Manually call your Data Feed endpoints using a known user ID and confirm:

* A 200 response is returned
* All expected fields are present

#### Verify emails

Send test messages from the Journey editor and confirm:

* Booking emails contain real booking details
* Recovery emails contain a valid coupon
* No Liquid variables render empty

<Check>
  If personalization is missing, confirm that the user ID in the Data Feed
  request matches the user who triggered the Journey.
</Check>

## Example: Data Feed implementation

<Accordion title="Example Node.js Data Feed endpoints">
  This example shows a minimal Express implementation for booking confirmation and recovery Data Feeds. Your backend language, framework, and data source can differ as long as the JSON response shape matches your email templates.

### Booking Data Feed example

  ```js  theme={null}
  import express from "express";

  const app = express();

  function dataFeedAuth(req, res, next) {
    if (req.headers["x-api-key"] !== process.env.DATAFEED_API_KEY) {
      return res.status(401).json({ error: "Unauthorized" });
    }
    next();
  }

  app.get("/datafeed/booking", dataFeedAuth, async (req, res) => {
    const { user_id } = req.query;

    if (!user_id) {
      return res.status(400).json({ error: "Missing user_id" });
    }

    const booking = await getLatestBookingForUser(user_id);

    if (!booking) {
      return res.status(404).json({ error: "No booking found" });
    }

    res.json({
      first_name: booking.first_name,
      last_booking: {
        service_type: booking.service_type,
        booking_date: booking.booking_date,
        booking_time: booking.booking_time,
        price: booking.price,
      },
    });
  });
  ```

### Coupon Data Feed example

  ```js  theme={null}
  app.get("/datafeed/coupon", dataFeedAuth, async (req, res) => {
    const { user_id } = req.query;

    if (!user_id) {
      return res.status(400).json({ error: "Missing user_id" });
    }

    const coupon = await generateCouponForUser(user_id);

    res.json({
      first_name: coupon.first_name,
      code: coupon.code,
      discount_text: coupon.discount_text,
      expires_in_hours: coupon.expires_in_hours,
      deep_link: coupon.deep_link,
    });
  });
  ```

### Implementation guidelines

* Keep responses fast (Data Feeds are called at send time)
* Always return a predictable JSON structure
* Use 404 when no data exists
* Secure endpoints with an API key sent via request headers
</Accordion>

## Common issues

### Email shows empty values

* Data Feed returned 404
* Field names changed in the JSON response
* User identity mismatch

### Journey does not branch

* `booking_complete` event not tracked
* Event name mismatch (case-sensitive)
* Event occurs outside the wait window

### Data Feed returns 401 or 403

* Missing or invalid API key
* Header not configured in the Data Feed settings

## Next steps

* Add event properties (service type, price) for more advanced Journey conditions
* Add additional recovery steps such as push or SMS reminders
* Use Journey exit rules to prevent repeated recovery messages

***

Built with [Mintlify](https://mintlify.com).
