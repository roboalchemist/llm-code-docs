# Source: https://posthog.com/docs/product-os.md

# Product OS - Docs

PostHog is a platform of many products:

-   [Product analytics](/docs/product-analytics.md) to help you quantitatively understand how users behave
-   [Web analytics](/docs/web-analytics.md) for tracking behavior on your marketing websites
-   [Session replay](/docs/session-replay.md) for diagnosing issues and seeing how users use your product
-   [Feature flags](/docs/feature-flags.md) for testing new features and safely rolling them out
-   [A/B testing](/docs/experiments.md) for scientifically verifying changes to improve conversion
-   [Surveys](/docs/surveys.md) for collecting qualitative feedback running satisfaction surveys
-   [Data warehouse](/docs/data-warehouse.md) for importing data from external sources and querying it alongside your data in PostHog

PostHog's Product OS is the foundation on which they're built.

It ties all your user and product data together, so you can focus on improving your product instead of engineering your data.

## Product OS features

Product OS comprises things like:

-   Our easy to implement [client and server SDKs](/docs/getting-started/install?tab=sdks.md) like `posthog-js` client library, which [autocaptures](/docs/product-analytics/autocapture.md) frontend events, so you don't have to waste time manually instrumenting every button and simple interaction

-   Our [APIs](/docs/api.md), which enable you to capture, evaluate, create, update, and delete nearly all of your information in PostHog, and [pull information into your app](/tutorials/embedded-analytics.md)

-   Collaboration features like [notebooks](/docs/notebooks.md), which enable you to analyze data from all PostHog products in a single document you can share and collaborate on with teammates

-   Built-in [data management tools](/docs/data.md), where you can define and organize events, person properties, data tables, and audit changes made by colleagues

-   [Data pipelines](/docs/cdp.md), which enable you to transform your PostHog data and send it to other tools for monitoring, marketing automation, sales, and support

-   [SQL](/docs/sql.md), which grants you unrestricted access to your data via custom SQL queries for advanced, custom analysis

-   [Our infrastructure](/docs/how-posthog-works.md), which is built upon [ClickHouse](/handbook/engineering/clickhouse.md), an ultra-fast open-source database system built specifically for real-time data analysis

-   The [toolbar](/docs/toolbar.md), which lets you easily toggle feature flags, access [heatmaps](/docs/toolbar/heatmaps.md), inspect elements, create [actions](/docs/data/actions.md), and see where users click

![](https://res.cloudinary.com/dmukukwp6/image/upload/texture_tan_9608fcca70)

![](https://res.cloudinary.com/dmukukwp6/image/upload/texture_tan_dark_a92b0e022d)

Install PostHog with one command

Paste this into your terminal and make AI do all the work.

`npx @posthog/wizard`

[Learn more](/wizard.md)

![PostHog Wizard hedgehog](https://res.cloudinary.com/dmukukwp6/image/upload/wizard_3f8bb7a240.png)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better