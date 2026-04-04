# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/imdsv1_is_enabled.md

---
title: IMDSv1 enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IMDSv1 enabled
---

# IMDSv1 enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f1g2h3i4-j5k6-7lmn-8opq-9012rstuvwxy`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#metadata-options)

### Description{% #description %}

AWS Instance Metadata Service Version 1 (IMDSv1) is susceptible to Server-Side Request Forgery (SSRF) attacks, which can allow attackers to access instance metadata and potentially steal credentials or sensitive information from EC2 instances. IMDSv2 mitigates this risk by requiring session tokens for metadata requests, providing an additional layer of protection against SSRF vulnerabilities. To secure your infrastructure, set `http_tokens` to `"required"` in your AWS instance or launch template metadata options, as shown in the following example:

```hcl
resource "aws_instance" "secure_example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  metadata_options {
    http_tokens = "required"  // Secure configuration
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_launch_template" "good_example" {
  name_prefix   = "example"
  image_id      = "ami-123456"
  instance_type = "t2.micro"

  metadata_options {
    http_tokens = "required" # â Secure
  }
}
```

```terraform
resource "aws_instance" "good_example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  metadata_options {
    http_tokens = "required" # â Secure
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
# Test case 2: aws_instance with incorrect http_tokens = "optional"
resource "aws_instance" "bad_example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  metadata_options {
    http_tokens = "optional" # â Should be "required"
  }
}

# Test case 3: aws_launch_template with incorrect http_tokens = "optional"
resource "aws_launch_template" "bad_example" {
  name_prefix   = "example"
  image_id      = "ami-123456"
  instance_type = "t2.micro"

  metadata_options {
    http_tokens = "optional" # â Should be "required"
  }
}

# Test case 1: Missing metadata_options entirely (should trigger this resource to be flagged by security checks)
resource "aws_launch_template" "missing_metadata_options" {
  name_prefix   = "missing-metadata"
  image_id      = "ami-123456"
  instance_type = "t2.micro"
}

resource "aws_launch_template" "good_example" {
  name_prefix   = "secure"
  image_id      = "ami-123456"
  instance_type = "t2.micro"

  metadata_options {
    http_tokens = "required" # â Correct value
  }
}
```
