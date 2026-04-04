# Source: https://documentation.onesignal.com/docs/en/conversion-metrics.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversion metrics

> Track the business impact of your messaging by attributing conversions like purchases and sign-ups to push, email, SMS, in-app, and RCS messages.

<Info>
  **Beta** — Conversion metrics is in beta and rolling out to all paid plans soon.
</Info>

## Overview

Conversion metrics let you measure the business impact of your OneSignal messaging by tracking real-world outcomes like purchases, sign-ups, and trial starts. You define which [custom events](./custom-events) count as conversions, and OneSignal attributes those conversions to the messages that drove them using a last-touch attribution model across all channels.

This gives you a clear picture of how push notifications, emails, SMS, in-app messages, and RCS messages contribute to your business goals — all from within the OneSignal dashboard.

## Default conversion metrics

OneSignal tracks these conversion metrics out of the box — no additional setup or configuration required on your part:

* **App Sessions** — Counts when a user opens your app after receiving a message.
* **Clicks** — Counts when a user clicks a message.

As long as the OneSignal SDK is integrated in your app or website, these metrics are collected automatically.

***

## Set up custom conversion metrics

Before you can set up custom conversion metrics, you need:

* **Custom events flowing into OneSignal** — Custom conversion metrics are powered by custom events. You must be sending events via the SDK, API, or an integration. See [Custom events](./custom-events) for setup instructions.
* **A paid plan** — Custom conversion metrics are available on all paid plans (Growth, Professional, and Enterprise).

