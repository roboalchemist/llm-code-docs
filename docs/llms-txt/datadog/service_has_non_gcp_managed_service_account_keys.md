# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/service_has_non_gcp_managed_service_account_keys.md

---
title: There are non GCP-managed service account keys for a service account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > There are non GCP-managed service account keys
  for a service account
---

# There are non GCP-managed service account keys for a service account

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `3jh54js8-e5f6-7890-abcd-ef1234567890`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)

### Description{% #description %}

Service account keys provide access to GCP resources. Manually created keys pose significant security risks because they can be leaked, shared inappropriately, or remain active indefinitely without rotation. GCP-managed service account keys follow security best practices by default, including automatic key rotation and secure storage managed by Google. To ensure security, avoid manually specifying key data in Terraform, such as `public_key_data = "dummy-key"`. Instead, rely on GCP's managed keys by omitting this attribute.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_service_account_key" "bad_key" {
  service_account_id = "projects/my-project/serviceAccounts/my-service-account"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_service_account_key" "bad_key" {
  service_account_id = "projects/my-project/serviceAccounts/my-service-account"
  public_key_data    = "dummy-key"
}
```
