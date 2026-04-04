# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/hardcoded_aws_access_key.md

---
title: Hardcoded AWS access key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Hardcoded AWS access key
---

# Hardcoded AWS access key

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d7b9d850-3e06-4a75-852f-c46c2e92240b`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)

### Description{% #description %}

Hardcoding AWS access keys in Terraform configuration files poses a significant security risk as these credentials can be exposed if the code is shared, stored in version control systems, or accidentally leaked. This vulnerability could allow unauthorized access to AWS resources, potentially leading to data breaches, resource manipulation, or incurring unexpected costs.

Instead of hardcoding credentials directly in configuration files like `user_data = "1234567890123456789012345678901234567890$"`, use more secure approaches such as referencing files (`file("scripts/first-boot-http.sh")`) or utilizing environment variables, AWS IAM roles, or secure secret management solutions. This helps maintain the principle of least privilege and significantly reduces the risk of credential exposure.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_instance" "negative1" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  user_data = file("scripts/first-boot-http.sh")
  tags = {
    Name = "HelloWorld"
  }
}
```

```terraform
module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 3.0"

  name = "single-instance"

  ami                    = "ami-ebd02392"
  instance_type          = "t2.micro"
  key_name               = "user1"
  monitoring             = true
  vpc_security_group_ids = ["sg-12345678"]
  subnet_id              = "subnet-eddcdzz4"
  user_data = file("scripts/first-boot-http.sh")

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_instance" "positive1" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  user_data = "1234567890123456789012345678901234567890$"
  tags = {
    Name = "HelloWorld"
  }
}
```

```terraform
module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 3.0"

  name = "single-instance"

  ami                    = "ami-ebd02392"
  instance_type          = "t2.micro"
  key_name               = "user1"
  monitoring             = true
  vpc_security_group_ids = ["sg-12345678"]
  subnet_id              = "subnet-eddcdzz4"
  user_data = "1234567890123456789012345678901234567890$"

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```
