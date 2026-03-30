# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cloud_storage_bucket_logging_not_enabled.md

---
title: Cloud Storage bucket logging not enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloud Storage bucket logging not enabled
---

# Cloud Storage bucket logging not enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d6cabc3a-d57e-48c2-b341-bf3dd4f4a120`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#log_bucket)

### Description{% #description %}

Cloud storage buckets should have logging enabled to capture access and usage data for auditing and monitoring purposes. If the `logging` block is not configured in the Terraform resource, access to and modifications of storage objects may go unnoticed, making it difficult to detect unauthorized activities or investigate security incidents.

A secure configuration includes a `logging` block, as shown below:

```
resource "google_storage_bucket" "auto_expiring_bucket" {
  name          = "auto-expiring-bucket"
  location      = "US"
  force_destroy = true

  logging {
    logBucket = "example-logs-bucket"
  }

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}
```

Enabling logging helps improve visibility into data access and can aid in compliance efforts.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_storage_bucket" "negative1" {
  name          = "auto-expiring-bucket"
  location      = "US"
  force_destroy = true

  logging {
    logBucket = "example-logs-bucket"
  }

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_storage_bucket" "positive1" {
  name          = "auto-expiring-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
}
```
