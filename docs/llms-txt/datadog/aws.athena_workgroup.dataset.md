# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.athena_workgroup.dataset.md

---
title: Athena Workgroup
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Athena Workgroup
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.athena_workgroup.dataset/index.html
---

# Athena Workgroup

This table represents the Athena Workgroup resource from Amazon Web Services.

```
aws.athena_workgroup
```

## Fields

| Title                           | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ------------------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string    |
| account_id                      | core | string    |
| configuration                   | core | json      | The configuration of the workgroup, which includes the location in Amazon S3 where query and calculation results are stored, the encryption configuration, if any, used for query and calculation results; whether the Amazon CloudWatch Metrics are enabled for the workgroup; whether workgroup settings override client-side settings; and the data usage limits for the amount of data scanned per query or per workgroup. The workgroup settings override is specified in <code>EnforceWorkGroupConfiguration</code> (true/false) in the <code>WorkGroupConfiguration</code>. See <a>WorkGroupConfiguration$EnforceWorkGroupConfiguration</a>. |
| creation_time                   | core | timestamp | The date and time the workgroup was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| description                     | core | string    | The workgroup description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| identity_center_application_arn | core | string    | The ARN of the IAM Identity Center enabled application associated with the workgroup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| name                            | core | string    | The workgroup name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| state                           | core | string    | The state of the workgroup: ENABLED or DISABLED.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| tags                            | core | hstore    |
| workgroup_arn                   | core | string    |
