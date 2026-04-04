# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/ami_shared_with_multiple_accounts.md

---
title: AMI shared with multiple accounts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > AMI shared with multiple accounts
---

# AMI shared with multiple accounts

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ba4e0031-3e9d-4d7d-b0d6-bd8f003f8698`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ami_launch_permission)

### Description{% #description %}

This check ensures that Amazon Machine Images (AMIs) are not granted launch permissions to multiple AWS accounts, which is controlled by the `aws_ami_launch_permission` resource's `account_id` attribute. Allowing more than one account to access the same AMI, as shown below, can lead to unauthorized use or distribution of potentially sensitive images:

```
resource "aws_ami_launch_permission" "positive1" {
  image_id   = "ami-1235678"
  account_id = "12345600012"
}

resource "aws_ami_launch_permission" "positive2" {
  image_id   = "ami-1235678"
  account_id = "123456789012"
}
```

If misconfigured, this may result in exposure of proprietary software or internal system images to unintended parties, increasing the risk of data leakage and compromise of your infrastructure. To mitigate this risk, only a single, trusted account should be granted access to each AMI, as shown below:

```
resource "aws_ami_launch_permission" "secure_example" {
  image_id   = "ami-1235678"
  account_id = "123456789012"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ami_launch_permission" "negative1" {
  image_id   = "ami-12345678"
  account_id = "123456789012"
}


resource "aws_ami_launch_permission" "example" {
  image_id   = "ami-12345680"
  account_id = "12345672"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_ami_launch_permission" "positive1" {

  image_id   = "ami-1235678"
  account_id = "12345600012"

}


resource "aws_ami_launch_permission" "positive2" {

  image_id   = "ami-1235678"
  account_id = "123456789012"

}
```
