# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/container_registry_repository_is_public.md

---
title: Container Registry repo is public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Container Registry repo is public
---

# Container Registry repo is public

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f6a7b8c9-d0e1-2345-f678-90abcdef1234`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_registry)

### Description{% #description %}

Allowing public access to Container Registry repositories creates significant security risks by exposing potentially sensitive container images and artifacts to anyone on the internet. When IAM configurations include public principals such as `allUsers` or `allAuthenticatedUsers`, it bypasses access controls and may lead to data exfiltration, intellectual property theft, or deployment of compromised containers. Instead of using public principals (for example, `member = "allUsers"` or `members = ["allAuthenticatedUsers", ...]`), implement proper access controls by explicitly specifying authorized users and groups, such as `members = ["user:someone@example.com", "group:admins@example.com"]` to ensure only legitimate users can access your container registry resources.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# Passing IAM Member Example
resource "google_storage_bucket_iam_member" "good_example_member" {
  bucket = "example-bucket"
  member = "user:someone@example.com" # â Non-public principal
  role   = "roles/storage.objectViewer"
}
```

```terraform
# Passing IAM Binding Example
resource "google_storage_bucket_iam_binding" "good_example_binding" {
  bucket  = "example-bucket"
  members = ["user:someone@example.com", "group:admins@example.com"] # â No public principals
  role    = "roles/storage.objectViewer"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# Failing IAM Member Example
resource "google_storage_bucket_iam_member" "bad_example_member" {
  bucket = "example-bucket"
  member = "allUsers" # â Public principal
  role   = "roles/storage.objectViewer"
}

# Failing IAM Binding Example
resource "google_storage_bucket_iam_binding" "bad_example_binding" {
  bucket  = "example-bucket"
  members = ["allAuthenticatedUsers", "user:someone@example.com"] # â Contains public principal
  role    = "roles/storage.objectViewer"
}
```
