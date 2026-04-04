# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/databricks/unrestricted_acl.md

---
title: Beta - unrestricted Databricks ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - unrestricted Databricks ACL
---

# Beta - unrestricted Databricks ACL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `2c4fe4a9-f44b-4c70-b09b-5b75cd251805`

**Cloud Provider:** Databricks

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/ip_access_list)

### Description{% #description %}

Flags `databricks_ip_access_list` resources where the `ip_addresses` attribute includes `0.0.0.0/0` or `::/0`. These CIDRs allow unrestricted ingress, which is insecure and exposes the workspace.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "databricks_workspace_conf" "negative" {
  custom_config = {
    "enableIpAccessLists" : true
  }
}

resource "databricks_ip_access_list" "negative" {
  label     = "allow_in"
  list_type = "ALLOW"
  ip_addresses = [
    "1.2.3.0/24",
    "1.2.5.0/24"
  ]
  depends_on = [databricks_workspace_conf.negative]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "databricks_workspace_conf" "positive2" {
  custom_config = {
    "enableIpAccessLists" : true
  }
}

resource "databricks_ip_access_list" "positive2" {
  label     = "allow_in"
  list_type = "ALLOW"
  ip_addresses = [
    "::/0",
    "1.2.5.0/24"
  ]
  depends_on = [databricks_workspace_conf.positive2]
}
```

```terraform
resource "databricks_workspace_conf" "positive1" {
  custom_config = {
    "enableIpAccessLists" : true
  }
}

resource "databricks_ip_access_list" "positive1" {
  label     = "allow_in"
  list_type = "ALLOW"
  ip_addresses = [
    "0.0.0.0/0",
    "1.2.5.0/24"
  ]
  depends_on = [databricks_workspace_conf.positive1]
}
```
