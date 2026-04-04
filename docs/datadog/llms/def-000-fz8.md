# Source: https://docs.datadoghq.com/security/default_rules/def-000-fz8.md

---
title: Support roles should be created to manage incidents with AWS Support
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Support roles should be created to
  manage incidents with AWS Support
---

# Support roles should be created to manage incidents with AWS Support

## Description{% #description %}

AWS provides a support center that can be used for incident notification and response, as well as technical support and customer services. Create an IAM Role to allow authorized users to manage incidents with AWS Support.

## Rationale{% #rationale %}

By implementing least privilege for access control, an IAM Role will require an appropriate IAM Policy to allow Support Center Access in order to manage Incidents with AWS Support.

### Impact{% #impact %}

All AWS Support plans include an unlimited number of accounts and billing support cases, with no long-term contracts. Support billing calculations are performed on a per-account basis for all plans. Enterprise Support plan customers have the option to include multiple enabled accounts in an aggregated monthly billing calculation. Monthly charges for the Business and Enterprise support plans are based on each month's AWS usage charges, subject to a monthly minimum, billed in advance.

## Remediation{% #remediation %}

### From the command line{% #from-the-command-line %}

1. Create an IAM role for managing incidents with AWS:

- Create a trust relationship policy document that allows <iam_user> to manage AWS incidents, and save it locally as /tmp/TrustPolicy.json:

  ```json
  {
     "Version": "2012-10-17",
     "Statement": [
        {
         "Effect": "Allow",
         "Principal": {
            "AWS": "<iam_user>"
          },
         "Action": "sts:AssumeRole"
        }
     ]
  }
  ```

Create the IAM role using the above trust policy:

```
aws iam create-role --role-name <aws_support_iam_role> --assume-role-policydocument file:///tmp/TrustPolicy.json
```

Attach 'AWSSupportAccess' managed policy to the created IAM role:

```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AWSSupportAccess --role-name <aws_support_iam_role>
```

## References{% #references %}

1. [http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html](http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html)
1. [https://aws.amazon.com/premiumsupport/pricing/](https://aws.amazon.com/premiumsupport/pricing/)
1. [http://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html](http://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html)
1. [http://docs.aws.amazon.com/cli/latest/reference/iam/attach-role-policy.html](http://docs.aws.amazon.com/cli/latest/reference/iam/attach-role-policy.html)
1. [http://docs.aws.amazon.com/cli/latest/reference/iam/list-entities-for-policy.html](http://docs.aws.amazon.com/cli/latest/reference/iam/list-entities-for-policy.html)
