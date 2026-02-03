# Source: https://docs.datadoghq.com/security/cloud_siem/guide/setting-up-security-monitoring-for-aws.md

---
title: Setting Up Cloud SIEM for AWS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Cloud SIEM Guides > Setting Up Cloud
  SIEM for AWS
---

# Setting Up Cloud SIEM for AWS

## Overview{% #overview %}

With Datadog Cloud SIEM, detection rules are applied to all processed logs. AWS service logs are collected with a Datadog Lambda function. This Lambda triggers on S3 Buckets and forwards logs to Datadog. Follow the setup instructions below to get started:

## Setup{% #setup %}

1. Navigate to the [Security Configuration Setup page](https://app.datadoghq.com/security/configuration) in the Datadog app.
1. Select **Cloud SIEM**.
1. Under **Secure your cloud environment**, select AWS.
1. Complete the **Detect threats with cloud logs** setup.
1. (Optional) Complete the **Secure your hosts and containers** setup.
1. (Optional) Complete the **Detect threats in additional logging sources** setup.
