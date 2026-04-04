# Source: https://docs.datadoghq.com/security/default_rules/def-000-bqd.md

---
title: AWS IAM user has a large permissions gap
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS IAM user has a large permissions
  gap
---

# AWS IAM user has a large permissions gap

## Description{% #description %}

To mitigate the impact of credential exposure or compromise, IAM policies should be scoped down to the least level of privilege needed to perform their responsibilities. This rule identifies when a user's policy's permissions are more broad than what is regularly used. Datadog considers a permissions gap to be large when the number of unused permissions is greater than 40% of the total permissions count.

## Rationale{% #rationale %}

By comparing what actions an IAM user performed recently with what the user's policies permit, we can identify a permissions gap. This gap should be removed to mitigate the impact of a potential compromise.

## Remediation{% #remediation %}

Datadog recommends reducing the permissions attached to an IAM user to the minimum necessary for it to fulfill its function. You can use AWS Access Advisor to identify effective permissions used by your instances, and use AWS IAM Access Analyzer to generate an IAM policy based on past CloudTrail events.

CloudTrail logs can be filtered in multiple ways that can impact rule detection.

1. CloudTrail logs forwarded to Datadog using the Datadog Forwarder Lambda function can be filtered through the `ExcludeAtMatch` parameter as detailed in the [log filtering section](https://docs.datadoghq.com/logs/guide/forwarder/?tab=cloudformation#log-filtering-optional) of the Datadog forwarder page. Check the Datadog Forwarder Lambda function settings for any unused permissions being excluded. If the unused permissions are part of the exclusion filters, remove the entries excluding the logs containing these permissions.
1. Please check AWS for any configured event selectors. Individual [trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-trails) can be configured to filter out events based on [Event Selectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_EventSelector.html). Please ensure forwarded logs don't have Event Selectors enabled.
