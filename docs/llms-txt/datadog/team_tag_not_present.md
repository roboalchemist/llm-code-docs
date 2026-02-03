# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/azure/team_tag_not_present.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/team_tag_not_present.md

---
title: Team tag missing on AWS resource
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Team tag missing on AWS resource
---

# Team tag missing on AWS resource

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `a2b3c4d5-e6f7-8901-gh23-ijkl456m7890`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Best Practices

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/resource-tagging)

### Description{% #description %}

This check ensures that every cloud resource defined in Terraform includes a "Team" tag within the `tags` attribute, which is critical for tracking resource ownership and accountability. Without a "Team" tag (for example, `tags = { Environment = "Production" }`), it becomes difficult to determine resource owners, leading to challenges in cost allocation, incident response, and lifecycle management. If left unaddressed, the absence of this tag can result in unmanaged resources remaining active, increasing the risk of security vulnerabilities and unnecessary expenses.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
# â "team" tag is not a valid attribute for this resource type
resource "aws_acm_certificate_validation" "example" {
  certificate_arn         = aws_acm_certificate.example.arn
  validation_record_fqdns = [for record in aws_route53_record.example : record.fqdn]
}
```

```terraform
resource "aws_s3_bucket" "good_example" {
  bucket = "my-bucket"

  tags = {
    team = "Security" # â "team" tag is present
  }
}
```

```terraform
resource "aws_s3_bucket" "good_example" {
  bucket = "my-bucket"

  tags = {
    Team = "Security" # â "Team" tag is present
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_instance" "bad_example" {
  ami           = "ami-123456"
  instance_type = "t2.micro"

  tags = {
    Environment = "Production" # â Missing "Team" tag
  }
}

resource "aws_s3_bucket" "bad_example" {
  bucket = "my-bucket"

  # â No tags at all
}
```
