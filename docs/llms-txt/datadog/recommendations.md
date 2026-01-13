# Source: https://docs.datadoghq.com/cloud_cost_management/recommendations.md

# Source: https://docs.datadoghq.com/tracing/recommendations.md

---
title: APM Recommendations
description: >-
  Learn how to optimize your application's performance and reliability with APM
  Recommendations.
breadcrumbs: Docs > APM > APM Recommendations
source_url: https://docs.datadoghq.com/recommendations/index.html
---

# APM Recommendations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

APM Recommendations are in Preview. Features and recommendations may change before general availability. To request access, fill out this form.

[Request Access](https://www.datadoghq.com/product-preview/apm-proactive-recommendations/)
{% /callout %}

APM Recommendations help you improve your applications' performance and reliability by providing optimization opportunities based on the telemetry collected on your applications. These recommendations are designed to:

- Identify and resolve performance bottlenecks
- Improve service reliability and uptime
- Reduce error rates and improve end-user experience

{% image
   source="https://datadog-docs.imgix.net/images/tracing/recommendations/apm_recommendations.780a3dd8b76533fb2a3761154cc70ca8.png?auto=format"
   alt="Your image description" /%}

## Prerequisites{% #prerequisites %}

Certain recommendations rely on specific Datadog products. Use the **Recommendation Prerequisite** dropdown to filter for the recommendations you can expect to see based on your specific setup.

## How it works{% #how-it-works %}

APM Recommendations are based on data collected from different parts of your stack:

- Sessions and user journeys from Real User Monitoring (RUM)
- Distributed traces from Application Performance Monitoring (APM)
- Error data from Error Tracking
- Database telemetry from Database Monitoring (DBM)

By looking at these sources together, Datadog finds ways to help you improve performance, reliability, and user experience.

Datadog prioritizes recommendations by computing a severity score that weighs the potential impact of an issue against telemetry signals, such as relative request volume and performance trends. This ensures that the most critical insights for improving service health appear first.

## Using APM Recommendations{% #using-apm-recommendations %}

To review recommendations that need your attention:

1. Go to [**APM** > **Recommendations**](https://app.datadoghq.com/apm/recommendations).
1. Filter your recommendations by status or type.
1. Select a recommendation from the list to see a detailed description of the issue.
1. Review the problem, impact, and Datadog's recommendation for resolving it.

After you've reviewed the recommendation, you can use the **FOR REVIEW** dropdown to change the recommendation status to *Reviewed*, *Ignored*, or *Resolved*. Alternatively, you can click **Create Ticket** to assign the recommendation to an owner and track related work in Jira or Case Management.

## Supported recommendations{% #supported-recommendations %}

| Recommendation Category | Recommendation Type           | Scope of Recommendation                                   | Recommendation Description                                                                                                                                                | Recommendation Prerequisite |
| ----------------------- | ----------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Performance             | N+1 Queries on Database       | Backend services                                          | A backend application calls the same database sequentially instead of batching queries.                                                                                   | APM                         |
| Performance             | Repeated Sequential API calls | Backend services                                          | A backend application repeatedly retries failing API calls without sufficient backoff, increasing system load and masking underlying reliability issues.                  | APM                         |
| Performance             | Persistent Retries            | Backend services                                          | A backend application issues an excessive number of retry attempts when calling a downstream API, extending request duration and risking cascading failures under strain. | APM                         |
| Performance             | Missing index                 | Databases                                                 | The query's execution plan performs expensive sequential scans. When detected, Datadog recommends using an index to expedite the query.                                   | APM + DBM                   |
| User experience         | User frustration action       | Browser applications                                      | Common rage or dead actions are detected on elements on a page signaling misleading UI or broken elements.                                                                | RUM                         |
| User experience         | Unoptimized bundle size       | Browser applications and web views on mobile applications | Large JS resources causing delays in the initial page render signaling misleading UI or broken elements.                                                                  | RUM                         |
| Reliability             | High Exception Volumes        | Backend services                                          | A backend application is throwing a high number of exceptions as control-flow, adding CPU and memory overhead.                                                            | APM + Continuous Profiler   |
Recommendation CategoryAll Performance Reliability User experienceRecommendation TypeAll High Exception Volumes Missing index N+1 Queries on Database Persistent Retries Repeated Sequential API calls Unoptimized bundle size User frustration actionScope of RecommendationAll Backend services Browser applications Browser applications and web views on mobile applications DatabasesRecommendation PrerequisiteAll APM APM + Continuous Profiler APM + DBM RUM
## Further reading{% #further-reading %}

- [Learn about Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing/)
- [APM Dashboard Guide](https://docs.datadoghq.com/tracing/guide/apm_dashboard/)
- [Cloud Cost Recommendations](https://docs.datadoghq.com/cloud_cost_management/recommendations/)
- [DBM Recommendations](https://docs.datadoghq.com/database_monitoring/recommendations/)
- [Improve performance and reliability with Proactive App Recommendations](https://www.datadoghq.com/blog/proactive-app-recommendations/)
