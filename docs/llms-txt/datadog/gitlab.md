# Source: https://docs.datadoghq.com/continuous_testing/cicd_integrations/gitlab.md

# Source: https://docs.datadoghq.com/continuous_integration/pipelines/gitlab.md

---
title: GitLab Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  GitLab Setup for CI Visibility
source_url: https://docs.datadoghq.com/pipelines/gitlab/index.html
---

# GitLab Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[GitLab](https://about.gitlab.com/) is a DevOps platform that automates the software development lifecycle with integrated CI/CD features, enabling automated, continuous deployment of applications with built-in security controls.

Set up CI Visibility for GitLab to collect data on your pipeline executions, analyze performance bottlenecks, troubleshoot operational issues, and optimize your deployment workflows.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                                                                                                        | Platform                            | Definition                                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Running pipelines](https://docs.datadoghq.com/glossary/#running-pipeline)                                                                                                                                                 | Running pipelines                   | View pipeline executions that are running. Queued or waiting pipelines show with status "Running" on Datadog.                                                                                                                                                                                      |
| [CI jobs failure analysis](https://docs.datadoghq.com/continuous_integration/guides/use_ci_jobs_failure_analysis/)                                                                                                         | CI jobs failure analysis            | Uses LLM models on relevant logs to analyze the root cause of failed CI jobs.                                                                                                                                                                                                                      |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/)                                                                           | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                                                                                                                                                                                                               |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                                                                                                      | Partial pipelines                   | View partially retried pipeline executions.                                                                                                                                                                                                                                                        |
| [Manual steps](https://docs.datadoghq.com/glossary/#manual-step)                                                                                                                                                           | Manual steps                        | View manually triggered pipelines.                                                                                                                                                                                                                                                                 |
| [Queue time](https://docs.datadoghq.com/glossary/#queue-time)                                                                                                                                                              | Queue time                          | View the amount of time pipeline jobs sit in the queue before processing.                                                                                                                                                                                                                          |
| Logs correlation                                                                                                                                                                                                           | Logs correlation                    | Correlate pipeline spans to logs and enable [job log collection](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/#enable-job-log-collection).                                                                                                                                   |
| Infrastructure metric correlation                                                                                                                                                                                          | Infrastructure metric correlation   | Correlate jobs to [infrastructure host metrics](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/?tab=gitlabcom#correlate-infrastructure-metrics-to-jobs) for self-hosted GitLab runners.                                                                                        |
| Custom pre-defined tags                                                                                                                                                                                                    | Custom pre-defined tags             | Set [custom tags](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/?tab=gitlabcom#set-custom-tags) to all generated pipeline, stages, and job spans.                                                                                                                             |
| [Custom tags](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/?tab=gitlabcom#view-error-messages-for-pipeline-failures) [and measures at runtime](https://docs.datadoghq.com/account_management/teams/) | Custom tags and measures at runtime | Configure [custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/?tab=linux) at runtime.                                                                                                                                                  |
| Parameters                                                                                                                                                                                                                 | Parameters                          | Set custom `env` or `service` parameters when a pipeline is triggered.                                                                                                                                                                                                                             |
| [Pipeline failure reasons](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/?tab=gitlabcom#partial-and-downstream-pipelines)                                                                             | Pipeline failure reasons            | Identify pipeline failure reasons from [error messages](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab/?tab=gitlabcom#view-error-messages-for-pipeline-failures).                                                                                                              |
| [Approval wait time](https://docs.datadoghq.com/glossary/#approval-wait-time)                                                                                                                                              | Approval wait time                  | View the amount of time jobs and pipelines wait for manual approvals.                                                                                                                                                                                                                              |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                                                                                             | Execution time                      | View the amount of time pipelines have been running jobs. Gitlab refers to this metric as `duration`. Duration in Gitlab and execution time may show different values. Gitlab does not take into consideration jobs that failed due to certain kinds of failures (such as runner system failures). |
| [Custom spans](https://docs.datadoghq.com/glossary/#custom-span)                                                                                                                                                           | Custom spans                        | Configure custom spans for your pipelines.                                                                                                                                                                                                                                                         |

The following GitLab versions are supported:

- GitLab.com (SaaS)
- GitLab >= 14.1 (self-hosted)
- GitLab >= 13.7.0 (self-hosted) with the `datadog_ci_integration` feature flag enabled

### Terminology{% #terminology %}

This table shows the mapping of concepts between Datadog CI Visibility and GitLab:

| Datadog                    | GitLab   |
| -------------------------- | -------- |
| Pipeline                   | Pipeline |
| Stage                      | Stage    |
| Job                        | Job      |
| *Not available in Datadog* | Script   |

## Configure the Datadog integration{% #configure-the-datadog-integration %}

{% tab title="GitLab.com" %}
Configure the integration on a [project](https://docs.gitlab.com/ee/user/admin_area/settings/project_integration_management.html#view-projects-that-use-custom-settings) or [group](https://docs.gitlab.com/ee/user/project/integrations/index.html#manage-group-default-settings-for-a-project-integration) by going to **Settings > Integrations > Datadog** for each project or group you want to instrument.

Fill in the integration configuration settings:

{% dl %}

{% dt %}
**Active**
{% /dt %}

{% dd %}
Enables the integration.
{% /dd %}

{% dt %}
**Datadog site**
{% /dt %}

{% dd %}
Specifies which [Datadog site](https://docs.datadoghq.com/getting_started/site/) to send data to.**Default**: `datadoghq.com`**Selected site**: 
{% /dd %}

{% dt %}
**API URL** (optional)
{% /dt %}

{% dd %}
Allows overriding the API URL used for sending data directly, only used in advanced scenarios.**Default**: (empty, no override)
{% /dd %}

{% dt %}
**API key**
{% /dt %}

{% dd %}
Specifies which [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) to use when sending data.
{% /dd %}

{% dt %}
**Enable CI Visibility**
{% /dt %}

{% dd %}
Controls the enablement of CI Visibility features, including pipeline tracing, critical path computation and performance monitoring. Ensure this box is checked to activate these capabilities.
{% /dd %}

{% dt %}
**Service** (optional)
{% /dt %}

{% dd %}
Specifies which service name to attach to each span generated by the integration. Use this to differentiate between GitLab instances.**Default**: `gitlab-ci`
{% /dd %}

{% dt %}
**Env** (optional)
{% /dt %}

{% dd %}
Specifies which environment (`env` tag) to attach to each span generated by the integration. Use this to differentiate between groups of GitLab instances (for example, staging or production).**Default**: `none`
{% /dd %}

{% dt %}
**Tags** (optional)
{% /dt %}

{% dd %}
Specifies any custom tags to attach to each span generated by the integration. Provide one tag per line in the format: `key:value`.**Default**: (empty, no additional tags)**Note**: Available only in GitLab.com and GitLab >= 14.8 self-hosted.
{% /dd %}

{% /dl %}

You can test the integration with the **Test settings** button (only available when configuring the integration on a project). After it's successful, click **Save changes** to finish the integration set up. If the button fails, click **Save changes** and check that the first webhooks sent are successful by looking at the history in the "Recent events" section below.
{% /tab %}

{% tab title="GitLab >= 14.1" %}
Configure the integration on a [project](https://docs.gitlab.com/ee/administration/settings/project_integration_management.html#view-projects-that-use-custom-settings) or [group](https://docs.gitlab.com/ee/user/project/integrations/index.html#manage-group-default-settings-for-a-project-integration) by going to **Settings > Integrations > Datadog** for each project or group you want to instrument. You can also activate the integration at the GitLab [instance](https://docs.gitlab.com/ee/user/admin_area/settings/project_integration_management.html#manage-instance-level-default-settings-for-a-project-integration) level by going to **Admin > Settings > Integrations > Datadog**.

Fill in the integration configuration settings:

{% dl %}

{% dt %}
**Active**
{% /dt %}

{% dd %}
Enables the integration.
{% /dd %}

{% dt %}
**Datadog site**
{% /dt %}

{% dd %}
Specifies which [Datadog site](https://docs.datadoghq.com/getting_started/site/) to send data to.**Default**: `datadoghq.com`**Selected site**: 
{% /dd %}

{% dt %}
**API URL** (optional)
{% /dt %}

{% dd %}
Allows overriding the API URL used for sending data directly, only used in advanced scenarios.**Default**: (empty, no override)
{% /dd %}

{% dt %}
**API key**
{% /dt %}

{% dd %}
Specifies which [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) to use when sending data.
{% /dd %}

{% dt %}
**Enable CI Visibility**
{% /dt %}

{% dd %}
Controls the enablement of CI Visibility features, including pipeline tracing, critical path computation and performance monitoring. Ensure this box is checked to activate these capabilities. It's only present starting from GitLab 17.7, and isn't required in prior versions.
{% /dd %}

{% dt %}
**Service** (optional)
{% /dt %}

{% dd %}
Specifies which service name to attach to each span generated by the integration. Use this to differentiate between GitLab instances.**Default**: `gitlab-ci`
{% /dd %}

{% dt %}
**Env** (optional)
{% /dt %}

{% dd %}
Specifies which environment (`env` tag) to attach to each span generated by the integration. Use this to differentiate between groups of GitLab instances (for example, staging or production).**Default**: `none`
{% /dd %}

{% dt %}
**Tags** (optional)
{% /dt %}

{% dd %}
Specifies any custom tags to attach to each span generated by the integration. Provide one tag per line in the format: `key:value`.**Default**: (empty, no additional tags)**Note**: Available only in GitLab.com and GitLab >= 14.8 self-hosted.
{% /dd %}

{% /dl %}

You can test the integration with the **Test settings** button (only available when configuring the integration on a project). After it's successful, click **Save changes** to finish the integration setup. If the button fails, click **Save changes** and check that the first webhooks sent are successful by looking at the history in the "Recent events" section below.
{% /tab %}

{% tab title="GitLab < 14.1" %}
Enable the `datadog_ci_integration` [feature flag](https://docs.gitlab.com/ee/administration/feature_flags.html) to activate the integration.

Run one of the following commands, which use GitLab's [Rails Runner](https://docs.gitlab.com/ee/administration/operations/rails_console.html#using-the-rails-runner), depending on your installation type:

From **Omnibus Installations**:

```shell
sudo gitlab-rails runner "Feature.enable(:datadog_ci_integration)"
```

From **Source Installations**:

```shell
sudo -u git -H bundle exec rails runner \
  -e production \
  "Feature.enable(:datadog_ci_integration)"
```

From **Kubernetes Installations**:

```shell
kubectl exec -it <task-runner-pod-name> -- \
  /srv/gitlab/bin/rails runner "Feature.enable(:datadog_ci_integration)"
```

Then, configure the integration on a [project](https://docs.gitlab.com/ee/user/admin_area/settings/project_integration_management.html#use-custom-settings-for-a-group-or-project-integration) by going to **Settings > Integrations > Datadog** for each project you want to instrument.

{% alert level="warning" %}
Due to a [bug](https://gitlab.com/gitlab-org/gitlab/-/issues/335218) in early versions of GitLab, the Datadog integration cannot be enabled at **group or instance** level on **GitLab versions < 14.1**, even if the option is available on GitLab's UI.
{% /alert %}

Fill in the integration configuration settings:

{% dl %}

{% dt %}
**Active**
{% /dt %}

{% dd %}
Enables the integration.
{% /dd %}

{% dt %}
**Datadog site**
{% /dt %}

{% dd %}
Specifies which [Datadog site](https://docs.datadoghq.com/getting_started/site/) to send data to.**Default**: `datadoghq.com`**Selected site**: 
{% /dd %}

{% dt %}
**API URL** (optional)
{% /dt %}

{% dd %}
Allows overriding the API URL used for sending data directly, only used in advanced scenarios.**Default**: (empty, no override)
{% /dd %}

{% dt %}
**API key**
{% /dt %}

{% dd %}
Specifies which [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) to use when sending data.
{% /dd %}

{% dt %}
**Service** (optional)
{% /dt %}

{% dd %}
Specifies which service name to attach to each span generated by the integration. Use this to differentiate between GitLab instances.**Default**: `gitlab-ci`
{% /dd %}

{% dt %}
**Env** (optional)
{% /dt %}

{% dd %}
Specifies which environment (`env` tag) to attach to each span generated by the integration. Use this to differentiate between groups of GitLab instances (for example, staging or production).**Default**: `none`
{% /dd %}

{% dt %}
**Tags** (optional)
{% /dt %}

{% dd %}
Specifies any custom tags to attach to each span generated by the integration. Provide one tag per line in the format: `key:value`.**Default**: (empty, no additional tags)**Note**: Available only in GitLab.com and GitLab >= 14.8 self-hosted.
{% /dd %}

{% /dl %}

You can test the integration with the **Test settings** button (only available when configuring the integration on a project). After it's successful, click **Save changes** to finish the integration set up. If the button fails, click **Save changes** and check that the first webhooks sent are successful by looking at the history in the "Recent events" section below.
{% /tab %}

{% tab title="GitLab < 13.7" %}

{% alert level="danger" %}
Direct support with webhooks is not under development. Unexpected issues could happen. Datadog recommends that you update GitLab instead.
{% /alert %}

For older versions of GitLab, you can use [webhooks](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html) to send pipeline data to Datadog.

Go to **Settings > Webhooks** in your repository (or GitLab instance settings), and add a new webhook:

- **URL**: `https://webhook-intake.  /api/v2/webhook/?dd-api-key=<API_KEY>` where `<API_KEY>` is your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).
- **Secret Token**: Leave this field empty.
- **Trigger**: Select `Job events` and `Pipeline events`.

To set custom `env` or `service` parameters, add more query parameters in the webhooks URL. For example, `&env=<YOUR_ENV>&service=<YOUR_SERVICE_NAME>`.

### Set custom tags{% #set-custom-tags %}

To set custom tags to all the pipeline and job spans generated by the integration, add a URL-encoded query parameter `tags` with `key:value` pairs separated by commas to the URL.

If a key:value pair contains any commas, surround it with quotes. For example, to add `key1:value1,"key2: value with , comma",key3:value3`, the following string would need to be appended to the **Webhook URL**: `?tags=key1%3Avalue1%2C%22key2%3A+value+with+%2C+comma%22%2Ckey3%3Avalue3`.
{% /tab %}

## Advanced configuration{% #advanced-configuration %}

### Set custom tags{% #set-custom-tags %}

You can set custom tags for all pipeline and job spans from your GitLab projects to improve traceability. For more information, see [Custom Tags and Measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/?tab=linux).

#### Integrate with Datadog Teams{% #integrate-with-datadog-teams %}

To display and filter the teams associated with your pipelines, add `team:<your-team>` as a custom tag. The custom tag name must match your [Datadog Teams](https://docs.datadoghq.com/account_management/teams/) team handle exactly.

### Correlate infrastructure metrics to jobs{% #correlate-infrastructure-metrics-to-jobs %}

If you are using self-hosted GitLab runners, you can correlate jobs with the infrastructure that is running them.

Datadog infrastructure correlation is possible using different methods:

{% tab title="Non autoscaling executors" %}
The GitLab runner must have a tag in the form `host:<hostname>`. Tags can be added while [registering a new runner](https://docs.gitlab.com/runner/register/). As a result, this method is only available when the runner is directly running the job.

This excludes executors that are autoscaling the infrastructure in order to run the job (such as the Kubernetes, Docker Autoscaler, or Instance executors) as it is not possible to add tags dynamically for those runners.

For existing runners:

- GitLab >= 15.8: Add tags through the UI by going to **Settings > CI/CD > Runners** and editing the appropriate runner.

- GitLab < 15.8: Add tags by updating the runner's `config.toml`. Or add tags through the UI by going to **Settings > CI/CD > Runners** and editing the appropriate runner.

After these steps, CI Visibility adds the hostname to each job. To see the metrics, click on a job span in the trace view. In the drawer, a new tab named **Infrastructure** appears which contains the host metrics.
{% /tab %}

{% tab title="Docker Autoscaler" %}
CI Visibility supports Infrastructure metrics for "Docker Autoscaler" executors. For more information, see the [Correlate Infrastructure Metrics with GitLab Jobs guide](https://docs.datadoghq.com/continuous_integration/guides/infrastructure_metrics_with_gitlab).
{% /tab %}

{% tab title="Instance" %}
CI Visibility supports Infrastructure metrics for "Instance" executors. For more information, see the [Correlate Infrastructure Metrics with GitLab Jobs guide](https://docs.datadoghq.com/continuous_integration/guides/infrastructure_metrics_with_gitlab).
{% /tab %}

{% tab title="Kubernetes" %}
CI Visibility supports Infrastructure metrics for the Kubernetes executor. For this, it is necessary to have the Datadog Agent monitoring the Kubernetes Gitlab infrastructure. See [Install the Datadog Agent on Kubernetes](https://docs.datadoghq.com/containers/kubernetes/installation/?tab=datadogoperator) to install the Datadog Agent in a Kubernetes cluster.

Due to limitations in the Datadog Agent, jobs shorter than the minimum collection interval of the Datadog Agent might not always display infrastructure correlation metrics. To adjust this value, see [Datadog Agent configuration template](https://github.com/DataDog/datadog-agent/blob/main/pkg/config/config_template.yaml) and adjust the variable `min_collection_interval` to be less than 15 seconds.
{% /tab %}

{% tab title="Other executors" %}
CI Visibility does not support Infrastructure metrics for other executors.
{% /tab %}

### View error messages for pipeline failures{% #view-error-messages-for-pipeline-failures %}

For failed GitLab pipeline executions, each error under the `Errors` tab within a specific pipeline execution displays a message associated with the error type from GitLab.

{% image
   source="https://datadog-docs.imgix.net/images/ci/ci_gitlab_failure_reason_new.952d0477c6e3d449a562b35f5d189330.png?auto=format"
   alt="GitLab Failure Reason" /%}

#### CI jobs failure analysis{% #ci-jobs-failure-analysis %}

If job logs collection is enabled, CI Visibility uses LLM models to analyze failed CI jobs based on relevant logs coming from GitLab.

You can also add job failure analysis to a PR comment. See the guide on [using PR comments](https://docs.datadoghq.com/continuous_integration/guides/use_ci_jobs_failure_analysis/#using-pr-comments).

For a full explanation, see the guide on [using CI jobs failure analysis](https://docs.datadoghq.com/continuous_integration/guides/use_ci_jobs_failure_analysis/).

#### Errors provided by GitLab{% #errors-provided-by-gitlab %}

Error messages are supported for GitLab versions 15.2.0 and above.

The error information provided by GitLab is stored in `error.provider_message` and `error.provider_domain` tags.

The following table describes the message and domain correlated with each error type. Any unlisted error type results in a `Job failed` error message and an `unknown` error domain.

| Error Type                               | Error Domain | Error Message                                           |
| ---------------------------------------- | ------------ | ------------------------------------------------------- |
| `unknown_failure`                        | unknown      | Failed due to unknown reason.                           |
| `config_error`                           | user         | Failed due to error on CI/CD configuration file.        |
| `external_validation_failure`            | unknown      | Failed due to external pipeline validation.             |
| `user_not_verified`                      | user         | The pipeline failed due to the user not being verified. |
| `activity_limit_exceeded`                | provider     | The pipeline activity limit was exceeded.               |
| `size_limit_exceeded`                    | provider     | The pipeline size limit was exceeded.                   |
| `job_activity_limit_exceeded`            | provider     | The pipeline job activity limit was exceeded.           |
| `deployments_limit_exceeded`             | provider     | The pipeline deployments limit was exceeded.            |
| `project_deleted`                        | provider     | The project associated with this pipeline was deleted.  |
| `api_failure`                            | provider     | API failure.                                            |
| `stuck_or_timeout_failure`               | unknown      | Pipeline is stuck or timed out.                         |
| `runner_system_failure`                  | provider     | Failed due to runner system failure.                    |
| `missing_dependency_failure`             | unknown      | Failed due to missing dependency.                       |
| `runner_unsupported`                     | provider     | Failed due to unsupported runner.                       |
| `stale_schedule`                         | provider     | Failed due to stale schedule.                           |
| `job_execution_timeout`                  | unknown      | Failed due to job timeout.                              |
| `archived_failure`                       | provider     | Archived failure.                                       |
| `unmet_prerequisites`                    | unknown      | Failed due to unmet prerequisite.                       |
| `scheduler_failure`                      | provider     | Failed due to schedule failure.                         |
| `data_integrity_failure`                 | provider     | Failed due to data integrity.                           |
| `forward_deployment_failure`             | unknown      | Deployment failure.                                     |
| `user_blocked`                           | user         | Blocked by user.                                        |
| `ci_quota_exceeded`                      | provider     | CI quota exceeded.                                      |
| `pipeline_loop_detected`                 | user         | Pipeline loop detected.                                 |
| `builds_disabled`                        | user         | Build disabled.                                         |
| `deployment_rejected`                    | user         | Deployment rejected.                                    |
| `protected_environment_failure`          | provider     | Environment failure.                                    |
| `secrets_provider_not_found`             | user         | Secret provider not found.                              |
| `reached_max_descendant_pipelines_depth` | user         | Reached max descendant pipelines.                       |
| `ip_restriction_failure`                 | provider     | IP restriction failure.                                 |

### Collect job logs{% #collect-job-logs %}

The following GitLab versions support collecting job logs:

- GitLab.com (SaaS)
- GitLab >= 15.3 (self-hosted) only if you are using [object storage to store job logs](https://docs.gitlab.com/ee/administration/job_artifacts.html#using-object-storage)
- GitLab >= 14.8 (self-hosted) by enabling the `datadog_integration_logs_collection` feature flag

Job logs are collected in [Log Management](https://docs.datadoghq.com/logs/) and are automatically correlated with the GitLab pipeline in CI Visibility. Log files larger than one GiB are truncated.

To enable collection of job logs:

{% tab title="GitLab.com" %}

1. Click the **Enable job logs collection** checkbox in the GitLab integration **Settings > Integrations > Datadog**.
1. Click **Save changes**.

{% /tab %}

{% tab title="GitLab >= 15.3" %}

{% alert level="danger" %}
Datadog downloads log files directly from your GitLab logs [object storage](https://docs.gitlab.com/ee/administration/job_artifacts.html#using-object-storage) with temporary pre-signed URLs. This means that for Datadog servers to access the storage, the storage must not have network restrictions The [endpoint](https://docs.gitlab.com/ee/administration/object_storage.html#amazon-s3), if set, should resolve to a publicly accessible URL.
{% /alert %}

1. Click **Enable job logs collection** checkbox in the GitLab integration under **Settings > Integrations > Datadog**.
1. Click **Save changes**.

{% /tab %}

{% tab title="GitLab >= 14.8" %}

{% alert level="danger" %}
Datadog downloads log files directly from your GitLab logs [object storage](https://docs.gitlab.com/ee/administration/job_artifacts.html#using-object-storage) with temporary pre-signed URLs. This means that for Datadog servers to access the storage, the storage must not have network restrictions The [endpoint](https://docs.gitlab.com/ee/administration/object_storage.html#amazon-s3), if set, should resolve to a publicly accessible URL.
{% /alert %}

1. Enable the `datadog_integration_logs_collection` [feature flag](https://docs.gitlab.com/ee/administration/feature_flags.html) in your GitLab. This allows you to see the **Enable job logs collection** checkbox in the GitLab integration under **Settings > Integrations > Datadog**.
1. Click **Enable job logs collection**.
1. Click **Save changes**.

{% /tab %}

Logs are billed separately from CI Visibility. Log retention, exclusion, and indexes are configured in [Log Management](https://docs.datadoghq.com/logs/guide/best-practices-for-log-management/). Logs for GitLab jobs can be identified by the `datadog.product:cipipeline` and `source:gitlab` tags.

For more information about processing job logs collected from the GitLab integration, see the [Processors documentation](https://docs.datadoghq.com/logs/log_configuration/processors/).

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

Once the integration is successfully configured, the [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages populate with data after the pipelines finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
- [Extend Pipeline Visibility by adding custom tags and measures](https://docs.datadoghq.com/continuous_integration/pipelines/custom_tags_and_measures/)
