# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/gke_legacy_authorization_enabled.md

---
title: GKE legacy authorization enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > GKE legacy authorization enabled
---

# GKE legacy authorization enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5baa92d2-d8ee-4c75-88a4-52d9d8bb8067`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster)

### Description{% #description %}

Legacy Authorization (ABAC) in GKE grants all authenticated users full cluster administrator privileges, violating the principle of least privilege and introducing significant security risks. When enabled, any authenticated user can perform any operation on any resource in the cluster, potentially leading to unauthorized access, data breaches, and complete cluster compromise. To secure your GKE cluster, ensure `enable_legacy_abac` is set to false as shown below:

```hcl
resource "google_container_cluster" "secure_cluster" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  enable_legacy_abac = false
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "google_container_cluster" "negative1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  enable_legacy_abac = false

  timeouts {
    create = "30m"
    update = "40m"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
resource "google_container_cluster" "positive1" {
  name               = "marcellus-wallace"
  location           = "us-central1-a"
  initial_node_count = 3
  enable_legacy_abac = true

  timeouts {
    create = "30m"
    update = "40m"
  }
}
```
