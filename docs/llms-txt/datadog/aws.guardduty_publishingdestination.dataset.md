# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.guardduty_publishingdestination.dataset.md

---
title: GuardDuty Publishing Destination
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GuardDuty Publishing Destination
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.guardduty_publishingdestination.dataset/index.html
---

# GuardDuty Publishing Destination

This table represents the GuardDuty Publishing Destination resource from Amazon Web Services.

```
aws.guardduty_publishingdestination
```

## Fields

| Title                              | ID   | Type   | Data Type                                                                                                                                           | Description |
| ---------------------------------- | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string |
| account_id                         | core | string |
| destination_id                     | core | string | The ID of the publishing destination.                                                                                                               |
| destination_properties             | core | json   | A <code>DestinationProperties</code> object that includes the <code>DestinationArn</code> and <code>KmsKeyArn</code> of the publishing destination. |
| destination_type                   | core | string | The type of publishing destination. Currently, only Amazon S3 buckets are supported.                                                                |
| publishing_failure_start_timestamp | core | int64  | The time, in epoch millisecond format, at which GuardDuty was first unable to publish findings to the destination.                                  |
| status                             | core | string | The status of the publishing destination.                                                                                                           |
| tags                               | core | hstore |
