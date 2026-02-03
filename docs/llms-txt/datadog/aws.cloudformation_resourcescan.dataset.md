# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cloudformation_resourcescan.dataset.md

---
title: CloudFormation Resourcescan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CloudFormation Resourcescan
---

# CloudFormation Resourcescan

This table represents the CloudFormation Resourcescan resource from Amazon Web Services.

```
aws.cloudformation_resourcescan
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                  | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| account_id           | core | string        |
| end_time             | core | timestamp     | The time that the resource scan was finished.                                                                                                                                                                                                                                                              |
| percentage_completed | core | float64       | The percentage of the resource scan that has been completed.                                                                                                                                                                                                                                               |
| resource_scan_id     | core | string        | The Amazon Resource Name (ARN) of the resource scan. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:resourceScan/${Id}</code>. An example is <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:resourceScan/<i>f5b490f7-7ed4-428a-aa06-31ff25db0772</i> </code>. |
| resource_types       | core | array<string> | The list of resource types for the specified scan. Resource types are only available for scans with a <code>Status</code> set to <code>COMPLETE</code> or <code>FAILED </code>.                                                                                                                            |
| resources_read       | core | int64         | The number of resources that were read. This is only available for scans with a <code>Status</code> set to <code>COMPLETE</code>, <code>EXPIRED</code>, or <code>FAILED</code>. <note> This field may be 0 if the resource scan failed with a <code>ResourceScanLimitExceededException</code>. </note>     |
| resources_scanned    | core | int64         | The number of resources that were listed. This is only available for scans with a <code>Status</code> set to <code>COMPLETE</code>, <code>EXPIRED</code>, or <code>FAILED </code>.                                                                                                                         |
| scan_filters         | core | json          | The scan filters that were used.                                                                                                                                                                                                                                                                           |
| start_time           | core | timestamp     | The time that the resource scan was started.                                                                                                                                                                                                                                                               |
| status               | core | string        | Status of the resource scan. <dl> <dt> IN_PROGRESS </dt> <dd> The resource scan is still in progress. </dd> <dt> COMPLETE </dt> <dd> The resource scan is complete. </dd> <dt> EXPIRED </dt> <dd> The resource scan has expired. </dd> <dt> FAILED </dt> <dd> The resource scan has failed. </dd> </dl>    |
| status_reason        | core | string        | The reason for the resource scan status, providing more information if a failure happened.                                                                                                                                                                                                                 |
| tags                 | core | hstore_csv    |
