# Source: https://posthog.com/docs/cdp.md

# Source: https://posthog.com/docs/advanced/cdp.md

# Using PostHog with a CDP - Docs

## What is a CDP?

CDP stands for Customer Data Platform. It is a service that collects and unifies customer data from many sources and then sends it for use in other tools like product analytics, marketing automation, your CRM, data warehouses, and more.

The most common CDPs are [Segment](/docs/libraries/segment.md) and [RudderStack](/docs/libraries/rudderstack.md), both of which work with PostHog.

## Do I need a CDP?

If you don't have a CDP already set up, you might not need one. PostHog has:

-   [SDKs](/docs/libraries.md) and [API](/docs/api/capture.md) to capture data from anywhere.
-   A [data warehouse](/docs/data-warehouse.md) to easily import and query data from [Stripe](/tutorials/stripe-reports.md), [Hubspot](/tutorials/hubspot-reports.md), [Zendesk](/tutorials/zendesk-reports.md), [S3](/docs/data-warehouse/setup/s3.md), and more.
-   Pre-built and customizable [transformations and destinations](/docs/cdp.md) for cleaning and sending data to other tools like [webhooks](/docs/cdp/destinations/webhook.md), [Slack](/docs/cdp/destinations/slack.md), and more.
-   A suite of dev tools including [SQL querying](/docs/product-analytics/sql.md) and visualizations.

This means PostHog can act as your single source of truth without needing to set up and pay for another tool.

Here's a decision tree that you might find handy:

graph TD A\[Are you using a 3rd party CDP currently?\] --> |Yes| B\[Option 2<br/>Integrate PostHog\] A --> |No| C\[Are there destinations you need that PostHog doesn't have yet?\] --> |Yes| D\[Option 2<br/>Integrate PostHog\] C --> |No| E\[Option 1<br/>Use PostHog as a CDP\]

## Option 1: Use PostHog as a CDP

In general, we recommend starting with PostHog as your CDP using our SDKs, data warehouse, destinations, and transformations as needed. This is the easiest and least expensive way to get started.

We have most of the [destinations](/docs/cdp/destinations.md) you need, but if we don't currently support, you have three options:

1.  Use our [custom webhook destination](/docs/cdp/destinations/webhook.md) or build your own [realtime destinations](/docs/cdp/destinations.md) to call the 3rd-party API.
2.  Request a new destination by clicking **Can't find what your looking for?** when [creating a new destination](https://app.posthog.com/pipeline/new/destination) in-app and our team will be notified.
3.  Fully transition to a 3rd party CDP.

graph LR A\[Website - Javascript Web SDK\] --> B\[PostHog\] C\[iOS App - Swift SDK\] --> B\[PostHog\] D\[Android App - Java SDK\] --> B\[PostHog\] E\[Backend - Python SDK\] --> B\[PostHog\] B\[PostHog\] --> H\[Saleforce\] B\[PostHog\] --> I\[Intercom\] B\[PostHog\] --> K\[Customer.io\] B\[PostHog\] --> F\[Data warehouse e.g. BigQuery / Snowflake\]

**Pros:**

-   Least expensive as you don't need a 3rd party CDP.
-   Fewer services means reduced risk of data being dropped.
-   Works with all the features of PostHog (analytics, autocapture, feature flags, session recording, etc.)

**Cons:**

-   We may not have all the destinations as "pure CDP" products. If you need these destinations immediately and you have the time and money for a 3rd party CDP, you might want to go with option 2.

### Sending PostHog data to a 3rd party CDP for extra destinations

If PostHog doesn't have your destination and you can't build your own, another option is to send data to your CDP like [RudderStack](/docs/cdp/rudderstack-export.md) and then add the destination you need. This gives you more destinations than PostHog alone, while also mostly relying on PostHog.

> **Note:** This won't work for the CDP device-mode sources such as Facebook Ads and Google Ads (where the CDP injects the marketing script onto the page). If you need this, we'd recommend integrating the marketing platforms directly, using Google Tag Manager or using a 3rd party CDP as your primary CDP (option 2).

graph LR A\[Website - Javascript Web SDK\] --> B\[PostHog\] C\[iOS App - Swift SDK\] --> B\[PostHog\] D\[Android App - Java SDK\] --> B\[PostHog\] E\[Backend - Python SDK\] --> B\[PostHog\] B --> G G\[3rd party CDP e.g. RudderStack\] --> N\[Extra destinations\] B --> H\[Saleforce\] B --> I\[Intercom\] B --> K\[Customer.io\] B --> F\[Data warehouse e.g. BigQuery / Snowflake\]

## Option 2: Use a 3rd party CDP with PostHog as a destination

If you already use a CDP extensively, you'll likely want to integrate PostHog with it. For your frontend sources, configure PostHog as a destination to ensure you get the full functionality. See our guides for [Segment](/docs/libraries/segment.md) and [RudderStack](/docs/libraries/rudderstack.md) for more information.

graph LR A\[Website - CDP Javascript SDK\] --> G C\[iOS App - CDP Swift SDK\] --> G D\[Android App - CDP Java SDK\] --> G E\[Backend - CDP Python SDK\] --> G G\[3rd party - CDP<br/>e.g. Segment/RudderStack\] --> B\[PostHog\] G --> N\[Google Ads\] G --> O\[Facebook Ads\] G --> H\[Saleforce\] G --> I\[Intercom\] G --> K\[Customer.io\] G --> F\[Data warehouse e.g. BigQuery / Snowflake\]

**Pros:**

-   You can integrate PostHog with your existing CDP.
-   Manage all your sources and destinations in one place.
-   A broader range of destinations available than PostHog alone.

**Cons:**

-   You'll need to pay for a 3rd party CDP.
-   If you use PostHog's event autocapture, the other CDP destinations will not receive the autocapture events.
-   Enabling feature flags and session recordings requires extra setup or manually installing the PostHog script.
-   Variable support by the CDP libraries for PostHog's features.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better