# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/network_acl_with_unrestricted_access_to_rdp.md

---
title: Network ACL with unrestricted access to RDP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Network ACL with unrestricted access to RDP
---

# Network ACL with unrestricted access to RDP

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a20be318-cac7-457b-911d-04cc6e812c25`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/network_acl)

### Description{% #description %}

This check ensures that network ACLs don't allow unrestricted access to RDP (TCP port 3389) from the public internet (`0.0.0.0/0`). Exposing RDP to the entire internet significantly increases the risk of brute force attacks and unauthorized access to your instances, potentially leading to data breaches or system compromise. Instead of using a wide-open CIDR block like `0.0.0.0/0`, restrict RDP access to specific IP ranges as shown in the following secure configuration: `ingress = [{ protocol = "tcp", rule_no = 100, action = "allow", cidr_block = "10.3.0.0/18", from_port = 3389, to_port = 3389 }]`.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.52.0"
    }
  }
}

resource "aws_network_acl" "negative3" {
  vpc_id = aws_vpc.main.id

  egress {
      protocol   = "tcp"
      rule_no    = 200
      action     = "allow"
      cidr_block = "10.3.0.0/18"
      from_port  = 443
      to_port    = 443
  }

  ingress {
      protocol   = "tcp"
      rule_no    = 100
      action     = "allow"
      cidr_block = "10.3.0.0/18"
      from_port   = 3389
      to_port     = 3389
  }

  tags = {
    Name = "main"
  }
}
```

```terraform
provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

resource "aws_network_acl" "negative2" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main"
  }
}

resource "aws_network_acl_rule" "negative2" {
  network_acl_id = aws_network_acl.negative2.id
  rule_number    = 100
  egress         = false
  protocol       = "tcp"
  rule_action    = "allow"
  from_port      = 3389
  to_port        = 3389
  cidr_block     = "10.3.0.0/18"
}
```

```terraform
provider "aws" {
    region = "us-east-1"
  }

  terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 3.0"
      }
    }
  }

  # This should NOT be flagged - denying RDP from all IPs is SECURE
  resource "aws_network_acl" "negative6" {
    vpc_id = aws_vpc.main.id

    tags = {
      Name = "deny-all-rdp"
    }
  }

  resource "aws_network_acl_rule" "negative6" {
    network_acl_id = aws_network_acl.negative6.id
    rule_number    = 100
    egress         = false
    protocol       = "tcp"
    rule_action    = "deny"        # â KEY: Denying access
    cidr_block     = "0.0.0.0/0"   # â From ALL IPs
    from_port      = 3389          # â RDP port
    to_port        = 3389
  }
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

resource "aws_network_acl" "positive2" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main"
  }
}

resource "aws_network_acl_rule" "postive2" {
  network_acl_id = aws_network_acl.positive2.id
  rule_number    = 100
  egress         = false
  protocol       = "tcp"
  rule_action    = "allow"
  from_port      = 3389
  to_port        = 3389
  cidr_block     = "0.0.0.0/0"
}
```

```terraform
provider "aws" {
  region = "us-east-1"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "<= 3.52.0"
    }
  }
}

resource "aws_network_acl" "positive3" {
  vpc_id = aws_vpc.main.id

  egress {
      protocol   = "tcp"
      rule_no    = 200
      action     = "allow"
      cidr_block = "10.3.0.0/18"
      from_port  = 443
      to_port    = 443
  }

  ingress {
      protocol   = "tcp"
      rule_no    = 100
      action     = "allow"
      cidr_block = "0.0.0.0/0"
      from_port   = 3389
      to_port     = 3389
  }

  tags = {
    Name = "main"
  }
}
```

```terraform
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.7.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  default_network_acl_ingress = [
    {
      "action" : "allow",
      "cidr_block" : "0.0.0.0/0",
      "from_port" : 0,
      "protocol" : "tcp",
      "rule_no" : 3389,
      "to_port" : 0
    }
  ]

  enable_nat_gateway = true
  enable_vpn_gateway = true

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
```
