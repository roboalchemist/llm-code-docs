# Source: https://docs.datadoghq.com/security/default_rules/def-000-bxd.md

---
title: RDS clusters should be configured to copy tags to snapshots
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS clusters should be configured to
  copy tags to snapshots
---

# RDS clusters should be configured to copy tags to snapshots
 
## Description{% #description %}

This control verifies RDS DB clusters are set to automatically copy all tags to snapshots upon creation. Proper identification and inventory management of IT assets are fundamental for robust governance and security. Full visibility into your RDS DB clusters allows you to evaluate their security status and address vulnerabilities effectively. Snapshots should carry the same tags as their parent database clusters to maintain consistency. Enabling tag inheritance ensures that snapshots adopt the tags of their parent clusters, which aids in asset management and security tracking.

## Remediation{% #remediation %}

To configure tags to automatically copy to snapshots for an RDS DB cluster, refer to the [Modifying the DB cluster section in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html#Aurora.Modifying.Cluster).
