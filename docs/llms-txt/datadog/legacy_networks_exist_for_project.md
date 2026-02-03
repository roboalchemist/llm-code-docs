# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/legacy_networks_exist_for_project.md

---
title: Ensure legacy networks do not exist for a project
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Ensure legacy networks do not exist for a
  project
---

# Ensure legacy networks do not exist for a project

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `550e8400-e29b-41d4-a716-446655440000`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://cloud.google.com/vpc/docs/legacy)

### Description{% #description %}

Legacy networks in Google Cloud Platform (GCP) with `auto_create_subnetworks` enabled represent a significant security risk as they automatically create subnets with predefined IP ranges in every region. This can lead to overly permissive network configurations and potentially expose internal services to unauthorized access or lateral movement within your infrastructure.

The secure configuration (as shown below) explicitly avoids enabling auto-created subnetworks, giving administrators complete control over subnet creation and IP addressing:

```hcl
resource "google_compute_network" "legacy_network_2" {
  name = "legacy-network"
}
```

Insecure configuration example with `auto_create_subnetworks` enabled:

```hcl
resource "google_compute_network" "legacy_network" {
  name                    = "legacy-network"
  auto_create_subnetworks = true
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_network" "modern_network" {
  name                    = "modern-network"
  auto_create_subnetworks = false
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_network" "legacy_network" {
  name                    = "legacy-network"
  auto_create_subnetworks = true
}
```
