# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/google_compute_ssl_policy_weak_cipher_in_use.md

---
title: Google Compute SSL policy weak cipher in use
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Google Compute SSL policy weak cipher in use
---

# Google Compute SSL policy weak cipher in use

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `14a457f0-473d-4d1d-9e37-6d99b355b336`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_ssl_policy)

### Description{% #description %}

This check determines whether Google Compute SSL policies enforce strong TLS versions by verifying that the `min_tls_version` attribute is set to `"TLS_1_2"`. Allowing lower TLS versions, such as `"TLS_1_1"`, exposes services to vulnerabilities associated with outdated cryptographic algorithms and weak cipher suites, increasing the risk of data breaches and interception. For example, the following secure configuration ensures strong encryption by setting `min_tls_version` to `"TLS_1_2"`:

```
resource "google_compute_ssl_policy" "example" {
  name            = "custom-ssl-policy"
  min_tls_version = "TLS_1_2"
  profile         = "CUSTOM"
  custom_features = ["TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"]
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_ssl_policy" "negative1" {
  name            = "custom-ssl-policy"
  min_tls_version = "TLS_1_2"
  profile         = "CUSTOM"
  custom_features = ["TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_ssl_policy" "positive1" {
  name            = "custom-ssl-policy"
  min_tls_version = "TLS_1_1"
  profile         = "CUSTOM"
  custom_features = ["TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"]
}

resource "google_compute_ssl_policy" "positive2" {
  name            = "custom-ssl-policy"
  profile         = "CUSTOM"
  custom_features = ["TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"]
}
```
