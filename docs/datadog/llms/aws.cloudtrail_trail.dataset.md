# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudtrail_trail.dataset.md

---
title: CloudTrail Trail
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudTrail Trail
---

# CloudTrail Trail

CloudTrail Trail is an AWS resource that records account activity and API usage across your AWS environment. It captures management and data events, delivering logs to Amazon S3, CloudWatch Logs, or CloudWatch Events for monitoring, auditing, and compliance. Trails help track user actions, detect unusual activity, and support security investigations.

```
aws.cloudtrail_trail
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                                                                                      | Description |
| ------------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| advanced_event_selectors       | core | json       | The advanced event selectors that are configured for the trail.                                                                                                                                                                                |
| cloud_watch_logs_log_group_arn | core | string     | Specifies an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered.                                                                                                         |
| cloud_watch_logs_role_arn      | core | string     | Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.                                                                                                                                                  |
| event_selectors                | core | json       | The event selectors that are configured for the trail.                                                                                                                                                                                         |
| has_custom_event_selectors     | core | bool       | Specifies if the trail has custom event selectors.                                                                                                                                                                                             |
| has_insight_selectors          | core | bool       | Specifies whether a trail has insight types specified in an InsightSelector list.                                                                                                                                                              |
| home_region                    | core | string     | The Region in which the trail was created.                                                                                                                                                                                                     |
| include_global_service_events  | core | bool       | Set to True to include Amazon Web Services API calls from Amazon Web Services global services such as IAM. Otherwise, False.                                                                                                                   |
| is_multi_region_trail          | core | bool       | Specifies whether the trail exists only in one Region or exists in all Regions.                                                                                                                                                                |
| is_organization_trail          | core | bool       | Specifies whether the trail is an organization trail.                                                                                                                                                                                          |
| kms_key_id                     | core | string     | Specifies the KMS key ID that encrypts the logs and digest files delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format. arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012 |
| log_file_validation_enabled    | core | bool       | Specifies whether log file validation is enabled.                                                                                                                                                                                              |
| name                           | core | string     | Name of the trail set by calling CreateTrail. The maximum length is 128 characters.                                                                                                                                                            |
| s3_bucket_name                 | core | string     | Name of the Amazon S3 bucket into which CloudTrail delivers your trail files. See Amazon S3 Bucket naming rules.                                                                                                                               |
| s3_key_prefix                  | core | string     | Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files. The maximum length is 200 characters.                       |
| sns_topic_arn                  | core | string     | Specifies the ARN of the Amazon SNS topic that CloudTrail uses to send notifications when log files are delivered. The following is the format of a topic ARN. arn:aws:sns:us-east-2:123456789012:MyTopic                                      |
| sns_topic_name                 | core | string     | This field is no longer in use. Use SnsTopicARN.                                                                                                                                                                                               |
| tags                           | core | hstore_csv |
| trail_arn                      | core | string     | Specifies the ARN of the trail. The following is the format of a trail ARN. arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail                                                                                                            |
| trail_status                   | core | json       |
