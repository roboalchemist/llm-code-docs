# Source: https://docs.datadoghq.com/continuous_integration/pipelines/awscodepipeline.md

---
title: AWS CodePipeline Setup for CI Visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Pipeline Visibility in Datadog >
  AWS CodePipeline Setup for CI Visibility
source_url: https://docs.datadoghq.com/pipelines/awscodepipeline/index.html
---

# AWS CodePipeline Setup for CI Visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

[AWS CodePipeline](https://aws.amazon.com/codepipeline/) is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates.

Set up CI Visibility for AWS CodePipeline to collect data about pipeline executions, analyze performance bottlenecks or operational issues, and monitor your deployment workflows.

### Compatibility{% #compatibility %}

| Pipeline Visibility                                                                                                                              | Platform                            | Definition                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [Partial retries](https://docs.datadoghq.com/glossary/#partial-retry)                                                                            | Partial pipelines                   | View partially retried pipeline executions.                                                                   |
| \*[Running pipelines](https://docs.datadoghq.com/glossary/#running-pipeline)                                                                     | Running pipelines                   | View pipeline executions that are running. Queued or waiting pipelines show with status "Running" on Datadog. |
| \**Logs correlation                                                                                                                              | Logs correlation                    | Correlate pipeline and job spans to logs and enable job log correlation.                                      |
| [Approval wait time](https://docs.datadoghq.com/glossary/#approval-wait-time)                                                                    | Approval wait time                  | View the amount of time jobs and pipelines wait for manual approvals.                                         |
| [Custom spans](https://docs.datadoghq.com/glossary/#custom-span)                                                                                 | Custom spans                        | Configure custom spans for your pipelines.                                                                    |
| [Filter CI Jobs on the critical path](https://docs.datadoghq.com/continuous_integration/guides/identify_highest_impact_jobs_with_critical_path/) | Filter CI Jobs on the critical path | Filter by jobs on the critical path.                                                                          |
| [Execution time](https://docs.datadoghq.com/glossary/#pipeline-execution-time)                                                                   | Execution time                      | View the amount of time pipelines have been running jobs.                                                     |

\*AWS CodePipeline running pipelines don't have Git information until they have finished.\**AWS CodePipeline logs correlation is only available for AWS CodeBuild actions.

### Terminology{% #terminology %}

This table shows the mapping of concepts between Datadog CI Visibility and AWS CodePipeline:

| Datadog  | AWS CodePipeline |
| -------- | ---------------- |
| Pipeline | Pipeline         |
| Stage    | Stage            |
| Job      | Action           |

## Configure the Datadog integration{% #configure-the-datadog-integration %}

To set up the integration between [AWS CodePipeline](https://aws.amazon.com/codepipeline/) and Pipeline Visibility, create two AWS resources.

{% dl %}

{% dt %}
[API Destination](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html)
{% /dt %}

{% dd %}
An HTTP endpoint pointing to Datadog's intake.
{% /dd %}

{% dt %}
[AWS EventBridge Rule](https://aws.amazon.com/eventbridge/)
{% /dt %}

{% dd %}
A rule that forwards CodePipeline events to the API destination.
{% /dd %}

{% /dl %}

You can create these resources separately, or at the same time, during the EventBridge Rule creation process. For more information about monitoring pipeline events, see the [official AWS guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html).

## Create the API destination{% #create-the-api-destination %}

1. In the AWS Console, navigate to **EventBridge > API destinations** and click **Create API destination**.
1. Choose a name for the API Destination (for example, `datadog-ci-visibility-api`) and optionally add a description.
1. Under **API destination endpoint**, input `https://webhook-intake.  /api/v2/webhook`.
1. Under **HTTP method**, select **POST**.
1. Under Connection type, select **Create a new connection**:
   1. Choose a name for the connection (for example, `datadog-ci-visibility-connection`) and optionally add a description.
   1. Under **Destination type**, select **Other**.
   1. Under **Authorization type**, select **API key**. Input `DD-API-KEY` as the **API key name** and add your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys) in the **Value** field.
1. Click **Create**.

## Create the EventBridge rule{% #create-the-eventbridge-rule %}

1. In the AWS Console, navigate to **EventBridge > Rules** and click **Create Rule**.

1. Choose a name for the rule (for example, `datadog-ci-visibility-integration`) and optionally add a description.

1. Leave the event bus as **default**, and under **Rule Type**, select **Rule with an event pattern**. Click **Next**.

1. Under **Event Source**, select **AWS events or EventBridge partner events**.

1. Under **Creation Method**, select **Custom pattern (JSON editor)**. Then, under **Event Pattern**, input the following:

   ```json
   {
     "source": ["aws.codepipeline"],
     "detail-type": ["CodePipeline Pipeline Execution State Change", "CodePipeline Action Execution State Change", "CodePipeline Stage Execution State Change"]
   }
   ```

The JSON above sets up the integration for all of your pipelines. To restrict the set of pipelines, follow the Only monitor specific pipelines section below.

1. Click **Next**.

1. Under **Target Types**, select **EventBridge API destination**. Then, choose **Use an existing API Destination** and select the API destination that you created in the previous step. Alternatively, you can also create the API destination by following the steps outlined in the Create the API Destination section.

1. Under **Headers Parameters**, click **Add header parameter**. Input `DD-CI-PROVIDER-AWSCODEPIPELINE` as the key and `true` as the value.

1. Choose **Create a new role for this specific resource** (or use an existing one).

1. Review that the information is correct and create the rule.

Once you've created the rule, you can monitor your pipelines in Datadog.

## Advanced configuration{% #advanced-configuration %}

### Only monitor specific pipelines{% #only-monitor-specific-pipelines %}

You can optionally restrict the pipelines that are monitored by Pipeline Visibility. To do this, add the `detail.pipeline` filter in the rule event pattern defined when creating the EventBridge Rule. For example:

```json
 {
   "source": ["aws.codepipeline"],
   "detail-type": ["CodePipeline Pipeline Execution State Change", "CodePipeline Action Execution State Change", "CodePipeline Stage Execution State Change"],
   "detail": {
     "pipeline": ["first-pipeline", "second-pipeline"]
   }
 }
```

The event pattern sets up the integration only for the `first-pipeline` and `second-pipeline` pipelines.

### Correlate pipelines with tests{% #correlate-pipelines-with-tests %}

If you are using [Test Optimization](https://docs.datadoghq.com/tests/) and your pipeline contains one or more [AWS CodeBuild](https://aws.amazon.com/codebuild/) actions to execute tests, you can correlate your tests with the related pipeline inside Datadog Pipeline Visibility. For instructions, refer to Add the pipeline execution ID.

### Collect job logs{% #collect-job-logs %}

The AWS CodePipeline integration supports correlating **CodeBuild** actions with their respective job and pipeline spans. To enable log collection for your CodeBuild actions, see the [AWS log forwarding guide](https://docs.datadoghq.com/logs/guide/send-aws-services-logs-with-the-datadog-lambda-function).

{% alert level="warning" %}
Log correlation for CodeBuild actions requires the CodeBuild project to have the default CloudWatch log group and log stream names.
{% /alert %}

Logs are billed separately from CI Visibility. Log retention, exclusion, and indexes are configured in Logs Settings. Logs for AWS CodeBuild can be identified by the `source:codebuild` and `sourcecategory:aws` tags.

### Add the pipeline execution ID as an environment variable{% #add-the-pipeline-execution-id-as-an-environment-variable %}

The pipeline execution ID is an identifier Datadog needs to uniquely identify a pipeline execution. Perform the following steps to assign a pipeline execution ID to correlate pipelines with tests and custom commands:

1. In the AWS Console, go to your pipeline configuration and click **Edit**
1. Go to the stage containing the AWS CodeBuild action, click **Edit Stage**, and then edit the relevant action.
1. Under **Environment variables**, add an environment variable. Name the variable `DD_PIPELINE_EXECUTION_ID`, and the value `#{codepipeline.PipelineExecutionId}`. Leave the type as *Plaintext*.
1. Click **Done** to save your changes.

The steps above allow you to add the pipeline execution ID to your CodeBuild action environment variables. For more information on working with variables, see the [official AWS guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html).

## Visualize pipeline data in Datadog{% #visualize-pipeline-data-in-datadog %}

View your data on the [**CI Pipeline List**](https://app.datadoghq.com/ci/pipelines) and [**Executions**](https://app.datadoghq.com/ci/pipeline-executions) pages after the pipelines finish.

The **CI Pipeline List** page shows data for only the default branch of each repository. For more information, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/#search-for-pipelines).

## Further reading{% #further-reading %}

- [Explore Pipeline Execution Results and Performance](https://docs.datadoghq.com/continuous_integration/pipelines)
- [Troubleshooting CI Visibility](https://docs.datadoghq.com/continuous_integration/troubleshooting/)
- [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_integration/search/)
- [Monitor and improve your CI/CD on AWS CodePipeline with Datadog CI Visibility](https://www.datadoghq.com/blog/aws-codepipeline-ci-visibility/)
