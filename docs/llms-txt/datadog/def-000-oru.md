# Source: https://docs.datadoghq.com/security/default_rules/def-000-oru.md

---
title: DMS replication instances should not be public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DMS replication instances should not be
  public
---

# DMS replication instances should not be public
 
## Description{% #description %}

This control evaluates the `PubliclyAccessible` field to confirm that AWS DMS replication instances are not publicly accessible.

Private replication instances, which use private IP addresses, are inaccessible from outside the network. When source and target databases share the same network, ensure the instance is private and connected to its VPC via AWS Direct Connect, VPC peering, or VPN.

## Remediation{% #remediation %}

The public access setting for a DMS instance cannot be changed after creation. To disable public access, [delete the instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Deleting.html) and [create a new one](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html), leaving the **Publicly accessible** option off.
