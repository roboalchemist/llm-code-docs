# Source: https://docs.datadoghq.com/security/default_rules/rxi-7oi-e5x.md

---
title: S3 buckets should have versioning enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 buckets should have versioning
  enabled
---

# S3 buckets should have versioning enabled

## Description{% #description %}

Enable versioning on S3 buckets to keep multiple versions of an object in one bucket.

## Rationale{% #rationale %}

Versioning-enabled buckets help [recover objects in the case of accidental deletion or overwriting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) AWS documentation to enable bucket versioning within the S3 console.

### From the command line{% #from-the-command-line %}

Follow the [Enabling versioning on buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) AWS documentation to enable bucket versioning with the AWS CLI.
