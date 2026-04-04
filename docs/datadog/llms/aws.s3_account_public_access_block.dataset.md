# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.s3_account_public_access_block.dataset.md

---
title: S3 Account Public Access Block
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > S3 Account Public Access Block
---

# S3 Account Public Access Block

This table represents the S3 Account Public Access Block resource from Amazon Web Services.

```
aws.s3_account_public_access_block
```

## Fields

| Title                           | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| account_public_access_block_arn | core | string     |
| block_public_acls               | core | bool       | Specifies whether Amazon S3 should block public access control lists (ACLs) for buckets in this account. Setting this element to <code>TRUE</code> causes the following behavior: <ul> <li> PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public. </li> <li> PUT Object calls fail if the request includes a public ACL. </li> <li> PUT Bucket calls fail if the request includes a public ACL. </li> </ul> Enabling this setting doesn't affect existing policies or ACLs. This is not supported for Amazon S3 on Outposts.         |
| block_public_policy             | core | bool       | Specifies whether Amazon S3 should block public bucket policies for buckets in this account. Setting this element to <code>TRUE</code> causes Amazon S3 to reject calls to PUT Bucket policy if the specified bucket policy allows public access. Enabling this setting doesn't affect existing bucket policies. This property is not supported for Amazon S3 on Outposts.                                                                                                                                                                                  |
| ignore_public_acls              | core | bool       | Specifies whether Amazon S3 should ignore public ACLs for buckets in this account. Setting this element to <code>TRUE</code> causes Amazon S3 to ignore all public ACLs on buckets in this account and any objects that they contain. Enabling this setting doesn't affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. This property is not supported for Amazon S3 on Outposts.                                                                                                                               |
| restrict_public_buckets         | core | bool       | Specifies whether Amazon S3 should restrict public bucket policies for buckets in this account. Setting this element to <code>TRUE</code> restricts access to buckets with public policies to only Amazon Web Service principals and authorized users within this account. Enabling this setting doesn't affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. This property is not supported for Amazon S3 on Outposts. |
| tags                            | core | hstore_csv |
