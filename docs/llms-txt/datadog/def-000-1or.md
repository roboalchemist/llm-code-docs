# Source: https://docs.datadoghq.com/security/default_rules/def-000-1or.md

---
title: Neptune DB clusters should be deployed across multiple Availability Zones
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Neptune DB clusters should be deployed
  across multiple Availability Zones
---

# Neptune DB clusters should be deployed across multiple Availability Zones
 
## Description{% #description %}

This control verifies whether an Amazon Neptune DB cluster has read replica instances spread across multiple Availability Zones (AZs). The control fails if the cluster is only deployed in a single AZ.

Read replica instances play a crucial role as failover targets during AZ outages or routine maintenance. In the event of a primary instance failure, Neptune promotes a read replica to become the new primary instance. However, if no read replica is present, the DB cluster remains unavailable until the primary instance is re-created, which takes significantly longer than promoting a read replica. To enhance high availability, it is recommended to deploy one or more read replica instances with the same DB instance class as the primary instance and place them in different AZs.

## Remediation{% #remediation %}

For guidance on configuring availability zones, please refer to the [Read replica DB instances in a Neptune DB cluster][1] section of the Neptune User Guide.

[1]: [https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-db-clusters.html#feature-overview-read](https://docs.aws.amazon.com/neptune/latest/userguide/feature-overview-db-clusters.html#feature-overview-read) replicas
