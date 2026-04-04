# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/nas_file_system_without_kms.md

---
title: NAS file system without KMS
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > NAS file system without KMS
---

# NAS file system without KMS

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `5f670f9d-b1b4-4c90-8618-2288f1ab9676`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/nas_file_system#kms_key_id)

### Description{% #description %}

NAS file system resources (`alicloud_nas_file_system`) must include the `encrypt_type` attribute set to `"2"` to enable user-managed KMS encryption. The rule reports a `MissingAttribute` issue when `encrypt_type` is absent, and an `IncorrectValue` issue when it is present but not set to `"2"`. To remediate, ensure that `encrypt_type` is explicitly set to `"2"`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_nas_file_system" "foo" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
  encrypt_type  = "2"
  kms_key_id = "1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_nas_file_system" "fooabr" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
  encrypt_type  = "0"
}
```

```terraform
resource "alicloud_nas_file_system" "foo" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
}
```
