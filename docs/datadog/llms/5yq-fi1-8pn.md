# Source: https://docs.datadoghq.com/security/default_rules/5yq-fi1-8pn.md

---
title: S3 bucket ACLs should block public write actions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > S3 bucket ACLs should block public
  write actions
---

# S3 bucket ACLs should block public write actions

## Description{% #description %}

Modify your access control permissions to remove `WRITE_ACP`, `WRITE`, or `FULL_CONTROL` access for all AWS users or any authenticated AWS user.

## Rationale{% #rationale %}

- Public `WRITE_ACP` access gives anyone permissions to change the S3 bucket Access Control List. With these permissions, anyone can grant any permissions they want, such as reading or writing objects inside the bucket.

- Public `WRITE` access allows the grantee to create new objects in the bucket. For the bucket and object owners of existing objects, also allows deletions and overwrites of those objects.

- Public `FULL_CONTROL` access allows the grantee the `READ`, `WRITE`, `READ_ACP`, and `WRITE_ACP` permissions on the bucket.

For more information about S3 bucket ACLs, see the [Access control list (ACL) documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [Controlling access to a bucket with user policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html) docs to edit your existing policy and set the policy permissions to private.

### From the command line{% #from-the-command-line %}

1. Run `put-bucket-acl` with your [S3 bucket name and the ACL](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-acl.html#) set to `private`.

```
aws s3api put-bucket-acl
  --bucket your-bucket-name
  --acl private
```
