# Source: https://docs.datadoghq.com/security/default_rules/def-000-zp9.md

---
title: Azure Bastion host should exist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Bastion host should exist
---

# Azure Bastion host should exist
 
## Description{% #description %}

Azure Bastion provides secure and seamless RDP/SSH connectivity to your virtual machines directly in the Azure portal over SSL. When you connect through Azure Bastion, your virtual machines do not need a public IP address, agent, or special client software.

## Remediation{% #remediation %}

To create a Bastion host, see [Create a Bastion host](https://docs.microsoft.com/en-us/azure/bastion/quickstart-host-portal).
