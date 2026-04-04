# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/db_security_group_has_public_interface.md

---
title: DB security group has public interface
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DB security group has public interface
---

# DB security group has public interface

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `f0d8781f-99bf-4958-9917-d39283b168a0`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** High

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/rgeraskin/aws3/latest/docs/resources/db_security_group)

### Description{% #description %}

AWS DB security groups control access to RDS database instances by defining which IP addresses or Amazon EC2 instances can connect to them. Configuring a DB security group with a public interface (`0.0.0.0/0`) allows unrestricted access from any IP address, potentially exposing your database to unauthorized access and attacks from the internet.

This vulnerability significantly increases the risk of data breaches, unauthorized data access, and potential compromise of sensitive information stored in your database. Instead of using public interfaces, you should restrict access to specific IP ranges or VPC CIDR blocks.

Secure example:

```
resource "aws_db_security_group" "example" {
  name = "rds_sg"

  ingress {
    cidr = "10.0.0.0/8"
  }
}
```

Insecure example:

```
resource "aws_db_security_group" "example" {
  name = "rds_sg"

  ingress {
    cidr = "0.0.0.0/0"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_db_security_group" "negative1" {
  name = "rds_sg"

  ingress {
    cidr = "10.0.0.0/8"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_db_security_group" "positive1" {
  name = "rds_sg"

  ingress {
    cidr = "10.0.0.0/8"
  }

  ingress {
    cidr = "0.0.0.0/0"
  }
}
```

```terraform
resource "aws_db_security_group" "positive1" {
  name = "rds_sg"

  ingress {
    cidr = "0.0.0.0/0"
  }
}
```
