# Source: https://docs.datadoghq.com/api/latest/ci-visibility-pipelines.md

---
title: CI Visibility Pipelines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > CI Visibility Pipelines
---

# CI Visibility Pipelines

Search or aggregate your CI Visibility pipeline events and send them to your Datadog site over HTTP. See the [CI Pipeline Visibility in Datadog page](https://docs.datadoghq.com/continuous_integration/pipelines/) for more information.

## Send pipeline event{% #send-pipeline-event %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                          |
| ----------------- | ----------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/ci/pipeline |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/ci/pipeline |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/ci/pipeline      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/ci/pipeline      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/ci/pipeline     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/ci/pipeline |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/ci/pipeline |

### Overview



Send your pipeline event to your Datadog platform over HTTP. For details about how pipeline executions are modeled and what execution types we support, see [Pipeline Data Model And Execution Types](https://docs.datadoghq.com/continuous_integration/guides/pipeline_data_model/).

Multiple events can be sent in an array (up to 1000).

Pipeline events can be submitted with a timestamp that is up to 18 hours in the past. The duration between the event start and end times cannot exceed 1 year.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field         | Field                                | Type          | Description                                                                                                                                                                                             |
| -------------------- | ------------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                      | data                                 |  <oneOf> | Data of the pipeline events to create.                                                                                                                                                                  |
| data                 | Option 1                             | object        | Data of the pipeline event to create.                                                                                                                                                                   |
| Option 1             | attributes                           | object        | Attributes of the pipeline event to create.                                                                                                                                                             |
| attributes           | env                                  | string        | The Datadog environment.                                                                                                                                                                                |
| attributes           | provider_name                        | string        | The name of the CI provider. By default, this is "custom".                                                                                                                                              |
| attributes           | resource [*required*]           |  <oneOf> | Details of the CI pipeline event.                                                                                                                                                                       |
| resource             | Option 1                             |  <oneOf> | Details of the top level pipeline, build, or workflow of your CI.                                                                                                                                       |
| Option 1             | Option 1                             | object        | Details of a finished pipeline.                                                                                                                                                                         |
| Option 1             | end [*required*]                | date-time     | Time when the pipeline run finished. It cannot be older than 18 hours in the past from the current time. The time format must be RFC3339.                                                               |
| Option 1             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 1             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 1             | is_manual                            | boolean       | Whether or not the pipeline was triggered manually by the user.                                                                                                                                         |
| Option 1             | is_resumed                           | boolean       | Whether or not the pipeline was resumed after being blocked.                                                                                                                                            |
| Option 1             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs, and steps. Allowed enum values: `pipeline`                                                                                                         |
| Option 1             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 1             | name [*required*]               | string        | Name of the pipeline. All pipeline runs for the builds should have the same name.                                                                                                                       |
| Option 1             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 1             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 1             | parent_pipeline                      | object        | If the pipeline is triggered as child of another pipeline, this should contain the details of the parent pipeline.                                                                                      |
| parent_pipeline      | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| parent_pipeline      | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 1             | partial_retry [*required*]      | boolean       | Whether or not the pipeline was a partial retry of a previous attempt. A partial retry is one which only runs a subset of the original jobs.                                                            |
| Option 1             | pipeline_id                          | string        | Any ID used in the provider to identify the pipeline run even if it is not unique across retries. If the `pipeline_id` is unique, then both `unique_id` and `pipeline_id` can be set to the same value. |
| Option 1             | previous_attempt                     | object        | If the pipeline is a retry, this should contain the details of the previous attempt.                                                                                                                    |
| previous_attempt     | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| previous_attempt     | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 1             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 1             | start [*required*]              | date-time     | Time when the pipeline run started (it should not include any queue time). The time format must be RFC3339.                                                                                             |
| Option 1             | status [*required*]             | enum          | The final status of the pipeline. Allowed enum values: `success,error,canceled,skipped,blocked`                                                                                                         |
| Option 1             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 1             | unique_id [*required*]          | string        | UUID of the pipeline run. The ID has to be unique across retries and pipelines, including partial retries.                                                                                              |
| Option 1             | url [*required*]                | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 1             | Option 2                             | object        | Details of a running pipeline.                                                                                                                                                                          |
| Option 2             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 2             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 2             | is_manual                            | boolean       | Whether or not the pipeline was triggered manually by the user.                                                                                                                                         |
| Option 2             | is_resumed                           | boolean       | Whether or not the pipeline was resumed after being blocked.                                                                                                                                            |
| Option 2             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs, and steps. Allowed enum values: `pipeline`                                                                                                         |
| Option 2             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 2             | name [*required*]               | string        | Name of the pipeline. All pipeline runs for the builds should have the same name.                                                                                                                       |
| Option 2             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 2             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 2             | parent_pipeline                      | object        | If the pipeline is triggered as child of another pipeline, this should contain the details of the parent pipeline.                                                                                      |
| parent_pipeline      | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| parent_pipeline      | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 2             | partial_retry [*required*]      | boolean       | Whether or not the pipeline was a partial retry of a previous attempt. A partial retry is one which only runs a subset of the original jobs.                                                            |
| Option 2             | pipeline_id                          | string        | Any ID used in the provider to identify the pipeline run even if it is not unique across retries. If the `pipeline_id` is unique, then both `unique_id` and `pipeline_id` can be set to the same value. |
| Option 2             | previous_attempt                     | object        | If the pipeline is a retry, this should contain the details of the previous attempt.                                                                                                                    |
| previous_attempt     | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| previous_attempt     | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 2             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 2             | start [*required*]              | date-time     | Time when the pipeline run started (it should not include any queue time). The time format must be RFC3339.                                                                                             |
| Option 2             | status [*required*]             | enum          | The in progress status of the pipeline. Allowed enum values: `running`                                                                                                                                  |
| Option 2             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 2             | unique_id [*required*]          | string        | UUID of the pipeline run. The ID has to be the same as the finished pipeline.                                                                                                                           |
| Option 2             | url [*required*]                | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| resource             | Option 2                             | object        | Details of a CI stage.                                                                                                                                                                                  |
| Option 2             | dependencies                         | [string]      | A list of stage IDs that this stage depends on.                                                                                                                                                         |
| Option 2             | end [*required*]                | date-time     | Time when the stage run finished. The time format must be RFC3339.                                                                                                                                      |
| Option 2             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 2             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 2             | id [*required*]                 | string        | UUID for the stage. It has to be unique at least in the pipeline scope.                                                                                                                                 |
| Option 2             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs and steps. Allowed enum values: `stage`                                                                                                             |
| Option 2             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 2             | name [*required*]               | string        | The name for the stage.                                                                                                                                                                                 |
| Option 2             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 2             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 2             | pipeline_name [*required*]      | string        | The parent pipeline name.                                                                                                                                                                               |
| Option 2             | pipeline_unique_id [*required*] | string        | The parent pipeline UUID.                                                                                                                                                                               |
| Option 2             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 2             | start [*required*]              | date-time     | Time when the stage run started (it should not include any queue time). The time format must be RFC3339.                                                                                                |
| Option 2             | status [*required*]             | enum          | The final status of the stage. Allowed enum values: `success,error,canceled,skipped`                                                                                                                    |
| Option 2             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| resource             | Option 3                             | object        | Details of a CI job.                                                                                                                                                                                    |
| Option 3             | dependencies                         | [string]      | A list of job IDs that this job depends on.                                                                                                                                                             |
| Option 3             | end [*required*]                | date-time     | Time when the job run finished. The time format must be RFC3339.                                                                                                                                        |
| Option 3             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 3             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 3             | id [*required*]                 | string        | The UUID for the job. It has to be unique within each pipeline execution.                                                                                                                               |
| Option 3             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs, and steps. Allowed enum values: `job`                                                                                                              |
| Option 3             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 3             | name [*required*]               | string        | The name for the job.                                                                                                                                                                                   |
| Option 3             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 3             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 3             | pipeline_name [*required*]      | string        | The parent pipeline name.                                                                                                                                                                               |
| Option 3             | pipeline_unique_id [*required*] | string        | The parent pipeline UUID.                                                                                                                                                                               |
| Option 3             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 3             | stage_id                             | string        | The parent stage UUID (if applicable).                                                                                                                                                                  |
| Option 3             | stage_name                           | string        | The parent stage name (if applicable).                                                                                                                                                                  |
| Option 3             | start [*required*]              | date-time     | Time when the job run instance started (it should not include any queue time). The time format must be RFC3339.                                                                                         |
| Option 3             | status [*required*]             | enum          | The final status of the job. Allowed enum values: `success,error,canceled,skipped`                                                                                                                      |
| Option 3             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 3             | url [*required*]                | string        | The URL to look at the job in the CI provider UI.                                                                                                                                                       |
| resource             | Option 4                             | object        | Details of a CI step.                                                                                                                                                                                   |
| Option 4             | end [*required*]                | date-time     | Time when the step run finished. The time format must be RFC3339.                                                                                                                                       |
| Option 4             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 4             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 4             | id [*required*]                 | string        | UUID for the step. It has to be unique within each pipeline execution.                                                                                                                                  |
| Option 4             | job_id                               | string        | The parent job UUID (if applicable).                                                                                                                                                                    |
| Option 4             | job_name                             | string        | The parent job name (if applicable).                                                                                                                                                                    |
| Option 4             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs and steps. Allowed enum values: `step`                                                                                                              |
| Option 4             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 4             | name [*required*]               | string        | The name for the step.                                                                                                                                                                                  |
| Option 4             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 4             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 4             | pipeline_name [*required*]      | string        | The parent pipeline name.                                                                                                                                                                               |
| Option 4             | pipeline_unique_id [*required*] | string        | The parent pipeline UUID.                                                                                                                                                                               |
| Option 4             | stage_id                             | string        | The parent stage UUID (if applicable).                                                                                                                                                                  |
| Option 4             | stage_name                           | string        | The parent stage name (if applicable).                                                                                                                                                                  |
| Option 4             | start [*required*]              | date-time     | Time when the step run started. The time format must be RFC3339.                                                                                                                                        |
| Option 4             | status [*required*]             | enum          | The final status of the step. Allowed enum values: `success,error`                                                                                                                                      |
| Option 4             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 4             | url                                  | string        | The URL to look at the step in the CI provider UI.                                                                                                                                                      |
| attributes           | service                              | string        | If the CI provider is SaaS, use this to differentiate between instances.                                                                                                                                |
| Option 1             | type                                 | enum          | Type of the event. Allowed enum values: `cipipeline_resource_request`                                                                                                                                   |
| data                 | Option 2                             | [object]      | Array of pipeline events to create in batch.                                                                                                                                                            |
| Option 2             | attributes                           | object        | Attributes of the pipeline event to create.                                                                                                                                                             |
| attributes           | env                                  | string        | The Datadog environment.                                                                                                                                                                                |
| attributes           | provider_name                        | string        | The name of the CI provider. By default, this is "custom".                                                                                                                                              |
| attributes           | resource [*required*]           |  <oneOf> | Details of the CI pipeline event.                                                                                                                                                                       |
| resource             | Option 1                             |  <oneOf> | Details of the top level pipeline, build, or workflow of your CI.                                                                                                                                       |
| Option 1             | Option 1                             | object        | Details of a finished pipeline.                                                                                                                                                                         |
| Option 1             | end [*required*]                | date-time     | Time when the pipeline run finished. It cannot be older than 18 hours in the past from the current time. The time format must be RFC3339.                                                               |
| Option 1             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 1             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 1             | is_manual                            | boolean       | Whether or not the pipeline was triggered manually by the user.                                                                                                                                         |
| Option 1             | is_resumed                           | boolean       | Whether or not the pipeline was resumed after being blocked.                                                                                                                                            |
| Option 1             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs, and steps. Allowed enum values: `pipeline`                                                                                                         |
| Option 1             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 1             | name [*required*]               | string        | Name of the pipeline. All pipeline runs for the builds should have the same name.                                                                                                                       |
| Option 1             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 1             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 1             | parent_pipeline                      | object        | If the pipeline is triggered as child of another pipeline, this should contain the details of the parent pipeline.                                                                                      |
| parent_pipeline      | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| parent_pipeline      | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 1             | partial_retry [*required*]      | boolean       | Whether or not the pipeline was a partial retry of a previous attempt. A partial retry is one which only runs a subset of the original jobs.                                                            |
| Option 1             | pipeline_id                          | string        | Any ID used in the provider to identify the pipeline run even if it is not unique across retries. If the `pipeline_id` is unique, then both `unique_id` and `pipeline_id` can be set to the same value. |
| Option 1             | previous_attempt                     | object        | If the pipeline is a retry, this should contain the details of the previous attempt.                                                                                                                    |
| previous_attempt     | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| previous_attempt     | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 1             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 1             | start [*required*]              | date-time     | Time when the pipeline run started (it should not include any queue time). The time format must be RFC3339.                                                                                             |
| Option 1             | status [*required*]             | enum          | The final status of the pipeline. Allowed enum values: `success,error,canceled,skipped,blocked`                                                                                                         |
| Option 1             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 1             | unique_id [*required*]          | string        | UUID of the pipeline run. The ID has to be unique across retries and pipelines, including partial retries.                                                                                              |
| Option 1             | url [*required*]                | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 1             | Option 2                             | object        | Details of a running pipeline.                                                                                                                                                                          |
| Option 2             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 2             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 2             | is_manual                            | boolean       | Whether or not the pipeline was triggered manually by the user.                                                                                                                                         |
| Option 2             | is_resumed                           | boolean       | Whether or not the pipeline was resumed after being blocked.                                                                                                                                            |
| Option 2             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs, and steps. Allowed enum values: `pipeline`                                                                                                         |
| Option 2             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 2             | name [*required*]               | string        | Name of the pipeline. All pipeline runs for the builds should have the same name.                                                                                                                       |
| Option 2             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 2             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 2             | parent_pipeline                      | object        | If the pipeline is triggered as child of another pipeline, this should contain the details of the parent pipeline.                                                                                      |
| parent_pipeline      | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| parent_pipeline      | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 2             | partial_retry [*required*]      | boolean       | Whether or not the pipeline was a partial retry of a previous attempt. A partial retry is one which only runs a subset of the original jobs.                                                            |
| Option 2             | pipeline_id                          | string        | Any ID used in the provider to identify the pipeline run even if it is not unique across retries. If the `pipeline_id` is unique, then both `unique_id` and `pipeline_id` can be set to the same value. |
| Option 2             | previous_attempt                     | object        | If the pipeline is a retry, this should contain the details of the previous attempt.                                                                                                                    |
| previous_attempt     | id [*required*]                 | string        | UUID of a pipeline.                                                                                                                                                                                     |
| previous_attempt     | url                                  | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| Option 2             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 2             | start [*required*]              | date-time     | Time when the pipeline run started (it should not include any queue time). The time format must be RFC3339.                                                                                             |
| Option 2             | status [*required*]             | enum          | The in progress status of the pipeline. Allowed enum values: `running`                                                                                                                                  |
| Option 2             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 2             | unique_id [*required*]          | string        | UUID of the pipeline run. The ID has to be the same as the finished pipeline.                                                                                                                           |
| Option 2             | url [*required*]                | string        | The URL to look at the pipeline in the CI provider UI.                                                                                                                                                  |
| resource             | Option 2                             | object        | Details of a CI stage.                                                                                                                                                                                  |
| Option 2             | dependencies                         | [string]      | A list of stage IDs that this stage depends on.                                                                                                                                                         |
| Option 2             | end [*required*]                | date-time     | Time when the stage run finished. The time format must be RFC3339.                                                                                                                                      |
| Option 2             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 2             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 2             | id [*required*]                 | string        | UUID for the stage. It has to be unique at least in the pipeline scope.                                                                                                                                 |
| Option 2             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs and steps. Allowed enum values: `stage`                                                                                                             |
| Option 2             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 2             | name [*required*]               | string        | The name for the stage.                                                                                                                                                                                 |
| Option 2             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 2             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 2             | pipeline_name [*required*]      | string        | The parent pipeline name.                                                                                                                                                                               |
| Option 2             | pipeline_unique_id [*required*] | string        | The parent pipeline UUID.                                                                                                                                                                               |
| Option 2             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 2             | start [*required*]              | date-time     | Time when the stage run started (it should not include any queue time). The time format must be RFC3339.                                                                                                |
| Option 2             | status [*required*]             | enum          | The final status of the stage. Allowed enum values: `success,error,canceled,skipped`                                                                                                                    |
| Option 2             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| resource             | Option 3                             | object        | Details of a CI job.                                                                                                                                                                                    |
| Option 3             | dependencies                         | [string]      | A list of job IDs that this job depends on.                                                                                                                                                             |
| Option 3             | end [*required*]                | date-time     | Time when the job run finished. The time format must be RFC3339.                                                                                                                                        |
| Option 3             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 3             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 3             | id [*required*]                 | string        | The UUID for the job. It has to be unique within each pipeline execution.                                                                                                                               |
| Option 3             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs, and steps. Allowed enum values: `job`                                                                                                              |
| Option 3             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 3             | name [*required*]               | string        | The name for the job.                                                                                                                                                                                   |
| Option 3             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 3             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 3             | pipeline_name [*required*]      | string        | The parent pipeline name.                                                                                                                                                                               |
| Option 3             | pipeline_unique_id [*required*] | string        | The parent pipeline UUID.                                                                                                                                                                               |
| Option 3             | queue_time                           | int64         | The queue time in milliseconds, if applicable.                                                                                                                                                          |
| Option 3             | stage_id                             | string        | The parent stage UUID (if applicable).                                                                                                                                                                  |
| Option 3             | stage_name                           | string        | The parent stage name (if applicable).                                                                                                                                                                  |
| Option 3             | start [*required*]              | date-time     | Time when the job run instance started (it should not include any queue time). The time format must be RFC3339.                                                                                         |
| Option 3             | status [*required*]             | enum          | The final status of the job. Allowed enum values: `success,error,canceled,skipped`                                                                                                                      |
| Option 3             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 3             | url [*required*]                | string        | The URL to look at the job in the CI provider UI.                                                                                                                                                       |
| resource             | Option 4                             | object        | Details of a CI step.                                                                                                                                                                                   |
| Option 4             | end [*required*]                | date-time     | Time when the step run finished. The time format must be RFC3339.                                                                                                                                       |
| Option 4             | error                                | object        | Contains information of the CI error.                                                                                                                                                                   |
| error                | domain                               | enum          | Error category used to differentiate between issues related to the developer or provider environments. Allowed enum values: `provider,user,unknown`                                                     |
| error                | message                              | string        | Error message.                                                                                                                                                                                          |
| error                | stack                                | string        | The stack trace of the reported errors.                                                                                                                                                                 |
| error                | type                                 | string        | Short description of the error type.                                                                                                                                                                    |
| Option 4             | git                                  | object        | If pipelines are triggered due to actions to a Git repository, then all payloads must contain this. Note that either `tag` or `branch` has to be provided, but not both.                                |
| git                  | author_email [*required*]       | string        | The commit author email.                                                                                                                                                                                |
| git                  | author_name                          | string        | The commit author name.                                                                                                                                                                                 |
| git                  | author_time                          | string        | The commit author timestamp in RFC3339 format.                                                                                                                                                          |
| git                  | branch                               | string        | The branch name (if a tag use the tag parameter).                                                                                                                                                       |
| git                  | commit_time                          | string        | The commit timestamp in RFC3339 format.                                                                                                                                                                 |
| git                  | committer_email                      | string        | The committer email.                                                                                                                                                                                    |
| git                  | committer_name                       | string        | The committer name.                                                                                                                                                                                     |
| git                  | default_branch                       | string        | The Git repository's default branch.                                                                                                                                                                    |
| git                  | message                              | string        | The commit message.                                                                                                                                                                                     |
| git                  | repository_url [*required*]     | string        | The URL of the repository.                                                                                                                                                                              |
| git                  | sha [*required*]                | string        | The git commit SHA.                                                                                                                                                                                     |
| git                  | tag                                  | string        | The tag name (if a branch use the branch parameter).                                                                                                                                                    |
| Option 4             | id [*required*]                 | string        | UUID for the step. It has to be unique within each pipeline execution.                                                                                                                                  |
| Option 4             | job_id                               | string        | The parent job UUID (if applicable).                                                                                                                                                                    |
| Option 4             | job_name                             | string        | The parent job name (if applicable).                                                                                                                                                                    |
| Option 4             | level [*required*]              | enum          | Used to distinguish between pipelines, stages, jobs and steps. Allowed enum values: `step`                                                                                                              |
| Option 4             | metrics                              | [string]      | A list of user-defined metrics. The metrics must follow the `key:value` pattern and the value must be numeric.                                                                                          |
| Option 4             | name [*required*]               | string        | The name for the step.                                                                                                                                                                                  |
| Option 4             | node                                 | object        | Contains information of the host running the pipeline, stage, job, or step.                                                                                                                             |
| node                 | hostname                             | string        | FQDN of the host.                                                                                                                                                                                       |
| node                 | labels                               | [string]      | A list of labels used to select or identify the node.                                                                                                                                                   |
| node                 | name                                 | string        | Name for the host.                                                                                                                                                                                      |
| node                 | workspace                            | string        | The path where the code is checked out.                                                                                                                                                                 |
| Option 4             | parameters                           | object        | A map of key-value parameters or environment variables that were defined for the pipeline.                                                                                                              |
| additionalProperties | <any-key>                            | string        |
| Option 4             | pipeline_name [*required*]      | string        | The parent pipeline name.                                                                                                                                                                               |
| Option 4             | pipeline_unique_id [*required*] | string        | The parent pipeline UUID.                                                                                                                                                                               |
| Option 4             | stage_id                             | string        | The parent stage UUID (if applicable).                                                                                                                                                                  |
| Option 4             | stage_name                           | string        | The parent stage name (if applicable).                                                                                                                                                                  |
| Option 4             | start [*required*]              | date-time     | Time when the step run started. The time format must be RFC3339.                                                                                                                                        |
| Option 4             | status [*required*]             | enum          | The final status of the step. Allowed enum values: `success,error`                                                                                                                                      |
| Option 4             | tags                                 | [string]      | A list of user-defined tags. The tags must follow the `key:value` pattern.                                                                                                                              |
| Option 4             | url                                  | string        | The URL to look at the step in the CI provider UI.                                                                                                                                                      |
| attributes           | service                              | string        | If the CI provider is SaaS, use this to differentiate between instances.                                                                                                                                |
| Option 2             | type                                 | enum          | Type of the event. Allowed enum values: `cipipeline_resource_request`                                                                                                                                   |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "data": {
    "attributes": {
      "resource": {
        "level": "pipeline",
        "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        "name": "Deploy to AWS",
        "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        "start": "2021-11-11T11:09:11+00:00",
        "end": "2021-11-11T11:10:41+00:00",
        "status": "success",
        "partial_retry": false,
        "git": {
          "repository_url": "https://github.com/DataDog/datadog-agent",
          "sha": "7f263865994b76066c4612fd1965215e7dcb4cd2",
          "author_email": "john.doe@email.com"
        }
      }
    },
    "type": "cipipeline_resource_request"
  }
}
```

##### 

```json
{
  "data": {
    "attributes": {
      "provider_name": "example-provider",
      "resource": {
        "level": "pipeline",
        "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        "name": "Deploy to AWS",
        "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        "start": "2021-11-11T11:09:11+00:00",
        "end": "2021-11-11T11:10:41+00:00",
        "status": "success",
        "partial_retry": false,
        "git": {
          "repository_url": "https://github.com/DataDog/datadog-agent",
          "sha": "7f263865994b76066c4612fd1965215e7dcb4cd2",
          "author_email": "john.doe@email.com"
        }
      }
    },
    "type": "cipipeline_resource_request"
  }
}
```

##### 

```json
{
  "data": {
    "attributes": {
      "resource": {
        "level": "pipeline",
        "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        "name": "Deploy to AWS",
        "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        "start": "2021-11-11T11:09:11+00:00",
        "status": "running",
        "partial_retry": false,
        "git": {
          "repository_url": "https://github.com/DataDog/datadog-agent",
          "sha": "7f263865994b76066c4612fd1965215e7dcb4cd2",
          "author_email": "john.doe@email.com"
        }
      }
    },
    "type": "cipipeline_resource_request"
  }
}
```

{% /tab %}

### Response

{% tab title="202" %}
Request accepted for processing
{% tab title="Model" %}

| Field | Type | Description |
| ----- | ---- | ----------- |

{% /tab %}

{% tab title="Example" %}

```json
{}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="401" %}
Unauthorized
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Forbidden
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="408" %}
Request Timeout
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="413" %}
Payload Too Large
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too Many Requests
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="500" %}
Internal Server Error
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="503" %}
Service Unavailable
{% tab title="Model" %}
Errors occurred.

