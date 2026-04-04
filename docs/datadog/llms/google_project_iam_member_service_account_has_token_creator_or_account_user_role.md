# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/google_project_iam_member_service_account_has_token_creator_or_account_user_role.md

---
title: >-
  Google project IAM member service account has token creator or account user
  role
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google project IAM member service account has
  token creator or account user role
---

# Google project IAM member service account has token creator or account user role

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `c68b4e6d-4e01-4ca1-b256-1e18e875785c`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam#google_project_iam_member)

### Description{% #description %}

This check verifies that Google Project IAM Member service accounts are not assigned the Token Creator (`iam.serviceAccountTokenCreator`) or Account User (`iam.serviceAccountUser`) roles. These privileged roles allow the members to impersonate service accounts by creating tokens or using the service account identity to access resources, which could lead to privilege escalation if compromised. The recommended approach is to use more restrictive roles that provide only the necessary permissions required for the specific workload, as shown in the secure example below where a standard `editor` role is used instead of these high-risk roles:

```terraform
resource "google_project_iam_member" "secure_example" {
  project = "your-project-id"
  role    = "roles/editor"
  member  = "user:jane@example.com"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_project_iam_member" "negative1" {
  project = "your-project-id"
  role    = "roles/editor"
  members  = "user:jane@example.com"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_project_iam_member" "positive1" {
  project = "your-project-id"
  role    = "roles/iam.serviceAccountTokenCreator"
  member  = "serviceAccount:my-other-app@appspot.gserviceacccount.com"
}

resource "google_project_iam_member" "positive2" {
  project = "your-project-id"
  role    = "roles/iam.serviceAccountUser"
  members  = ["user:jane@example.com", "serviceAccount:my-other-app@appspot.gserviceacccount.com"]
}
```
