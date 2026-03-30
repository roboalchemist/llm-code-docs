# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ami_not_encrypted.md

---
title: AMI not encrypted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > AMI not encrypted
---

# AMI not encrypted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `8bbb242f-6e38-4127-86d4-d8f0b2687ae2`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/ami)

### Description{% #description %}

Amazon Machine Images (AMIs) created without EBS encryption can result in sensitive data stored on volumes being exposed if the underlying storage is compromised. To mitigate this, AMI resources should have the `encrypted = true` attribute set within each `ebs_block_device` block to ensure all data at rest is protected.

For example, a secure Terraform configuration would look like the following:

```
resource "aws_ami" "secure" {
  name                = "terraform-example"
  virtualization_type = "hvm"
  root_device_name    = "/dev/xvda"

  ebs_block_device {
    device_name = "/dev/xvda"
    snapshot_id = "snap-xxxxxxxx"
    volume_size = 8
    encrypted   = true
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
#this code is a correct code for which the query should not find any result
resource "aws_ami" "negative1" {
  name                = "terraform-example"
  virtualization_type = "hvm"
  root_device_name    = "/dev/xvda2"

  ebs_block_device {
    device_name = "/dev/xvda2"
    snapshot_id = "snap-xxxxxxxx"
    volume_size = 8
    encrypted   = true
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform

resource "aws_ami" "positive1" {
  name                = "terraform-example"
  virtualization_type = "hvm"
  root_device_name    = "/dev/xvda"

  ebs_block_device {
    device_name = "/dev/xvda"
    snapshot_id = "snap-xxxxxxxx"
    volume_size = 8
  }
}


resource "aws_ami" "positive2" {
  name                = "terraform-example"
  virtualization_type = "hvm"
  root_device_name    = "/dev/xvda1"


  ebs_block_device {
    device_name = "/dev/xvda1"
    snapshot_id = "snap-xxxxxxxx"
    volume_size = 8
      encrypted           = false
  }
}

resource "aws_ami" "positive3" {
  name                = "terraform-example"
  virtualization_type = "hvm"
  root_device_name    = "/dev/xvda1"
}
```
