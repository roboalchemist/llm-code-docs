# Source: https://docs.datadoghq.com/security/default_rules/hkp-p6b-f7w.md

---
title: S3 buckets should have 'Block Public Access' enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 buckets should have 'Block Public
  Access' enabled
---

# S3 buckets should have 'Block Public Access' enabled

## Description{% #description %}

Amazon S3 provides the `Block public access` bucket setting and the `Block public access` account setting to help restrict unintended public access to resources. By default, S3 buckets and objects are created without public access, but someone with sufficient permissions can enable public access at the bucket or object level, often unexpectedly. When you enable these settings, they prevent buckets, objects, or entire accounts from becoming publicly accessible, reducing the risk of accidental or malicious data exposure. Blocking public access should be an organizational decision based on data sensitivity, least privilege, and use case. Note that if a bucket is configured to host a static website, the **Block public access** setting must be disabled to serve the site.

## Remediation{% #remediation %}

For instructions on configuring Block Public Access settings, refer to [Blocking Public Access to S3 Resources](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/block-public-access-account.html).
