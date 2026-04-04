# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/alb_deletion_protection_disabled.md

---
title: ALB deletion protection disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ALB deletion protection disabled
---

# ALB deletion protection disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `afecd1f1-6378-4f7e-bb3b-60c35801fdd4`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lb#enable_deletion_protection)

### Description{% #description %}

Enabling deletion protection for an Application Load Balancer (ALB) helps prevent accidental or unauthorized deletion of the ALB resource, which could cause significant downtime or impact application availability. If the `enable_deletion_protection` attribute is set to `false`, as shown below, malicious or inadvertent actions could destroy the ALB and disrupt traffic flow to critical applications:

```gdscript3
resource "aws_alb" "example" {
  name                      = "test-lb-tf"
  internal                  = false
  load_balancer_type        = "network"
  subnets                   = aws_subnet.public.*.id

  enable_deletion_protection = true

  tags = {
    Environment = "production"
  }
}
```

Enabling this setting minimizes the risk of outages by requiring an extra step to delete the load balancer, thereby safeguarding essential network infrastructure.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
module "alb" {
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 6.0"

  name = "my-alb"

  load_balancer_type = "application"

  enable_deletion_protection = true

  vpc_id             = "vpc-abcde012"
  subnets            = ["subnet-abcde012", "subnet-bcde012a"]
  security_groups    = ["sg-edcd9784", "sg-edcd9785"]

  access_logs = {
    bucket = "my-alb-logs"
  }

  target_groups = [
    {
      name_prefix      = "pref-"
      backend_protocol = "HTTP"
      backend_port     = 80
      target_type      = "instance"
      targets = [
        {
          target_id = "i-0123456789abcdefg"
          port = 80
        },
        {
          target_id = "i-a1b2c3d4e5f6g7h8i"
          port = 8080
        }
      ]
    }
  ]

  https_listeners = [
    {
      port               = 443
      protocol           = "HTTPS"
      certificate_arn    = "arn:aws:iam::123456789012:server-certificate/test_cert-123456789012"
      target_group_index = 0
    }
  ]

  http_tcp_listeners = [
    {
      port               = 80
      protocol           = "HTTP"
      target_group_index = 0
    }
  ]

  tags = {
    Environment = "Test"
  }
}
```

```terraform
resource "aws_lb" "negative2" {
  name               = "test-lb-tf"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.public.*.id

  enable_deletion_protection = true

  tags = {
    Environment = "production"
  }
}
```

```terraform
resource "aws_alb" "negative1" {
  name               = "test-lb-tf"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.public.*.id

  enable_deletion_protection = true

  tags = {
    Environment = "production"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
module "alb" {
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 6.0"

  name = "my-alb"

  load_balancer_type = "application"

  vpc_id             = "vpc-abcde012"
  subnets            = ["subnet-abcde012", "subnet-bcde012a"]
  security_groups    = ["sg-edcd9784", "sg-edcd9785"]

  access_logs = {
    bucket = "my-alb-logs"
  }

  target_groups = [
    {
      name_prefix      = "pref-"
      backend_protocol = "HTTP"
      backend_port     = 80
      target_type      = "instance"
      targets = [
        {
          target_id = "i-0123456789abcdefg"
          port = 80
        },
        {
          target_id = "i-a1b2c3d4e5f6g7h8i"
          port = 8080
        }
      ]
    }
  ]

  https_listeners = [
    {
      port               = 443
      protocol           = "HTTPS"
      certificate_arn    = "arn:aws:iam::123456789012:server-certificate/test_cert-123456789012"
      target_group_index = 0
    }
  ]

  http_tcp_listeners = [
    {
      port               = 80
      protocol           = "HTTP"
      target_group_index = 0
    }
  ]

  tags = {
    Environment = "Test"
  }
}
```

```terraform
resource "aws_alb" "positive2" {
  name               = "test-lb-tf"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.public.*.id


  tags = {
    Environment = "production"
  }
}
```

```terraform
resource "aws_lb" "positive3" {
  name               = "test-lb-tf"
  internal           = false
  load_balancer_type = "network"
  subnets            = aws_subnet.public.*.id

  enable_deletion_protection = false

  tags = {
    Environment = "production"
  }
}
```
