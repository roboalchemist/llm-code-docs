# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/kms_admin_and_crypto_key_roles_in_use.md

---
title: KMS admin and CryptoKey roles in use
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > KMS admin and CryptoKey roles in use
---

# KMS admin and CryptoKey roles in use

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `92e4464a-4139-4d57-8742-b5acc0347680`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam#policy_data)

### Description{% #description %}

Assigning both the `roles/cloudkms.admin` and `roles/cloudkms.cryptoKeyDecrypter` IAM roles to the same member on a Google Cloud project grants that user full administrative control over Cloud KMS keys and the ability to decrypt data. This combination of permissions allows a single user to manage (create, destroy, and modify) cryptographic keys and decrypt sensitive information, greatly increasing the risk of unauthorized data access or key misuse. To minimize risk, ensure that these roles are assigned to separate members as shown below:

```
data "google_iam_policy" "secure_example" {
  binding {
    role = "roles/cloudkms.admin"
    members = ["user:jane@example.com"]
  }
  binding {
    role = "roles/cloudkms.cryptoKeyDecrypter"
    members = ["user:jane2@example.com"]
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_project_iam_policy" "negative1" {
  project     = "your-project-id"
  policy_data = data.google_iam_policy.negative1.policy_data
}

data "google_iam_policy" "negative1" {
  binding {
    role = "roles/cloudkms.admin"

    members = [
      "user:jane@example.com",
    ]
  }

  binding {
    role = "roles/cloudkms.cryptoKeyDecrypter"

    members = [
      "user:jane2@example.com",
    ]
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_project_iam_policy" "positive1" {
  project     = "your-project-id"
  policy_data = data.google_iam_policy.positive1.policy_data
}

data "google_iam_policy" "positive1" {
  binding {
    role = "roles/cloudkms.admin"

    members = [
      "user:jane@example.com",
    ]
  }

  binding {
    role = "roles/cloudkms.cryptoKeyDecrypter"

    members = [
      "user:jane@example.com",
    ]
  }
}
```
