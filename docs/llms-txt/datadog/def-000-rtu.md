# Source: https://docs.datadoghq.com/security/default_rules/def-000-rtu.md

---
title: CloudTrail logs S3 bucket should not be public accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudTrail logs S3 bucket should not be
  public accessible
---

# CloudTrail logs S3 bucket should not be public accessible
 
## Description{% #description %}

The bucket policy or access control list (ACL) applied to the CloudTrail logs S3 bucket should prevent public access to the CloudTrail logs.

## Rationale{% #rationale %}

Allowing public access to CloudTrail log content can help an adversary identify weaknesses in the affected account's use or configuration.

## Remediation{% #remediation %}

Perform the following steps to remove public access granted to the bucket through an ACL or S3 bucket policy.

### From the console{% #from-the-console %}

1. Go to [Amazon S3 console](https://console.aws.amazon.com/s3/home).
1. Right-click on the bucket and click **Properties**.
1. In the Properties pane, click the **Permissions** tab.
1. The tab shows a list of grants, one row per grant, in the bucket ACL. Each row identifies the grantee and the permissions granted.
1. Select the row if it grants permission to Everyone or Any Authenticated User.
1. Uncheck all the permissions granted to Everyone or Any Authenticated User (click x to delete the row).
1. Click **Save** to save the ACL.
1. If the **Edit bucket policy** button is present, click it.
1. Remove any Statement having an `Effect` set to `Allow` and a `Principal` set to `"*"` or `{"AWS" : "*"}`.

## Default value{% #default-value %}

By default, S3 buckets are not publicly accessible.

## References{% #references %}

1. [https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html)
