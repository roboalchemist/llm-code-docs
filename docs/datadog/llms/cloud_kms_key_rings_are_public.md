# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/cloud_kms_key_rings_are_public.md

---
title: Cloud KMS key ring is anonymously or publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Cloud KMS key ring is anonymously or publicly
  accessible
---

# Cloud KMS key ring is anonymously or publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d4e5f6g7-h8i9-0jkl-mnop-qrstuvwx1234`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_key_ring)

### Description{% #description %}

Cloud KMS Key Rings store and manage cryptographic keys used for data encryption in Google Cloud. Making them publicly accessible creates severe security risks that could lead to unauthorized access to sensitive encrypted data. When IAM policies grant permissions to `allUsers` or `allAuthenticatedUsers`, it allows anyone on the internet or any authenticated Google account to access and potentially use these cryptographic keys. To properly secure key rings, ensure IAM members are specific identities (such as `user:someone@example.com`) rather than public principals (`allUsers` or `allAuthenticatedUsers`). For example, use `member = "user:someone@example.com"` instead of `member = "allUsers"` or `members = ["allAuthenticatedUsers", "user:someone@example.com"]`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# IAM Binding compliant
resource "google_kms_key_ring_iam_binding" "good_example_binding" {
  key_ring_id = "example-key-ring"
  members     = ["user:someone@example.com", "group:admins@example.com"] # â No public principals
  role        = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
}
```

```terraform
# IAM Member compliant
resource "google_kms_key_ring_iam_member" "good_example_member" {
  key_ring_id = "example-key-ring"
  member      = "user:someone@example.com" # â Non-public principal
  role        = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# IAM Member violation
resource "google_kms_key_ring_iam_member" "bad_example_member" {
  key_ring_id = "example-key-ring"
  member      = "allUsers" # â Public principal
  role        = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
}

# IAM Binding violation
resource "google_kms_key_ring_iam_binding" "bad_example_binding" {
  key_ring_id = "example-key-ring"
  members     = ["allAuthenticatedUsers", "user:someone@example.com"] # â Contains public principal
  role        = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
}
```
