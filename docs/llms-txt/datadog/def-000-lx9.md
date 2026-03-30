# Source: https://docs.datadoghq.com/security/default_rules/def-000-lx9.md

---
title: Redshift clusters should not use the default database name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Redshift clusters should not use the
  default database name
---

# Redshift clusters should not use the default database name

## Description{% #description %}

This control verifies if the database name of an Amazon Redshift cluster has been changed from its default setting of `dev`.

When setting up a Redshift cluster, it is recommended to assign a unique database name instead of using the default. Default names are widely known and should be customized during configuration. For instance, using a common name could unintentionally allow access if referenced in IAM policy conditions.

## Remediation{% #remediation %}

Redshift cluster database names must be chosen when the cluster is created. For guidance on the creation process, refer to the [Getting started with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html) section of the Amazon Redshift Management Guide.
