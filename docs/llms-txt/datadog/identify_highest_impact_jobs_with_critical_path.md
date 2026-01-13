# Source: https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path.md

---
title: Identify CI Jobs on the Critical Path to Reduce the Pipeline Duration
description: >-
  Learn how to identify CI jobs that are on the critical path to improve the
  duration of your CI pipelines.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Visibility Guides > Identify CI
  Jobs on the Critical Path to Reduce the Pipeline Duration
source_url: >-
  https://docs.datadoghq.com/guides/identify_highest_impact_jobs_with_critical_path/index.html
---

# Identify CI Jobs on the Critical Path to Reduce the Pipeline Duration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

This guide explains how to identify the CI jobs that are on the critical path to help you determine which jobs to prioritize in order to reduce the overall duration of the CI pipelines.

### Understanding the critical path in a CI pipeline{% #understanding-the-critical-path-in-a-ci-pipeline %}

The critical path of a CI pipeline execution is the longest sequence of CI jobs that determines the total duration of that pipeline execution. Essentially, it is the path through the dependency graph of CI jobs that takes the most time to complete. To reduce the total duration of a CI pipeline execution, you need to shorten the duration of CI jobs along this critical path.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/critical_path_highlight_pipeline.ca3ff985dc8384978c09fe57a1e0e983.png?auto=format"
   alt="Highlight of jobs on the critical path in a pipeline execution." /%}

Looking at the job duration may not be enough. CI jobs are typically executed in parallel with other jobs, which means the reduction of the pipeline execution time is determined by reducing the **exclusive time** of the CI job.

The exclusive time of a job on the critical path represents the amount of time the CI runner has spent executing a specific job, excluding the execution time of other jobs that were running in parallel.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/critical_path_highlight_pipeline_exclusive_time.cc2b9f0e846532f8a2ad629858a0a8bf.png?auto=format"
   alt="Highlight exclusive time of the jobs on the critical path in a pipeline execution." /%}

If a CI job `job1` is on the critical path with a duration of 100ms and runs in parallel with a CI job `job2`, which has a duration of 80ms, the exclusive time of `job1` on the critical path is 20ms. This means that reducing the duration of the `job1` by more than 20ms would still only decrease the overall pipeline duration by 20ms.

## Identify the key CI jobs to improve your CI pipeline{% #identify-the-key-ci-jobs-to-improve-your-ci-pipeline %}

### Using the facet{% #using-the-facet %}

You can use the facet `@ci.on_critical_path` or `@ci.critical_path.exclusive_time` to identify which CI jobs are on the critical path in your CI pipelines. Using those facets, you can create custom dashboards and notebooks for your needs.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/critical_path_facets.cd51c107daf849371453f4556b573feb.png?auto=format"
   alt="Filter using critical path facets" /%}

Notice that these facets are only available using the `ci_level:job` in your queries.

### Using the dashboard template{% #using-the-dashboard-template %}

You can also import the [CI Visibility - Critical Path](https://docs.datadoghq.com/resources/json/civisibility-critical-path-dashboard.json) dashboard template:

- Open the [civisibility-critical-path-dashboard.json](https://docs.datadoghq.com/resources/json/civisibility-critical-path-dashboard.json) dashboard template and copy the content in the clipboard.
- Create a [New Dashboard](https://docs.datadoghq.com/dashboards/) in Datadog.
- Paste the copied content in the new dashboard.
- Save the dashboard.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/critical_path_dashboard.f3173509fbf0a17bd1795718fddee44d.png?auto=format"
   alt="Critical path dashboard for CI Visibility" /%}

#### Terminology{% #terminology %}

| Column                                | Description                                                                                                                                                          |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Total Exclusive Time On Critical Path | Sum of all exclusive time of the job. It estimates the potential time savings for the pipelines involved.                                                            |
| Avg Exclusive Time On Critical Path   | Average exclusive time of a particular job on the critical path. This measures the potential reduction of a pipeline duration if the job reduces its exclusive time. |
| Rate On Critical Path                 | Measures how often a job is on the critical path.                                                                                                                    |

##### Example{% #example %}

In the previous image, we can observe that a CI job called `metrics` is a potential candidate for improvement, as its total exclusive time is the highest. The average exclusive time is around 21 minutes, meaning there is room for improvement of up to 21 minutes for this CI job.

Since we know this CI job is on the critical path 43.5% of the time, we could potentially reduce the average pipeline duration by up to 21 minutes for 43.5% of the pipeline executions.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/critical_path_dashboard_outlier_job_highlighted.99dc10306302143f37b15edd633dea3f.png?auto=format"
   alt="Potential CI Job candidate to improve the exclusive time." /%}

## Further reading{% #further-reading %}

- [Learn how to search and manage your pipeline executions](https://docs.datadoghq.com/continuous_integration/search/#pipeline-details-and-executions)
- [Highlight critical path in your Pipeline Execution](https://docs.datadoghq.com/continuous_integration/search/#highlight-critical-path)
