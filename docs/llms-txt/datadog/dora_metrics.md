# Source: https://docs.datadoghq.com/dora_metrics.md

---
title: DORA Metrics
description: >-
  Learn how to use DORA metrics to measure and improve your organization's
  software delivery processes.
breadcrumbs: Docs > DORA Metrics
---

# DORA Metrics

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

DevOps Research and Assessment (DORA) metrics are [four key metrics](https://www.datadoghq.com/knowledge-center/dora-metrics/) that indicate the velocity and stability of software development.

{% dl %}

{% dt %}
Deployment frequency
{% /dt %}

{% dd %}
How often an organization successfully releases to production.
{% /dd %}

{% dt %}
Change lead time
{% /dt %}

{% dd %}
The amount of time it takes a commit to get into production.
{% /dd %}

{% dt %}
Change failure rate
{% /dt %}

{% dd %}
The ratio of deployments that fail and require immediate intervention.
{% /dd %}

{% dt %}
Failed deployment recovery time
{% /dt %}

{% dd %}
The time it takes to recover from a deployment that fails and requires immediate intervention.
{% /dd %}

{% /dl %}

Defining and tracking DORA metrics can help you identify areas of improvement for your team or organization's speed and quality of software delivery.

## Set up DORA Metrics{% #set-up-dora-metrics %}

To start configuring data sources to send deployment events to Datadog, see the [Setup documentation](https://docs.datadoghq.com/dora_metrics/setup/).

## Analyze DORA Metrics{% #analyze-dora-metrics %}

After you've set up the data sources for your deployment and failure events, navigate to [**Software Delivery** > **DORA Metrics**](https://app.datadoghq.com/ci/dora) to identify improvements or regressions for each metric. You can also aggregate the metrics by team, service, repository, environment, time period, and [custom tags](https://docs.datadoghq.com/dora_metrics/data_collected/#custom-tags) to compare trends over time.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/dora_ui_3.1c02efe2d644b5baafe7caa0de0678cf.png?auto=format"
   alt="An overview of DORA Metrics calculations filtered by the Language custom tag" /%}

Click **View Deployments** to open a new tab with the list of deployment events.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/deployments_list.25e630d3cb95255ec049a5db3418cf2a.png?auto=format"
   alt="The Deployments Breakdown displaying a breakdown of metrics and a list of related events" /%}

Click **View Change Failures** to open a side panel with the list of deployment events marked as change failures.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/change_failures_list.2c4e0bb64ebe91b8a6ee11b94f687ec9.png?auto=format"
   alt="The Failures Breakdown displaying a breakdown of metrics and a list of related events" /%}

## Use DORA Metrics data{% #use-dora-metrics-data %}

### Export DORA Metrics widgets{% #export-dora-metrics-widgets %}

Export your visualization widgets to dashboards, notebooks, or add them to existing incidents.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/dora_ui_2.65615d376171c9c13d717c88c53ecdeb.png?auto=format"
   alt="Click the Export icon to add the visualization widget to an incident or to a dashboard or notebook" /%}

Click the **Export** icon on any visualization to add it to an incident, dashboard, or notebook. For more information about the metrics calculated by DORA Metrics, see the [Data Collected documentation](https://docs.datadoghq.com/dora_metrics/data_collected/).

### Create custom dashboards{% #create-custom-dashboards %}

DORA metrics are highly flexible and can be used in custom dashboards to fit your team's specific needs.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/dashboard.fd2b15cbda0b270cbd1f74a5ddb1eb6c.png?auto=format"
   alt="An example of a custom DORA Metrics Dashboard" /%}

Within dashboards and graphs, custom tags are treated as [attributes](https://docs.datadoghq.com/dashboards/guide/quick-graphs/#graphing-events). To filter or group by a custom tag, it must be prefixed with an `@` symbol.

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/graph_with_custom_tag.405358f27d3a4ed20068046c3c89f682.png?auto=format"
   alt="An example of a custom DORA Metrics graph grouped by a custom tag" /%}

## Further Reading{% #further-reading %}

- [Learn how Datadog calculates DORA metrics](https://docs.datadoghq.com/dora_metrics/calculation/)
- [Check out the latest Software Delivery releases! (App login required)](https://app.datadoghq.com/release-notes?category=Software%20Delivery)
- [Best practices for using DORA metrics to improve software delivery](https://www.datadoghq.com/blog/dora-metrics-software-delivery/)
- [3 ways to drive software delivery success with Datadog DORA Metrics](https://www.datadoghq.com/blog/datadog-dora-metrics/)
- [Learn about Deployment Visibility](https://docs.datadoghq.com/continuous_delivery/deployments)
- [Learn about Event Management](https://docs.datadoghq.com/events)
- [Learn about Metric Monitors](https://docs.datadoghq.com/monitors/types/metric)
- [Learn about the Software Catalog](https://docs.datadoghq.com/software_catalog)
