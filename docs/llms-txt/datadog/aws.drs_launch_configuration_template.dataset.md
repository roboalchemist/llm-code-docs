# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.drs_launch_configuration_template.dataset.md

---
title: Elastic Disaster Recovery Launch Configuration Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elastic Disaster Recovery Launch
  Configuration Template
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.drs_launch_configuration_template.dataset/index.html
---

# Elastic Disaster Recovery Launch Configuration Template

An Elastic Disaster Recovery Launch Configuration Template in AWS defines the settings used when launching recovery instances during a failover or drill. It specifies parameters such as instance type, networking, security groups, and other configurations to ensure that recovered workloads run with the desired infrastructure setup. This template helps automate and standardize recovery processes, reducing downtime and ensuring consistency across recovery environments.

```
aws.drs_launch_configuration_template
```

## Fields

| Title                                    | ID   | Type   | Data Type                                                                                                                                                                                                | Description |
| ---------------------------------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string |
| account_id                               | core | string |
| arn                                      | core | string | ARN of the Launch Configuration Template.                                                                                                                                                                |
| copy_private_ip                          | core | bool   | Copy private IP.                                                                                                                                                                                         |
| copy_tags                                | core | bool   | Copy tags.                                                                                                                                                                                               |
| export_bucket_arn                        | core | string | S3 bucket ARN to export Source Network templates.                                                                                                                                                        |
| launch_configuration_template_id         | core | string | ID of the Launch Configuration Template.                                                                                                                                                                 |
| launch_disposition                       | core | string | Launch disposition.                                                                                                                                                                                      |
| launch_into_source_instance              | core | bool   | DRS will set the 'launch into instance ID' of any source server when performing a drill, recovery or failback to the previous region or availability zone, using the instance ID of the source instance. |
| licensing                                | core | json   | Licensing.                                                                                                                                                                                               |
| post_launch_enabled                      | core | bool   | Post-launch actions activated.                                                                                                                                                                           |
| tags                                     | core | hstore |
| target_instance_type_right_sizing_method | core | string | Target instance type right-sizing method.                                                                                                                                                                |
