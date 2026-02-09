# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cloud_run_service_is_public.md

---
title: Cloud Run service is public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloud Run service is public
---

# Cloud Run service is public

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7e3c1a2b-9d4f-4c8e-8a5b-0f1e2d3c4b6a`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_service_iam)

### Description{% #description %}

Cloud Run services with IAM bindings or members that include public principals such as `allUsers` or `allAuthenticatedUsers` expose your service to anyone on the internet, creating a significant security risk. Public access can lead to unauthorized access, data breaches, or exploitation of vulnerabilities in your application. To secure access, grant roles only to specific users or service accounts. For example, use `members = ["user:someone@example.com", "group:admins@example.com"]` instead of `members = ["allAuthenticatedUsers", "user:someone@example.com"]`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# Passing Terraform Example for IAM Binding
resource "google_cloud_run_service_iam_binding" "good_example_binding" {
  service = "my-cloud-run-service"
  members = ["user:someone@example.com", "group:admins@example.com"] # â No public principals
  role    = "roles/run.invoker"
}
```

```terraform
# Passing Terraform Example for IAM Member
resource "google_cloud_run_service_iam_member" "good_example_member" {
  service = "my-cloud-run-service"
  member  = "user:someone@example.com" # â Non-public principal
  role    = "roles/run.invoker"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# Failing Terraform Example for IAM Member
resource "google_cloud_run_service_iam_member" "bad_example_member" {
  service = "my-cloud-run-service"
  member  = "allUsers" # â Public principal
  role    = "roles/run.invoker"
}

# Failing Terraform Example for IAM Binding
resource "google_cloud_run_service_iam_binding" "bad_example_binding" {
  service = "my-cloud-run-service"
  members = ["allAuthenticatedUsers", "user:someone@example.com"] # â Contains public principal
  role    = "roles/run.invoker"
}
```
