# Source: https://docs.datadoghq.com/continuous_integration/pipelines/codefresh.md

---
title: Codefresh Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  Codefresh Setup for CI Visibility
---

# Codefresh Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[Codefresh](https://codefresh.io/) is a continuous integration and delivery platform built for Kubernetes which offers automation features that streamline the building, testing, and deploying of your applications.

Set up CI Visibility for Codefresh to collect data on each step of your pipelines, analyze performance bottlenecks, troubleshoot operational challenges, and monitor your deployment workflows.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                            | Partial pipelines                   | View partially retried pipeline executions.                                                                                                                                |
| [Manual steps](https://docs.datadoghq.com/glossary/#manual-step)                                                                                 | Manual steps                        | View manually triggered pipelines.                                                                                                                                         |
| [Parameters](https://docs.datadoghq.com/glossary/#parameter)                                                                                     | Parameters                          | Set custom parameters (for example, [Codefresh variables](https://codefresh.io/docs/docs/codefresh-yaml/variables/#user-provided-variables)) when a pipeline is triggered. |
| [Pipeline failure reasons](https://docs.datadoghq.com/glossary/#pipeline-failure)                                                                | Pipeline failure reasons            | Identify pipeline failure reasons from error messages.                                                                                                                     |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                                                                                       |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                                                                                                                  |

## Configure the Datadog integration{% #configure-the-datadog-integration %}

To set up the Datadog integration for [Codefresh](https://codefresh.io/):

1. Go to **[Account Settings > Configuration > Integrations](https://g.codefresh.io/account-admin/account-conf/integration/datadog)** in Codefresh and click **Configure** on the Datadog row.
1. Click **Add Integration**.
1. Fill the form with the following information:
   - **Datadog site**: Select `` from the dropdown.
   - **Token**: Add your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
1. Click **Save** to save the integration.

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

The [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages populate with data after the pipelines finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
