# Source: https://docs.datadoghq.com/security/default_rules/def-000-k1x.md

---
title: >-
  CloudFront distributions using origin access identity should be migrated to
  origin access control
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distributions using origin
  access identity should be migrated to origin access control
---

# CloudFront distributions using origin access identity should be migrated to origin access control

## Description{% #description %}

CloudFront distributions using Origin Access Identity (OAI) should be migrated to Origin Access Control (OAC) for enhanced security features, including signed requests, granular permissions, and support for AWS Identity and Access Management (IAM) policies. Additionally, OAC offers broader compatibility with various AWS origins, such as S3 and custom origins, enhancing both flexibility and security.

## Remediation{% #remediation %}

For guidance on migrating legacy OAI to OAC, refer to the [Migrating from origin access identity (OAI) to origin access control (OAC)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html#migrate-from-oai-to-oac) section of the Amazon CloudFront Developer Guide.
