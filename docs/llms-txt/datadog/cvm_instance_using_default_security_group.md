# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/cvm_instance_using_default_security_group.md

---
title: Beta - CVM instance using default security group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - CVM instance using default security
  group
---

# Beta - CVM instance using default security group

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `93bb2065-63ec-45a2-a466-f106b56f2e32`

**Cloud Provider:** TencentCloud

**Platform:** Terraform

**Severity:** Low

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/instance#orderly_security_groups)

### Description{% #description %}

CVM instances (`tencentcloud_instance`) should not include the default security group. This rule inspects the `orderly_security_groups` and `security_groups` attributes for any occurrence of `default` and flags the resource if found. Relying on the default security group can result in overly permissive network access and should be avoided.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "test"
}

resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name     = "cvm_postpaid"
  availability_zone = "ap-guangzhou-7"
  image_id          = "img-9qrfy1xt"
  instance_type     = "POSTPAID_BY_HOUR"
  system_disk_type  = "CLOUD_PREMIUM"
  system_disk_size  = 50
  hostname          = "root"
  project_id        = 0
  vpc_id            = "vpc-axrsmmrv"
  subnet_id         = "subnet-861wd75e"

  security_groups = [
    tencentcloud_security_group.sg.id
  ]

  data_disks {
    data_disk_type = "CLOUD_PREMIUM"
    data_disk_size = 50
    encrypt        = false
  }

  tags = {
    tagKey = "tagValue"
  }
}
```

```terraform
resource "tencentcloud_security_group" "sg" {
  name        = "tf-example"
  description = "test"
}

resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name     = "cvm_postpaid"
  availability_zone = "ap-guangzhou-7"
  image_id          = "img-9qrfy1xt"
  instance_type     = "POSTPAID_BY_HOUR"
  system_disk_type  = "CLOUD_PREMIUM"
  system_disk_size  = 50
  hostname          = "root"
  project_id        = 0
  vpc_id            = "vpc-axrsmmrv"
  subnet_id         = "subnet-861wd75e"

  orderly_security_groups = [
    tencentcloud_security_group.sg.id
  ]

  data_disks {
    data_disk_type = "CLOUD_PREMIUM"
    data_disk_size = 50
    encrypt        = false
  }

  tags = {
    tagKey = "tagValue"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "tencentcloud_security_group" "default" {
  name        = "tf-example"
  description = "test"
}

resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name     = "cvm_postpaid"
  availability_zone = "ap-guangzhou-7"
  image_id          = "img-9qrfy1xt"
  instance_type     = "POSTPAID_BY_HOUR"
  system_disk_type  = "CLOUD_PREMIUM"
  system_disk_size  = 50
  hostname          = "root"
  project_id        = 0
  vpc_id            = "vpc-axrsmmrv"
  subnet_id         = "subnet-861wd75e"

  security_groups = [tencentcloud_security_group.default.id]

  data_disks {
    data_disk_type = "CLOUD_PREMIUM"
    data_disk_size = 50
    encrypt        = false
  }

  tags = {
    tagKey = "tagValue"
  }
}
```

```terraform
resource "tencentcloud_security_group" "default" {
  name        = "tf-example"
  description = "test"
}

resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name     = "cvm_postpaid"
  availability_zone = "ap-guangzhou-7"
  image_id          = "img-9qrfy1xt"
  instance_type     = "POSTPAID_BY_HOUR"
  system_disk_type  = "CLOUD_PREMIUM"
  system_disk_size  = 50
  hostname          = "root"
  project_id        = 0
  vpc_id            = "vpc-axrsmmrv"
  subnet_id         = "subnet-861wd75e"

  orderly_security_groups = [tencentcloud_security_group.default.id]

  data_disks {
    data_disk_type = "CLOUD_PREMIUM"
    data_disk_size = 50
    encrypt        = false
  }

  tags = {
    tagKey = "tagValue"
  }
}
```
