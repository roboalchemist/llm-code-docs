# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/dataproc_clusters_is_public.md

---
title: Dataproc clusters publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Dataproc clusters publicly accessible
---

# Dataproc clusters publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `e3f7a9b1-c2d3-4e5f-8901-23456789abcd`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataproc_cluster_iam)

### Description{% #description %}

Google Cloud Dataproc clusters should not be publicly accessible as this could allow unauthorized access to sensitive data and resources. When IAM bindings or members include public principals such as `allUsers` or `allAuthenticatedUsers`, the Dataproc cluster becomes exposed to anyone on the internet or any authenticated Google account, respectively. To secure Dataproc clusters, use specific identities in IAM policies instead of public principals. For example, use `members = ["user:someone@example.com", "group:admins@example.com"]` instead of `members = ["allAuthenticatedUsers", "user:someone@example.com"]` or `member = "allUsers"`. Limiting access to specific users and groups significantly reduces the attack surface and helps maintain the principle of least privilege.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# Passing IAM Member example
resource "google_dataproc_cluster_iam_member" "good_member" {
  name   = "good-dataproc-member"
  member = "user:someone@example.com" # â Non-public principal
}
```

```terraform
# Passing IAM Binding example
resource "google_dataproc_cluster_iam_binding" "good_binding" {
  name    = "good-dataproc-binding"
  members = ["user:someone@example.com", "group:admins@example.com"] # â No public principals
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# Positive test case# Failing IAM Member example
resource "google_dataproc_cluster_iam_member" "bad_member" {
  name   = "bad-dataproc-member"
  member = "allUsers" # â Public principal
}

# Failing IAM Binding example
resource "google_dataproc_cluster_iam_binding" "bad_binding" {
  name    = "bad-dataproc-binding"
  members = ["allAuthenticatedUsers", "user:someone@example.com"] # â Contains public principal
}
```
