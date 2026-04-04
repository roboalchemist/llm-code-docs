# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/nas_file_system_not_encrypted.md

---
title: NAS file system not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > NAS file system not encrypted
---

# NAS file system not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `67bfdff1-31ce-4525-b564-e94368735360`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/nas_file_system#encrypt_type)

### Description{% #description %}

NAS file systems must be encrypted. The `alicloud_nas_file_system` resource must include the `encrypt_type` attribute, and it must not be set to `0`. To remediate, set `encrypt_type` to `"2"` to enable user-managed KMS encryption.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_nas_file_system" "foo2" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
  encrypt_type  = "2"
}
```

```terraform
resource "alicloud_nas_file_system" "foo" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
  encrypt_type  = "1"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_nas_file_system" "foopos2" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
}
```

```terraform
resource "alicloud_nas_file_system" "foopos" {
  protocol_type = "NFS"
  storage_type  = "Performance"
  description   = "tf-testAccNasConfig"
  encrypt_type  = "0"
}
```
