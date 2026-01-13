# Source: https://docs.datadoghq.com/product_analytics.md

---
title: Product Analytics
description: Product Analytics help you understand your application usage at a glance.
breadcrumbs: Docs > Product Analytics
source_url: https://docs.datadoghq.com/index.html
---

# Product Analytics

## Overview{% #overview %}

Product Analytics helps you gain insight into user behavior and make data-driven decisions. It can help solve the following types of use cases in your application:

- Understand product adoption
- Track conversion rates and their evolution over time
- Track key user behavior patterns
- Visualize the most and least interacted with buttons on a given page

## Getting started{% #getting-started %}

To start using Product Analytics, enable it for each application where you want to monitor user behavior:

1. Select the application you want to monitor from the [Application Management](https://app.datadoghq.com/rum/list) list.
1. Under PRODUCT SETTINGS, click **Product Analytics**.
1. Click the **Enable** button.

{% image
   source="https://datadog-docs.imgix.net/images/product_analytics/enable-product-analytics.9549a6f256f7c25962dc2ba878c1c770.png?auto=format"
   alt="Enable Product Analytics from the Application Management page." /%}

If you don't have an application set up in Datadog yet, create one for your platform ([browser](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser), [iOS](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/ios), or [Android](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/android)) or use your [coding assistant](https://docs.datadoghq.com/product_analytics/agentic_onboarding).

By default, Product Analytics data is retained for 15 months. Learn more about [Datadog's data retention periods](https://docs.datadoghq.com/data_security/data_retention_periods/).

## Navigating the Product Analytics UI{% #navigating-the-product-analytics-ui %}

Each Product Analytics feature provides context into your users' journeys. This section describes the context each feature can provide for your individual use case.

### Understand product adoption{% #understand-product-adoption %}

The [Home](https://app.datadoghq.com/product-analytics) page gives you a bird's-eye view of your users' activity and a pulse into your product's adoption. This is where you most often land when accessing Product Analytics.

{% image
   source="https://datadog-docs.imgix.net/images/product_analytics/pana_home_page.37675aa9f59ecd152d1c3a825b6977a8.png?auto=format"
   alt="Understand end-to-end conversions with Funnel Analysis." /%}

By default, this page displays the `active users`, `page views`, and `average time spent by user` charts, but you have the ability to add additional charts or a dashboard. The Home page also includes the following out-of-the-box sub-sections that provide additional context about your product's users and usage:

{% dl %}

{% dt %}
[Users](https://app.datadoghq.com/product-analytics/user-trends)
{% /dt %}

{% dd %}
At a glance, see who is using your product.
{% /dd %}

{% dt %}
[App & Devices](https://app.datadoghq.com/product-analytics/app-and-devices)
{% /dt %}

{% dd %}
Visualize the split between desktop and mobile usage, spot which versions are in use, and identify what can be deprecated.
{% /dd %}

{% dt %}
[Engagement](https://app.datadoghq.com/product-analytics/engagement-and-features)
{% /dt %}

{% dd %}
Understand how users are engaging with your product to answer questions like how long users are staying on pages and what their top actions are.
{% /dd %}

{% dt %}
[Traffic](https://app.datadoghq.com/product-analytics/traffic-and-acquisition)
{% /dt %}

{% dd %}
Get a view into bounce rates, top traffic sources, and where your growth is really coming from.
{% /dd %}

{% dt %}
[Performance](https://app.datadoghq.com/product-analytics/performance)
{% /dt %}

{% dd %}
View surface top errors and frustrations, and see exactly which views they impact.
{% /dd %}

{% /dl %}

### Track conversion rates and their evolution over time{% #track-conversion-rates-and-their-evolution-over-time %}

The Product Analytics charts help you visualize your users' journey as they use your product.

{% video
   url="https://datadog-docs.imgix.net/images//product_analytics/pana_charts_video.mp4" /%}

Each chart type provides a different view into the user's journey:

{% dl %}

{% dt %}
[Pathways](https://docs.datadoghq.com/product_analytics/charts/pathways)
{% /dt %}

{% dd %}
You can visualize all user journeys across your application to analyze the critical path.
{% /dd %}

{% dt %}
[Funnel](https://docs.datadoghq.com/product_analytics/charts/funnel_analysis)
{% /dt %}

{% dd %}
Track conversion rates across key workflows to identify and address any bottlenecks in end-to-end user journeys.For example, you can see if customers drop off at a certain point due to poor website performance or measure how adding new steps to a workflow impacts drop off rate.
{% /dd %}

{% dt %}
[Retention](https://docs.datadoghq.com/product_analytics/charts/retention_analysis)
{% /dt %}

{% dd %}
Measure how often users are successfully returning to a page or action to gain insights into overall user satisfaction.
{% /dd %}

{% dt %}
[Analytics](https://docs.datadoghq.com/product_analytics/charts/analytics_explorer)
{% /dt %}

{% dd %}
Contains views data aggregation for understanding how your product is being used.
{% /dd %}

{% /dl %}

### Track key user behavior patterns{% #track-key-user-behavior-patterns %}

You may want to better understand a specific group of users. This could be for the purpose of improving their user experience, or nudge them to buy the content in their cart. Regardless of the purpose, you can use the [Users & Segments](https://docs.datadoghq.com/product_analytics/segmentation/) section to group your users based on a desired characteristic.

{% image
   source="https://datadog-docs.imgix.net/images/product_analytics/segmentation/userprofiles_pana-ga.02890a136fd71ef9b4a5fb141bb86fad.png?auto=format"
   alt="See individual profiles of users and create a segment from these profiles." /%}

You can see the individual profiles of user, and create a segment, or a specified grouping, from these profiles to fit the behavior you would like to observe. For example, you can create a segment on users who have items in their carts but have not yet checked out to send an email nudging them to make a purchase.

### Visualize the most and least interacted with buttons on a given page{% #visualize-the-most-and-least-interacted-with-buttons-on-a-given-page %}

Suppose you want to make changes to your application interface but want to first understand how users navigate in the page. Is there a specific path they take more than others? Can you make user actions and flows smoother? The following features can help you capture and replay your users' browsing experience to inform your product change decisions.

{% image
   source="https://datadog-docs.imgix.net/images/product_analytics/pana_session_replay_page.2481b92dc9cf66c6385bf14a5f947483.png?auto=format"
   alt="Capture and replay your users' browsing experience to inform your product design decisions." /%}

{% dl %}

{% dt %}
[Session replay](https://docs.datadoghq.com/session_replay/)
{% /dt %}

{% dd %}
Expands your user experience monitoring by allowing you to capture and visually replay the web browsing or mobile app experience of your users.This is beneficial for *error identification*, *reproduction*, and *resolution*, and provides insights into your application's usage patterns and design pitfalls
{% /dd %}

{% dt %}
[Heatmaps](https://docs.datadoghq.com/session_replay/heatmaps)
{% /dt %}

{% dd %}
This is a visualization of your user's interactions overlaid on Session Replay data. Product Analytics has three different types of heatmaps: Click maps, Top elements, Scroll maps.Use heatmaps to review complex data at a glance, gaining insights around optimizing your user experience.
{% /dd %}

{% dt %}
[Playlist](https://docs.datadoghq.com/session_replay/playlists)
{% /dt %}

{% dd %}
You can create a playlist of Session Replays to organize them by any patterns you notice. Learn more about [Session Replay Playlists](https://docs.datadoghq.com/session_replay/playlists).
{% /dd %}

{% /dl %}

## Further reading{% #further-reading %}

- [From performance to impact: Bridging frontend teams through shared context](https://www.datadoghq.com/blog/rum-product-analytics-bridging-teams)
- [Make data-driven design decisions with Product Analytics](https://www.datadoghq.com/blog/datadog-product-analytics/)
- [Analytics Explorer](https://docs.datadoghq.com/product_analytics/analytics_explorer/)
