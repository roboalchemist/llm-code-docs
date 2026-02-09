# Source: https://docs.datadoghq.com/security/default_rules/def-000-ua9.md

---
title: Neptune cluster replicates to a publicly accessible Neptune instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune cluster replicates to a
  publicly accessible Neptune instance
---

# Neptune cluster replicates to a publicly accessible Neptune instance

## Description{% #description %}

A private Neptune cluster replicating to a publicly accessible Neptune read replica instance increases the likelihood of unauthorized data access. If the public Neptune read replica instance is accessed, it could lead to unauthorized data access or destruction of sensitive information replicated from the private Neptune cluster.

## Remediation{% #remediation %}

1. Create a new Neptune read replica instance. Review [Adding Neptune reader instances to a DB Cluster](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-add-replicas.html) for more information on how to create a Neptune read replica instance.

Note: You cannot change public accessibility on a Neptune read replica instance. If you need to disable public accessibility, create a new Neptune read replica instance and migrate the data to the new instance.
