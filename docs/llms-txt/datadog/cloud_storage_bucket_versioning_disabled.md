# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cloud_storage_bucket_versioning_disabled.md

---
title: Cloud Storage bucket versioning disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloud Storage bucket versioning disabled
---

# Cloud Storage bucket versioning disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e7e961ac-d17e-4413-84bc-8a1fbe242944`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket#enabled)

### Description{% #description %}

Enabling versioning on a Google Cloud Storage bucket ensures that previous versions of objects are preserved, preventing accidental or malicious data loss or overwrites. Without versioning enabled (for example, `versioning = { enabled = false }` or omitting the `versioning` block entirely), deleted or overwritten objects cannot be recovered, increasing the risk of permanent data loss. To mitigate this risk, enable versioning by setting `versioning = { enabled = true }` in your Terraform configuration:

```
resource "google_storage_bucket" "secure_example" {
  name     = "foo"
  location = "EU"

  versioning = {
    enabled = true
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_storage_bucket" "negative1" {
  name     = "foo"
  location = "EU"

  versioning = {
    enabled = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_storage_bucket" "positive1" {
  name     = "foo"
  location = "EU"

  versioning = {
    enabled = false
  }
}

resource "google_storage_bucket" "positive2" {
  name     = "foo"
  location = "EU"
}
```
