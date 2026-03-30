# Source: https://docs.datadoghq.com/security/default_rules/def-000-tnm.md

---
title: Neptune DB clusters should be configured to copy tags to snapshots
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune DB clusters should be
  configured to copy tags to snapshots
---

# Neptune DB clusters should be configured to copy tags to snapshots

## Description{% #description %}

This control verifies whether a Neptune DB cluster is set to automatically copy all tags to its snapshots when they are created.

Maintaining an accurate inventory of your IT assets is vital for governance and security purposes. It's recommended to tag snapshots in the same manner as their parent Amazon RDS database clusters. By copying tags, you ensure that the metadata for the snapshots aligns with that of the parent clusters and that the access policies for the snapshots mirror those of the parent DB instances.

## Remediation{% #remediation %}

For guidance on copying tags to snapshots, please refer to the [Copying tags in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/tagging.html#tagging-overview) section of the Neptune User Guide.
