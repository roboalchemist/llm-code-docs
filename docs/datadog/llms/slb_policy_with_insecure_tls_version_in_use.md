# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/slb_policy_with_insecure_tls_version_in_use.md

---
title: SLB policy with insecure TLS version in use
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SLB policy with insecure TLS version in use
---

# SLB policy with insecure TLS version in use

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `dbfc834a-56e5-4750-b5da-73fda8e73f70`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/slb_tls_cipher_policy)

### Description{% #description %}

An SLB policy should not include insecure TLS protocol versions. Specifically, `alicloud_slb_tls_cipher_policy` resources must not specify `TLSv1.0` or `TLSv1.1` in the `tls_versions` attribute. This rule detects resources whose `tls_versions` contains insecure entries and reports details using the attributes `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, `keyActualValue`, and `searchLine`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_slb_tls_cipher_policy" "negative" {
  tls_cipher_policy_name = "Test-example_value"
  tls_versions           = ["TLSv1.2","TLSv1.3"]
  ciphers                = ["AES256-SHA256", "AES128-GCM-SHA256","TLS_AES_256_GCM_SHA384"]
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_slb_tls_cipher_policy" "positive" {
  tls_cipher_policy_name = "Test-example_value"
  tls_versions           = ["TLSv1.1","TLSv1.2"]
  ciphers                = ["AES256-SHA","AES256-SHA256", "AES128-GCM-SHA256"]
}
```
