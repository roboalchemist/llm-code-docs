# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/redis_entirely_accessible.md

---
title: Redis entirely accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Redis entirely accessible
---

# Redis entirely accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fd8da341-6760-4450-b26c-9f6d8850575e`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Critical

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/redis_firewall_rule)

### Description{% #description %}

This check identifies Azure Redis Cache instances with firewall rules that permit access from any IP address (`0.0.0.0/0`), effectively exposing the Redis cache to the entire internet. When firewall rules are configured with `start_ip` and `end_ip` set to `0.0.0.0`, it creates a significant security vulnerability by allowing unrestricted access to your Redis cache. Instead, restrict access by specifying a limited IP range, as shown below:

```
// Insecure configuration
resource "azurerm_redis_firewall_rule" "insecure" {
  start_ip = "0.0.0.0"
  end_ip   = "0.0.0.0"
}

// Secure configuration
resource "azurerm_redis_firewall_rule" "secure" {
  start_ip = "10.2.3.4"
  end_ip   = "10.3.4.5"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_redis_cache" "negative1" {
  name                = "redis${random_id.server.hex}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  capacity            = 1
  family              = "P"
  sku_name            = "Premium"
  enable_non_ssl_port = false

  redis_configuration {
    maxclients         = 256
    maxmemory_reserved = 2
    maxmemory_delta    = 2
    maxmemory_policy   = "allkeys-lru"
  }
}

resource "azurerm_redis_firewall_rule" "negative2" {
  name                = "someIPrange"
  redis_cache_name    = azurerm_redis_cache.example.name
  resource_group_name = azurerm_resource_group.example.name
  start_ip            = "10.2.3.4"
  end_ip              = "10.3.4.5"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_redis_cache" "positive1" {
  name                = "redis${random_id.server.hex}"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  capacity            = 1
  family              = "P"
  sku_name            = "Premium"
  enable_non_ssl_port = false

  redis_configuration {
    maxclients         = 256
    maxmemory_reserved = 2
    maxmemory_delta    = 2
    maxmemory_policy   = "allkeys-lru"
  }
}

resource "azurerm_redis_firewall_rule" "positive2" {
  name                = "someIPrange"
  redis_cache_name    = azurerm_redis_cache.example.name
  resource_group_name = azurerm_resource_group.example.name
  start_ip            = "0.0.0.0"
  end_ip              = "0.0.0.0"
}
```
