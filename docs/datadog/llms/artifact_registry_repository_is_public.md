# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/artifact_registry_repository_is_public.md

---
title: Artifact Registry repo is public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Artifact Registry repo is public
---

# Artifact Registry repo is public

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a7b8c9d0-e1f2-3a4b-5c6d-7e8f90123456`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/artifact_registry_repository_iam)

### Description{% #description %}

Google Cloud Artifact Registry repositories store container images, language packages, and other artifacts that may contain sensitive code or data. When IAM bindings or members include public principals like `allUsers` or `allAuthenticatedUsers`, these artifacts become accessible to anyone on the internet or any authenticated Google account, respectively, potentially exposing proprietary code or sensitive configurations.

This security risk could lead to intellectual property theft, discovery of hardcoded secrets, or provide attackers information about your infrastructure that could be used in further attacks. To properly secure your artifact repositories, specify only the necessary users and groups that require access, as shown in the following example:

```terraform
resource "google_artifact_registry_repository_iam_binding" "good_example_binding" {
  repository = "example-repo"
  members    = ["user:someone@example.com", "group:admins@example.com"]
  role       = "roles/artifactregistry.admin"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# IAM Member compliant
resource "google_artifact_registry_repository_iam_member" "good_example_member" {
  repository = "example-repo"
  member     = "user:someone@example.com" # â Non-public principal
  role       = "roles/artifactregistry.reader"
}
```

```terraform

# IAM Binding compliant
resource "google_artifact_registry_repository_iam_binding" "good_example_binding" {
  repository = "example-repo"
  members    = ["user:someone@example.com", "group:admins@example.com"] # â No public principals
  role       = "roles/artifactregistry.admin"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# IAM Member violation
resource "google_artifact_registry_repository_iam_member" "bad_example_member" {
  repository = "example-repo"
  member     = "allUsers" # â Public principal
  role       = "roles/artifactregistry.reader"
}

# IAM Binding violation
resource "google_artifact_registry_repository_iam_binding" "bad_example_binding" {
  repository = "example-repo"
  members    = ["allAuthenticatedUsers", "user:someone@example.com"] # â Contains public principal
  role       = "roles/artifactregistry.admin"
}
```
