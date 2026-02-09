# Source: https://docs.datadoghq.com/continuous_integration/guides/infrastructure_metrics_with_gitlab.md

---
title: Correlate Infrastructure Metrics with GitLab Jobs in Datadog
description: >-
  Learn how to correlate infrastructure metrics with your GitLab Autoscale job
  executions.
breadcrumbs: >-
  Docs > Continuous Integration Visibility > CI Visibility Guides > Correlate
  Infrastructure Metrics with GitLab Jobs in Datadog
---

# Correlate Infrastructure Metrics with GitLab Jobs in Datadog

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% alert level="info" %}
This method only applies to runners using the "Instance" or "Docker Autoscaler" executors.
{% /alert %}

## Overview{% #overview %}

When you click on a GitLab job in the [CI Visibility Explorer](https://docs.datadoghq.com/continuous_integration/explorer/?tab=pipelineexecutions), you can access an **Infrastructure** tab with information about the host, system, host tags, host metrics, and more.

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/infrastructure_tab.77fde09c495939b511bd8ace545fdd57.png?auto=format"
   alt="The Infrastructure tab displaying information about a host and its system, along with host metrics such as CPU usage and load averages." /%}

This guide explains how to correlate infrastructure metrics with your GitLab jobs if you are using GitLab "Instance" or "Docker Autoscaler" executors and [CI Visibility](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab).

## Prerequisites{% #prerequisites %}

The Datadog Agent must be installed in the virtual machines (VM) where the GitLab jobs will be run. This is not where the [GitLab instance](https://docs.gitlab.com/runner/executors/instance.html) or the [Docker Autoscaler](https://docs.gitlab.com/runner/executors/docker_autoscaler.html) executor is running, but in the VMs that are created with the fleeting plugin.

## Ensure that the Datadog Agent is installed in your instances{% #ensure-that-the-datadog-agent-is-installed-in-your-instances %}

If you are using an [AWS Autoscaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html), you should make sure that the machine image that is configured in the template launches with the [Datadog Agent](https://docs.datadoghq.com/agent/).

To test that you have performed this step successfully, you can try executing a job and you should see the host appear on the [Infrastructure List page](https://app.datadoghq.com/infrastructure).

If you are using AWS, make sure that the host name is in the format `"i-xxxxx"`. If this is not the case, you should check that your instance is compatible with IMDSv1. For more information, see the [official AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html).

You can set this up inside the template of your AWS Autoscaling Group. The Datadog Agent uses the metadata service endpoint to resolve the host name.

## Set up CI Visibility and log collection for your GitLab jobs{% #set-up-ci-visibility-and-log-collection-for-your-gitlab-jobs %}

For instructions on setting up CI Visibility for your GitLab jobs, see [Set up Pipeline Visibility on a GitLab Pipeline](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab).

To test that you have performed the setup successfully, you can try running a GitLab pipeline and checking if it appears on the [**Executions** page](https://app.datadoghq.com/ci/pipeline-executions).

You must enable job log collection. You can check if Datadog is receiving the logs correctly by clicking on the Logs tab of your pipeline execution. Ensure GitLab job logs are indexed and include messages in the form `Instance <hostname> connected`. Users also need [log read access](https://docs.datadoghq.com/logs/guide/logs-rbac/) to see the Infrastructure tab. GitLab job logs include the `datadog.product:cipipeline` and `source:gitlab` tags, which you can use in [Log Indexes](https://docs.datadoghq.com/logs/indexes/) filters.

After you have completed these steps, your GitLab jobs should be correlated with infrastructure metrics. The correlation is per job and not pipeline, as different jobs may run on different hosts. The **Infrastructure** tab appears after the job is finished and Datadog receives the logs for that job.

## Further reading{% #further-reading %}

- [Set up CI Visibility on a GitLab pipeline](https://docs.datadoghq.com/continuous_integration/pipelines/gitlab)
- [Learn how to search and manage your pipeline executions](https://docs.datadoghq.com/continuous_integration/search/#pipeline-details-and-executions)