<Steps>
  <Step title="Confirm custom events are sending">
    Verify your custom events are reaching OneSignal by checking **Data > Custom Events** in the dashboard. You should see the events you want to use as conversion metrics listed there.
  </Step>

  <Step title="Go to Settings > Analytics > Conversion Metrics">
    In the OneSignal dashboard, navigate to **Settings > Analytics > Conversion Metrics** to open the configuration page.
  </Step>

  <Step title="Select a custom event">
    Choose the custom event you want to track as a conversion metric. For example, select a `purchase` event to track revenue or a `signup` event to track new registrations.
  </Step>

  <Step title="Choose the tracking type">
    Select how you want to measure the conversion:

    | Tracking type | Description                        | Example            |
    | ------------- | ---------------------------------- | ------------------ |
    | **Count**     | Number of times the event occurred | 15 purchases       |
    | **Value**     | Total of a numeric property value  | \$1,250 in revenue |

    Use **Count** when you want to know how often something happened. Use **Value** when you want to track a cumulative numeric value like revenue or points.
  </Step>

  <Step title="Configure attribution windows">
    Set the attribution window for each channel. The attribution window determines how long after a message interaction a conversion can still be credited to that message. See [Attribution windows](#attribution-windows) for details.
  </Step>
</Steps>

<Frame caption="Settings > Analytics > Conversion Metrics setup page">
  <img src="https://mintcdn.com/onesignal/WNxr3MUofq7K6HBb/images/dashboard/conversion-metrics-setup.png?fit=max&auto=format&n=WNxr3MUofq7K6HBb&q=85&s=38090b549147e55107552cf929230118" alt="Conversion metrics setup page showing event selection, tracking type, and attribution window configuration" width="2722" height="1034" data-path="images/dashboard/conversion-metrics-setup.png" />
</Frame>

***

## Attribution windows

An attribution window is the time period after a message interaction during which a conversion can be credited to that message. If a user converts within the window, the message receives credit. If the user converts after the window closes, the message does not.

You can configure attribution windows per channel in **Settings > Analytics > Conversion Metrics**.

| Channel | Notes                                                               |
| ------- | ------------------------------------------------------------------- |
| Push    | Window starts when the notification is delivered or clicked         |
| Email   | Window starts when the email is opened or clicked                   |
| In-App  | Window starts when the message receives an impression or is clicked |
| SMS     | Window starts when the message is delivered                         |
| RCS     | Window starts when the message is delivered or read                 |

***

## Attribution model

Conversion metrics use a **last-touch attribution** model. When a user converts, OneSignal evaluates all qualifying message interactions within their respective attribution windows and classifies the conversion as **attributed**, **influenced**, or **unattributed**.

### Attributed conversions

The most recent qualifying message interaction across **all channels** before the conversion receives attributed credit. Only **one message** gets attribution per conversion.

| Channel | Qualifying interactions |
| ------- | ----------------------- |
| Push    | Clicked                 |
| In-App  | Clicked                 |
| Email   | Opened or clicked       |
| SMS     | Clicked                 |
| RCS     | Read or clicked         |

### Influenced conversions

Any message that meets the qualifying criteria within its attribution window — **except** the one attributed message — receives influenced credit. Multiple messages can receive influenced credit for a single conversion.

| Channel | Qualifying interactions     |
| ------- | --------------------------- |
| Push    | Delivered or clicked        |
| In-App  | Impression or clicked       |
| Email   | Opened or clicked           |
| SMS     | Delivered or clicked        |
| RCS     | Delivered, read, or clicked |

### Unattributed conversions

A conversion is unattributed when no message interaction qualifies within any attribution window. The conversion happened organically, without a traceable message interaction.

<Note>
  **Key rules:**

* A message receives **either** attributed **or** influenced credit for a given conversion, never both.
* Attribution is cross-channel: the last qualifying interaction from **any** channel wins attributed credit.
</Note>

***

## View conversion metrics

Conversion data appears across several areas of the OneSignal dashboard.

### Global conversions dashboard

The global conversions dashboard provides a high-level view of all conversion activity. It shows total, attributed, influenced, and unattributed conversions over time.

You can switch between a combined view and per-channel breakdowns using the tabs at the top of the chart.

<Frame caption="Global conversions dashboard showing total, attributed, influenced, and unattributed conversions">
  <img src="https://mintcdn.com/onesignal/WNxr3MUofq7K6HBb/images/dashboard/global-conversions-chart.png?fit=max&auto=format&n=WNxr3MUofq7K6HBb&q=85&s=2267ac4d2a44b515166993026262b5a4" alt="Global conversions dashboard chart showing total, attributed, influenced, and unattributed conversions over time" width="2690" height="1420" data-path="images/dashboard/global-conversions-chart.png" />
</Frame>

### Message, template, and Journey reports

Conversion metrics appear on all channel message reports, template reports, and Journey reports. Each report shows the attributed and influenced conversions for that specific message or aggregated across messages.

You'll see different metrics depending on whether you're viewing **Counts** or **Values.**

### Count metrics

* **Direct conversions** -- This is all conversions with direct attribution credit, including those that also have influenced credit.
* **Influenced conversions** -- This is all conversions that only have influenced credit. Multiple messages may influence a conversion, so a conversion may be counted more than once across different summary views.
* **Conversion yield** -- Measures how effectively your messages drive conversions. Calculated as direct conversions divided by total delivered messages.

### Value metrics

* **Direct conversion value** -- This is the sum of the value property for conversions with direct attribution credit, including those that also have influenced credit.
* **Influenced conversion value** -- This is the sum of the value property for conversions that only have influenced credit. Multiple messages may influence a conversion, so a conversion may be counted more than once across different summary views.
* **Value per delivery** -- Measures how much conversion value your messages drive. Calculated as direct conversion value divided by total delivered messages.

### Cross-channel calculation methodology

When presenting aggregated metrics across multiple channels, we use the following methodology:

* **Clicks and Click-through rate** -- CTR is always calculated using unique clicks. Because all push notifications can be clicked (opened) exactly once, we use the push notification total click count.
* **Delivered messages** -- This is used as the denominator in click-through rate, conversion yield, and value per delivery. We count delivered messages for push, email, and SMS / RCS and impressions for in-app messages.

<Note>
  **Global vs. message-level reporting:**

  On the global dashboard, each channel receives at most **1 influenced credit** per conversion, even if multiple messages on that channel influenced it. On individual message reports, **each message** that received influenced credit shows it.

  This means the sum of influenced credits across individual message reports may be higher than the channel-level influenced count on the global dashboard.
</Note>

***

## Plan availability

Default conversion metrics (App Sessions and Clicks) are available on all plans. Custom conversion metrics are available on paid plans (Growth, Professional, and Enterprise).

***

## Migration from Custom Outcomes

Custom Outcomes is being deprecated and replaced by conversion metrics.

* **Legacy data is preserved** — Your existing Custom Outcomes data remains accessible as historical data.
* **Separate reporting** — Legacy Custom Outcomes will **not** appear on the new conversion metrics charts. They remain in their original location.
* **No automatic migration** — To track the same metrics with the new attribution model, you need to:
  1. Implement [custom events](./custom-events) via the SDK, API, or integrations (if you haven't already).
  2. Configure those events as conversion metrics in **Settings > Analytics > Conversion Metrics**.
* **Default metrics are migrated** — The default OneSignal outcomes (sessions, clicks) are automatically available as default conversion metrics.

***

## FAQ

### How is this different from Custom Outcomes?

Custom Outcomes only attribute conversions from push notifications and in-app messages. Conversion metrics use a cross-channel last-touch attribution model that covers push, email, SMS, in-app, and RCS. Conversion metrics are also powered by custom events instead of SDK outcome methods, and they provide more granular control over attribution windows per channel.

### What channels support conversion metrics?

Push notifications, email, SMS, in-app messages, and RCS.

### Can I track revenue with conversion metrics?

Yes. When setting up a conversion metric, choose the **Value** tracking type and select the numeric property from your custom event that represents the monetary value (for example, `price` or `order_total`).

### How long is conversion data retained?

Conversion data is retained based on your plan. See [Analytics data retention](./billing-faq#analytics-data-retention) for details.

### What happens to my existing Custom Outcomes data?

Your existing Custom Outcomes data is preserved and remains accessible as historical data. It will not be migrated to or displayed on the new conversion metrics charts. See [Migration from Custom Outcomes](#migration-from-custom-outcomes) for details.

***

## Related pages

<Columns cols={2}>
  <Card title="Custom events" icon="bolt" href="./custom-events">
    Set up and manage the events that power conversion metrics.
  </Card>

  <Card title="Analytics overview" icon="chart-line" href="./analytics-overview">
    Explore all analytics features available in OneSignal.
  </Card>
</Columns>

Built with [Mintlify](https://mintlify.com).
