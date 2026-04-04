# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/sso_identity_user_unsafe_creation.md

---
title: SSO identity user unsafe creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > SSO identity user unsafe creation
---

# SSO identity user unsafe creation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `4003118b-046b-4640-b200-b8c7a4c8b89f`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Medium

**Category:** Access Control

#### Learn More{% #learn-more %}

- [Provider Reference](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/identitystore_user)

### Description{% #description %}

Using the `aws_identitystore_user` resource in Terraform to create AWS SSO users directly can result in misalignment between your AWS identities and external Identity Providers (IdPs) such as Active Directory. Because these users are not automatically synchronized with external directories, this configuration can introduce inconsistencies, orphaned accounts, or the risk of unauthorized access if users are not properly managed or deprovisioned. If left unaddressed, this may compromise the integrity of access controls and leave your AWS environment vulnerable to privilege escalation or account misuse.

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_ssoadmin_permission_set_inline_policy" "neg1" {
  instance_arn       = aws_ssoadmin_permission_set.example.instance_arn
  permission_set_arn = aws_ssoadmin_permission_set.example.arn
  inline_policy = <<POLICY
{
  "Statement": [
    {
      "Action": [
        "s3:ListBucket*",
        "s3:HeadBucket",
        "s3:Get*"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::b1",
        "arn:aws:s3:::b1/*",
        "arn:aws:s3:::b2",
        "arn:aws:s3:::b2/*"
      ],
      "Sid": ""
    },
    {
      "Action": "s3:PutObject*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::b1/*",
      "Sid": ""
    }
  ],
  "Version": "2012-10-17"
}
POLICY
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_identitystore_user" "example" {
  identity_store_id = tolist(data.aws_ssoadmin_instances.example.identity_store_ids)[0]

  display_name = "John Doe"
  user_name    = "johndoe"

  name {
    given_name  = "John"
    family_name = "Doe"
  }

  emails {
    value = "john@example.com"
  }
}
```
