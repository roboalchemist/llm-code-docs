# Source: https://docs.datadoghq.com/security/default_rules/def-000-j5t.md

---
title: S3 general purpose buckets should have a lifecycle configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 general purpose buckets should have
  a lifecycle configuration
---

# S3 general purpose buckets should have a lifecycle configuration

## Description{% #description %}

This check verifies if an Amazon S3 general-purpose bucket has at least one active Lifecycle configuration in place. The check will fail if the bucket has no Lifecycle configurations, or if all Lifecycle configurations are disabled.

Implementing a lifecycle configuration for your S3 bucket allows you to define specific actions for objects throughout their lifecycle. For instance, you can set rules to move objects to a different storage class, archive them, or remove them after a certain period.

## Remediation{% #remediation %}

For guidance on configuring lifecycle policies, refer to the [Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) and [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) sections of the Amazon S3 User Guide.
