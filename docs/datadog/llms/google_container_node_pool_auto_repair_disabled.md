# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/google_container_node_pool_auto_repair_disabled.md

---
title: Google Container node pool auto repair disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Container node pool auto repair
  disabled
---

# Google Container node pool auto repair disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `acfdbec6-4a17-471f-b412-169d77553332`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_node_pool)

### Description{% #description %}

Enabling auto repair for Google Kubernetes Engine (GKE) node pools ensures that failed or unhealthy nodes are automatically detected and repaired, maintaining cluster health and minimizing manual intervention. If the `auto_repair` attribute is set to `false` or omitted in a Terraform resource, as in the following configuration, unhealthy nodes may persist and degrade application availability or introduce operational risks:

```
management {
  auto_repair = false
}
```

To address this, set `auto_repair` to `true` in your Terraform configuration:

```
management {
  auto_repair = true
}
```

This configuration helps maintain a resilient and self-healing node environment in your GKE cluster.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_container_cluster" "negative1" {
  name     = "my-gke-cluster"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "negative2" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.primary.name
  node_count = 1

  management {
    auto_repair  = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_container_cluster" "positive1" {
  name     = "my-gke-cluster"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1
}

resource "google_container_node_pool" "positive2" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.primary.name
  node_count = 1

  management {
    auto_repair  = false
  }
}

resource "google_container_node_pool" "positive3" {
  name       = "my-node-pool"
  location   = "us-central1"
  cluster    = google_container_cluster.primary.name
  node_count = 1
}
```
