# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/shielded_gke_nodes_disabled.md

---
title: Shielded GKE nodes disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Shielded GKE nodes disabled
---

# Shielded GKE nodes disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `579a0727-9c29-4d58-8195-fc5802a8bdb4`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#enable_shielded_nodes)

### Description{% #description %}

GKE cluster nodes should be launched with Shielded VM enabled by setting the `enable_shielded_nodes` attribute to `true` in the `google_container_cluster` resource. Failing to enable Shielded VM features exposes cluster nodes to potential rootkit and boot-level malware attacks, as these features help ensure node integrity through secure boot and trusted platform module (TPM) protections. For secure configuration, use:

```
resource "google_container_cluster" "secure" {
  name                  = "my-gke-cluster"
  location              = "us-central1"
  enable_shielded_nodes = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_container_cluster" "negative1" {
  name                  = "my-gke-cluster"
  location              = "us-central1"
  enable_shielded_nodes = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_container_cluster" "false" {
  name                  = "my-gke-cluster"
  location              = "us-central1"
  enable_shielded_nodes = false
}
```
