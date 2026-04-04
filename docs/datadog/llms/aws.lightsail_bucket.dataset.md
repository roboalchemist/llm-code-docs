# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.lightsail_bucket.dataset.md

---
title: Lightsail Bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Lightsail Bucket
---

# Lightsail Bucket

A Lightsail Bucket is an object storage resource in Amazon Lightsail that allows you to store and manage unstructured data such as images, videos, backups, and logs. It provides a simplified interface for creating and managing storage compared to Amazon S3, making it easier for developers and small businesses to use. Lightsail Buckets support secure access, scalability, and integration with other Lightsail resources, enabling straightforward storage solutions without needing to manage complex configurations.

```
aws.lightsail_bucket
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                        | Description |
| -------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| able_to_update_bundle      | core | bool          | Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly Amazon Web Services billing cycle. Use the UpdateBucketBundle action to change a bucket's bundle.                                                           |
| access_log_config          | core | json          | An object that describes the access log configuration for the bucket.                                                                                                                                                                                                                                                            |
| access_rules               | core | json          | An object that describes the access rules of the bucket.                                                                                                                                                                                                                                                                         |
| account_id                 | core | string        |
| arn                        | core | string        | The Amazon Resource Name (ARN) of the bucket.                                                                                                                                                                                                                                                                                    |
| bundle_id                  | core | string        | The ID of the bundle currently applied to the bucket. A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket. Use the UpdateBucketBundle action to change the bundle of a bucket.                                                                                                       |
| created_at                 | core | timestamp     | The timestamp when the distribution was created.                                                                                                                                                                                                                                                                                 |
| location                   | core | json          | An object that describes the location of the bucket, such as the Amazon Web Services Region and Availability Zone.                                                                                                                                                                                                               |
| name                       | core | string        | The name of the bucket.                                                                                                                                                                                                                                                                                                          |
| object_versioning          | core | string        | Indicates whether object versioning is enabled for the bucket. The following options can be configured: Enabled - Object versioning is enabled. Suspended - Object versioning was previously enabled but is currently suspended. Existing object versions are retained. NeverEnabled - Object versioning has never been enabled. |
| readonly_access_accounts   | core | array<string> | An array of strings that specify the Amazon Web Services account IDs that have read-only access to the bucket.                                                                                                                                                                                                                   |
| resource_type              | core | string        | The Lightsail resource type of the bucket.                                                                                                                                                                                                                                                                                       |
| resources_receiving_access | core | json          | An array of objects that describe Lightsail instances that have access to the bucket. Use the SetResourceAccessForBucket action to update the instances that have access to a bucket.                                                                                                                                            |
| state                      | core | json          | An object that describes the state of the bucket.                                                                                                                                                                                                                                                                                |
| support_code               | core | string        | The support code for a bucket. Include this code in your email to support when you have questions about a Lightsail bucket. This code enables our support team to look up your Lightsail information more easily.                                                                                                                |
| tags                       | core | hstore_csv    |
| url                        | core | string        | The URL of the bucket.                                                                                                                                                                                                                                                                                                           |
