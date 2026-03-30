# Source: https://posthog.com/docs/web-analytics/web-vs-product-analytics.md

# What is the difference between web analytics and product analytics? - Docs

In a nutshell:

-   [Web analytics](/web-analytics.md) is good for tracking and monitoring high-level website metrics like page views, bounce rate, and the top sources of traffic. It's a pre-defined dashboard, so it's easy to quickly dip into and find what you need.

-   [Product analytics](/product-analytics.md) is good for diving deep into how specific users, or groups of users, behave. There are [dashboard templates](/templates.md) to help you get started, but you can build custom insights and dashboards to your precise needs, and use [notebooks](/docs/notebooks.md) for adhoc analysis.

Here's a quick comparison:

| Web analytics | Product analytics |
| --- | --- |
| Dashboards | One, pre-built | Unlimited, customizable |
| Custom insights | ✖ | ✔ |
| Events | Pageview, pageleave, conversions | Any, custom |
| Properties | Limited, pre-defined | Any, custom |
| Built for | Small teams, marketers | Engineering, product, data teams |
| Use case | At-a-glance view of website traffic | Analysis of product usage and user behavior |

## When should you use web analytics?

Web analytics gives you a single, pre-built [dashboard](https://us.posthog.com/web) for a high-level overview of your site. It's about collecting data in the aggregate, as opposed to tracking specific interactions from specific users.

It can help you figure out which pages and products are most popular and resonate the most with people.

![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/web_analytics_top_light_mode_2024_10_be53cf5325.png)![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/web_analytics_top_dark_mode_2024_10_6aa6dc9aeb.png)

You can use web analytics to find out:

How many visitors were there in recent days, weeks, and months?

Use the [web analytics dashboard](/docs/web-analytics/dashboard.md) to see the number of visitors currently online. Or filter by a specific time period like the last 14 days. You can also filter by unique visitors, pageviews, and sessions.

![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/web_analytics_top_light_mode_2024_10_be53cf5325.png)![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/web_analytics_top_dark_mode_2024_10_6aa6dc9aeb.png)

Which pages are people visiting?

Use the [paths](/docs/web-analytics/dashboard.md#paths) section on the dashboard to see which paths people are navigating to. You can also filter by the entry path, end path, and outbound clicks.

![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580005/posthog.com/contents/images/docs/web-analytics/dashboard/paths-light.png)![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580004/posthog.com/contents/images/docs/web-analytics/dashboard/paths-dark.png)

What is the bounce rate for pages on the site?

You can see the bounce rate percentage in the [paths](/docs/web-analytics/dashboard.md#paths) section in the web analytics dashboard.

![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580005/posthog.com/contents/images/docs/web-analytics/dashboard/paths-light.png)![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580004/posthog.com/contents/images/docs/web-analytics/dashboard/paths-dark.png)

What are the top sources of traffic?

List the top [referrers, channels, and UTM sources](/docs/web-analytics/dashboard.md#referrers-channels-utms) for the traffic to your website.

![Web analytics referrers](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580002/posthog.com/contents/images/docs/web-analytics/dashboard/referrers-light.png)![Web analytics referrers](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580002/posthog.com/contents/images/docs/web-analytics/dashboard/referrers-dark.png)

Where are visitors located geographically?

Use the [world map](/docs/web-analytics/dashboard.md#world-map) to visualize where visitors are located. You can also filter by the top countries, regions, and cities.

![Web analytics regions](https://res.cloudinary.com/dmukukwp6/image/upload/v1711579999/posthog.com/contents/images/docs/web-analytics/dashboard/regions-light.png)![Web analytics regions](https://res.cloudinary.com/dmukukwp6/image/upload/v1711580000/posthog.com/contents/images/docs/web-analytics/dashboard/regions-dark.png)

Which device types, browsers, and operating systems are visitors using?

![Web analytics regions](https://res.cloudinary.com/dmukukwp6/image/upload/device_type_light_ce42d4cd93.png)![Web analytics regions](https://res.cloudinary.com/dmukukwp6/image/upload/device_type_dark_5abbf3a671.png)

How long do sessions last on average?

You can use the web analytics dashboard to see how long sessions last on average over a given period of time, and also see how that duration is increasing or decreasing from the previous period.

![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/web_analytics_top_light_mode_2024_10_be53cf5325.png)![Web analytics dashboard](https://res.cloudinary.com/dmukukwp6/image/upload/web_analytics_top_dark_mode_2024_10_6aa6dc9aeb.png)

How many people are converting?

Use the **Add conversion goal** button to view conversion rates for particular events or groups of events.

![Conversion rate example](https://res.cloudinary.com/dmukukwp6/image/upload/conversion_rate_light_7e2eee73a2.png)![Conversion rate example](https://res.cloudinary.com/dmukukwp6/image/upload/conversion_rate_dark_afc4fee674.png)

For more on web analytics, check out our [getting started](/docs/web-analytics/getting-started.md) guide.

## When should you use product analytics?

When you want to dive deeper into user behavior in your app and how they are interacting with features. It gives you insights into metrics such as feature adoption rate, user retention, and churn.

![Product analytics example](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/funnel-steps-breakdown-light-mode.png)![Product analytics example](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/funnel-steps-breakdown-dark-mode.png)

You can use product analytics to:

Build custom dashboards

You can create custom [dashboards](/docs/product-analytics/dashboards.md) to track all your most important product and performance metrics.

![Dashboard example](https://res.cloudinary.com/dmukukwp6/image/upload/dashboard_light_61b3bab3b6.png)![Dashboard example](https://res.cloudinary.com/dmukukwp6/image/upload/dashboard_dark_5f2002f750.png)

Analyze trends and patterns in usage data

Use [trends](/docs/product-analytics/trends/overview.md) to plot data and find patterns.

![Trend insight example](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/product-analytics/trends/active-viewers-trend-light.png)![Trend insight example](https://res.cloudinary.com/dmukukwp6/image/upload//posthog.com/contents/docs/product-analytics/trends/active-viewers-dark.png)

Find where people are getting stuck during onboarding with funnels

Use [funnels](/docs/product-analytics/funnels.md) to understand where people are getting stuck or dropping off in your flow.

![Funnel insight example](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/identifying-drop-offs-light-mode.png)![Funnel insight example](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/identifying-drop-offs-dark-mode.png)

Follow users along their journey through your product with user paths

Use [user paths](/docs/product-analytics/paths.md) to find which parts of your product people are actually using, where users are getting confused or stuck, etc.

![User path insight example](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/example-light-mode.png)![User path insight example](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/example-dark-mode.png)

Look for particularly engaging features with stickiness

Use [stickiness](/docs/product-analytics/stickiness.md) to find engaging features by seeing how many times users perform an event within a specific time period.

![Stickiness insight example](https://res.cloudinary.com/dmukukwp6/image/upload/v1716289464/posthog.com/contents/stickiness-light.png)![Stickiness insight example](https://res.cloudinary.com/dmukukwp6/image/upload/v1716289465/posthog.com/contents/stickiness-dark.png)

Visualize user cohorts and retention metrics

Use [retention](/docs/product-analytics/retention.md) insights to find how many users sign up and come back to use your product after trying it.

![Retention insight example](https://res.cloudinary.com/dmukukwp6/image/upload/retention_light_805120c74c.png)![Retention insight example](https://res.cloudinary.com/dmukukwp6/image/upload/retention_dark_c319006162.png)

Check out the [product analytics docs](/docs/product-analytics.md) for more examples and guides.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better