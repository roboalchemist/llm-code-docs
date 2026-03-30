# Source: https://docs.datadoghq.com/security/default_rules/def-000-rdc.md

---
title: Access to Azure services for PostgreSQL Database Server should be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Access to Azure services for PostgreSQL
  Database Server should be disabled
---

# Access to Azure services for PostgreSQL Database Server should be disabled

## Description{% #description %}

Disable access from Azure services to PostgreSQL Database Server. If access from Azure services is enabled, the server's firewall will accept connections from all Azure resources, including resources not in your subscription. This is usually not a desired configuration. Instead, set up firewall rules to allow access from specific network ranges or VNET rules to allow access from specific virtual networks.

## Remediation{% #remediation %}

To disable this [firewall rule](https://learn.microsoft.com/en-us/azure/postgresql/single-server/concepts-firewall-rules) on your Azure PostgreSQL Server, follow these steps:

1. Log in to [Azure Portal](https://portal.azure.com).
1. Go to **Azure Database for PostgreSQL server**.
1. For each database, click on **Connection security**.
1. In **Firewall rules**, ensure **Allow access to Azure services** is set to **OFF**.
1. Click **Save** to apply the changed rule.
