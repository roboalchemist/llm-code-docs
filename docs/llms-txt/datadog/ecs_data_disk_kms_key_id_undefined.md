# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/ecs_data_disk_kms_key_id_undefined.md

---
title: ECS data disk KMS key ID undefined
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ECS data disk KMS key ID undefined
---

# ECS data disk KMS key ID undefined

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f262118c-1ac6-4bb3-8495-cc48f1775b85`

**Cloud Provider:** Alicloud

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/aliyun/alicloud/latest/docs/resources/disk#kms_key_id)

### Description{% #description %}

ECS data disks must have the `kms_key_id` attribute set. This rule flags any `alicloud_disk` resource missing the `kms_key_id` attribute. Setting this ensures disks are encrypted using a KMS key and avoids unencrypted storage.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# Create a new ECS disk.
resource "alicloud_disk" "ecs_disk" {
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
# Create a new ECS disk.
resource "alicloud_disk" "ecs_disk" {
  # cn-beijing
  availability_zone = "cn-beijing-b"
  name              = "New-disk"
  description       = "Hello ecs disk."
  category          = "cloud_efficiency"
  size              = "30"
  encrypted         = true
  tags = {
    Name = "TerraformTest"
  }
}
```
