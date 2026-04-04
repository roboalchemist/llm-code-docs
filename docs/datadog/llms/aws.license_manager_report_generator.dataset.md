# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.license_manager_report_generator.dataset.md

---
title: License Manager Report Generator
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > License Manager Report Generator
---

# License Manager Report Generator

This table represents the license_manager_report_generator resource from Amazon Web Services.

```
aws.license_manager_report_generator
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                | Description |
| ------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------ | ----------- |
| _key                                 | core | string        |
| account_id                           | core | string        |
| create_time                          | core | string        | Time the report was created.                                             |
| description                          | core | string        | Description of the report generator.                                     |
| last_report_generation_time          | core | string        | Time the last report was generated at.                                   |
| last_run_failure_reason              | core | string        | Failure message for the last report generation attempt.                  |
| last_run_status                      | core | string        | Status of the last report generation attempt.                            |
| license_manager_report_generator_arn | core | string        | Amazon Resource Name (ARN) of the report generator.                      |
| report_context                       | core | json          | License configuration type for this generator.                           |
| report_creator_account               | core | string        | The Amazon Web Services account ID used to create the report generator.  |
| report_frequency                     | core | json          | Details about how frequently reports are generated.                      |
| report_generator_name                | core | string        | Name of the report generator.                                            |
| report_type                          | core | array<string> | Type of reports that are generated.                                      |
| s3_location                          | core | json          | Details of the S3 bucket that report generator reports are published to. |
| tags                                 | core | hstore_csv    |
