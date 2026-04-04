# Source: https://docs.datadoghq.com/security/default_rules/def-000-stp.md

---
title: Private endpoint connections on Azure SQL Database should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Private endpoint connections on Azure
  SQL Database should be enabled
---

# Private endpoint connections on Azure SQL Database should be enabled

## Description{% #description %}

This rule checks if private endpoint connections are enabled on Azure SQL Database. Private endpoint connections help secure communication between resources within a virtual network and the Azure SQL Database, reducing exposure to the public internet.

## Remediation{% #remediation %}

To enable private endpoint connections on Azure SQL Database, follow the instructions provided in the Azure documentation: [Enable private endpoint connections for an Azure SQL Database](https://docs.microsoft.com/en-us/azure/azure-sql/database/private-endpoint-overview#enable-private-endpoint-connections-for-an-azure-sql-database).
