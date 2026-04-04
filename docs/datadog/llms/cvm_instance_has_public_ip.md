# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/tencentcloud/cvm_instance_has_public_ip.md

---
title: Beta - CVM instance has public IP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Beta - CVM instance has public IP
---

# Beta - CVM instance has public IP

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a74b4602-a62c-4a02-956a-e19f86ea24b5`

**Cloud Provider:** TencentCloud

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/instance#allocate_public_ip)

### Description{% #description %}

A CVM instance should not include a public IP address. This rule flags Tencent Cloud CVM instances where the `allocate_public_ip` attribute is set to `true`; it must be set to `false` to prevent assignment of a public IP. The rule returns the attributes `documentId`, `resourceType`, `resourceName`, `searchKey`, `issueType`, `keyExpectedValue`, `keyActualValue`, and `searchLine`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "tencentcloud_instance" "cvm_postpaid" {
  instance_name      = "cvm_postpaid"
  availability_zone  = "ap-guangzhou-7"
  image_id           = "img-9qrfy1xt"
  instance_type      = "POSTPAID_BY_HOUR"
  system_disk_type   = "CLOUD_PREMIUM"
  system_disk_size   = 50
  hostname           = "root"
  project_id         = 0
  vpc_id             = "vpc-axrsmmrv"
  subnet_id          = "subnet-861wd75e"
  allocate_public_ip = false

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
  allocate_public_ip         = true

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
