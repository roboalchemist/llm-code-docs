# Source: https://docs.datadoghq.com/security/default_rules/def-000-pjl.md

---
title: RDS instances should be configured to use Enhanced Monitoring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS instances should be configured to
  use Enhanced Monitoring
---

# RDS instances should be configured to use Enhanced Monitoring

## Description{% #description %}

This control evaluates if Enhanced Monitoring is activated for an Amazon Relational Database Service (RDS) DB instance. In Amazon RDS, Enhanced Monitoring allows for a more immediate response to performance variations in the underlying infrastructure. Such variations could impact the availability of data. Enhanced Monitoring delivers real-time operating system metrics of the RDS instance. An installed agent on the instance collects metrics with greater precision compared to the hypervisor layer. Enhanced Monitoring metrics are also beneficial for visualizing CPU usage by different processes or threads on an RDS instance. To learn more, refer to the [Enhanced Monitoring section of the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Enabling.html).

## Remediation{% #remediation %}

For guidance on how to enable Enhanced Monitoring for your DB instance, refer to [Setting up for and enabling Enhanced Monitoring in the Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html).
