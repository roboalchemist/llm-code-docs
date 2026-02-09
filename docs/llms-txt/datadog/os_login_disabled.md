# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/os_login_disabled.md

---
title: OSLogin disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > OSLogin disabled
---

# OSLogin disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `32ecd6eb-0711-421f-9627-1a28d9eff217`

**Cloud Provider:** GCP

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_metadata#metadata)

### Description{% #description %}

This check verifies whether the `enable-oslogin` metadata key is set to `true` in Google Cloud project or instance metadata, as shown below:

```
resource "google_compute_project_metadata" "secure_example" {
  metadata = {
    enable-oslogin = true
  }
}
```

If OS Login is not enabled, user and SSH key management is handled by instance-level metadata, which can lead to inconsistent access policies and increased risk of unauthorized access. Enabling OS Login centralizes and streamlines IAM-based SSH access, reducing the attack surface of compute resources.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "google_compute_project_metadata" "negative1" {
  metadata = {
    enable-oslogin = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "google_compute_project_metadata" "positive1" {
  metadata = {
    enable-oslogin = false
  }
}

resource "google_compute_project_metadata" "positive2" {
  metadata = {
      foo  = "bar"
  }
}
```
