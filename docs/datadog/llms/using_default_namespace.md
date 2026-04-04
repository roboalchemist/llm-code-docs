# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/kubernetes/using_default_namespace.md

---
title: Using default namespace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Using default namespace
---

# Using default namespace

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `abcb818b-5af7-4d72-aba9-6dd84956b451`

**Cloud Provider:** Kubernetes

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/pod#namespace)

### Description{% #description %}

Resources must not use the `default` namespace. This rule flags Kubernetes resources that either lack `metadata` or `metadata.namespace`, or have `metadata.namespace` set to `default`. It applies to resource kinds: `kubernetes_ingress`, `kubernetes_config_map`, `kubernetes_secret`, `kubernetes_service`, `kubernetes_cron_job`, `kubernetes_service_account`, `kubernetes_role`, `kubernetes_role_binding`, `kubernetes_pod`, `kubernetes_deployment`, `kubernetes_daemonset`, `kubernetes_job`, `kubernetes_stateful_set`, `kubernetes_replication_controller`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "kubernetes_pod" "test3" {
  metadata {
    name = "terraform-example"
    namespace = "terraform-namespace"
  }
}

resource "kubernetes_cron_job" "test4" {
  metadata {
    name = "terraform-example"
    namespace = "terraform-namespace"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "kubernetes_pod" "test" {
  metadata {
    name = "terraform-example"
    namespace = "default"
  }
}

resource "kubernetes_cron_job" "test2" {
  metadata {
    name = "terraform-example"
  }
}
```
