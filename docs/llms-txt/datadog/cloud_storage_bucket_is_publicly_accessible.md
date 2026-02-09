# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cloud_storage_bucket_is_publicly_accessible.md

---
title: Cloud Storage bucket is publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloud Storage bucket is publicly accessible
---

# Cloud Storage bucket is publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c010082c-76e0-4b91-91d9-6e8439e455dd`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam)

### Description{% #description %}

Granting public or anonymous access to a Google Cloud Storage bucket using Terraform, such as by setting the member to `allUsers` (anyone on the internet) or `allAuthenticatedUsers` (any authenticated Google account) in a `google_storage_bucket_iam_member` resource, exposes your data to unauthorized access. This can lead to data leaks, theft, or manipulation since anyone could potentially view, download, modify, or delete sensitive data. To prevent this, IAM bindings for storage buckets should only specify trusted user or service accounts, as shown below:

```
resource "google_storage_bucket_iam_member" "secure_example" {
  bucket = google_storage_bucket.default.name
  role   = "roles/storage.admin"
  member = "user:jane@example.com"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_storage_bucket_iam_member" "negative1" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  member = "user:jane@example.com"
}


resource "google_storage_bucket_iam_member" "negative2" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = ["user:john@example.com","user:john@example.com"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_storage_bucket_iam_member" "positive1" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  member = "allUsers"

  condition {
    title       = "expires_after_2019_12_31"
    description = "Expiring at midnight of 2019-12-31"
    expression  = "request.time < timestamp(\"2020-01-01T00:00:00Z\")"
  }
}


resource "google_storage_bucket_iam_member" "positive2" {
  bucket = google_storage_bucket.default.name
  role = "roles/storage.admin"
  members = ["user:john@example.com","allAuthenticatedUsers"]
}
```
