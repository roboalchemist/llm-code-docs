# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.databrew_schedule.dataset.md

---
title: Glue DataBrew Schedule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Glue DataBrew Schedule
---

# Glue DataBrew Schedule

AWS Glue DataBrew Schedule is a resource that defines a recurring timetable for running DataBrew jobs, such as data preparation or transformation tasks. It allows you to automate job execution at specified intervals without manual intervention, ensuring consistent and timely data processing workflows.

```
aws.databrew_schedule
```

## Fields

| Title              | ID   | Type          | Data Type                                                                                                                    | Description |
| ------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string        |
| account_id         | core | string        | The ID of the Amazon Web Services account that owns the schedule.                                                            |
| create_date        | core | timestamp     | The date and time that the schedule was created.                                                                             |
| created_by         | core | string        | The Amazon Resource Name (ARN) of the user who created the schedule.                                                         |
| cron_expression    | core | string        | The dates and times when the job is to run. For more information, see Cron expressions in the Glue DataBrew Developer Guide. |
| job_names          | core | array<string> | A list of jobs to be run, according to the schedule.                                                                         |
| last_modified_by   | core | string        | The Amazon Resource Name (ARN) of the user who last modified the schedule.                                                   |
| last_modified_date | core | timestamp     | The date and time when the schedule was last modified.                                                                       |
| name               | core | string        | The name of the schedule.                                                                                                    |
| resource_arn       | core | string        | The Amazon Resource Name (ARN) of the schedule.                                                                              |
| tags               | core | hstore_csv    |
