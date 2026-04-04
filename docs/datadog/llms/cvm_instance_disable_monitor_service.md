# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/cvm_instance_disable_monitor_service.md

---
title: Beta - CVM instance disable monitor service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - CVM instance disable monitor service
---

# Beta - CVM instance disable monitor service

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `966ed4f7-b8a5-4e8d-b2bf-098657c98960`

**Cloud Provider:** TencentCloud

**Platform:** Terraform

**Severity:** Low

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/instance#disable_monitor_service)

### Description{% #description %}

CVM instances should have detailed monitoring enabled. The `tencentcloud_instance` resource must not set `disable_monitor_service` to `true`. To ensure detailed monitoring is enabled, `disable_monitor_service` should be set to `false`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name           = "cvm_postpaid"
  availability_zone       = "ap-guangzhou-7"
  image_id                = "img-9qrfy1xt"
  instance_type           = "POSTPAID_BY_HOUR"
  system_disk_type        = "CLOUD_PREMIUM"
  system_disk_size        = 50
  hostname                = "root"
  project_id              = 0
  vpc_id                  = "vpc-axrsmmrv"
  subnet_id               = "subnet-861wd75e"
  disable_monitor_service = false

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
resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name              = "cvm_postpaid"
  availability_zone          = "ap-guangzhou-7"
  image_id                   = "img-9qrfy1xt"
  instance_type              = "POSTPAID_BY_HOUR"
  system_disk_type           = "CLOUD_PREMIUM"
  system_disk_size           = 50
  hostname                   = "root"
  project_id                 = 0
  vpc_id                     = "vpc-axrsmmrv"
  subnet_id                  = "subnet-861wd75e"
  internet_max_bandwidth_out = 100
  disable_monitor_service    = true

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
