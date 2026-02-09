# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/cosmosdb_account_ip_range_filter_not_set.md

---
title: CosmosDB account IP range filter not set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > CosmosDB account IP range filter not set
---

# CosmosDB account IP range filter not set

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c2a3efb6-8a58-481c-82f2-bfddf34bb4b7`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Critical

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/cosmosdb_account#ip_range_filter)

### Description{% #description %}

Azure CosmosDB Account IP range filter provides network-level access control for your database by restricting connections to specified IP addresses or ranges. When this filter is not configured, the database is potentially accessible from any IP address, exposing sensitive data to unauthorized access. Setting the `ip_range_filter` attribute (for example, 'ip_range_filter = "104.42.195.92"') limits access to only approved network locations, significantly enhancing your database security posture.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_cosmosdb_account" "negative1" {
  name                  = "example" 

  ip_range_filter       = "104.42.195.92"
  is_virtual_network_filter_enabled = true
 

}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_cosmosdb_account" "positive1" {
  name                  = "example" 
  is_virtual_network_filter_enabled = true
 

}
```
