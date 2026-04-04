# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/mysql_enforce_ssl_connection_disabled.md

---
title: ssl_enforcement_enabled is not set to ENABLED for MySQL database server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ssl_enforcement_enabled is not set to ENABLED
  for MySQL database server
---

# ssl_enforcement_enabled is not set to ENABLED for MySQL database server

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c3f2e1d0-b9a8-7c6d-5e4f-3210fedcba98`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/3.6.0/docs/resources/mysql_server)

### Description{% #description %}

When SSL enforcement is disabled on Azure MySQL Database Servers, connections to the database are vulnerable to man-in-the-middle attacks and data interception. This security vulnerability allows attackers to potentially capture sensitive data transmitted between client applications and the database server, including credentials, personally identifiable information, and business-critical data. To secure your MySQL server, you must explicitly set `ssl_enforcement_enabled` to `ENABLED`, as shown below:

```terraform
resource "azurerm_mysql_server" "good_example" {
  name                = "good-mysql-server"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled = ["ENABLED"]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_mysql_server" "good_example" {
  name                = "good-mysql-server"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled = ["ENABLED"] # â Correct setting
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_mysql_server" "bad_example" {
  name                = "bad-mysql-server"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled = ["DISABLED"] # â SSL enforcement is not enabled
}
```
