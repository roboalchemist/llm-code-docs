# Source: https://docs.datadoghq.com/security/default_rules/def-000-etc.md

---
title: Azure storage accounts should not allow cross tenant replication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure storage accounts should not allow
  cross tenant replication
---

# Azure storage accounts should not allow cross tenant replication
 
## Description{% #description %}

Cross-tenant replication in Azure enables replicating storage account data from a source in one Azure AD tenant to a destination in another. This allows replication of data outside of your tenant, significantly increasing the risk of data leakage and unauthorized access.

## Remediation{% #remediation %}

To disable cross-tenant replication, see [Prevent object replication across Microsoft Entra tenants](https://learn.microsoft.com/en-us/azure/storage/blobs/object-replication-prevent-cross-tenant-policies?tabs=portal).
