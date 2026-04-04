# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/gke_using_default_service_account.md

---
title: GKE using default service account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > GKE using default service account
---

# GKE using default service account

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `1c8eef02-17b1-4a3e-b01d-dcc3292d2c38`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#node_config)

### Description{% #description %}

Kubernetes Engine Clusters should not be configured to use the default service account. Using the default service account (`node_config.service_account` not set) can grant workloads excessive permissions, increasing the risk of privilege escalation and unauthorized access to other Google Cloud resources if a node is compromised. To mitigate this, assign a dedicated and minimally privileged service account as shown below:

```
resource "google_container_cluster" "example" {
  // ...
  node_config {
    service_account = google_service_account.custom_sa.email
    // ...
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_container_cluster" "negative1" {
  name     = "my-gke-cluster"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1

  node_config {
    service_account = google_service_account.myserviceaccount.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    labels = {
      foo = "bar"
    }
    tags = ["foo", "bar"]
  }
  timeouts {
    create = "30m"
    update = "40m"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_container_cluster" "positive2" {
  name     = "my-gke-cluster"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1

  node_config {
    service_account = google_service_account.default.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    labels = {
      foo = "bar"
    }
    tags = ["foo", "bar"]
  }
  timeouts {
    create = "30m"
    update = "40m"
  }
}
```

```terraform
resource "google_container_cluster" "positive1" {
  name     = "my-gke-cluster"
  location = "us-central1"
  remove_default_node_pool = true
  initial_node_count       = 1

  node_config {
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    labels = {
      foo = "bar"
    }
    tags = ["foo", "bar"]
  }
  timeouts {
    create = "30m"
    update = "40m"
  }
}
```
