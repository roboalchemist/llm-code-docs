# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sagemaker_endpoint_configuration_encryption_disabled.md

---
title: SageMaker endpoint configuration encryption disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SageMaker endpoint configuration encryption
  disabled
---

# SageMaker endpoint configuration encryption disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `58b35504-0287-4154-bf69-02c0573deab8`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sagemaker_endpoint_configuration#kms_key_arn)

### Description{% #description %}

Amazon SageMaker endpoint configurations should have encryption enabled using a KMS key to protect sensitive data at rest. Without proper encryption, data stored within SageMaker endpoints may be vulnerable to unauthorized access if the underlying storage is compromised. This represents a significant security risk as machine learning endpoints often process and store sensitive information.

To address this vulnerability, specify the `kms_key_arn` attribute in your SageMaker endpoint configuration. For example, the secure implementation uses the following configuration, where kms_key_arn is specified to enable encryption:

```
resource "aws_sagemaker_endpoint_configuration" "example" {
  // other configuration
  kms_key_arn = "aws_kms_key.example.arn"
}
```

In contrast, the insecure version omits this critical encryption setting.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_sagemaker_endpoint_configuration" "negative" {
  name = "my-endpoint-config"

  production_variants {
    variant_name           = "variant-1"
    model_name             = aws_sagemaker_model.m.name
    initial_instance_count = 1
    instance_type          = "ml.t2.medium"
  }

  tags = {
    Name = "foo"
  }

  kms_key_arn = "aws_kms_key.example.arn"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_sagemaker_endpoint_configuration" "positive" {
  name = "my-endpoint-config"

  production_variants {
    variant_name           = "variant-1"
    model_name             = aws_sagemaker_model.m.name
    initial_instance_count = 1
    instance_type          = "ml.t2.medium"
  }

  tags = {
    Name = "foo"
  }
}
```
