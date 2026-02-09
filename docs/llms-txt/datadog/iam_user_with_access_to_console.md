# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_user_with_access_to_console.md

---
title: IAM user with access to console
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM user with access to console
---

# IAM user with access to console

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9ec311bf-dfd9-421f-8498-0b063c8bc552`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user_login_profile)

### Description{% #description %}

This check ensures that AWS IAM users are not granted access to the AWS Management Console by omitting the creation of an associated login profile in Terraform configurations. Allowing console access exposes user credentials to potential phishing and brute-force attacks, especially if multifactor authentication is not enforced or passwords are weak. If left unaddressed, attackers could use compromised credentials to access AWS resources with the permissions of the affected user, potentially resulting in data leaks, resource manipulation, or unauthorized changes to cloud infrastructure. Removing console access for IAM users reduces the attack surface and encourages the use of more secure access methods, such as IAM roles and API keys with strict controls.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_user" "example" {
  name          = "example"
  path          = "/"
  force_destroy = true
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_user" "example" {
  name          = "example"
  path          = "/"
  force_destroy = true
}

resource "aws_iam_user_login_profile" "example_login" {
  user    = aws_iam_user.example.name
  pgp_key = "keybase:some_person_that_exists"
}
```
