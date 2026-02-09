# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/mariadb_not_using_latest_tls.md

---
title: Ensure Azure MariaDB server is using latest TLS (1.2)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Ensure Azure MariaDB server is using latest
  TLS (1.2)
---

# Ensure Azure MariaDB server is using latest TLS (1.2)

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8f0e6b2d-3c9a-4f1e-8d2a-7b6c5d4e3f21`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/3.117.1/docs/resources/mariadb_server#ssl_minimal_tls_version_enforced-1)

### Description{% #description %}

Using outdated TLS versions in Azure MariaDB servers exposes your database to known vulnerabilities and encryption weaknesses, potentially allowing attackers to intercept and decrypt sensitive data. Without proper SSL enforcement and TLS 1.2 (or higher) configuration, your database communications remain susceptible to man-in-the-middle attacks and other security exploits that have been addressed in newer TLS versions.

To secure your Azure MariaDB server, you must set both the `ssl_enforcement_enabled` flag to `true` and `ssl_minimal_tls_version_enforced` to `TLS1_2`, as shown in the following example:

```terraform
resource "azurerm_mariadb_server" "good_example" {
  name                = "good-mariadb-server"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled          = ["true"]
  ssl_minimal_tls_version_enforced = ["TLS1_2"]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# Passing example: ssl_minimal_tls_version_enforced not defined (defaults to TLS1_2)
resource "azurerm_mariadb_server" "good_example_default" {
  name                = "good-mariadb-server-default"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled = ["true"]
  # ssl_minimal_tls_version_enforced not specified â defaults to TLS1_2
}
```

```terraform
# Passing example: Correct enforcement and TLS settings
resource "azurerm_mariadb_server" "good_example" {
  name                = "good-mariadb-server"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled          = ["true"]
  ssl_minimal_tls_version_enforced = ["TLS1_2"] # Correct setting
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# Failing example: ssl_enforcement_enabled is not "true"
resource "azurerm_mariadb_server" "bad_example" {
  name                = "bad-mariadb-server"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled          = ["false"]  # â Incorrect value
  ssl_minimal_tls_version_enforced = ["TLS1_2"] # Even if TLS is correct, enforcement flag is wrong
}

# Failing example: ssl_enforcement_enabled is "true" but minimal TLS is set incorrectly
resource "azurerm_mariadb_server" "bad_example2" {
  name                = "bad-mariadb-server-2"
  location            = "East US"
  resource_group_name = "example-rg"

  ssl_enforcement_enabled          = ["true"]
  ssl_minimal_tls_version_enforced = ["TLS1_0"] # â Incorrect TLS version
}
```
