# Source: https://docs.datadoghq.com/security/default_rules/def-000-uiq.md

---
title: S3 bucket ACLs should be restricted from public view
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket ACLs should be restricted
  from public view
---

# S3 bucket ACLs should be restricted from public view
 
## Description{% #description %}

Modify your bucket ACL to remove public `READ_ACP` access.

## Rationale{% #rationale %}

- Public `READ_ACP` access gives anyone the ability to read the bucket ACL. With this permission, anyone can see who controls your objects. This information can potentially be used to find misconfigured permissions and gain access to your S3 data.

For more information about S3 bucket ACLs, see the [Access control list (ACL) documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Controlling access to a bucket with user policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html) documentation to edit your existing policy and set the policy permissions to private.

### From the command line{% #from-the-command-line %}

1. Run `put-bucket-acl` with your [S3 bucket name and the ACL](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-acl.html#synopsis) set to `private`.

   ```
   aws s3api put-bucket-acl
    --bucket your-bucket-name
    --acl private
   ```