| Parent field | Field  | Type     | Description        |
| ------------ | ------ | -------- | ------------------ |
|              | errors | [object] | Structured errors. |
| errors       | detail | string   | Error message.     |
| errors       | status | string   | Error code.        |
| errors       | title  | string   | Error title.       |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    {
      "detail": "Malformed payload",
      "status": "400",
      "title": "Bad Request"
    }
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipeline" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "resource": {
        "level": "pipeline",
        "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        "name": "Deploy to AWS",
        "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        "start": "2021-11-11T11:09:11+00:00",
        "end": "2021-11-11T11:10:41+00:00",
        "status": "success",
        "partial_retry": false,
        "git": {
          "repository_url": "https://github.com/DataDog/datadog-agent",
          "sha": "7f263865994b76066c4612fd1965215e7dcb4cd2",
          "author_email": "john.doe@email.com"
        }
      }
    },
    "type": "cipipeline_resource_request"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipeline" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "provider_name": "example-provider",
      "resource": {
        "level": "pipeline",
        "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        "name": "Deploy to AWS",
        "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        "start": "2021-11-11T11:09:11+00:00",
        "end": "2021-11-11T11:10:41+00:00",
        "status": "success",
        "partial_retry": false,
        "git": {
          "repository_url": "https://github.com/DataDog/datadog-agent",
          "sha": "7f263865994b76066c4612fd1965215e7dcb4cd2",
          "author_email": "john.doe@email.com"
        }
      }
    },
    "type": "cipipeline_resource_request"
  }
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipeline" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "resource": {
        "level": "pipeline",
        "unique_id": "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        "name": "Deploy to AWS",
        "url": "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        "start": "2021-11-11T11:09:11+00:00",
        "status": "running",
        "partial_retry": false,
        "git": {
          "repository_url": "https://github.com/DataDog/datadog-agent",
          "sha": "7f263865994b76066c4612fd1965215e7dcb4cd2",
          "author_email": "john.doe@email.com"
        }
      }
    },
    "type": "cipipeline_resource_request"
  }
}
EOF
                        
