# Source: https://posthog.com/docs/revenue-analytics/payment-platforms.md

# Connect to payment platforms - Docs

**Revenue analytics is in beta**

Revenue analytics is currently works best for:

1.  Small to medium-sized companies
2.  Companies with subscription models (mostly SaaS)

If you process more than 20,000 transactions per month, or your revenue comes primarily from one-off payments rather than recurring subscriptions, revenue analytics may feel less useful, slower, or provide less insight than expected.

The simplest way to get started with revenue analytics is to connect to a payment platform.

![Data warehouse tables setup](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_09_05_at_14_18_19_eeec8127a9.png)![Data warehouse tables setup](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_09_05_at_14_18_30_c7ad45d637.png)

Start by connecting your payment platform(s) to PostHog as a data source:

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Stripe_Logo_revised_2016_24183d3284.svg)Stripe](/docs/revenue-analytics/payment-platforms/stripe.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/cb_597858b354.svg)ChargebeeComing soon](#)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/logomark_black_a7518b0322.svg)PolarComing soon](#)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/logomark_red_background_9ea591e17a.svg)RevenueCatComing soon](#)

> We currently only support revenue analytics data from Stripe. More platforms will be supported in the future.

## How is the data stored?

When you connect your payment platform(s) to PostHog, the data is transformed into standardized [managed views](/docs/revenue-analytics/managed-views.md). Revenue analytics uses this data to build your [revenue analytics dashboard](/docs/revenue-analytics/dashboard.md).

The data is stored in the [data warehouse](/docs/data-warehouse.md) and is available for you to run custom queries and visualize like any other data in PostHog.

## Deferred revenue

When using revenue data from your data warehouse (from sources like Stripe), PostHog automatically defers revenue recognition to match your accounting practices. This means we spread the revenue across all the months a charge is relevant for.

You can learn more about this on the [deferred revenue](/docs/revenue-analytics/deferred-revenue.md) page.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better