# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_user_policy_without_mfa.md

---
title: IAM user policy without MFA
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM user policy without MFA
---

# IAM user policy without MFA

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `b5681959-6c09-4f55-b42b-c40fa12d03ec`

**Cloud Provider:** AWS

**Platform:** Terraform

**Severity:** Low

**Category:** Insecure Configurations

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)

### Description{% #description %}

This check verifies that the AWS root user is required to authenticate using Multi-Factor Authentication (MFA). If the root user is not protected with MFA, as in a policy lacking a condition on `"aws:MultiFactorAuthPresent"`, unauthorized users with access to the root credentials could compromise the entire AWS account. Enforcing MFA by adding a policy condition, such as the following, significantly reduces the risk of credential theft, unauthorized privilege escalation, and account takeovers.

```
"Condition": {
  "BoolIfExists": {
    "aws:MultiFactorAuthPresent": "true"
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```terraform
resource "aws_iam_user" "negative1" {
  name = "root"
  path = "/system/"

  tags = {
    tag-key = "tag-value"
  }
}

resource "aws_iam_access_key" "negative2" {
  user = aws_iam_user.lb.name
}

resource "aws_iam_user_policy" "negative3" {
  name = "test"
  user = aws_iam_user.lb.name

  policy = <<EOF
{
   "Version": "2012-10-17",
   "Statement": [
     {
       "Effect": "Allow",
       "Principal": {
         "AWS": "arn:aws:iam::111122223333:root"
       },
       "Action": "sts:AssumeRole",
       "Condition": {
         "BoolIfExists": {
           "aws:MultiFactorAuthPresent" : "true"
         }
       }
     }
   ]
}
EOF
}

resource "aws_iam_user_policy" "negative4" {
  name = "test"
  user = aws_iam_user.lb.name

  policy = <<EOF
{
   "Version": "2012-10-17",
   "Statement": [
     {
       "Effect": "Allow",
       "Principal": {
         "AWS": "arn:aws:iam::mfa/111122223333:root"
       },
       "Action": "sts:AssumeRole"
     }
   ]
}
EOF
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```terraform
resource "aws_iam_user" "positive1" {
  name = "root"
  path = "/system/"

  tags = {
    tag-key = "tag-value"
  }
}

resource "aws_iam_access_key" "positive2" {
  user = aws_iam_user.lb.name
}

resource "aws_iam_user_policy" "positive3" {
  name = "test"
  user = aws_iam_user.lb.name

  policy = <<EOF
{
   "Version": "2012-10-17",
   "Statement": [
     {
       "Effect": "Allow",
       "Principal": {
         "AWS": "arn:aws:iam::111122223333:root"
       },
       "Action": "sts:AssumeRole"
     }
   ]
}
EOF
}
```
