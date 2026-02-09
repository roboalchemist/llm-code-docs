# Source: https://docs.datadoghq.com/security/default_rules/def-000-maz.md

---
title: DocumentDB clusters should have deletion protection enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DocumentDB clusters should have
  deletion protection enabled
---

# DocumentDB clusters should have deletion protection enabled
 
## Description{% #description %}

This feature verifies if deletion protection is active on an Amazon DocumentDB cluster. The feature will not pass if deletion protection is not enabled.

Deletion protection provides an extra level of security to prevent accidental deletion of databases or unauthorized deletions. A cluster with deletion protection enabled cannot be deleted. Prior to deleting a cluster, deletion protection must be disabled. Deletion protection is automatically enabled when creating a cluster in the Amazon DocumentDB console.

## Remediation{% #remediation %}

To activate deletion protection for an already existing Amazon DocumentDB cluster, refer to the section on [modifying a cluster in the Amazon DocumentDB Developer Guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/db-cluster-modify.html). In the `Modify Cluster` section, select the option to enable deletion protection.
