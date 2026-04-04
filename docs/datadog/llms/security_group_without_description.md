# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/security_group_without_description.md

---
title: Security group rule without description
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Security group rule without description
---

# Security group rule without description

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `cb3f5ed6-0d18-40de-a93d-b3538db31e8c`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group#description)

### Description{% #description %}

It is a best practice for AWS security groups to include a meaningful `description` attribute in their Terraform configuration, such as in the following example:

```
description = "Allow TLS inbound traffic"
```

Omitting the description field, as shown below, can lead to confusion and hinder effective management or auditing of security groups, especially in environments with many resources:

```
resource "aws_security_group" "allow_tls" {
  name   = "allow_tls"
  vpc_id = aws_vpc.main.id
  // missing description
  ...
}
```

Without clear descriptions, security teams may struggle to quickly identify the purpose of a group, increasing the risk of misconfigurations and delayed incident response.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = [aws_vpc.main.cidr_block]
    ipv6_cidr_blocks = [aws_vpc.main.ipv6_cidr_block]
  }

  tags = {
    Name = "allow_tls"
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = [aws_vpc.main.cidr_block]
    ipv6_cidr_blocks = [aws_vpc.main.ipv6_cidr_block]
  }

  tags = {
    Name = "allow_tls"
  }
}
```
