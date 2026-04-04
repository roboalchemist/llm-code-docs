# Source: https://docs.datadoghq.com/security/default_rules/def-000-qk5.md

---
title: IAM roles should not allow untrusted GitLab runners to assume them
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > IAM roles should not allow untrusted
  GitLab runners to assume them
---

# IAM roles should not allow untrusted GitLab runners to assume them

## Description{% #description %}

When using GitLab CI/CD to assume an IAM role, it is recommended to use [identity federation](https://docs.gitlab.com/ee/ci/cloud_services/aws/) to avoid using hardcoded, long-lived credentials.

However, in some cases the trust policy of the role may be misconfigured and allow any untrusted GitLab runner to assume the IAM role.

## Rationale{% #rationale %}

If the role trust policy does not have a properly configured condition, any untrusted GitLab runner from any repository (including outside your organization) can assume the role and retrieve credentials to your AWS account.

## Remediation{% #remediation %}

Ensure that the IAM role has a condition on the `gitlab.com:sub` condition key, for instance:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Effect": "Allow",
        "Principal": {
          "Federated": "arn:aws:iam::123456123456:oidc-provider/gitlab.com"
        },
        "Action": "sts:AssumeRoleWithWebIdentity",
        "Condition": {
          "StringEquals": {
            "gitlab.example.com:sub": "project_path:mygroup/myproject:ref_type:branch:ref:main"
          }
        }
    }
  ]
}
```

### From the console{% #from-the-console %}

1. In the AWS Console, navigate to the IAM role you would like to change.
1. On the IAM role page, click the **Trust relationships** tab.
1. Click **Edit trust policy**.
1. Make changes to the trust policy, as shown in the previous section.
1. Click **Update policy**.

### From the command line{% #from-the-command-line %}

Using `update-assume-role-policy`, [update the role trust policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-assume-role-policy.html) to remediate the risk.

```
aws iam update-assume-role-policy
   --role-name Test-Role
   --policy-document file://<NEW_ROLE_POLICY>.json
```
