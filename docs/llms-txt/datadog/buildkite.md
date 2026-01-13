# Source: https://docs.datadoghq.com/continuous_integration/pipelines/buildkite.md

---
title: Buildkite Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  Buildkite Setup for CI Visibility
source_url: https://docs.datadoghq.com/pipelines/buildkite/index.html
---

# Buildkite Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[Buildkite](https://buildkite.com) is a continuous integration and deployment platform that allows you to run builds on your own infrastructure, providing you with full control over security and customizing your build environment while managing orchestration in the cloud.

Set up CI Visibility for Buildkite to optimize your resource usage, reduce overhead, and improve the speed and quality of your software development lifecycle.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                            | Partial pipelines                   | View partially retried pipeline executions.                                                                                                                            |
| Infrastructure metric correlation                                                                                                                | Infrastructure metric correlation   | Correlate jobs to [infrastructure host metrics](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/?tab=linux) for Buildkite agents. |
| [Manual steps](https://docs.datadoghq.com/glossary/#manual-step)                                                                                 | Manual steps                        | View manually triggered pipelines.                                                                                                                                     |
| [Queue time](https://docs.datadoghq.com/glossary/#queue-time)                                                                                    | Queue time                          | View the amount of time pipeline jobs sit in the queue before processing.                                                                                              |
| [Custom tags](https://docs.datadoghq.com/glossary/#custom-tag) [and measures at runtime](https://docs.datadoghq.com/glossary/#custom-measure)    | Custom tags and measures at runtime | Configure [custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/?tab=linux) at runtime.                      |
| [Custom spans](https://docs.datadoghq.com/glossary/#custom-span)                                                                                 | Custom spans                        | Configure custom spans for your pipelines.                                                                                                                             |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                                                                                   |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                                                                                                              |

### Terminology{% #terminology %}

This table shows the mapping of concepts between Datadog CI Visibility and Buildkite:

| Datadog  | Buildkite                       |
| -------- | ------------------------------- |
| Pipeline | Build (execution of a pipeline) |
| Job      | Job (execution of a step)       |

## Configure the Datadog integration{% #configure-the-datadog-integration %}

To set up the Datadog integration for [Buildkite](https://buildkite.com):

1. Go to **Settings > Notification Services** in Buildkite and click the **Add** button next to **Datadog Pipeline Visibility**.
1. Fill in the form with the following information:
   - **Description**: A description to help identify the integration in the future, such as `Datadog CI Visibility integration`.
   - **API key**: Your [Datadog API Key](https://app.datadoghq.com/organization-settings/api-keys).
   - **Datadog site**: ``
   - **Pipelines**: Select all pipelines or the subset of pipelines you want to trace.
   - **Branch filtering**: Leave empty to trace all branches or select the subset of branches you want to trace.
1. Click **Add Datadog Pipeline Visibility Notification** to save the integration.

## Advanced configuration{% #advanced-configuration %}

### Set custom tags{% #set-custom-tags %}

Custom tags can be added to Buildkite traces by using the `buildkite-agent meta-data set` command. Any metadata tags with a key starting with `dd_tags.` are added to the job and pipeline spans. These tags can be used to create string facets to search and organize the pipelines.

The YAML below illustrates a simple pipeline where tags for the team name and the Go version have been set.

```yaml
steps:
  - command: buildkite-agent meta-data set "dd_tags.team" "backend"
  - command: go version | buildkite-agent meta-data set "dd_tags.go.version"
    label: Go version
  - commands: go test ./...
    label: Run tests
```

The following tags are shown in the root span as well as the relevant job span in Datadog.

- `team: backend`
- `go.version: go version go1.17 darwin/amd64` (output depends on the runner)

The resulting pipeline looks like the following:

{% image
   source="https://datadog-docs.imgix.net/images/ci/buildkite-custom-tags.9f5cb09665c2965325b42ddd57ecd3f3.png?auto=format"
   alt="Buildkite pipeline trace with custom tags" /%}

Any metadata with a key starting with `dd-measures.` and containing a numerical value will be set as a metric tag that can be used to create numerical measures.

You can use the `buildkite-agent meta-data set` command to create these tags.

For example, you can measure the binary size in a pipeline with this command:

```yaml
steps:
  - commands:
    - go build -o dst/binary .
    - ls -l dst/binary | awk '{print \$5}' | tr -d '\n' | buildkite-agent meta-data set "dd_measures.binary_size"
    label: Go build
```

The resulting pipeline will have the tags shown below in the pipeline span:

- `binary_size: 502` (output depends on the file size)

In this example, you can use the value of `binary_size` to plot the change in the binary size over time.

### Correlate infrastructure metrics to jobs{% #correlate-infrastructure-metrics-to-jobs %}

If you are using Buildkite agents, you can correlate jobs with the infrastructure that is running them. For this feature to work, install the [Datadog Agent](https://docs.datadoghq.com/agent/) in the hosts running the Buildkite agents.

## View partial and downstream pipelines{% #view-partial-and-downstream-pipelines %}

You can use the following filters to customize your search query in the [CI Visibility Explorer](https://docs.datadoghq.com/continuous_integration/explorer).

{% image
   source="https://datadog-docs.imgix.net/images/ci/partial_retries_search_tags.528805ecdfa4cad926a8b38cefb12613.png?auto=format"
   alt="The Pipeline executions page with Partial Pipeline:retry entered in the search query" /%}

| Facet Name          | Facet ID                  | Possible Values              |
| ------------------- | ------------------------- | ---------------------------- |
| Downstream Pipeline | `@ci.pipeline.downstream` | `true`, `false`              |
| Manually Triggered  | `@ci.is_manual`           | `true`, `false`              |
| Partial Pipeline    | `@ci.partial_pipeline`    | `retry`, `paused`, `resumed` |

You can also apply these filters using the facet panel on the left hand side of the page.

{% image
   source="https://datadog-docs.imgix.net/images/ci/partial_retries_facet_panel.16cb1d85c4e6200cc538e3be7a459c29.png?auto=format"
   alt="The facet panel with Partial Pipeline facet expanded and the value Retry selected, the Partial Retry facet expanded and the value true selected" /%}

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

The [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages populate with data after the pipelines finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
- [Extend Pipeline Visibility by adding custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/)
