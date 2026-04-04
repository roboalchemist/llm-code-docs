# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_access_key_is_exposed.md

---
title: IAM access key is exposed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM access key is exposed
---

# IAM access key is exposed

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `7081f85c-b94d-40fd-8b45-a4f1cac75e46`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_access_key)

### Description{% #description %}

IAM access keys should never be created or kept active for AWS root user accounts, as specified by the `user = "root"` and `status = "Active"` attributes in a Terraform `aws_iam_access_key` resource block. Allowing active access keys for root users significantly increases the attack surface and exposes highly privileged credentials to potential misuse or compromise, since the root account has unrestricted control over the entire AWS environment. To ensure security, root accounts should have all access keys disabled. For example:

```
resource "aws_iam_access_key" "secure_root" {
  user   = "root"
  status = "Inactive"
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_access_key" "negative1" {
  user = "some-user"
}

resource "aws_iam_access_key" "negative2" {
  user = "some-user"
  status = "Active"
}

resource "aws_iam_access_key" "negative3" {
  user = "root"
  status = "Inactive"
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_access_key" "positive1" {
  user = "root"
  status = "Active"
}

resource "aws_iam_access_key" "positive2" {
  user = "root"
}
```
