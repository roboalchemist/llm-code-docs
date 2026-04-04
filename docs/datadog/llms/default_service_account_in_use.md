# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/default_service_account_in_use.md

---
title: Default service account in use
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Default service account in use
---

# Default service account in use

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `737a0dd9-0aaa-4145-8118-f01778262b8a`

**Cloud Provider:** Kubernetes

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/service_account#automount_service_account_token)

### Description{% #description %}

Default service accounts should not be actively used. The `kubernetes_service_account` resource named `default` must include the `automount_service_account_token` attribute and it must be set to `false`. If `automount_service_account_token` is missing, add `automount_service_account_token = false`; if it is set to `true`, replace it with `false`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "kubernetes_service_account" "example3" {
  metadata {
    name = "default"
  }

  automount_service_account_token = false
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "kubernetes_service_account" "example" {
  metadata {
    name = "default"
  }
}

resource "kubernetes_service_account" "example2" {
  metadata {
    name = "default"
  }

  automount_service_account_token = true
}
```
