# Source: https://docs.datadoghq.com/continuous_integration/pipelines/circleci.md

---
title: CircleCI Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  CircleCI Setup for CI Visibility
source_url: https://docs.datadoghq.com/pipelines/circleci/index.html
---

# CircleCI Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[CircleCI](https://circleci.com/) is a continuous integration and delivery platform that enables teams to build, test, and deploy software at scale.

Set up CI Visibility for CircleCI to optimize the performance of your pipelines, improve collaboration across teams, and ensure consistent, compliant build processes.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                            | Partial pipelines                   | View partially retried pipeline executions.                                                                                                                            |
| Logs correlation                                                                                                                                 | Logs correlation                    | Correlate pipeline and job spans to logs and enable [job log collection](https://docs.datadoghq.com/continuous_integration/pipelines/circleci/#enable-log-collection). |
| [Custom spans](https://docs.datadoghq.com/glossary/#custom-span)                                                                                 | Custom spans                        | Configure custom spans for your pipelines.                                                                                                                             |
| Custom pre-defined tags                                                                                                                          | Custom pre-defined tags             | Set [custom tags](https://docs.datadoghq.com/continuous_integration/pipelines/circleci/#set-custom-tags) to all generated pipeline and job spans.                      |
| [Custom tags](https://docs.datadoghq.com/glossary/#custom-tag) [and measures at runtime](https://docs.datadoghq.com/glossary/#custom-measure)    | Custom tags and measures at runtime | Configure [custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/?tab=linux) at runtime.                      |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                                                                                   |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                                                                                                              |

### Terminology{% #terminology %}

This table shows the mapping of concepts between Datadog CI Visibility and CircleCI:

| Datadog                    | CircleCI |
| -------------------------- | -------- |
| Pipeline                   | Workflow |
| Job                        | Job      |
| *Not available in Datadog* | Step     |

## Configure the Datadog integration{% #configure-the-datadog-integration %}

The Datadog integration for [CircleCI](https://circleci.com/) works by using [webhooks](https://circleci.com/docs/2.0/webhooks) to send data to Datadog.

1. For each project, go to **Project Settings > Webhooks** in CircleCI and add a new webhook:

   - **Webhook Name**: `Datadog CI Visibility` or any other identifier name that you want to provide.
   - **Receiver URL**: `https://webhook-intake.  /api/v2/webhook/?dd-api-key=<API_KEY>` where `<API_KEY>` is your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
   - **Certificate verifications**: Enable this check.
   - **Events**: Select `Workflow Completed` and `Job Completed`.

1. Click **Add Webhook** to save the new webhook.

## Advanced configuration{% #advanced-configuration %}

### Configure multiple projects in bulk{% #configure-multiple-projects-in-bulk %}

Datadog offers a [script](https://raw.githubusercontent.com/DataDog/ci-visibility-circle-ci/main/service_hooks.py) to help you enable service hooks across multiple or all of your CircleCI projects using the CircleCI API. The script requires Python 3 and the `requests` package.

To run this script, you need:

- Your Datadog API key
- A CircleCI personal API token

For more information, you can run the following command:

```shell
./service_hooks.py --help
```

To bulk configure hooks for your projects:

1. Log in to your CircleCI account and follow all the projects you want to enable the hooks. Optionally, use the **Follow All** button on the Projects page.

1. Run the script by using environment variables `DD_API_KEY` and `DD_SITE`, or passing in flag parameters `--dd-api-key` and `--dd-site`:

For example:

   ```shell
   ./service_hooks.py \
       --dd-api-key <DD_API_KEY> \
       --circle-token <CIRCLECI_TOKEN> \
       --dd-site <YOUR_DATADOG_SITE> \
       --threads 4
   ```

### Set custom tags{% #set-custom-tags %}

To set custom tags to all the pipeline and job spans generated by the integration, add to the **Receiver URL** a URL-encoded query parameter `tags` with `key:value` pairs separated by commas.

If a `key:value` pair contains any commas, surround it with quotes. For example, to add `key1:value1,"key2: value with , comma",key3:value3`, the following string would need to be appended to the **Receiver URL**: `?tags=key1%3Avalue1%2C%22key2%3A+value+with+%2C+comma%22%2Ckey3%3Avalue3`.

#### Integrate with Datadog Teams{% #integrate-with-datadog-teams %}

To display and filter the teams associated with your pipelines, add `team:<your-team>` as a custom tag. The custom tag name must match your [Datadog Teams](https://docs.datadoghq.com/account_management/teams/) team handle exactly.

### Collect job logs{% #collect-job-logs %}

The Datadog CircleCI integration collects logs from your finished CircleCI jobs and forwards them to Datadog. To install and configure this integration, see the [CircleCI integration documentation](https://docs.datadoghq.com/integrations/circleci/#setup).

Logs are billed separately from CI Visibility. Log retention, exclusion, and indexes are configured in [Log Management](https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/). Logs for CircleCI jobs can be identified by the `datadog.product:cipipeline` and `source:circleci` tags.

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

The [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages populate with data after the workflows finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Extend Pipeline Visibility by tracing individual commands](https://docs.datadoghq.com/continuous_integration/pipelines/custom_commands/)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
- [Extend Pipeline Visibility by adding custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/)
