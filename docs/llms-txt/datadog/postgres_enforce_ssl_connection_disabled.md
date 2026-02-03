# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/postgres_enforce_ssl_connection_disabled.md

---
title: ssl_enforcement_enabled is not set to ENABLED for PostgreSQL database server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ssl_enforcement_enabled is not set to ENABLED
  for PostgreSQL database server
---

# ssl_enforcement_enabled is not set to ENABLED for PostgreSQL database server

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `93f9tyjk-e5f6-7890-ab12-cd34ef567890`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/postgresql_server)

### Description{% #description %}

SSL/TLS encryption is essential for PostgreSQL Database Servers to protect sensitive data during transmission between the client and server. When `ssl_enforcement_enabled` is not set to `ENABLED`, data transferred between clients and the database is vulnerable to eavesdropping, man-in-the-middle attacks, and data tampering. This security vulnerability could lead to unauthorized access and data exposure.

Insecure configuration example:

```terraform
resource "azurerm_postgresql_server" "bad_example" {
  // ... other configuration
  ssl_enforcement_enabled = ["DISABLED"] // Insecure
}
```

Secure configuration example:

```terraform
resource "azurerm_postgresql_server" "good_example" {
  // ... other configuration
  ssl_enforcement_enabled = ["ENABLED"] // Secure setting
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_postgresql_server" "good_example" {
  name                = "good-postgresql-server"
  location            = "East US"
  resource_group_name = "example-rg"
  sku_name            = "B_Gen5_1"
  version             = "9.6"

  ssl_enforcement_enabled = ["ENABLED"] # â Correct setting
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_postgresql_server" "bad_example" {
  name                = "bad-postgresql-server"
  location            = "East US"
  resource_group_name = "example-rg"
  sku_name            = "B_Gen5_1"
  version             = "9.6"

  ssl_enforcement_enabled = ["DISABLED"] # â SSL enforcement is not enabled
}
```
