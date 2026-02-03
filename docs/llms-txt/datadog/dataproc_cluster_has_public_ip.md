# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/dataproc_cluster_has_public_ip.md

---
title: Dataproc clusters has public IPs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Dataproc clusters has public IPs
---

# Dataproc clusters has public IPs

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d2c4b6a8-1234-4f56-9abc-def012345678`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataproc_cluster)

### Description{% #description %}

Google Cloud Dataproc clusters with public IP addresses are directly accessible from the internet, creating an expanded attack surface that could be exploited by malicious actors. When `internal_ip_only` is set to `false` or omitted, clusters receive both internal and external IP addresses, potentially exposing sensitive data processing operations and administrative interfaces to unauthorized access.

Secure configuration requires setting `internal_ip_only` to true as shown in this example:

```terraform
resource "google_dataproc_cluster" "good_example" {
  cluster_config {
    gce_cluster_config {
      internal_ip_only = true
    }
  }
}
```

The following is an insecure configuration that should be avoided:

```terraform
resource "google_dataproc_cluster" "bad_example" {
  cluster_config {
    gce_cluster_config {
      internal_ip_only = false
    }
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_dataproc_cluster" "good_example" {
  name   = "good-cluster"
  region = "us-central1"

  cluster_config {
    gce_cluster_config {
      internal_ip_only = true # â Private cluster (no public IP)
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_dataproc_cluster" "bad_example" {
  name   = "bad-cluster"
  region = "us-central1"

  cluster_config {
    gce_cluster_config {
      internal_ip_only = false # â Public IP enabled
    }
  }
}
```
