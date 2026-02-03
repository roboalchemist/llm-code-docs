# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/glue_with_vulnerable_policy.md

---
title: Glue with vulnerable policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Glue with vulnerable policy
---

# Glue with vulnerable policy

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `d25edb51-07fb-4a73-97d4-41cecdc53a22`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/glue_resource_policy#policy)

### Description{% #description %}

Resource-based policies for AWS Glue should not use wildcard values (`"*"`) in the `principals` or `actions` attributes, as shown in the example below:

```
principals {
  identifiers = ["*"]
  type        = "AWS"
}
actions = ["glue:*"]
```

Allowing all actions and granting access to any principal exposes the Glue resources to unauthorized access or privilege escalation, significantly increasing the risk of data breaches or malicious modifications. Restricting both principals and allowed actions to the minimum necessary set reduces the attack surface and enforces least privilege.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
data "aws_iam_policy_document" "glue-example-policy2" {
  statement {
    actions = [
      "glue:CreateTable",
    ]
    resources = ["arn:data.aws_partition.current.partition:glue:data.aws_region.current.name:data.aws_caller_identity.current.account_id:*"]
    principals {
      identifiers = ["arn:aws:iam::var.account_id:saml-provider/var.provider_name"]
      type        = "AWS"
    }
  }
}

resource "aws_glue_resource_policy" "example2" {
  policy = data.aws_iam_policy_document.glue-example-policy2.json
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
data "aws_iam_policy_document" "glue-example-policy" {
  statement {
    actions = [
      "glue:*",
    ]
    resources = ["arn:data.aws_partition.current.partition:glue:data.aws_region.current.name:data.aws_caller_identity.current.account_id:*"]
    principals {
      identifiers = ["*"]
      type        = "AWS"
    }
  }
}

resource "aws_glue_resource_policy" "example" {
  policy = data.aws_iam_policy_document.glue-example-policy.json
}
```
