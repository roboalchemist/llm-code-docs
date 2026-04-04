# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/storage_table_allows_all_acl_permissions.md

---
title: Storage table allows all ACL permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Storage table allows all ACL permissions
---

# Storage table allows all ACL permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3ac3e75c-6374-4a32-8ba0-6ed69bda404e`

**Cloud Provider:** Azure

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/storage_table#permissions)

### Description{% #description %}

Allowing all Access Control List (ACL) permissions (`rwdl` for read, write, delete, and list) on an Azure storage Table grants overly broad access, increasing the risk of unauthorized data modification or deletion. This misconfiguration may lead to data leakage, loss, or manipulation if the credentials are compromised or abused. To enhance security, permissions should be limited to only those operations necessary for the application's function, such as using only `r` for read access:

```
resource "azurerm_storage_table" "table_resource2" {
  name                 = "my_table_name"
  storage_account_name = "mystoragexxx"
  acl {
    id = "someid-1XXXXXXXXX"
    access_policy {
      expiry = "2022-10-03T05:05:00.0000000Z"
      permissions = "r"
      start = "2021-05-28T04:05:00.0000000Z"
    }
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "azurerm_storage_table" "table_resource2" {
  name                 = "my_table_name"
  storage_account_name = "mystoragexxx"
  acl {
    id = "someid-1XXXXXXXXX"
    access_policy {
      expiry = "2022-10-03T05:05:00.0000000Z"
      permissions = "r"
      start = "2021-05-28T04:05:00.0000000Z"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "azurerm_storage_table" "table_resource" {
  name                 = "my_table_name"
  storage_account_name = "mystoragexxx"
  acl {
    id = "someid-1XXXXXXXXX"
    access_policy {
      expiry = "2022-10-03T05:05:00.0000000Z"
      permissions = "rwdl"
      start = "2021-05-28T04:05:00.0000000Z"
    }
  }
}
```
