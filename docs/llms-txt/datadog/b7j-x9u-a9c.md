# Source: https://docs.datadoghq.com/security/default_rules/b7j-x9u-a9c.md

---
title: S3 bucket objects should not allow public listing via ACL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket objects should not allow
  public listing via ACL
---

# S3 bucket objects should not allow public listing via ACL

## Description{% #description %}

Modify your bucket ACL to remove public `READ` access.

## Rationale{% #rationale %}

- Public `READ` access allows the grantee to list all objects within your bucket and exploit objects with misconfigured ACL permissions.

For more information about S3 bucket ACLs, see the [Access control list (ACL) documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Controlling access to a bucket with user policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html) docs to edit your existing policy and set the policy permissions to private.

### From the command line{% #from-the-command-line %}

1. Run `put-bucket-acl` with your [S3 bucket name and the ACL](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-versioning.html#synopsis) set to `private`.

   ```
   aws s3api get-bucket-acl
    --bucket your-bucket-name
    --acl private
   ```
