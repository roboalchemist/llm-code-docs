# Source: https://docs.datadoghq.com/actions/connections/aws_integration.md

---
title: Use the AWS Integration in Actions
description: >-
  Use Datadog's built-in AWS Integration to run Workflows read Actions without
  additional configuration in AWS.
breadcrumbs: Docs > Connections > Use the AWS Integration in Actions
---

# Use the AWS Integration in Actions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog Workflows and Actions can use your existing Datadog AWS integration credentials to perform read-only operations in your AWS environment. This eliminates the need to manually configure a separate AWS Connection, simplifying onboarding and allowing immediate access to your AWS data.

When configured, Datadog uses the same AWS credentials that power integrations such as Amazon EC2, RDS, and S3 monitoring to securely execute supported read-only actions.

There are two ways to execute AWS actions in your environment:

- Use the Datadog AWS Integration to execute **Read-only** actions allowed under the [`ViewOnlyAccess` permissions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ViewOnlyAccess.html) policy.
- Or, use a custom AWS Connection linked to a **dedicated AWS IAM Role** with specific permissions, for operations not included in the [`ViewOnlyAccess` permissions](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ViewOnlyAccess.html).

This guide walks through how to use the Datadog AWS Integration to execute **Read-only** actions allowed under the [ViewOnlyAccess permissions policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ViewOnlyAccess.html). To execute other AWS actions, you need to [create a custom Connection](https://docs.datadoghq.com/actions/connections/?tab=workflowautomation#work-with-connections) instead.

## Supported use cases{% #supported-use-cases %}

Examples include:

- Listing or describing AWS resources (such as `ListECSClusters`, `DescribeInstances`, and `GetBucketPolicy`)
- Reading configurations or metadata from AWS services (such as `GetFunctionConfiguration`, and `ListSecrets`)
- Inspecting resource tags, metrics, or logs

For other actions, use a [dedicated Connection](https://docs.datadoghq.com/actions/connections/?tab=workflowautomation#work-with-connections) instead.

### Requirements{% #requirements %}

To successfully execute actions with this integration:

- The **AWS Integration IAM Role** configured for Role Delegation must have the permissions required for the operations desired (such as `ecs:ListClusters`).
- The selected action must be read-only. Write or mutating actions (such as `Put*`, `Delete*`, and `Update*`) are not supported and fail when running.
- The user, user's team, or user's org **must** have been given explicit 'Executor' permission on the AWS Integration in Datadog (more details below).

{% alert level="info" %}
Executing actions using the Datadog AWS Integration is only available for users that have set up the Datadog AWS Integration through role delegation. Additionally, while operations under the ViewOnlyAccess permissions are allowed, the IAM Role associated with the Datadog AWS Integration may not have the permissions needed. Make sure that the role has the correct permissions if you encounter issues.
{% /alert %}

## Configuration{% #configuration %}

{% alert level="info" %}
Before getting started, make sure these conditions have been met:
- The AWS integration is active for your target AWS Account and no integration issues are detected by Datadog. If you haven't set up the AWS integration yet, you can follow the AWS integration setup guide.
- The IAM Role associated with the integration has the permissions for the correct operations (for example `ecs:ListClusters`).
- You have access to edit the permissions for the AWS account(s) you want to set up.

{% /alert %}

### 1. Configure AWS Integration permissions

To configure the **Executor** permission for the Datadog AWS Integration:

1. In Datadog, navigate to [**Integrations**](https://app.datadoghq.com/integrations).
1. Click the **Amazon Web Services** integration.
1. In the left pane, select the AWS Account you want to run actions with.
1. Click **Set Permissions**.
   - If you see a **Request Edit Access** button instead of a **Set Permissions** button, ask your Datadog organization's admin to add you as an Editor for the AWS account.
1. Select a user, term, or organization and click **Add**.
1. Under **People with access**, select the **Executor** permission.
1. Click **Save**.

### 2. Add the integration to an action

1. In [Workflow Automation](https://app.datadoghq.com/workflow), click the workflow you want to edit.
1. Add an AWS action, such as **List ECS Clusters**.
1. In the configuration pane, click the **Connection** dropdown and scroll to **Existing AWS Integrations**.
1. Select the AWS Account you configured in step one.
1. Click **Save**.
