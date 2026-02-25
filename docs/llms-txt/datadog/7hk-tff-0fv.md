# Source: https://docs.datadoghq.com/security/default_rules/7hk-tff-0fv.md

---
title: IAM roles should not have a trust policy that contains a wildcard principal
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM roles should not have a trust
  policy that contains a wildcard principal
---

# IAM roles should not have a trust policy that contains a wildcard principal

## Description{% #description %}

Each IAM role must have a [trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#term_trust-policy) which defines the principals who are trusted to assume that role. It is possible to specify a [wildcard principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-anonymous) which permits any principal, including those outside your organization, the ability to assume the role. It is strongly discouraged to use the wildcard principal in a trust policy unless there is a [`Condition` element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) to restrict access.

## Rationale{% #rationale %}

A trust policy with a wildcard principal permits any AWS account the ability to assume the role. It is therefore discouraged.

## Remediation{% #remediation %}

Ensure the identified role does not have a principal value of `"AWS": "*"`. If a wildcard principal is necessary, use a `Condition` element to restrict access. Follow the [AWS documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html) to properly scope the `Principal` policy element.

### From the console{% #from-the-console %}

1. In the AWS Console, navigate to the IAM role you would like to change.
1. On the IAM role page, click the **Trust relationships** tab.
1. Click **Edit trust policy**.
1. Make changes to the trust policy to remediate the risk.
1. Click **Update policy**.

### From the command line{% #from-the-command-line %}

Use the `update-assume-role-policy` action to [update the role trust policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-assume-role-policy.html) to remediate the risk.

```
aws iam update-assume-role-policy
   --role-name Test-Role
   --policy-document file://<NEW_ROLE_POLICY>.json
```
