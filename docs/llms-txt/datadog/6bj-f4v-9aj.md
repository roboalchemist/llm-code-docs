# Source: https://docs.datadoghq.com/security/default_rules/6bj-f4v-9aj.md

---
title: >-
  PostgreSQL Database ingress traffic should be restricted to specified IP
  addresses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > PostgreSQL Database ingress traffic
  should be restricted to specified IP addresses
---

# PostgreSQL Database ingress traffic should be restricted to specified IP addresses
 
## Description{% #description %}

Ensure that no PostgreSQL Databases allow ingress from 0.0.0.0/0 (ANY IP).

## Rationale{% #rationale %}

PostgreSQL Server includes a firewall to block access to unauthorized connections. More granular IP addresses can be defined by referencing the range of addresses available from specific datacenters.

### Impact{% #impact %}

Disabling Allow access to Azure Services will break all connections to PostgreSQL server and Hosted Databases unless custom IP specific rules are not added in Firewall Policy.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to PostgreSQL servers
1. For each PostgreSQL server, click on Firewall / Virtual Networks
1. Set Allow access to Azure services to `OFF`
1. Set firewall rules to limit access to only authorized connections

### Using PowerShell{% #using-powershell %}

Disable default firewall rule "Allow access to Azure services":

```powershell
Remove-AzPostgreSqlFirewallRule -Name "AllowAllWindowsAzureIps" -ResourceGroupName <resource group name> -ServerName <server name>
```

Remove custom firewall rule:

```powershell
Remove-AzPostgreSqlFirewallRule -Name <name> -ResourceGroupName <resource group name> -ServerName <server name>
```

Set the appropriate firewall rules:

```powershell
New-AzPostgreSqlFirewallRule -Name "<rule name>" -ResourceGroupName "<resource group name>" -ServerName "<server name>" -EndIPAddress "<IP Address other than 0.0.0.0>" -StartIPAddress "<IP Address other than 0.0.0.0 or 255.255.255.255>"
```

## References{% #references %}

1. [https://docs.microsoft.com/en-us/azure/postgresql/concepts-firewall-rules](https://docs.microsoft.com/en-us/azure/postgresql/concepts-firewall-rules)
