# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/disk_encryption_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/gcp/disk_encryption_disabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/disk_encryption_disabled.md

---
title: Disk encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Disk encryption disabled
---

# Disk encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `39750e32-3fe9-453b-8c33-dd277acdb2cc`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/disk#encrypted)

### Description{% #description %}

Alicloud disks (`alicloud_disk`) should have encryption enabled.

The rule flags resources where the `encrypted` attribute is explicitly set to `false` (issue type `IncorrectValue`) or where both the `encrypted` and `snapshot_id` attributes are missing (issue type `MissingAttribute`).

Remediation is to set `encrypted` to `true` (replacement) or add `encrypted = true` (addition).

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "alicloud_disk" "disk_encryption3" {
  # cn-beijing
  availability_zone = "cn-beijing-b"
  name              = "New-disk"
  description       = "Hello ecs disk."
  category          = "cloud_efficiency"
  size              = "30"
  encrypted         = true
  kms_key_id        = "2a6767f0-a16c-4679-a60f-13bf*****"
  tags = {
    Name = "TerraformTest"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "alicloud_disk" "disk_encryption2" {
  # cn-beijing
  availability_zone = "cn-beijing-b"
  name              = "New-disk"
  description       = "Hello ecs disk."
  category          = "cloud_efficiency"
  size              = "30"
  encrypted         = false
  kms_key_id        = "2a6767f0-a16c-4679-a60f-13bf*****"
  tags = {
    Name = "TerraformTest"
  }
}
```

```terraform
resource "alicloud_disk" "disk_encryption1" {
  # cn-beijing
  availability_zone = "cn-beijing-b"
  name              = "New-disk"
  description       = "Hello ecs disk."
  category          = "cloud_efficiency"
  size              = "30"
  tags = {
    Name = "TerraformTest"
  }
}
```
