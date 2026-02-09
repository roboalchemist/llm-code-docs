# Source: https://docs.datadoghq.com/continuous_integration/pipelines/custom.md

---
title: Send Custom Pipelines to Datadog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  Send Custom Pipelines to Datadog
---

# Send Custom Pipelines to Datadog

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

If your CI provider is not supported, you can send custom pipelines through HTTP using the [public API endpoint](https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/#send-pipeline-event). For more information about how pipeline executions are modeled, see [Pipeline Data Model and Execution Types](https://docs.datadoghq.com/continuous_integration/guides/pipeline_data_model/).

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Running pipelines](https://docs.datadoghq.com/glossary/#running-pipeline)                                                                       | Running pipelines                   | View pipeline executions that are running.                                                                                                        |
| [Custom tags](https://docs.datadoghq.com/glossary/#custom-tag) [and measures at runtime](https://docs.datadoghq.com/glossary/#custom-measure)    | Custom tags and measures at runtime | Configure [custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/?tab=linux) at runtime. |
| [Manual steps](https://docs.datadoghq.com/glossary/#manual-step)                                                                                 | Manual steps                        | View manually triggered pipelines.                                                                                                                |
| [Parameters](https://docs.datadoghq.com/glossary/#parameter)                                                                                     | Parameters                          | Set custom parameters when a pipeline is triggered.                                                                                               |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                            | Partial pipelines                   | View partially retried pipeline executions.                                                                                                       |
| [Pipeline failure reasons](https://docs.datadoghq.com/glossary/#pipeline-failure)                                                                | Pipeline failure reasons            | Identify pipeline failure reasons from error messages.                                                                                            |
| [Queue time](https://docs.datadoghq.com/glossary/#queue-time)                                                                                    | Queue time                          | View the amount of time pipeline jobs sit in the queue before processing.                                                                         |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                                                              |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                                                                                         |

## Configure CI Visibility{% #configure-ci-visibility %}

To send pipeline events programmatically to Datadog, ensure that your [`DD_API_KEY`](https://app.datadoghq.com/organization-settings/api-keys) is configured.

1. Set the headers of your HTTP request:

   - `DD-API-KEY`: Your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
   - `Content-Type`: `application/json`.

1. Prepare the payload body by entering information about the [pipeline execution](https://docs.datadoghq.com/continuous_integration/guides/pipeline_data_model/) in a cURL command:

| Parameter Name | Description                                                                                                                                                                                          | Example Value                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Unique ID      | The UUID of the pipeline run. The ID has to be unique across retries and pipelines, including partial retries.                                                                                       | `b3262537-a573-44eb-b777-4c0f37912b05`               |
| Name           | The name of the pipeline. All pipeline runs for the builds should have the same name.                                                                                                                | `Documentation Build`                                |
| Git Repository | The Git repository URL that triggered the pipeline.                                                                                                                                                  | `https://github.com/Datadog/documentation`           |
| Commit Author  | The commit author email that triggered the pipeline.                                                                                                                                                 | `contributor@github.com`                             |
| Commit SHA     | The commit hash that triggered the pipeline.                                                                                                                                                         | `cf852e17dea14008ac83036430843a1c`                   |
| Status         | The final status of the pipeline. Allowed enum values: `success`, `error`, `canceled`, `skipped`, `blocked`, or `running`.                                                                           | `success`                                            |
| Partial Retry  | Whether or not the pipeline was a partial retry of a previous attempt. This field expects a boolean value (`true` or `false`). A partial retry is one which only runs a subset of the original jobs. | `false`                                              |
| Start          | Time when the pipeline run started (it should not include any [queue time](https://docs.datadoghq.com/glossary/#queue-time)). The time format must be RFC3339.                                       | `2024-08-22T11:36:29-07:00`                          |
| End            | Time when the pipeline run finished. The time format must be RFC3339. The end time cannot be longer than 1 year after the start time.                                                                | `2024-08-22T14:36:00-07:00`                          |
| URL            | The URL to look at the pipeline in the CI provider UI.                                                                                                                                               | `http://your-ci-provider.com/pipeline/{pipeline-id}` |

For example, this payload sends a CI pipeline event to Datadog:

   ```bash
      curl -X POST "https://api.datadoghq.com/api/v2/ci/pipeline" \
      -H "Content-Type: application/json" \
      -H "DD-API-KEY: <YOUR_API_KEY>" \
      -d @- << EOF
      {
        "data": {
          "attributes": {
            "provider_name": "<YOUR_CI_PROVIDER>",
            "resource": {
              "level": "pipeline",
              "unique_id": "b3262537-a573-44eb-b777-4c0f37912b05",
              "name": "Documentation Build",
              "git": {
                "repository_url": "https://github.com/Datadog/documentation",
                "author_email": "contributor@github.com",
                "sha": "cf852e17dea14008ac83036430843a1c"
              },
              "status": "success",
              "start": "2024-08-22T11:36:29-07:00",
              "end": "2024-08-22T14:36:00-07:00",
              "partial_retry": false,
              "url": ""
            }
          },
          "type": "cipipeline_resource_request"
        }
      }
      EOF
      
```

1. After sending your pipeline event to Datadog, you can integrate additional event types such as `stage`, `job`, and `step`. For more information, see the [Send Pipeline Event endpoint](https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/#send-pipeline-event).

## Running pipelines{% #running-pipelines %}

Pipeline events sent with the `status` set to `running` have the same `unique_id` as the final pipeline event. Running pipelines can be updated by adding more information while they are still running. A running pipeline consists of the following events:

1. The initial running pipeline event with the `status` set to `running`.
1. Optionally, `N` running pipeline events that update the pipeline with more information, with the same `unique_id` and the `status` set to `running`.
1. The final pipeline event **without** a `running` status and the same `unique_id`.

**Note**: The most recent value may not always be the one displayed in the UI when a field is updated. For example, if the tag `my_tag` is set to `value1` in the first running pipeline, and then is updated to `value2`, you may see `value1` instead of `value2` in the UI. It is recommended to only update running pipelines by adding more fields instead modifying existing ones.

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

The [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages populate with data after the pipelines are accepted for processing.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Learn about the Pipeline Data Model and Execution Types](https://docs.datadoghq.com/continuous_integration/guides/pipeline_data_model)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
