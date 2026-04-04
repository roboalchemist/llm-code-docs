# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/redis_not_updated_regularly.md

---
title: Redis not updated regularly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Redis not updated regularly
---

# Redis not updated regularly

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b947809d-dd2f-4de9-b724-04d101c515aa`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/redis_cache#patch_schedule)

### Description{% #description %}

Configuring an Azure Redis Cache without a regular patch schedule leaves the service vulnerable to missing important security and operational updates, increasing the risk of exploitation by attackers targeting known vulnerabilities. By using the `patch_schedule` block in Terraform, such as shown below, organizations can ensure updates are applied in a timely manner, minimizing the attack surface and helping maintain service reliability and compliance:

```
patch_schedule {
    day_of_week     = "Thursday"
    start_hour_utc  = 7
}
```

Failure to address this may result in exposure to security threats or outages due to unpatched software flaws.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_redis_cache" "negative1" {
    name                = "timeout-redis"
    location            = "West Europe"
    resource_group_name = azurerm_resource_group.example_rg.name
    subnet_id           = azurerm_subnet.example_redis_snet.id

    family              = "P"
    capacity            = 1
    sku_name            = "Premium"
    shard_count         = 1

    enable_non_ssl_port = false
    minimum_tls_version = "1.2"

    redis_configuration {
        enable_authentication   = true
        maxmemory_policy        = "volatile-lru"
    }

    patch_schedule {
        day_of_week     = "Thursday"
        start_hour_utc  = 7
    }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_redis_cache" "positive1" {
    name                = "timeout-redis"
    location            = "West Europe"
    resource_group_name = azurerm_resource_group.example_rg.name
    subnet_id           = azurerm_subnet.example_redis_snet.id

    family              = "P"
    capacity            = 1
    sku_name            = "Premium"
    shard_count         = 1

    enable_non_ssl_port = false
    minimum_tls_version = "1.2"

    redis_configuration {
        enable_authentication   = true
        maxmemory_policy        = "volatile-lru"
    }
}
```