##### 

```go
// Send pipeline event returns "Request accepted for processing" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CIAppCreatePipelineEventRequest{
		Data: &datadogV2.CIAppCreatePipelineEventRequestDataSingleOrArray{
			CIAppCreatePipelineEventRequestData: &datadogV2.CIAppCreatePipelineEventRequestData{
				Attributes: &datadogV2.CIAppCreatePipelineEventRequestAttributes{
					Resource: datadogV2.CIAppCreatePipelineEventRequestAttributesResource{
						CIAppPipelineEventPipeline: &datadogV2.CIAppPipelineEventPipeline{
							CIAppPipelineEventFinishedPipeline: &datadogV2.CIAppPipelineEventFinishedPipeline{
								Level:        datadogV2.CIAPPPIPELINEEVENTPIPELINELEVEL_PIPELINE,
								UniqueId:     "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
								Name:         "Deploy to AWS",
								Url:          "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
								Start:        time.Now().Add(time.Second * -120),
								End:          time.Now().Add(time.Second * -30),
								Status:       datadogV2.CIAPPPIPELINEEVENTPIPELINESTATUS_SUCCESS,
								PartialRetry: false,
								Git: *datadogV2.NewNullableCIAppGitInfo(&datadogV2.CIAppGitInfo{
									RepositoryUrl: "https://github.com/DataDog/datadog-agent",
									Sha:           "7f263865994b76066c4612fd1965215e7dcb4cd2",
									AuthorEmail:   "john.doe@email.com",
								}),
							}}},
				},
				Type: datadogV2.CIAPPCREATEPIPELINEEVENTREQUESTDATATYPE_CIPIPELINE_RESOURCE_REQUEST.Ptr(),
			}},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, r, err := api.CreateCIAppPipelineEvent(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.CreateCIAppPipelineEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityPipelinesApi.CreateCIAppPipelineEvent`:\n%s\n", responseContent)
}
```

##### 

```go
// Send pipeline event with custom provider returns "Request accepted for processing" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CIAppCreatePipelineEventRequest{
		Data: &datadogV2.CIAppCreatePipelineEventRequestDataSingleOrArray{
			CIAppCreatePipelineEventRequestData: &datadogV2.CIAppCreatePipelineEventRequestData{
				Attributes: &datadogV2.CIAppCreatePipelineEventRequestAttributes{
					ProviderName: datadog.PtrString("example-provider"),
					Resource: datadogV2.CIAppCreatePipelineEventRequestAttributesResource{
						CIAppPipelineEventPipeline: &datadogV2.CIAppPipelineEventPipeline{
							CIAppPipelineEventFinishedPipeline: &datadogV2.CIAppPipelineEventFinishedPipeline{
								Level:        datadogV2.CIAPPPIPELINEEVENTPIPELINELEVEL_PIPELINE,
								UniqueId:     "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
								Name:         "Deploy to AWS",
								Url:          "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
								Start:        time.Now().Add(time.Second * -120),
								End:          time.Now().Add(time.Second * -30),
								Status:       datadogV2.CIAPPPIPELINEEVENTPIPELINESTATUS_SUCCESS,
								PartialRetry: false,
								Git: *datadogV2.NewNullableCIAppGitInfo(&datadogV2.CIAppGitInfo{
									RepositoryUrl: "https://github.com/DataDog/datadog-agent",
									Sha:           "7f263865994b76066c4612fd1965215e7dcb4cd2",
									AuthorEmail:   "john.doe@email.com",
								}),
							}}},
				},
				Type: datadogV2.CIAPPCREATEPIPELINEEVENTREQUESTDATATYPE_CIPIPELINE_RESOURCE_REQUEST.Ptr(),
			}},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, r, err := api.CreateCIAppPipelineEvent(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.CreateCIAppPipelineEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityPipelinesApi.CreateCIAppPipelineEvent`:\n%s\n", responseContent)
}
```

##### 

```go
// Send running pipeline event returns "Request accepted for processing" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CIAppCreatePipelineEventRequest{
		Data: &datadogV2.CIAppCreatePipelineEventRequestDataSingleOrArray{
			CIAppCreatePipelineEventRequestData: &datadogV2.CIAppCreatePipelineEventRequestData{
				Attributes: &datadogV2.CIAppCreatePipelineEventRequestAttributes{
					Resource: datadogV2.CIAppCreatePipelineEventRequestAttributesResource{
						CIAppPipelineEventPipeline: &datadogV2.CIAppPipelineEventPipeline{
							CIAppPipelineEventInProgressPipeline: &datadogV2.CIAppPipelineEventInProgressPipeline{
								Level:        datadogV2.CIAPPPIPELINEEVENTPIPELINELEVEL_PIPELINE,
								UniqueId:     "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
								Name:         "Deploy to AWS",
								Url:          "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
								Start:        time.Now().Add(time.Second * -120),
								Status:       datadogV2.CIAPPPIPELINEEVENTPIPELINEINPROGRESSSTATUS_RUNNING,
								PartialRetry: false,
								Git: *datadogV2.NewNullableCIAppGitInfo(&datadogV2.CIAppGitInfo{
									RepositoryUrl: "https://github.com/DataDog/datadog-agent",
									Sha:           "7f263865994b76066c4612fd1965215e7dcb4cd2",
									AuthorEmail:   "john.doe@email.com",
								}),
							}}},
				},
				Type: datadogV2.CIAPPCREATEPIPELINEEVENTREQUESTDATATYPE_CIPIPELINE_RESOURCE_REQUEST.Ptr(),
			}},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, r, err := api.CreateCIAppPipelineEvent(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.CreateCIAppPipelineEvent`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityPipelinesApi.CreateCIAppPipelineEvent`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" go run "main.go"
##### 

```java
// Send pipeline event returns "Request accepted for processing" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequest;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestAttributes;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestAttributesResource;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestData;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestDataSingleOrArray;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestDataType;
import com.datadog.api.client.v2.model.CIAppGitInfo;
import com.datadog.api.client.v2.model.CIAppPipelineEventFinishedPipeline;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipeline;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipelineLevel;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipelineStatus;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    CIAppCreatePipelineEventRequest body =
        new CIAppCreatePipelineEventRequest()
            .data(
                new CIAppCreatePipelineEventRequestDataSingleOrArray(
                    new CIAppCreatePipelineEventRequestData()
                        .attributes(
                            new CIAppCreatePipelineEventRequestAttributes()
                                .resource(
                                    new CIAppCreatePipelineEventRequestAttributesResource(
                                        new CIAppPipelineEventPipeline(
                                            new CIAppPipelineEventFinishedPipeline()
                                                .level(CIAppPipelineEventPipelineLevel.PIPELINE)
                                                .uniqueId("3eacb6f3-ff04-4e10-8a9c-46e6d054024a")
                                                .name("Deploy to AWS")
                                                .url(
                                                    "https://my-ci-provider.example/pipelines/my-pipeline/run/1")
                                                .start(OffsetDateTime.now().plusSeconds(-120))
                                                .end(OffsetDateTime.now().plusSeconds(-30))
                                                .status(CIAppPipelineEventPipelineStatus.SUCCESS)
                                                .partialRetry(false)
                                                .git(
                                                    new CIAppGitInfo()
                                                        .repositoryUrl(
                                                            "https://github.com/DataDog/datadog-agent")
                                                        .sha(
                                                            "7f263865994b76066c4612fd1965215e7dcb4cd2")
                                                        .authorEmail("john.doe@email.com"))))))
                        .type(
                            CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST)));

    try {
      apiInstance.createCIAppPipelineEvent(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CiVisibilityPipelinesApi#createCIAppPipelineEvent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Send pipeline event with custom provider returns "Request accepted for processing" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequest;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestAttributes;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestAttributesResource;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestData;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestDataSingleOrArray;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestDataType;
import com.datadog.api.client.v2.model.CIAppGitInfo;
import com.datadog.api.client.v2.model.CIAppPipelineEventFinishedPipeline;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipeline;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipelineLevel;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipelineStatus;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    CIAppCreatePipelineEventRequest body =
        new CIAppCreatePipelineEventRequest()
            .data(
                new CIAppCreatePipelineEventRequestDataSingleOrArray(
                    new CIAppCreatePipelineEventRequestData()
                        .attributes(
                            new CIAppCreatePipelineEventRequestAttributes()
                                .providerName("example-provider")
                                .resource(
                                    new CIAppCreatePipelineEventRequestAttributesResource(
                                        new CIAppPipelineEventPipeline(
                                            new CIAppPipelineEventFinishedPipeline()
                                                .level(CIAppPipelineEventPipelineLevel.PIPELINE)
                                                .uniqueId("3eacb6f3-ff04-4e10-8a9c-46e6d054024a")
                                                .name("Deploy to AWS")
                                                .url(
                                                    "https://my-ci-provider.example/pipelines/my-pipeline/run/1")
                                                .start(OffsetDateTime.now().plusSeconds(-120))
                                                .end(OffsetDateTime.now().plusSeconds(-30))
                                                .status(CIAppPipelineEventPipelineStatus.SUCCESS)
                                                .partialRetry(false)
                                                .git(
                                                    new CIAppGitInfo()
                                                        .repositoryUrl(
                                                            "https://github.com/DataDog/datadog-agent")
                                                        .sha(
                                                            "7f263865994b76066c4612fd1965215e7dcb4cd2")
                                                        .authorEmail("john.doe@email.com"))))))
                        .type(
                            CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST)));

    try {
      apiInstance.createCIAppPipelineEvent(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CiVisibilityPipelinesApi#createCIAppPipelineEvent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Send running pipeline event returns "Request accepted for processing" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequest;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestAttributes;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestAttributesResource;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestData;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestDataSingleOrArray;
import com.datadog.api.client.v2.model.CIAppCreatePipelineEventRequestDataType;
import com.datadog.api.client.v2.model.CIAppGitInfo;
import com.datadog.api.client.v2.model.CIAppPipelineEventInProgressPipeline;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipeline;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipelineInProgressStatus;
import com.datadog.api.client.v2.model.CIAppPipelineEventPipelineLevel;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    CIAppCreatePipelineEventRequest body =
        new CIAppCreatePipelineEventRequest()
            .data(
                new CIAppCreatePipelineEventRequestDataSingleOrArray(
                    new CIAppCreatePipelineEventRequestData()
                        .attributes(
                            new CIAppCreatePipelineEventRequestAttributes()
                                .resource(
                                    new CIAppCreatePipelineEventRequestAttributesResource(
                                        new CIAppPipelineEventPipeline(
                                            new CIAppPipelineEventInProgressPipeline()
                                                .level(CIAppPipelineEventPipelineLevel.PIPELINE)
                                                .uniqueId("3eacb6f3-ff04-4e10-8a9c-46e6d054024a")
                                                .name("Deploy to AWS")
                                                .url(
                                                    "https://my-ci-provider.example/pipelines/my-pipeline/run/1")
                                                .start(OffsetDateTime.now().plusSeconds(-120))
                                                .status(
                                                    CIAppPipelineEventPipelineInProgressStatus
                                                        .RUNNING)
                                                .partialRetry(false)
                                                .git(
                                                    new CIAppGitInfo()
                                                        .repositoryUrl(
                                                            "https://github.com/DataDog/datadog-agent")
                                                        .sha(
                                                            "7f263865994b76066c4612fd1965215e7dcb4cd2")
                                                        .authorEmail("john.doe@email.com"))))))
                        .type(
                            CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST)));

    try {
      apiInstance.createCIAppPipelineEvent(body);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CiVisibilityPipelinesApi#createCIAppPipelineEvent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" java "Example.java"
##### 

```python
"""
Send pipeline event returns "Request accepted for processing" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request import CIAppCreatePipelineEventRequest
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes import (
    CIAppCreatePipelineEventRequestAttributes,
)
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data import CIAppCreatePipelineEventRequestData
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data_type import (
    CIAppCreatePipelineEventRequestDataType,
)
from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
from datadog_api_client.v2.model.ci_app_pipeline_event_finished_pipeline import CIAppPipelineEventFinishedPipeline
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_level import CIAppPipelineEventPipelineLevel
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_status import CIAppPipelineEventPipelineStatus

body = CIAppCreatePipelineEventRequest(
    data=CIAppCreatePipelineEventRequestData(
        attributes=CIAppCreatePipelineEventRequestAttributes(
            resource=CIAppPipelineEventFinishedPipeline(
                level=CIAppPipelineEventPipelineLevel.PIPELINE,
                unique_id="3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
                name="Deploy to AWS",
                url="https://my-ci-provider.example/pipelines/my-pipeline/run/1",
                start=(datetime.now() + relativedelta(seconds=-120)),
                end=(datetime.now() + relativedelta(seconds=-30)),
                status=CIAppPipelineEventPipelineStatus.SUCCESS,
                partial_retry=False,
                git=CIAppGitInfo(
                    repository_url="https://github.com/DataDog/datadog-agent",
                    sha="7f263865994b76066c4612fd1965215e7dcb4cd2",
                    author_email="john.doe@email.com",
                ),
            ),
        ),
        type=CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.create_ci_app_pipeline_event(body=body)

    print(response)
```

##### 

```python
"""
Send pipeline event with custom provider returns "Request accepted for processing" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request import CIAppCreatePipelineEventRequest
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes import (
    CIAppCreatePipelineEventRequestAttributes,
)
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data import CIAppCreatePipelineEventRequestData
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data_type import (
    CIAppCreatePipelineEventRequestDataType,
)
from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
from datadog_api_client.v2.model.ci_app_pipeline_event_finished_pipeline import CIAppPipelineEventFinishedPipeline
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_level import CIAppPipelineEventPipelineLevel
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_status import CIAppPipelineEventPipelineStatus

body = CIAppCreatePipelineEventRequest(
    data=CIAppCreatePipelineEventRequestData(
        attributes=CIAppCreatePipelineEventRequestAttributes(
            provider_name="example-provider",
            resource=CIAppPipelineEventFinishedPipeline(
                level=CIAppPipelineEventPipelineLevel.PIPELINE,
                unique_id="3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
                name="Deploy to AWS",
                url="https://my-ci-provider.example/pipelines/my-pipeline/run/1",
                start=(datetime.now() + relativedelta(seconds=-120)),
                end=(datetime.now() + relativedelta(seconds=-30)),
                status=CIAppPipelineEventPipelineStatus.SUCCESS,
                partial_retry=False,
                git=CIAppGitInfo(
                    repository_url="https://github.com/DataDog/datadog-agent",
                    sha="7f263865994b76066c4612fd1965215e7dcb4cd2",
                    author_email="john.doe@email.com",
                ),
            ),
        ),
        type=CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.create_ci_app_pipeline_event(body=body)

    print(response)
```

##### 

```python
"""
Send running pipeline event returns "Request accepted for processing" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request import CIAppCreatePipelineEventRequest
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_attributes import (
    CIAppCreatePipelineEventRequestAttributes,
)
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data import CIAppCreatePipelineEventRequestData
from datadog_api_client.v2.model.ci_app_create_pipeline_event_request_data_type import (
    CIAppCreatePipelineEventRequestDataType,
)
from datadog_api_client.v2.model.ci_app_git_info import CIAppGitInfo
from datadog_api_client.v2.model.ci_app_pipeline_event_in_progress_pipeline import CIAppPipelineEventInProgressPipeline
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_in_progress_status import (
    CIAppPipelineEventPipelineInProgressStatus,
)
from datadog_api_client.v2.model.ci_app_pipeline_event_pipeline_level import CIAppPipelineEventPipelineLevel

body = CIAppCreatePipelineEventRequest(
    data=CIAppCreatePipelineEventRequestData(
        attributes=CIAppCreatePipelineEventRequestAttributes(
            resource=CIAppPipelineEventInProgressPipeline(
                level=CIAppPipelineEventPipelineLevel.PIPELINE,
                unique_id="3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
                name="Deploy to AWS",
                url="https://my-ci-provider.example/pipelines/my-pipeline/run/1",
                start=(datetime.now() + relativedelta(seconds=-120)),
                status=CIAppPipelineEventPipelineInProgressStatus.RUNNING,
                partial_retry=False,
                git=CIAppGitInfo(
                    repository_url="https://github.com/DataDog/datadog-agent",
                    sha="7f263865994b76066c4612fd1965215e7dcb4cd2",
                    author_email="john.doe@email.com",
                ),
            ),
        ),
        type=CIAppCreatePipelineEventRequestDataType.CIPIPELINE_RESOURCE_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.create_ci_app_pipeline_event(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" python3 "example.py"
##### 

```ruby
# Send pipeline event returns "Request accepted for processing" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new

body = DatadogAPIClient::V2::CIAppCreatePipelineEventRequest.new({
  data: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestData.new({
    attributes: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestAttributes.new({
      resource: DatadogAPIClient::V2::CIAppPipelineEventFinishedPipeline.new({
        level: DatadogAPIClient::V2::CIAppPipelineEventPipelineLevel::PIPELINE,
        unique_id: "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        name: "Deploy to AWS",
        url: "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        start: (Time.now + -120),
        _end: (Time.now + -30),
        status: DatadogAPIClient::V2::CIAppPipelineEventPipelineStatus::SUCCESS,
        partial_retry: false,
        git: DatadogAPIClient::V2::CIAppGitInfo.new({
          repository_url: "https://github.com/DataDog/datadog-agent",
          sha: "7f263865994b76066c4612fd1965215e7dcb4cd2",
          author_email: "john.doe@email.com",
        }),
      }),
    }),
    type: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestDataType::CIPIPELINE_RESOURCE_REQUEST,
  }),
})
p api_instance.create_ci_app_pipeline_event(body)
```

##### 

```ruby
# Send pipeline event with custom provider returns "Request accepted for processing" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new

body = DatadogAPIClient::V2::CIAppCreatePipelineEventRequest.new({
  data: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestData.new({
    attributes: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestAttributes.new({
      provider_name: "example-provider",
      resource: DatadogAPIClient::V2::CIAppPipelineEventFinishedPipeline.new({
        level: DatadogAPIClient::V2::CIAppPipelineEventPipelineLevel::PIPELINE,
        unique_id: "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        name: "Deploy to AWS",
        url: "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        start: (Time.now + -120),
        _end: (Time.now + -30),
        status: DatadogAPIClient::V2::CIAppPipelineEventPipelineStatus::SUCCESS,
        partial_retry: false,
        git: DatadogAPIClient::V2::CIAppGitInfo.new({
          repository_url: "https://github.com/DataDog/datadog-agent",
          sha: "7f263865994b76066c4612fd1965215e7dcb4cd2",
          author_email: "john.doe@email.com",
        }),
      }),
    }),
    type: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestDataType::CIPIPELINE_RESOURCE_REQUEST,
  }),
})
p api_instance.create_ci_app_pipeline_event(body)
```

##### 

```ruby
# Send running pipeline event returns "Request accepted for processing" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new

body = DatadogAPIClient::V2::CIAppCreatePipelineEventRequest.new({
  data: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestData.new({
    attributes: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestAttributes.new({
      resource: DatadogAPIClient::V2::CIAppPipelineEventInProgressPipeline.new({
        level: DatadogAPIClient::V2::CIAppPipelineEventPipelineLevel::PIPELINE,
        unique_id: "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
        name: "Deploy to AWS",
        url: "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
        start: (Time.now + -120),
        status: DatadogAPIClient::V2::CIAppPipelineEventPipelineInProgressStatus::RUNNING,
        partial_retry: false,
        git: DatadogAPIClient::V2::CIAppGitInfo.new({
          repository_url: "https://github.com/DataDog/datadog-agent",
          sha: "7f263865994b76066c4612fd1965215e7dcb4cd2",
          author_email: "john.doe@email.com",
        }),
      }),
    }),
    type: DatadogAPIClient::V2::CIAppCreatePipelineEventRequestDataType::CIPIPELINE_RESOURCE_REQUEST,
  }),
})
p api_instance.create_ci_app_pipeline_event(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" rb "example.rb"
##### 

```rust
// Send pipeline event returns "Request accepted for processing" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequest;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestAttributes;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestAttributesResource;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestData;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestDataSingleOrArray;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestDataType;
use datadog_api_client::datadogV2::model::CIAppGitInfo;
use datadog_api_client::datadogV2::model::CIAppPipelineEventFinishedPipeline;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipeline;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipelineLevel;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipelineStatus;

#[tokio::main]
async fn main() {
    let body =
        CIAppCreatePipelineEventRequest
        ::new().data(
            CIAppCreatePipelineEventRequestDataSingleOrArray::CIAppCreatePipelineEventRequestData(
                Box::new(
                    CIAppCreatePipelineEventRequestData::new()
                        .attributes(
                            CIAppCreatePipelineEventRequestAttributes::new(
                                CIAppCreatePipelineEventRequestAttributesResource::CIAppPipelineEventPipeline(
                                    Box::new(
                                        CIAppPipelineEventPipeline::CIAppPipelineEventFinishedPipeline(
                                            Box::new(
                                                CIAppPipelineEventFinishedPipeline::new(
                                                    DateTime::parse_from_rfc3339("2021-11-11T11:10:41+00:00")
                                                        .expect("Failed to parse datetime")
                                                        .with_timezone(&Utc),
                                                    CIAppPipelineEventPipelineLevel::PIPELINE,
                                                    "Deploy to AWS".to_string(),
                                                    false,
                                                    DateTime::parse_from_rfc3339("2021-11-11T11:09:11+00:00")
                                                        .expect("Failed to parse datetime")
                                                        .with_timezone(&Utc),
                                                    CIAppPipelineEventPipelineStatus::SUCCESS,
                                                    "3eacb6f3-ff04-4e10-8a9c-46e6d054024a".to_string(),
                                                    "https://my-ci-provider.example/pipelines/my-pipeline/run/1".to_string(),
                                                ).git(
                                                    Some(
                                                        CIAppGitInfo::new(
                                                            "john.doe@email.com".to_string(),
                                                            "https://github.com/DataDog/datadog-agent".to_string(),
                                                            "7f263865994b76066c4612fd1965215e7dcb4cd2".to_string(),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        )
                        .type_(CIAppCreatePipelineEventRequestDataType::CIPIPELINE_RESOURCE_REQUEST),
                ),
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let resp = api.create_ci_app_pipeline_event(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Send pipeline event with custom provider returns "Request accepted for
// processing" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequest;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestAttributes;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestAttributesResource;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestData;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestDataSingleOrArray;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestDataType;
use datadog_api_client::datadogV2::model::CIAppGitInfo;
use datadog_api_client::datadogV2::model::CIAppPipelineEventFinishedPipeline;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipeline;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipelineLevel;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipelineStatus;

#[tokio::main]
async fn main() {
    let body =
        CIAppCreatePipelineEventRequest
        ::new().data(
            CIAppCreatePipelineEventRequestDataSingleOrArray::CIAppCreatePipelineEventRequestData(
                Box::new(
                    CIAppCreatePipelineEventRequestData::new()
                        .attributes(
                            CIAppCreatePipelineEventRequestAttributes::new(
                                CIAppCreatePipelineEventRequestAttributesResource::CIAppPipelineEventPipeline(
                                    Box::new(
                                        CIAppPipelineEventPipeline::CIAppPipelineEventFinishedPipeline(
                                            Box::new(
                                                CIAppPipelineEventFinishedPipeline::new(
                                                    DateTime::parse_from_rfc3339("2021-11-11T11:10:41+00:00")
                                                        .expect("Failed to parse datetime")
                                                        .with_timezone(&Utc),
                                                    CIAppPipelineEventPipelineLevel::PIPELINE,
                                                    "Deploy to AWS".to_string(),
                                                    false,
                                                    DateTime::parse_from_rfc3339("2021-11-11T11:09:11+00:00")
                                                        .expect("Failed to parse datetime")
                                                        .with_timezone(&Utc),
                                                    CIAppPipelineEventPipelineStatus::SUCCESS,
                                                    "3eacb6f3-ff04-4e10-8a9c-46e6d054024a".to_string(),
                                                    "https://my-ci-provider.example/pipelines/my-pipeline/run/1".to_string(),
                                                ).git(
                                                    Some(
                                                        CIAppGitInfo::new(
                                                            "john.doe@email.com".to_string(),
                                                            "https://github.com/DataDog/datadog-agent".to_string(),
                                                            "7f263865994b76066c4612fd1965215e7dcb4cd2".to_string(),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ).provider_name("example-provider".to_string()),
                        )
                        .type_(CIAppCreatePipelineEventRequestDataType::CIPIPELINE_RESOURCE_REQUEST),
                ),
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let resp = api.create_ci_app_pipeline_event(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Send running pipeline event returns "Request accepted for processing" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequest;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestAttributes;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestAttributesResource;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestData;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestDataSingleOrArray;
use datadog_api_client::datadogV2::model::CIAppCreatePipelineEventRequestDataType;
use datadog_api_client::datadogV2::model::CIAppGitInfo;
use datadog_api_client::datadogV2::model::CIAppPipelineEventInProgressPipeline;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipeline;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipelineInProgressStatus;
use datadog_api_client::datadogV2::model::CIAppPipelineEventPipelineLevel;

#[tokio::main]
async fn main() {
    let body =
        CIAppCreatePipelineEventRequest
        ::new().data(
            CIAppCreatePipelineEventRequestDataSingleOrArray::CIAppCreatePipelineEventRequestData(
                Box::new(
                    CIAppCreatePipelineEventRequestData::new()
                        .attributes(
                            CIAppCreatePipelineEventRequestAttributes::new(
                                CIAppCreatePipelineEventRequestAttributesResource::CIAppPipelineEventPipeline(
                                    Box::new(
                                        CIAppPipelineEventPipeline::CIAppPipelineEventInProgressPipeline(
                                            Box::new(
                                                CIAppPipelineEventInProgressPipeline::new(
                                                    CIAppPipelineEventPipelineLevel::PIPELINE,
                                                    "Deploy to AWS".to_string(),
                                                    false,
                                                    DateTime::parse_from_rfc3339("2021-11-11T11:09:11+00:00")
                                                        .expect("Failed to parse datetime")
                                                        .with_timezone(&Utc),
                                                    CIAppPipelineEventPipelineInProgressStatus::RUNNING,
                                                    "3eacb6f3-ff04-4e10-8a9c-46e6d054024a".to_string(),
                                                    "https://my-ci-provider.example/pipelines/my-pipeline/run/1".to_string(),
                                                ).git(
                                                    Some(
                                                        CIAppGitInfo::new(
                                                            "john.doe@email.com".to_string(),
                                                            "https://github.com/DataDog/datadog-agent".to_string(),
                                                            "7f263865994b76066c4612fd1965215e7dcb4cd2".to_string(),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        )
                        .type_(CIAppCreatePipelineEventRequestDataType::CIPIPELINE_RESOURCE_REQUEST),
                ),
            ),
        );
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let resp = api.create_ci_app_pipeline_event(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" cargo run
##### 

```typescript
/**
 * Send pipeline event returns "Request accepted for processing" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiCreateCIAppPipelineEventRequest = {
  body: {
    data: {
      attributes: {
        resource: {
          level: "pipeline",
          uniqueId: "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
          name: "Deploy to AWS",
          url: "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
          start: new Date(new Date().getTime() + -120 * 1000),
          end: new Date(new Date().getTime() + -30 * 1000),
          status: "success",
          partialRetry: false,
          git: {
            repositoryUrl: "https://github.com/DataDog/datadog-agent",
            sha: "7f263865994b76066c4612fd1965215e7dcb4cd2",
            authorEmail: "john.doe@email.com",
          },
        },
      },
      type: "cipipeline_resource_request",
    },
  },
};

apiInstance
  .createCIAppPipelineEvent(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Send pipeline event with custom provider returns "Request accepted for processing" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiCreateCIAppPipelineEventRequest = {
  body: {
    data: {
      attributes: {
        providerName: "example-provider",
        resource: {
          level: "pipeline",
          uniqueId: "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
          name: "Deploy to AWS",
          url: "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
          start: new Date(new Date().getTime() + -120 * 1000),
          end: new Date(new Date().getTime() + -30 * 1000),
          status: "success",
          partialRetry: false,
          git: {
            repositoryUrl: "https://github.com/DataDog/datadog-agent",
            sha: "7f263865994b76066c4612fd1965215e7dcb4cd2",
            authorEmail: "john.doe@email.com",
          },
        },
      },
      type: "cipipeline_resource_request",
    },
  },
};

apiInstance
  .createCIAppPipelineEvent(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Send running pipeline event returns "Request accepted for processing" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiCreateCIAppPipelineEventRequest = {
  body: {
    data: {
      attributes: {
        resource: {
          level: "pipeline",
          uniqueId: "3eacb6f3-ff04-4e10-8a9c-46e6d054024a",
          name: "Deploy to AWS",
          url: "https://my-ci-provider.example/pipelines/my-pipeline/run/1",
          start: new Date(new Date().getTime() + -120 * 1000),
          status: "running",
          partialRetry: false,
          git: {
            repositoryUrl: "https://github.com/DataDog/datadog-agent",
            sha: "7f263865994b76066c4612fd1965215e7dcb4cd2",
            authorEmail: "john.doe@email.com",
          },
        },
      },
      type: "cipipeline_resource_request",
    },
  },
};

apiInstance
  .createCIAppPipelineEvent(params)
  .then((data: any) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" tsc "example.ts"
{% /tab %}

## Get a list of pipelines events{% #get-a-list-of-pipelines-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                 |
| ----------------- | ------------------------------------------------------------ |
| ap1.datadoghq.com | GET https://api.ap1.datadoghq.com/api/v2/ci/pipelines/events |
| ap2.datadoghq.com | GET https://api.ap2.datadoghq.com/api/v2/ci/pipelines/events |
| app.datadoghq.eu  | GET https://api.datadoghq.eu/api/v2/ci/pipelines/events      |
| app.ddog-gov.com  | GET https://api.ddog-gov.com/api/v2/ci/pipelines/events      |
| app.datadoghq.com | GET https://api.datadoghq.com/api/v2/ci/pipelines/events     |
| us3.datadoghq.com | GET https://api.us3.datadoghq.com/api/v2/ci/pipelines/events |
| us5.datadoghq.com | GET https://api.us5.datadoghq.com/api/v2/ci/pipelines/events |

### Overview



List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/). [Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to see your latest pipeline events.
This endpoint requires the `ci_visibility_read` permission.
OAuth apps require the `ci_visibility_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ci-visibility-pipelines) to access this endpoint.



### Arguments

#### Query Strings

| Name          | Type    | Description                                                             |
| ------------- | ------- | ----------------------------------------------------------------------- |
| filter[query] | string  | Search query following log syntax.                                      |
| filter[from]  | string  | Minimum timestamp for requested events.                                 |
| filter[to]    | string  | Maximum timestamp for requested events.                                 |
| sort          | enum    | Order of events in results.Allowed enum values: `timestamp, -timestamp` |
| page[cursor]  | string  | List following results with a cursor provided in the previous query.    |
| page[limit]   | integer | Maximum number of events in the response.                               |

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all pipeline events matching the request and pagination information.

| Parent field | Field      | Type     | Description                                                                                                                               |
| ------------ | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | [object] | Array of events matching the request.                                                                                                     |
| data         | attributes | object   | JSON object containing all event attributes and their associated values.                                                                  |
| attributes   | attributes | object   | JSON object of attributes from CI Visibility pipeline events.                                                                             |
| attributes   | ci_level   | enum     | Pipeline execution level. Allowed enum values: `pipeline,stage,job,step,custom`                                                           |
| attributes   | tags       | [string] | Array of tags associated with your event.                                                                                                 |
| data         | id         | string   | Unique ID of the event.                                                                                                                   |
| data         | type       | enum     | Type of the event. Allowed enum values: `cipipeline`                                                                                      |
|              | links      | object   | Links attributes.                                                                                                                         |
| links        | next       | string   | Link for the next set of results. The request can also be made using the POST endpoint.                                                   |
|              | meta       | object   | The metadata associated with a request.                                                                                                   |
| meta         | elapsed    | int64    | The time elapsed in milliseconds.                                                                                                         |
| meta         | page       | object   | Paging attributes.                                                                                                                        |
| page         | after      | string   | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`. |
| meta         | request_id | string   | The identifier of the request.                                                                                                            |
| meta         | status     | enum     | The status of the response. Allowed enum values: `done,timeout`                                                                           |
| meta         | warnings   | [object] | A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.                    |
| warnings     | code       | string   | A unique code for this type of warning.                                                                                                   |
| warnings     | detail     | string   | A detailed explanation of this specific warning.                                                                                          |
| warnings     | title      | string   | A short human-readable summary of the warning.                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "ci_level": "pipeline",
        "tags": [
          "team:A"
        ]
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "cipipeline"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/ci/tests/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                  \# Curl commandcurl -X GET "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipelines/events" \
-H "Accept: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}"
                
##### 

```python
"""
Get a list of pipelines events returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.list_ci_app_pipeline_events(
        filter_query="@ci.provider.name:circleci",
        filter_from=(datetime.now() + relativedelta(minutes=-30)),
        filter_to=datetime.now(),
        page_limit=5,
    )

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Get a list of pipelines events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new
opts = {
  filter_query: "@ci.provider.name:circleci",
  filter_from: (Time.now + -30 * 60),
  filter_to: Time.now,
  page_limit: 5,
}
p api_instance.list_ci_app_pipeline_events(opts)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```go
// Get a list of pipelines events returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"
	"time"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, r, err := api.ListCIAppPipelineEvents(ctx, *datadogV2.NewListCIAppPipelineEventsOptionalParameters().WithFilterQuery("@ci.provider.name:circleci").WithFilterFrom(time.Now().Add(time.Minute * -30)).WithFilterTo(time.Now()).WithPageLimit(5))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.ListCIAppPipelineEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityPipelinesApi.ListCIAppPipelineEvents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Get a list of pipelines events returns "OK" response
import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi.ListCIAppPipelineEventsOptionalParameters;
import com.datadog.api.client.v2.model.CIAppPipelineEventsResponse;
import java.time.OffsetDateTime;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    try {
      CIAppPipelineEventsResponse result =
          apiInstance.listCIAppPipelineEvents(
              new ListCIAppPipelineEventsOptionalParameters()
                  .filterQuery("@ci.provider.name:circleci")
                  .filterFrom(OffsetDateTime.now().plusMinutes(-30))
                  .filterTo(OffsetDateTime.now())
                  .pageLimit(5));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CiVisibilityPipelinesApi#listCIAppPipelineEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```rust
// Get a list of pipelines events returns "OK" response
use chrono::{DateTime, Utc};
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::ListCIAppPipelineEventsOptionalParams;

#[tokio::main]
async fn main() {
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let resp = api
        .list_ci_app_pipeline_events(
            ListCIAppPipelineEventsOptionalParams::default()
                .filter_query("@ci.provider.name:circleci".to_string())
                .filter_from(
                    DateTime::parse_from_rfc3339("2021-11-11T10:41:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .filter_to(
                    DateTime::parse_from_rfc3339("2021-11-11T11:11:11+00:00")
                        .expect("Failed to parse datetime")
                        .with_timezone(&Utc),
                )
                .page_limit(5),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Get a list of pipelines events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiListCIAppPipelineEventsRequest = {
  filterQuery: "@ci.provider.name:circleci",
  filterFrom: new Date(new Date().getTime() + -30 * 60 * 1000),
  filterTo: new Date(),
  pageLimit: 5,
};

apiInstance
  .listCIAppPipelineEvents(params)
  .then((data: v2.CIAppPipelineEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Search pipelines events{% #search-pipelines-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                         |
| ----------------- | -------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/ci/pipelines/events/search |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/ci/pipelines/events/search |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/ci/pipelines/events/search      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/ci/pipelines/events/search      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/ci/pipelines/events/search     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/ci/pipelines/events/search |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/ci/pipelines/events/search |

### Overview



List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/). [Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).

Use this endpoint to build complex events filtering and search.
This endpoint requires the `ci_visibility_read` permission.
OAuth apps require the `ci_visibility_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ci-visibility-pipelines) to access this endpoint.



### Request

#### Body Data 



{% tab title="Model" %}

| Parent field | Field       | Type   | Description                                                                                                                               |
| ------------ | ----------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
|              | filter      | object | The search and filter query settings.                                                                                                     |
| filter       | from        | string | The minimum time for the requested events; supports date, math, and regular timestamps (in milliseconds).                                 |
| filter       | query       | string | The search query following the CI Visibility Explorer search syntax.                                                                      |
| filter       | to          | string | The maximum time for the requested events, supports date, math, and regular timestamps (in milliseconds).                                 |
|              | options     | object | Global query options that are used during the query. Only supply timezone or time offset, not both. Otherwise, the query fails.           |
| options      | time_offset | int64  | The time offset (in seconds) to apply to the query.                                                                                       |
| options      | timezone    | string | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York). |
|              | page        | object | Paging attributes for listing events.                                                                                                     |
| page         | cursor      | string | List following results with a cursor provided in the previous query.                                                                      |
| page         | limit       | int32  | Maximum number of events in the response.                                                                                                 |
|              | sort        | enum   | Sort parameters when querying events. Allowed enum values: `timestamp,-timestamp`                                                         |

{% /tab %}

{% tab title="Example" %}
##### 

```json
{
  "filter": {
    "from": "now-15m",
    "query": "@ci.provider.name:github AND @ci.status:error",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 5
  },
  "sort": "timestamp"
}
```

##### 

```json
{
  "filter": {
    "from": "now-30s",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
Response object with all pipeline events matching the request and pagination information.

| Parent field | Field      | Type     | Description                                                                                                                               |
| ------------ | ---------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
|              | data       | [object] | Array of events matching the request.                                                                                                     |
| data         | attributes | object   | JSON object containing all event attributes and their associated values.                                                                  |
| attributes   | attributes | object   | JSON object of attributes from CI Visibility pipeline events.                                                                             |
| attributes   | ci_level   | enum     | Pipeline execution level. Allowed enum values: `pipeline,stage,job,step,custom`                                                           |
| attributes   | tags       | [string] | Array of tags associated with your event.                                                                                                 |
| data         | id         | string   | Unique ID of the event.                                                                                                                   |
| data         | type       | enum     | Type of the event. Allowed enum values: `cipipeline`                                                                                      |
|              | links      | object   | Links attributes.                                                                                                                         |
| links        | next       | string   | Link for the next set of results. The request can also be made using the POST endpoint.                                                   |
|              | meta       | object   | The metadata associated with a request.                                                                                                   |
| meta         | elapsed    | int64    | The time elapsed in milliseconds.                                                                                                         |
| meta         | page       | object   | Paging attributes.                                                                                                                        |
| page         | after      | string   | The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`. |
| meta         | request_id | string   | The identifier of the request.                                                                                                            |
| meta         | status     | enum     | The status of the response. Allowed enum values: `done,timeout`                                                                           |
| meta         | warnings   | [object] | A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response.                    |
| warnings     | code       | string   | A unique code for this type of warning.                                                                                                   |
| warnings     | detail     | string   | A detailed explanation of this specific warning.                                                                                          |
| warnings     | title      | string   | A short human-readable summary of the warning.                                                                                            |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": [
    {
      "attributes": {
        "attributes": {
          "customAttribute": 123,
          "duration": 2345
        },
        "ci_level": "pipeline",
        "tags": [
          "team:A"
        ]
      },
      "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA",
      "type": "cipipeline"
    }
  ],
  "links": {
    "next": "https://app.datadoghq.com/api/v2/ci/tests/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "page": {
      "after": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
    },
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipelines/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-15m",
    "query": "@ci.provider.name:github AND @ci.status:error",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 5
  },
  "sort": "timestamp"
}
EOF
                        
##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipelines/events/search" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "filter": {
    "from": "now-30s",
    "to": "now"
  },
  "options": {
    "timezone": "GMT"
  },
  "page": {
    "limit": 2
  },
  "sort": "timestamp"
}
EOF
                        
##### 

```go
// Search pipelines events returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CIAppPipelineEventsRequest{
		Filter: &datadogV2.CIAppPipelinesQueryFilter{
			From:  datadog.PtrString("now-15m"),
			Query: datadog.PtrString("@ci.provider.name:github AND @ci.status:error"),
			To:    datadog.PtrString("now"),
		},
		Options: &datadogV2.CIAppQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
		Page: &datadogV2.CIAppQueryPageOptions{
			Limit: datadog.PtrInt32(5),
		},
		Sort: datadogV2.CIAPPSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, r, err := api.SearchCIAppPipelineEvents(ctx, *datadogV2.NewSearchCIAppPipelineEventsOptionalParameters().WithBody(body))

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.SearchCIAppPipelineEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityPipelinesApi.SearchCIAppPipelineEvents`:\n%s\n", responseContent)
}
```

##### 

```go
// Search pipelines events returns "OK" response with pagination

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CIAppPipelineEventsRequest{
		Filter: &datadogV2.CIAppPipelinesQueryFilter{
			From: datadog.PtrString("now-30s"),
			To:   datadog.PtrString("now"),
		},
		Options: &datadogV2.CIAppQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
		Page: &datadogV2.CIAppQueryPageOptions{
			Limit: datadog.PtrInt32(2),
		},
		Sort: datadogV2.CIAPPSORT_TIMESTAMP_ASCENDING.Ptr(),
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, _ := api.SearchCIAppPipelineEventsWithPagination(ctx, *datadogV2.NewSearchCIAppPipelineEventsOptionalParameters().WithBody(body))

	for paginationResult := range resp {
		if paginationResult.Error != nil {
			fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.SearchCIAppPipelineEvents`: %v\n", paginationResult.Error)
		}
		responseContent, _ := json.MarshalIndent(paginationResult.Item, "", "  ")
		fmt.Fprintf(os.Stdout, "%s\n", responseContent)
	}
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Search pipelines events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi.SearchCIAppPipelineEventsOptionalParameters;
import com.datadog.api.client.v2.model.CIAppPipelineEventsRequest;
import com.datadog.api.client.v2.model.CIAppPipelineEventsResponse;
import com.datadog.api.client.v2.model.CIAppPipelinesQueryFilter;
import com.datadog.api.client.v2.model.CIAppQueryOptions;
import com.datadog.api.client.v2.model.CIAppQueryPageOptions;
import com.datadog.api.client.v2.model.CIAppSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    CIAppPipelineEventsRequest body =
        new CIAppPipelineEventsRequest()
            .filter(
                new CIAppPipelinesQueryFilter()
                    .from("now-15m")
                    .query("@ci.provider.name:github AND @ci.status:error")
                    .to("now"))
            .options(new CIAppQueryOptions().timezone("GMT"))
            .page(new CIAppQueryPageOptions().limit(5))
            .sort(CIAppSort.TIMESTAMP_ASCENDING);

    try {
      CIAppPipelineEventsResponse result =
          apiInstance.searchCIAppPipelineEvents(
              new SearchCIAppPipelineEventsOptionalParameters().body(body));
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CiVisibilityPipelinesApi#searchCIAppPipelineEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

##### 

```java
// Search pipelines events returns "OK" response with pagination

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.PaginationIterable;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi.SearchCIAppPipelineEventsOptionalParameters;
import com.datadog.api.client.v2.model.CIAppPipelineEvent;
import com.datadog.api.client.v2.model.CIAppPipelineEventsRequest;
import com.datadog.api.client.v2.model.CIAppPipelinesQueryFilter;
import com.datadog.api.client.v2.model.CIAppQueryOptions;
import com.datadog.api.client.v2.model.CIAppQueryPageOptions;
import com.datadog.api.client.v2.model.CIAppSort;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    CIAppPipelineEventsRequest body =
        new CIAppPipelineEventsRequest()
            .filter(new CIAppPipelinesQueryFilter().from("now-30s").to("now"))
            .options(new CIAppQueryOptions().timezone("GMT"))
            .page(new CIAppQueryPageOptions().limit(2))
            .sort(CIAppSort.TIMESTAMP_ASCENDING);

    try {
      PaginationIterable<CIAppPipelineEvent> iterable =
          apiInstance.searchCIAppPipelineEventsWithPagination(
              new SearchCIAppPipelineEventsOptionalParameters().body(body));

      for (CIAppPipelineEvent item : iterable) {
        System.out.println(item);
      }
    } catch (RuntimeException e) {
      System.err.println(
          "Exception when calling"
              + " CiVisibilityPipelinesApi#searchCIAppPipelineEventsWithPagination");
      System.err.println("Reason: " + e.getMessage());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
"""
Search pipelines events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_pipeline_events_request import CIAppPipelineEventsRequest
from datadog_api_client.v2.model.ci_app_pipelines_query_filter import CIAppPipelinesQueryFilter
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort

body = CIAppPipelineEventsRequest(
    filter=CIAppPipelinesQueryFilter(
        _from="now-15m",
        query="@ci.provider.name:github AND @ci.status:error",
        to="now",
    ),
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
    page=CIAppQueryPageOptions(
        limit=5,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.search_ci_app_pipeline_events(body=body)

    print(response)
```

##### 

```python
"""
Search pipelines events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_pipeline_events_request import CIAppPipelineEventsRequest
from datadog_api_client.v2.model.ci_app_pipelines_query_filter import CIAppPipelinesQueryFilter
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort

body = CIAppPipelineEventsRequest(
    filter=CIAppPipelinesQueryFilter(
        _from="now-30s",
        to="now",
    ),
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
    page=CIAppQueryPageOptions(
        limit=2,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    items = api_instance.search_ci_app_pipeline_events_with_pagination(body=body)
    for item in items:
        print(item)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Search pipelines events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new

body = DatadogAPIClient::V2::CIAppPipelineEventsRequest.new({
  filter: DatadogAPIClient::V2::CIAppPipelinesQueryFilter.new({
    from: "now-15m",
    query: "@ci.provider.name:github AND @ci.status:error",
    to: "now",
  }),
  options: DatadogAPIClient::V2::CIAppQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::CIAppQueryPageOptions.new({
    limit: 5,
  }),
  sort: DatadogAPIClient::V2::CIAppSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
p api_instance.search_ci_app_pipeline_events(opts)
```

##### 

```ruby
# Search pipelines events returns "OK" response with pagination

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new

body = DatadogAPIClient::V2::CIAppPipelineEventsRequest.new({
  filter: DatadogAPIClient::V2::CIAppPipelinesQueryFilter.new({
    from: "now-30s",
    to: "now",
  }),
  options: DatadogAPIClient::V2::CIAppQueryOptions.new({
    timezone: "GMT",
  }),
  page: DatadogAPIClient::V2::CIAppQueryPageOptions.new({
    limit: 2,
  }),
  sort: DatadogAPIClient::V2::CIAppSort::TIMESTAMP_ASCENDING,
})
opts = {
  body: body,
}
api_instance.search_ci_app_pipeline_events_with_pagination(opts) { |item| puts item }
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Search pipelines events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::SearchCIAppPipelineEventsOptionalParams;
use datadog_api_client::datadogV2::model::CIAppPipelineEventsRequest;
use datadog_api_client::datadogV2::model::CIAppPipelinesQueryFilter;
use datadog_api_client::datadogV2::model::CIAppQueryOptions;
use datadog_api_client::datadogV2::model::CIAppQueryPageOptions;
use datadog_api_client::datadogV2::model::CIAppSort;

#[tokio::main]
async fn main() {
    let body = CIAppPipelineEventsRequest::new()
        .filter(
            CIAppPipelinesQueryFilter::new()
                .from("now-15m".to_string())
                .query("@ci.provider.name:github AND @ci.status:error".to_string())
                .to("now".to_string()),
        )
        .options(CIAppQueryOptions::new().timezone("GMT".to_string()))
        .page(CIAppQueryPageOptions::new().limit(5))
        .sort(CIAppSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let resp = api
        .search_ci_app_pipeline_events(
            SearchCIAppPipelineEventsOptionalParams::default().body(body),
        )
        .await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

##### 

```rust
// Search pipelines events returns "OK" response with pagination
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::SearchCIAppPipelineEventsOptionalParams;
use datadog_api_client::datadogV2::model::CIAppPipelineEventsRequest;
use datadog_api_client::datadogV2::model::CIAppPipelinesQueryFilter;
use datadog_api_client::datadogV2::model::CIAppQueryOptions;
use datadog_api_client::datadogV2::model::CIAppQueryPageOptions;
use datadog_api_client::datadogV2::model::CIAppSort;
use futures_util::pin_mut;
use futures_util::stream::StreamExt;

#[tokio::main]
async fn main() {
    let body = CIAppPipelineEventsRequest::new()
        .filter(
            CIAppPipelinesQueryFilter::new()
                .from("now-30s".to_string())
                .to("now".to_string()),
        )
        .options(CIAppQueryOptions::new().timezone("GMT".to_string()))
        .page(CIAppQueryPageOptions::new().limit(2))
        .sort(CIAppSort::TIMESTAMP_ASCENDING);
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let response = api.search_ci_app_pipeline_events_with_pagination(
        SearchCIAppPipelineEventsOptionalParams::default().body(body),
    );
    pin_mut!(response);
    while let Some(resp) = response.next().await {
        if let Ok(value) = resp {
            println!("{:#?}", value);
        } else {
            println!("{:#?}", resp.unwrap_err());
        }
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Search pipelines events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiSearchCIAppPipelineEventsRequest = {
  body: {
    filter: {
      from: "now-15m",
      query: "@ci.provider.name:github AND @ci.status:error",
      to: "now",
    },
    options: {
      timezone: "GMT",
    },
    page: {
      limit: 5,
    },
    sort: "timestamp",
  },
};

apiInstance
  .searchCIAppPipelineEvents(params)
  .then((data: v2.CIAppPipelineEventsResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

##### 

```typescript
/**
 * Search pipelines events returns "OK" response with pagination
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiSearchCIAppPipelineEventsRequest = {
  body: {
    filter: {
      from: "now-30s",
      to: "now",
    },
    options: {
      timezone: "GMT",
    },
    page: {
      limit: 2,
    },
    sort: "timestamp",
  },
};

(async () => {
  try {
    for await (const item of apiInstance.searchCIAppPipelineEventsWithPagination(
      params
    )) {
      console.log(item);
    }
  } catch (error) {
    console.error(error);
  }
})();
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}

## Aggregate pipelines events{% #aggregate-pipelines-events %}

{% tab title="v2" %}

| Datadog site      | API endpoint                                                               |
| ----------------- | -------------------------------------------------------------------------- |
| ap1.datadoghq.com | POST https://api.ap1.datadoghq.com/api/v2/ci/pipelines/analytics/aggregate |
| ap2.datadoghq.com | POST https://api.ap2.datadoghq.com/api/v2/ci/pipelines/analytics/aggregate |
| app.datadoghq.eu  | POST https://api.datadoghq.eu/api/v2/ci/pipelines/analytics/aggregate      |
| app.ddog-gov.com  | POST https://api.ddog-gov.com/api/v2/ci/pipelines/analytics/aggregate      |
| app.datadoghq.com | POST https://api.datadoghq.com/api/v2/ci/pipelines/analytics/aggregate     |
| us3.datadoghq.com | POST https://api.us3.datadoghq.com/api/v2/ci/pipelines/analytics/aggregate |
| us5.datadoghq.com | POST https://api.us5.datadoghq.com/api/v2/ci/pipelines/analytics/aggregate |

### Overview

Use this API endpoint to aggregate CI Visibility pipeline events into buckets of computed metrics and timeseries. This endpoint requires the `ci_visibility_read` permission.

OAuth apps require the `ci_visibility_read` authorization [scope](https://docs.datadoghq.com/api/latest/scopes/#ci-visibility-pipelines) to access this endpoint.



### Request

#### Body Data (required)



{% tab title="Model" %}

| Parent field | Field                         | Type          | Description                                                                                                                                           |
| ------------ | ----------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | compute                       | [object]      | The list of metrics or timeseries to compute for the retrieved buckets.                                                                               |
| compute      | aggregation [*required*] | enum          | An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median,latest,earliest,most_frequent,delta` |
| compute      | interval                      | string        | The time buckets' size (only used for type=timeseries) Defaults to a resolution of 150 points.                                                        |
| compute      | metric                        | string        | The metric to use.                                                                                                                                    |
| compute      | type                          | enum          | The type of compute. Allowed enum values: `timeseries,total`                                                                                          |
|              | filter                        | object        | The search and filter query settings.                                                                                                                 |
| filter       | from                          | string        | The minimum time for the requested events; supports date, math, and regular timestamps (in milliseconds).                                             |
| filter       | query                         | string        | The search query following the CI Visibility Explorer search syntax.                                                                                  |
| filter       | to                            | string        | The maximum time for the requested events, supports date, math, and regular timestamps (in milliseconds).                                             |
|              | group_by                      | [object]      | The rules for the group-by.                                                                                                                           |
| group_by     | facet [*required*]       | string        | The name of the facet to use (required).                                                                                                              |
| group_by     | histogram                     | object        | Used to perform a histogram computation (only for measure facets). At most, 100 buckets are allowed, the number of buckets is `(max - min)/interval`. |
| histogram    | interval [*required*]    | double        | The bin size of the histogram buckets.                                                                                                                |
| histogram    | max [*required*]         | double        | The maximum value for the measure used in the histogram (values greater than this one are filtered out).                                              |
| histogram    | min [*required*]         | double        | The minimum value for the measure used in the histogram (values smaller than this one are filtered out).                                              |
| group_by     | limit                         | int64         | The maximum buckets to return for this group-by.                                                                                                      |
| group_by     | missing                       |  <oneOf> | The value to use for logs that don't have the facet used to group-by.                                                                                 |
| missing      | Option 1                      | string        | The missing value to use if there is a string valued facet.                                                                                           |
| missing      | Option 2                      | double        | The missing value to use if there is a number valued facet.                                                                                           |
| group_by     | sort                          | object        | A sort rule. The `aggregation` field is required when `type` is `measure`.                                                                            |
| sort         | aggregation                   | enum          | An aggregation function. Allowed enum values: `count,cardinality,pc75,pc90,pc95,pc98,pc99,sum,min,max,avg,median,latest,earliest,most_frequent,delta` |
| sort         | metric                        | string        | The metric to sort by (only used for `type=measure`).                                                                                                 |
| sort         | order                         | enum          | The order to use, ascending or descending. Allowed enum values: `asc,desc`                                                                            |
| sort         | type                          | enum          | The type of sorting algorithm. Allowed enum values: `alphabetical,measure`                                                                            |
| group_by     | total                         |  <oneOf> | A resulting object to put the given computes in over all the matching records.                                                                        |
| total        | Option 1                      | boolean       | If set to true, creates an additional bucket labeled "$facet_total".                                                                                  |
| total        | Option 2                      | string        | A string to use as the key value for the total bucket.                                                                                                |
| total        | Option 3                      | double        | A number to use as the key value for the total bucket.                                                                                                |
|              | options                       | object        | Global query options that are used during the query. Only supply timezone or time offset, not both. Otherwise, the query fails.                       |
| options      | time_offset                   | int64         | The time offset (in seconds) to apply to the query.                                                                                                   |
| options      | timezone                      | string        | The timezone can be specified as GMT, UTC, an offset from UTC (like UTC+1), or as a Timezone Database identifier (like America/New_York).             |

{% /tab %}

{% tab title="Example" %}

```json
{
  "compute": [
    {
      "aggregation": "pc90",
      "metric": "@duration",
      "type": "total"
    }
  ],
  "filter": {
    "from": "now-15m",
    "query": "@ci.provider.name:(gitlab OR github)",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "@ci.status",
      "limit": 10,
      "total": false
    }
  ],
  "options": {
    "timezone": "GMT"
  }
}
```

{% /tab %}

### Response

{% tab title="200" %}
OK
{% tab title="Model" %}
The response object for the pipeline events aggregate API endpoint.

| Parent field         | Field      | Type          | Description                                                                                                            |
| -------------------- | ---------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
|                      | data       | object        | The query results.                                                                                                     |
| data                 | buckets    | [object]      | The list of matching buckets, one item per bucket.                                                                     |
| buckets              | by         | object        | The key-value pairs for each group-by.                                                                                 |
| additionalProperties | <any-key>  |               | The values for each group-by.                                                                                          |
| buckets              | computes   | object        | A map of the metric name to value for regular compute, or a list of values for a timeseries.                           |
| additionalProperties | <any-key>  |  <oneOf> | A bucket value, can either be a timeseries or a single value.                                                          |
| <any-key>            | Option 1   | string        | A single string value.                                                                                                 |
| <any-key>            | Option 2   | double        | A single number value.                                                                                                 |
| <any-key>            | Option 3   | [object]      | A timeseries array.                                                                                                    |
| Option 3             | time       | date-time     | The time value for this point.                                                                                         |
| Option 3             | value      | double        | The value for this point.                                                                                              |
|                      | links      | object        | Links attributes.                                                                                                      |
| links                | next       | string        | Link for the next set of results. The request can also be made using the POST endpoint.                                |
|                      | meta       | object        | The metadata associated with a request.                                                                                |
| meta                 | elapsed    | int64         | The time elapsed in milliseconds.                                                                                      |
| meta                 | request_id | string        | The identifier of the request.                                                                                         |
| meta                 | status     | enum          | The status of the response. Allowed enum values: `done,timeout`                                                        |
| meta                 | warnings   | [object]      | A list of warnings (non-fatal errors) encountered. Partial results may return if warnings are present in the response. |
| warnings             | code       | string        | A unique code for this type of warning.                                                                                |
| warnings             | detail     | string        | A detailed explanation of this specific warning.                                                                       |
| warnings             | title      | string        | A short human-readable summary of the warning.                                                                         |

{% /tab %}

{% tab title="Example" %}

```json
{
  "data": {
    "buckets": [
      {
        "by": {
          "<any-key>": "undefined"
        },
        "computes": {
          "<any-key>": {
            "description": "undefined",
            "type": "undefined"
          }
        }
      }
    ]
  },
  "links": {
    "next": "https://app.datadoghq.com/api/v2/ci/tests/events?filter[query]=foo\u0026page[cursor]=eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ=="
  },
  "meta": {
    "elapsed": 132,
    "request_id": "MWlFUjVaWGZTTTZPYzM0VXp1OXU2d3xLSVpEMjZKQ0VKUTI0dEYtM3RSOFVR",
    "status": "done",
    "warnings": [
      {
        "code": "unknown_index",
        "detail": "indexes: foo, bar",
        "title": "One or several indexes are missing or invalid, results hold data from the other indexes"
      }
    ]
  }
}
```

{% /tab %}

{% /tab %}

{% tab title="400" %}
Bad Request
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="403" %}
Not Authorized
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

{% tab title="429" %}
Too many requests
{% tab title="Model" %}
API error response.

| Field                    | Type     | Description       |
| ------------------------ | -------- | ----------------- |
| errors [*required*] | [string] | A list of errors. |

{% /tab %}

{% tab title="Example" %}

```json
{
  "errors": [
    "Bad Request"
  ]
}
```

{% /tab %}

{% /tab %}

### Code Example

##### 
                          \# Curl commandcurl -X POST "https://api.ap1.datadoghq.com"https://api.ap2.datadoghq.com"https://api.datadoghq.eu"https://api.ddog-gov.com"https://api.datadoghq.com"https://api.us3.datadoghq.com"https://api.us5.datadoghq.com/api/v2/ci/pipelines/analytics/aggregate" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: ${DD_API_KEY}" \
-H "DD-APPLICATION-KEY: ${DD_APP_KEY}" \
-d @- << EOF
{
  "compute": [
    {
      "aggregation": "pc90",
      "metric": "@duration",
      "type": "total"
    }
  ],
  "filter": {
    "from": "now-15m",
    "query": "@ci.provider.name:(gitlab OR github)",
    "to": "now"
  },
  "group_by": [
    {
      "facet": "@ci.status",
      "limit": 10,
      "total": false
    }
  ],
  "options": {
    "timezone": "GMT"
  }
}
EOF
                        
##### 

```go
// Aggregate pipelines events returns "OK" response

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"os"

	"github.com/DataDog/datadog-api-client-go/v2/api/datadog"
	"github.com/DataDog/datadog-api-client-go/v2/api/datadogV2"
)

func main() {
	body := datadogV2.CIAppPipelinesAggregateRequest{
		Compute: []datadogV2.CIAppCompute{
			{
				Aggregation: datadogV2.CIAPPAGGREGATIONFUNCTION_PERCENTILE_90,
				Metric:      datadog.PtrString("@duration"),
				Type:        datadogV2.CIAPPCOMPUTETYPE_TOTAL.Ptr(),
			},
		},
		Filter: &datadogV2.CIAppPipelinesQueryFilter{
			From:  datadog.PtrString("now-15m"),
			Query: datadog.PtrString("@ci.provider.name:(gitlab OR github)"),
			To:    datadog.PtrString("now"),
		},
		GroupBy: []datadogV2.CIAppPipelinesGroupBy{
			{
				Facet: "@ci.status",
				Limit: datadog.PtrInt64(10),
				Total: &datadogV2.CIAppGroupByTotal{
					CIAppGroupByTotalBoolean: datadog.PtrBool(false)},
			},
		},
		Options: &datadogV2.CIAppQueryOptions{
			Timezone: datadog.PtrString("GMT"),
		},
	}
	ctx := datadog.NewDefaultContext(context.Background())
	configuration := datadog.NewConfiguration()
	apiClient := datadog.NewAPIClient(configuration)
	api := datadogV2.NewCIVisibilityPipelinesApi(apiClient)
	resp, r, err := api.AggregateCIAppPipelineEvents(ctx, body)

	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `CIVisibilityPipelinesApi.AggregateCIAppPipelineEvents`: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}

	responseContent, _ := json.MarshalIndent(resp, "", "  ")
	fmt.Fprintf(os.Stdout, "Response from `CIVisibilityPipelinesApi.AggregateCIAppPipelineEvents`:\n%s\n", responseContent)
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=go) and then save the example to `main.go` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" go run "main.go"
##### 

```java
// Aggregate pipelines events returns "OK" response

import com.datadog.api.client.ApiClient;
import com.datadog.api.client.ApiException;
import com.datadog.api.client.v2.api.CiVisibilityPipelinesApi;
import com.datadog.api.client.v2.model.CIAppAggregationFunction;
import com.datadog.api.client.v2.model.CIAppCompute;
import com.datadog.api.client.v2.model.CIAppComputeType;
import com.datadog.api.client.v2.model.CIAppGroupByTotal;
import com.datadog.api.client.v2.model.CIAppPipelinesAggregateRequest;
import com.datadog.api.client.v2.model.CIAppPipelinesAnalyticsAggregateResponse;
import com.datadog.api.client.v2.model.CIAppPipelinesGroupBy;
import com.datadog.api.client.v2.model.CIAppPipelinesQueryFilter;
import com.datadog.api.client.v2.model.CIAppQueryOptions;
import java.util.Collections;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = ApiClient.getDefaultApiClient();
    CiVisibilityPipelinesApi apiInstance = new CiVisibilityPipelinesApi(defaultClient);

    CIAppPipelinesAggregateRequest body =
        new CIAppPipelinesAggregateRequest()
            .compute(
                Collections.singletonList(
                    new CIAppCompute()
                        .aggregation(CIAppAggregationFunction.PERCENTILE_90)
                        .metric("@duration")
                        .type(CIAppComputeType.TOTAL)))
            .filter(
                new CIAppPipelinesQueryFilter()
                    .from("now-15m")
                    .query("@ci.provider.name:(gitlab OR github)")
                    .to("now"))
            .groupBy(
                Collections.singletonList(
                    new CIAppPipelinesGroupBy()
                        .facet("@ci.status")
                        .limit(10L)
                        .total(new CIAppGroupByTotal(false))))
            .options(new CIAppQueryOptions().timezone("GMT"));

    try {
      CIAppPipelinesAnalyticsAggregateResponse result =
          apiInstance.aggregateCIAppPipelineEvents(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println(
          "Exception when calling CiVisibilityPipelinesApi#aggregateCIAppPipelineEvents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=java) and then save the example to `Example.java` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" java "Example.java"
##### 

```python
"""
Aggregate pipelines events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_aggregation_function import CIAppAggregationFunction
from datadog_api_client.v2.model.ci_app_compute import CIAppCompute
from datadog_api_client.v2.model.ci_app_compute_type import CIAppComputeType
from datadog_api_client.v2.model.ci_app_pipelines_aggregate_request import CIAppPipelinesAggregateRequest
from datadog_api_client.v2.model.ci_app_pipelines_group_by import CIAppPipelinesGroupBy
from datadog_api_client.v2.model.ci_app_pipelines_query_filter import CIAppPipelinesQueryFilter
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions

body = CIAppPipelinesAggregateRequest(
    compute=[
        CIAppCompute(
            aggregation=CIAppAggregationFunction.PERCENTILE_90,
            metric="@duration",
            type=CIAppComputeType.TOTAL,
        ),
    ],
    filter=CIAppPipelinesQueryFilter(
        _from="now-15m",
        query="@ci.provider.name:(gitlab OR github)",
        to="now",
    ),
    group_by=[
        CIAppPipelinesGroupBy(
            facet="@ci.status",
            limit=10,
            total=False,
        ),
    ],
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    response = api_instance.aggregate_ci_app_pipeline_events(body=body)

    print(response)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=python) and then save the example to `example.py` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" python3 "example.py"
##### 

```ruby
# Aggregate pipelines events returns "OK" response

require "datadog_api_client"
api_instance = DatadogAPIClient::V2::CIVisibilityPipelinesAPI.new

body = DatadogAPIClient::V2::CIAppPipelinesAggregateRequest.new({
  compute: [
    DatadogAPIClient::V2::CIAppCompute.new({
      aggregation: DatadogAPIClient::V2::CIAppAggregationFunction::PERCENTILE_90,
      metric: "@duration",
      type: DatadogAPIClient::V2::CIAppComputeType::TOTAL,
    }),
  ],
  filter: DatadogAPIClient::V2::CIAppPipelinesQueryFilter.new({
    from: "now-15m",
    query: "@ci.provider.name:(gitlab OR github)",
    to: "now",
  }),
  group_by: [
    DatadogAPIClient::V2::CIAppPipelinesGroupBy.new({
      facet: "@ci.status",
      limit: 10,
      total: false,
    }),
  ],
  options: DatadogAPIClient::V2::CIAppQueryOptions.new({
    timezone: "GMT",
  }),
})
p api_instance.aggregate_ci_app_pipeline_events(body)
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=ruby) and then save the example to `example.rb` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" rb "example.rb"
##### 

```rust
// Aggregate pipelines events returns "OK" response
use datadog_api_client::datadog;
use datadog_api_client::datadogV2::api_ci_visibility_pipelines::CIVisibilityPipelinesAPI;
use datadog_api_client::datadogV2::model::CIAppAggregationFunction;
use datadog_api_client::datadogV2::model::CIAppCompute;
use datadog_api_client::datadogV2::model::CIAppComputeType;
use datadog_api_client::datadogV2::model::CIAppGroupByTotal;
use datadog_api_client::datadogV2::model::CIAppPipelinesAggregateRequest;
use datadog_api_client::datadogV2::model::CIAppPipelinesGroupBy;
use datadog_api_client::datadogV2::model::CIAppPipelinesQueryFilter;
use datadog_api_client::datadogV2::model::CIAppQueryOptions;

#[tokio::main]
async fn main() {
    let body = CIAppPipelinesAggregateRequest::new()
        .compute(vec![CIAppCompute::new(
            CIAppAggregationFunction::PERCENTILE_90,
        )
        .metric("@duration".to_string())
        .type_(CIAppComputeType::TOTAL)])
        .filter(
            CIAppPipelinesQueryFilter::new()
                .from("now-15m".to_string())
                .query("@ci.provider.name:(gitlab OR github)".to_string())
                .to("now".to_string()),
        )
        .group_by(vec![CIAppPipelinesGroupBy::new("@ci.status".to_string())
            .limit(10)
            .total(CIAppGroupByTotal::CIAppGroupByTotalBoolean(false))])
        .options(CIAppQueryOptions::new().timezone("GMT".to_string()));
    let configuration = datadog::Configuration::new();
    let api = CIVisibilityPipelinesAPI::with_config(configuration);
    let resp = api.aggregate_ci_app_pipeline_events(body).await;
    if let Ok(value) = resp {
        println!("{:#?}", value);
    } else {
        println!("{:#?}", resp.unwrap_err());
    }
}
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=rust) and then save the example to `src/main.rs` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" cargo run
##### 

```typescript
/**
 * Aggregate pipelines events returns "OK" response
 */

import { client, v2 } from "@datadog/datadog-api-client";

const configuration = client.createConfiguration();
const apiInstance = new v2.CIVisibilityPipelinesApi(configuration);

const params: v2.CIVisibilityPipelinesApiAggregateCIAppPipelineEventsRequest = {
  body: {
    compute: [
      {
        aggregation: "pc90",
        metric: "@duration",
        type: "total",
      },
    ],
    filter: {
      from: "now-15m",
      query: "@ci.provider.name:(gitlab OR github)",
      to: "now",
    },
    groupBy: [
      {
        facet: "@ci.status",
        limit: 10,
        total: false,
      },
    ],
    options: {
      timezone: "GMT",
    },
  },
};

apiInstance
  .aggregateCIAppPipelineEvents(params)
  .then((data: v2.CIAppPipelinesAnalyticsAggregateResponse) => {
    console.log(
      "API called successfully. Returned data: " + JSON.stringify(data)
    );
  })
  .catch((error: any) => console.error(error));
```

#### Instructions

First [install the library and its dependencies](https://docs.datadoghq.com/api/latest/?code-lang=typescript) and then save the example to `example.ts` and run following commands:
    DD_SITE="datadoghq.comus3.datadoghq.comus5.datadoghq.comdatadoghq.euap1.datadoghq.comap2.datadoghq.comddog-gov.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>" tsc "example.ts"
{% /tab %}
