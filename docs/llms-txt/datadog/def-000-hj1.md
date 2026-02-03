# Source: https://docs.datadoghq.com/security/default_rules/def-000-hj1.md

---
title: Private Endpoints should be used to access Storage Accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Private Endpoints should be used to
  access Storage Accounts
---

# Private Endpoints should be used to access Storage Accounts
 
## Description{% #description %}

Private endpoints for your Azure Storage accounts allow clients and services to securely access data located over a network through an encrypted Private Link. Securing traffic between services through encryption protects the data from easy interception and reading.

## Remediation{% #remediation %}

1. Identify Azure Storage accounts that do not require public access.
1. Review the ['Use private endpoints for Azure Storage'](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints).
1. Create the private endpoint by using [Azure CLI](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-cli) or [Azure Powershell](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-powershell)
