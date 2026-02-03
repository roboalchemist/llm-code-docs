# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cloud_storage_anonymous_or_publicly_accessible.md

---
title: Cloud Storage is anonymous or publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloud Storage is anonymous or publicly
  accessible
---

# Cloud Storage is anonymous or publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a6cd52a1-3056-4910-96a5-894de9f3f3b3`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Critical

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam#google_storage_bucket_iam_binding)

### Description{% #description %}

Cloud Storage Buckets configured with anonymous or public access pose significant security risks by allowing anyone on the internet to access potentially sensitive data. Including `allUsers` in IAM bindings grants access to anyone, while `allAuthenticatedUsers` grants access to any Google account holder. Both violate the principle of least privilege.

Insecure configuration example:

```
resource "google_storage_bucket_iam_binding" "insecure" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = ["user:jane@example.com", "allUsers"]
}
```

Secure configuration example:

```
resource "google_storage_bucket_iam_binding" "secure" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = ["user:jane@example.com"]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "google_storage_bucket_iam_binding" "negative1" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = [
    "user:jane@example.com",
  ]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
#this is a problematic code where the query should report a result(s)
resource "google_storage_bucket_iam_binding" "positive1" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = []
}

resource "google_storage_bucket_iam_binding" "positive2" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = ["user:jane@example.com","allUsers"]
}

resource "google_storage_bucket_iam_binding" "positive3" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = ["user:jane@example.com", "allAuthenticatedUsers"]
}
```
