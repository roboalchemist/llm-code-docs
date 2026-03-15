# Source: https://posthog.com/docs/workflows/start-here.md

# Source: https://posthog.com/docs/support/start-here.md

# Source: https://posthog.com/docs/revenue-analytics/start-here.md

# Source: https://posthog.com/docs/product-tours/start-here.md

# Source: https://posthog.com/docs/posthog-ai/start-here.md

# Source: https://posthog.com/docs/logs/start-here.md

# Source: https://posthog.com/docs/llm-analytics/start-here.md

# Source: https://posthog.com/docs/getting-started/start-here.md

# Source: https://posthog.com/docs/feature-flags/start-here.md

# Source: https://posthog.com/docs/experiments/start-here.md

# Source: https://posthog.com/docs/error-tracking/start-here.md

# Source: https://posthog.com/docs/endpoints/start-here.md

# Source: https://posthog.com/docs/data-warehouse/start-here.md

# Source: https://posthog.com/docs/customer-analytics/start-here.md

# Getting started with customer analytics - Docs

**Customer Analytics is in beta**

Customer Analytics is currently in beta and free to use. We're actively developing this feature and would love your [feedback](https://app.posthog.com/customer_analytics#panel=support%3Afeedback%3Acustomer_analytics%3Alow%3Atrue).

Customer Analytics helps you understand your users without building dashboards from scratch. It tracks active users, signups, conversions, and engagement – the metrics that matter when you're building toward product-market fit.

## Configure dashboard events

The [customer analytics dashboard](https://app.posthog.com/customer_analytics) works immediately with `$pageview` events. To extract its full potential, configure it with your events in [customer analytics configurations](https://app.posthog.com/customer_analytics/configuration).

![Customer Analytics dashboard event configs](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_18_T18_45_30_373_Z_c57f043668.png)![Customer Analytics dashboard event configs](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_18_T18_46_37_819_Z_a0c5ad7667.png)

Tips for nailing the setup:

-   Use [PostHog AI](/docs/customer-analytics/configure-dashboard-with-ai.md) to help you find the events
-   Create actions to group multiple events under a single name for easier analysis
-   Be as specific as possible with event definitions. Sloppy definitions = sloppy metrics.

[Open dashboard configurations](https://app.posthog.com/customer_analytics/configuration)

## Define usage metrics

[Create usage metrics](/docs/customer-analytics/create-usage-metrics.md) to track custom activity for each interaction they have with your product. These appear on customer profiles and help you identify power users and churn risks.

![Usage metrics creation form](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_24_16_161_Z_0fde31684b.png)![Usage metrics creation form](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_23_19_968_Z_a4de4c95f4.png)

[Set up usage metrics](https://app.posthog.com/customer_analytics/configuration?tab=customer-analytics-usage-metrics#selectedSetting=customer-analytics-usage-metrics)

## Explore customer profiles

[Customer profiles](/docs/customer-analytics/customer-profiles.md) consolidate everything about a customer in one place: their events, [errors](/docs/error-tracking.md), [LLM traces](/docs/ai-engineering/observability.md), and support tickets.

![Person profile](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_30_34_040_Z_e0dea14b33.png)![Person profile](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/pasted_image_2025_12_19_T12_30_59_919_Z_8a54ff12bf.png)

[Explore customer profiles](https://app.posthog.com/persons)

1/3

[**Configure dashboard events** ***Required***](#quest-item-configure-dashboard-events)[**Define usage metrics** ***Recommended***](#quest-item-define-usage-metrics)[**Explore customer profiles** ***Optional***](#quest-item-explore-customer-profiles)

**Configure dashboard events**

***Required***

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better