# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cos_node_image_not_used.md

---
title: COS node image not used
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > COS node image not used
---

# COS node image not used

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8a893e46-e267-485a-8690-51f39951de58`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_node_pool#node_config)

### Description{% #description %}

The node image type should be set to Container-Optimized OS (COS) to enhance security and streamline workloads in Google Kubernetes Engine (GKE). Using other image types, such as `WINDOWS_LTSC` or failing to specify the `image_type` attribute, can introduce unnecessary vulnerabilities or increase the attack surface by including unneeded components. To ensure nodes use a hardened and minimal OS, configure the `image_type` field in your node pool's `node_config` block to `"COS"` or `"COS_CONTAINERD"`:

```
node_config {
  image_type = "COS"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_container_cluster" "negative1" {
  name     = "my-gke-cluster"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1
}


resource "google_container_node_pool" "negative2" {
  project = "gcp_project"
  name    = "primary-pool"
  region  = "us-west1"
  cluster = google_container_cluster.primary.name

  node_config {
    image_type   = "COS"
  }
}

 resource "google_container_node_pool" "negative3" {
  project = "gcp_project"
  name    = "primary-pool2"
  region  = "us-west1"
  cluster = google_container_cluster.primary.name
 }

resource "google_container_node_pool" "negative4" {
  project = "gcp_project"
  name    = "primary-pool2"
  region  = "us-west1"
  cluster = google_container_cluster.primary.name

  node_config {
    image_type   = "COS_CONTAINERD"
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
  project = "gcp_project"
  name    = "primary-pool"
  region  = "us-west1"
  cluster = google_container_cluster.primary.name

  node_config {
    image_type   = "WINDOWS_LTSC"
  }
 }
```
