# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/default_vpc_exists.md

---
title: Default VPC exists
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Default VPC exists
---

# Default VPC exists

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `96ed3526-0179-4c73-b1b2-372fde2e0d13`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Defaults

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/default_vpc)

### Description{% #description %}

Using the default VPC in AWS is not recommended, as it is a shared environment with default configurations that may not align with an organization's security and networking requirements. Resources created in the default VPC are more susceptible to unintended access, misconfiguration, or exposure. To mitigate this risk, it is best to define a custom VPC, as in the following example:

```
resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}
```

This ensures network isolation and enables more granular control over security settings.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.7.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```

```terraform
resource "aws_vpc" "negative1" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.7.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true
  default_vpc_name   = "my-default-vpc"

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```

```terraform
resource "aws_default_vpc" "positive1" {
  tags = {
    Name = "Default VPC"
  }
}
```
