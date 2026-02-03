# Source: https://docs.datadoghq.com/security/default_rules/def-000-k8k.md

---
title: Azure Key Vault should use RBAC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Key Vault should use RBAC
---

# Azure Key Vault should use RBAC
 
## Rationale:{% #rationale %}

This detection identifies Azure Key Vaults with `enable_rbac_authorization` not set to `true`. This identifies Key Vaults where RBAC authentication is not implemented.

## Remediation:{% #remediation %}

1. Evaluate the need for the access policy permissions model in your Key Vault.
1. If not required, migrate your Key Vault to the RBAC permissions model [following guidance from Microsoft](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-migration).
