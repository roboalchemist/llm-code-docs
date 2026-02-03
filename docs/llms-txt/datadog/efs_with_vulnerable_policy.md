# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/efs_with_vulnerable_policy.md

---
title: EFS with vulnerable policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > EFS with vulnerable policy
---

# EFS with vulnerable policy

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `fae52418-bb8b-4ac2-b287-0b9082d6a3fd`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/efs_file_system_policy#policy)

### Description{% #description %}

AWS EFS file system policies should avoid the use of wildcards (`*`) in the `Action` and `Principal` fields, as shown below, because this grants broad permissions to all users and all actions:

```
"Principal": { "AWS": "*" },
"Action": ["elasticfilesystem:*"]
```

Such overly permissive policies can allow any AWS account to perform any action on the EFS resource, leading to potential unauthorized data access, deletion, or modification. To mitigate this risk, restrict the `Principal` to specific IAM identities and limit `Action` to only what is necessary. For example:

```
"Principal": { "AWS": "arn:aws:iam::111122223333:user/Carlos" },
"Action": ["elasticfilesystem:ClientMount", "elasticfilesystem:ClientWrite"]
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_efs_file_system" "fs" {
  creation_token = "my-product"
}

resource "aws_efs_file_system_policy" "policy" {
  file_system_id = aws_efs_file_system.fs.id

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Id": "ExamplePolicy01",
    "Statement": [
        {
            "Sid": "ExampleStatement01",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::111122223333:user/Carlos"
            }
            "Resource": "aws_efs_file_system.test.arn",
            "Action": [
                "elasticfilesystem:ClientMount",
                "elasticfilesystem:ClientWrite"
            ],
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                }
            }
        }
    ]
}
POLICY
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
provider "aws" {
  region = "us-east-1"
}

resource "aws_efs_file_system" "not_secure" {
  creation_token = "efs-not-secure"

  tags = {
    Name = "NotSecure"
  }
}

resource "aws_efs_file_system_policy" "not_secure_policy" {
  file_system_id = aws_efs_file_system.not_secure.id

  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Id": "ExamplePolicy01",
    "Statement": [
        {
            "Sid": "ExampleStatement01",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "elasticfilesystem:*"
            ]
        }
    ]
}
POLICY
}
```
