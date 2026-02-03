# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sagemaker_direct_internet_access_enabled.md

---
title: SageMaker notebook internet access enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SageMaker notebook internet access enabled
---

# SageMaker notebook internet access enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f3g4h5i6-j7k8-9lmn-0opq-12345abcdefg`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sagemaker_notebook_instance#direct_internet_access)

### Description{% #description %}

Amazon SageMaker notebook instances with direct internet access enabled create potential security vulnerabilities by allowing unauthorized outbound connections and possible data exfiltration channels. When enabled, malicious code or compromised notebooks can directly communicate with external servers, bypassing network security controls and potentially leaking sensitive information or intellectual property. To secure SageMaker notebook instances, you should explicitly disable direct internet access as shown in the following example:

```hcl
resource "aws_sagemaker_notebook_instance" "good_example" {
  name                   = "example-notebook"
  role_arn               = "arn:aws:iam::123456789012:role/SageMakerRole"
  direct_internet_access = "Disabled"
  instance_type          = "ml.t2.medium"
}
```

Avoid the insecure configuration that enables direct internet access:

```hcl
resource "aws_sagemaker_notebook_instance" "bad_example" {
  name                   = "example-notebook"
  role_arn               = "arn:aws:iam::123456789012:role/SageMakerRole"
  direct_internet_access = "Enabled" 
  instance_type          = "ml.t2.medium"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_sagemaker_notebook_instance" "good_example" {
  name                   = "example-notebook"
  role_arn               = "arn:aws:iam::123456789012:role/SageMakerRole"
  direct_internet_access = "Disabled" # â Direct internet access is correctly disabled
  instance_type          = "ml.t2.medium"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_sagemaker_notebook_instance" "bad_example" {
  name                   = "example-notebook"
  role_arn               = "arn:aws:iam::123456789012:role/SageMakerRole"
  direct_internet_access = "Enabled" # â Direct internet access should be disabled
  instance_type          = "ml.t2.medium"
}
```
