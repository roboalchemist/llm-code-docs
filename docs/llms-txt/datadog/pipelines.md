# Source: https://docs.datadoghq.com/continuous_integration/pipelines.md

---
title: CI Pipeline Visibility in Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog
source_url: https://docs.datadoghq.com/pipelines/index.html
---

# CI Pipeline Visibility in Datadog

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[CI Visibility](https://app.datadoghq.com/ci/pipelines) provides a pipeline-first view into your CI health by displaying important metrics and results from your pipelines. It helps you troubleshoot pipeline failures, address performance bottlenecks, and track CI performance and reliability over time.

## Setup{% #setup %}

Select your CI provider to set up CI Visibility in Datadog:



- [aws codepipeline](https://docs.datadoghq.com/continuous_integration/pipelines/awscodepipeline/)
- [azure devops extension](https://docs.datadoghq.com/continuous_integration/pipelines/azure/)
- [buildkite](https://docs.datadoghq.com/continuous_integration/pipelines/buildkite/)
- [circleci orb](https://docs.datadoghq.com/continuous_integration/pipelines/circleci/)
- [codefresh](https://docs.datadoghq.com/continuous_integration/pipelines/codefresh/)
- [github actions](https://docs.datadoghq.com/continuous_integration/pipelines/github/)
- [gitlab](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/)
- [jenkins](https://docs.datadoghq.com/continuous_integration/pipelines/jenkins/)
- [teamcity](https://docs.datadoghq.com/continuous_integration/pipelines/teamcity/)
- [other ci providers](https://docs.datadoghq.com/continuous_integration/pipelines/custom/)



- [Custom Commands](https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands)
- [Custom Tags and Measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures)

## Supported features{% #supported-features %}

### Pipeline visibility and execution{% #pipeline-visibility-and-execution %}

|                                                                                                                                                                                                                                         | AWS CodePipeline | Azure Pipelines | Buildkite                     | CircleCI | Codefresh | GitHub Actions | GitLab | Jenkins | TeamCity | Other CI Providers |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------- | ----------------------------- | -------- | --------- | -------------- | ------ | ------- | -------- | ------------------ |
| {% collapsible-section style="margin-bottom:0" %}
  Logs collection: Retrieval of pipeline or job logs from the CI provider. Logs are displayed on the **Logs** tab in the Pipeline Execution view.
    {% /collapsible-section %}      | yes              | yes             | yes                           | yes      | yes       | yes            |
| {% collapsible-section style="margin-bottom:0" %}
  Infrastructure correlation: Correlation of host-level information for the Datadog Agent, CI pipelines, or job runners to CI pipeline execution data.
    {% /collapsible-section %} | yes              | yes             | yes                           | yes      |
| {% collapsible-section style="margin-bottom:0" %}
  Running pipelines: Identification of pipelines executions that are running with associated tracing.
    {% /collapsible-section %}                                                  | yes              | yes             | yes                           | yes      | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Partial retries: Identification of partial retries (for example, when only a subset of jobs were retried).
    {% /collapsible-section %}                                           | yes              | yes             | yes                           | yes      | yes       | yes            | yes    | yes     |
| {% collapsible-section style="margin-bottom:0" %}
  Step granularity: Step level spans are available for more granular visibility.
    {% /collapsible-section %}                                                                       | yes              | yes             | yes(*Presented as job spans*) | yes      |
| {% collapsible-section style="margin-bottom:0" %}
  Manual steps: Identification of when there is a job with a manual approval phase in the overall pipeline.
    {% /collapsible-section %}                                            | yes              | yes             | yes                           | yes      | yes       | yes            | yes    | yes     |

### Automatic analysis{% #automatic-analysis %}

|                                                                                                                                                                                                                                                                                                   | AWS CodePipeline | Azure Pipelines | Buildkite | CircleCI | Codefresh | GitHub Actions | GitLab | Jenkins | TeamCity | Other CI Providers |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------- | --------- | -------- | --------- | -------------- | ------ | ------- | -------- | ------------------ |
| {% collapsible-section style="margin-bottom:0" %}
  Job failure analysis: Uses LLM models on relevant logs to analyze the root cause of failed CI jobs. [More info](https://docs.datadoghq.com/continuous_integration/guides/use_ci_jobs_failure_analysis/).
    {% /collapsible-section %}       | yes              | yes             | yes       |
| {% collapsible-section style="margin-bottom:0" %}
  Critical path: Identification of CI jobs that are on the critical path of the pipeline. [More info](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/)
    {% /collapsible-section %} | yes              | yes             | yes       | yes      | yes       | yes            | yes    | yes     | yes      | yes                |

### Duration breakdown{% #duration-breakdown %}

|                                                                                                                                                                                 | AWS CodePipeline | Azure Pipelines | Buildkite | CircleCI | Codefresh | GitHub Actions | GitLab | Jenkins | TeamCity | Other CI Providers |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------- | --------- | -------- | --------- | -------------- | ------ | ------- | -------- | ------------------ |
| {% collapsible-section style="margin-bottom:0" %}
  Execution time: Time for which a pipeline has been actively running jobs.
    {% /collapsible-section %}                    | yes              | yes             | yes       | yes      | yes       | yes            | yes    | yes     | yes      | yes                |
| {% collapsible-section style="margin-bottom:0" %}
  Queue time: Time for which a pipeline or job was in the queue before execution.
    {% /collapsible-section %}              | yes              | yes             | yes       | yes      | yes       | yes            | yes    |
| {% collapsible-section style="margin-bottom:0" %}
  Approval wait time: Time for which a pipeline or job has been waiting for a manual approval.
    {% /collapsible-section %} | yes              | yes             | yes       | yes      |

### Customization and extensibility{% #customization-and-extensibility %}

|                                                                                                                                                                                                                                                                                                                                                                                                                   | AWS CodePipeline | Azure Pipelines | Buildkite | CircleCI | Codefresh | GitHub Actions | GitLab | Jenkins | TeamCity | Other CI Providers |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------- | --------- | -------- | --------- | -------------- | ------ | ------- | -------- | ------------------ |
| {% collapsible-section style="margin-bottom:0" %}
  Custom commands: Support for using datadog-ci to send command-level events to CI Visibility to be incorporated into pipeline waterfall visualization. You can then query and analyze [these events](https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands/).
    {% /collapsible-section %}                                             | yes              | yes             | yes       | yes      | yes       | yes            | yes    |
| {% collapsible-section style="margin-bottom:0" %}
  Static tags: Support for setting static pipeline tags in the CI provider that do not change between executions.
    {% /collapsible-section %}                                                                                                                                                                                                                | yes              | yes             | yes       | yes      |
| {% collapsible-section style="margin-bottom:0" %}
  Runtime tags: Support for adding [user-defined text and numerical tags](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/) to pipelines and jobs in CI Visibility.
    {% /collapsible-section %}                                                                                                                         | yes              | yes             | yes       | yes      | yes       | yes            | yes    |
| {% collapsible-section style="margin-bottom:0" %}
  Parameters: Support for adding custom pipeline parameters that users set (for example, `DYNAMICS_IS_CHILD:true`). You can then search using these parameters in the [CI Visibility Explorer](https://docs.datadoghq.com/continuous_integration/explorer/?tab=pipelineexecutions) to find all events with a specific parameter.
    {% /collapsible-section %} | yes              | yes             | yes       | yes      |

## Use CI pipelines data{% #use-ci-pipelines-data %}

When creating a [dashboard](https://app.datadoghq.com/dashboard/lists) or a [notebook](https://app.datadoghq.com/notebook/list), you can use CI pipeline data in your search query, which updates the visualization widget options. For more information, see the [Dashboards](https://docs.datadoghq.com/dashboards) and [Notebooks documentation](https://docs.datadoghq.com/notebooks).

## Alert on pipeline data{% #alert-on-pipeline-data %}

You can export your search query to a [CI Pipeline monitor](https://docs.datadoghq.com/monitors/types/ci) on the [**Executions** page](https://app.datadoghq.com/ci/pipeline-executions) or the [**Test Runs** page](https://app.datadoghq.com/ci/test-runs) by clicking the **Export** button.

## Further reading{% #further-reading %}

- [Creating CI Pipeline Monitors](https://docs.datadoghq.com/monitors/types/ci/)
- [Learning about CI Visibility Billing](https://docs.datadoghq.com/account_management/billing/ci_visibility)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
