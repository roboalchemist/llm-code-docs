# Source: https://docs.datadoghq.com/tracing/recommendations.md

---
title: APM Recommendations
description: >-
  Learn how to optimize your application's performance and reliability with APM
  Recommendations.
breadcrumbs: Docs > APM > APM Recommendations
---

# APM Recommendations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

APM Recommendations help you improve your applications' performance and reliability by surfacing optimization opportunities from your collected telemetry. These recommendations are designed to:

- Identify and resolve performance bottlenecks
- Improve service reliability and uptime
- Improve end-user experience

{% image
   source="https://datadog-docs.imgix.net/images/tracing/recommendations/apm_recommendations-2.d47f38095ea38f91b568ce57c70f761f.png?auto=format"
   alt="APM Recommendations page showing a list of recommendations with filters for status and type" /%}

## Prerequisites{% #prerequisites %}

Certain recommendations rely on specific Datadog products. Use the **Recommendation Prerequisite** dropdown to filter recommendations by the Datadog products in your setup.

## How it works{% #how-it-works %}

APM Recommendations are based on data collected from different parts of your stack:

- Distributed traces from Application Performance Monitoring (APM)
- Database telemetry from Database Monitoring (DBM)
- Sessions and user journeys from Real User Monitoring (RUM)

Datadog correlates these sources to identify opportunities to improve performance, reliability, and user experience.

Datadog ranks recommendations by computing a priority score that weighs the potential impact of an issue against telemetry signals, such as relative request volume and performance trends. The most critical insights for improving service reliability and performance appear first.

## Using APM Recommendations{% #using-apm-recommendations %}

To review recommendations that need your attention:

1. Go to [**APM** > **Recommendations**](https://app.datadoghq.com/apm/recommendations).
1. Filter your recommendations by status or type.
1. Select a recommendation from the list to see a detailed description of the issue.
1. Review the problem, impact, and Datadog's recommendation for resolving it.

After you've reviewed the recommendation, you can use the **FOR REVIEW** dropdown to change the recommendation status to *Reviewed*, *Ignored*, or *Resolved*. Alternatively, you can assign the recommendation to an owner and track related work in Case Management or Jira.

## Supported recommendations{% #supported-recommendations %}

| Recommendation Category | Recommendation Type           | Scope of Recommendation | Recommendation Description                                                                                                                                                                                                    | Recommendation Prerequisite |
| ----------------------- | ----------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Performance             | N+1 Queries on Database       | Backend services        | A backend application calls the same database sequentially instead of batching queries.                                                                                                                                       | APM                         |
| Performance             | Repeated Sequential API calls | Backend services        | A backend application repeatedly retries failing API calls without sufficient backoff, increasing system load and masking underlying reliability issues.                                                                      | APM                         |
| Performance             | Persistent Retries            | Backend services        | A backend application issues an excessive number of retry attempts when calling a downstream API, extending request duration and risking cascading failures under strain.                                                     | APM                         |
| Performance             | Missing index                 | Databases               | The query's execution plan performs expensive sequential scans. When detected, Datadog recommends using an index to expedite the query.                                                                                       | APM + DBM                   |
| Performance             | Unbalanced Read Load          | Databases               | A service is making read-only queries to a primary database instance when replicas are available. Routing these queries to replicas can reduce primary load and improve performance.                                          | APM + DBM                   |
| Reliability             | Aggressive Retries            | Backend services        | A backend application triggers rapid-fire retry attempts without adequate backoff, sustaining high pressure on struggling dependencies and risking prolonged outages by preventing system recovery during transient failures. | APM                         |
| Reliability             | High Exception Volumes        | Backend services        | A backend application is throwing a high number of exceptions as control-flow, adding CPU and memory overhead.                                                                                                                | APM + Continuous Profiler   |
Recommendation CategoryAll Performance ReliabilityRecommendation TypeAll Aggressive Retries High Exception Volumes Missing index N+1 Queries on Database Persistent Retries Repeated Sequential API calls Unbalanced Read LoadScope of RecommendationAll Backend services DatabasesRecommendation PrerequisiteAll APM APM + Continuous Profiler APM + DBM
**Note**: If you use both APM and Database Monitoring (DBM), you may see fewer Missing Index recommendations here than on the [DBM Recommendations page](https://docs.datadoghq.com/database_monitoring/recommendations/). APM Recommendations only surface Missing Index issues that Datadog can associate with an instrumented application service. Missing Index recommendations that cannot be linked to a specific service appear only in DBM.

## Further reading{% #further-reading %}

- [Learn about Application Performance Monitoring (APM)](https://docs.datadoghq.com/tracing/)
- [APM Dashboard Guide](https://docs.datadoghq.com/tracing/guide/apm_dashboard/)
- [Cloud Cost Recommendations](https://docs.datadoghq.com/cloud_cost_management/recommendations/)
- [DBM Recommendations](https://docs.datadoghq.com/database_monitoring/recommendations/)
- [Improve performance and reliability with Proactive App Recommendations](https://www.datadoghq.com/blog/proactive-app-recommendations/)
