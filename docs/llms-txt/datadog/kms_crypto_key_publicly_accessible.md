# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/kms_crypto_key_publicly_accessible.md

---
title: KMS CryptoKey is publicly accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > KMS CryptoKey is publicly accessible
---

# KMS CryptoKey is publicly accessible

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `16cc87d1-dd47-4f46-b3ce-4dfcac8fd2f5`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_kms_crypto_key_iam#google_kms_crypto_key_iam_policy)

### Description{% #description %}

Google Cloud KMS CryptoKeys provide cryptographic functionality for encrypting and decrypting sensitive data in Google Cloud. When KMS CryptoKey IAM policies include `allUsers` or `allAuthenticatedUsers`, they become publicly accessible, creating a serious security vulnerability that could lead to unauthorized access to encryption capabilities, data breaches, or compromised encrypted information.

Insecure configuration example:

```
data "google_iam_policy" {
  binding {
    role = "roles/cloudkms.cryptoKeyEncrypter"
    members = ["allUsers"]
  }
}
```

Secure configuration with specific user access:

```
data "google_iam_policy" {
  binding {
    role = "roles/cloudkms.cryptoKeyEncrypter"
    members = [
      "user:jane@example.com",
    ]
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_kms_key_ring" "negative" {
  name     = "negative-example"
  location = "global"
}
resource "google_kms_crypto_key" "negative" {
  name            = "crypto-key-example"
  key_ring        = google_kms_key_ring.negative.id
  rotation_period = "100000s"
  lifecycle {
    prevent_destroy = true
  }
}

data "google_iam_policy" "negative" {
  binding {
    role = "roles/cloudkms.cryptoKeyEncrypter"

    members = [
      "user:jane@example.com",
    ]
  }
}

resource "google_kms_crypto_key_iam_policy" "negative" {
  crypto_key_id = google_kms_crypto_key.negative.id
  policy_data = data.google_iam_policy.negative.policy_data
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_kms_key_ring" "positive2" {
  name     = "keyring-example"
  location = "global"
}
resource "google_kms_crypto_key" "positive2" {
  name            = "crypto-key-example"
  key_ring        = google_kms_key_ring.positive2.id
  rotation_period = "100000s"
  lifecycle {
    prevent_destroy = true
  }
}

data "google_iam_policy" "positive2" {
  binding {
    role = "roles/cloudkms.cryptoKeyEncrypter"

    member = "allAuthenticatedUsers"
  }
}

resource "google_kms_crypto_key_iam_policy" "positive2" {
  crypto_key_id = google_kms_crypto_key.keyyy.id
  policy_data = data.google_iam_policy.positive2.policy_data
}
```

```terraform
resource "google_kms_key_ring" "positive1" {
  name     = "keyring-example"
  location = "global"
}
resource "google_kms_crypto_key" "positive1" {
  name            = "crypto-key-example"
  key_ring        = google_kms_key_ring.positive1.id
  rotation_period = "100000s"
  lifecycle {
    prevent_destroy = true
  }
}

data "google_iam_policy" "positive1" {
  binding {
    role = "roles/cloudkms.cryptoKeyEncrypter"

    member = "allUsers"
  }
}

resource "google_kms_crypto_key_iam_policy" "positive1" {
  crypto_key_id = google_kms_crypto_key.positive1.id
  policy_data = data.google_iam_policy.positive1.policy_data
}
```
