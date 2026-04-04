# Source: https://docs.datadoghq.com/security/default_rules/def-000-fp2.md

---
title: DynamoDB Accelerator (DAX) clusters should be encrypted at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DynamoDB Accelerator (DAX) clusters
  should be encrypted at rest
---

# DynamoDB Accelerator (DAX) clusters should be encrypted at rest

## Description{% #description %}

This control verifies whether an Amazon DynamoDB Accelerator (DAX) cluster has encryption enabled for data at rest.

Encrypting data at rest helps mitigate the risk of unauthorized access to data stored on disk. Encryption introduces additional access controls, restricting unauthorized users from accessing the data.

## Remediation{% #remediation %}

Once a cluster is created, encryption at rest cannot be enabled or disabled. To use encryption at rest, the cluster must be recreated with this setting enabled. For step-by-step guidance on creating a DAX cluster with encryption at rest, refer to the [Enabling encryption at rest using the AWS Management Console](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAXEncryptionAtRest.html#dax.encryption.tutorial-console) section of the Amazon DynamoDB Developer Guide.
