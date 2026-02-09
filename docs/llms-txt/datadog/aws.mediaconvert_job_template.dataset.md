# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconvert_job_template.dataset.md

---
title: AWS Elemental MediaConvert Job Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > AWS Elemental MediaConvert Job
  Template
---

# AWS Elemental MediaConvert Job Template

An AWS Elemental MediaConvert Job Template defines preset settings for video transcoding jobs. It lets you preconfigure inputs, outputs, codecs, bitrates, and packaging options so you can run consistent, repeatable media processing workflows without redefining settings each time. This simplifies largeâscale video preparation for streaming, broadcasting, and archiving.

```
aws.mediaconvert_job_template
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                      | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| acceleration_settings  | core | json       | Accelerated transcoding can significantly speed up jobs with long, visually complex content.                                                                                                                                                                                                                   |
| account_id             | core | string     |
| arn                    | core | string     | An identifier for this resource that is unique within all of AWS.                                                                                                                                                                                                                                              |
| category               | core | string     | An optional category you create to organize your job templates.                                                                                                                                                                                                                                                |
| created_at             | core | timestamp  | The timestamp in epoch seconds for Job template creation.                                                                                                                                                                                                                                                      |
| description            | core | string     | An optional description you create for each job template.                                                                                                                                                                                                                                                      |
| hop_destinations       | core | json       | Optional list of hop destinations.                                                                                                                                                                                                                                                                             |
| last_updated           | core | timestamp  | The timestamp in epoch seconds when the Job template was last updated.                                                                                                                                                                                                                                         |
| name                   | core | string     | A name you create for each job template. Each name must be unique within your account.                                                                                                                                                                                                                         |
| priority               | core | int64      | Relative priority on the job.                                                                                                                                                                                                                                                                                  |
| queue                  | core | string     | Optional. The queue that jobs created from this template are assigned to. If you don't specify this, jobs will go to the default queue.                                                                                                                                                                        |
| settings               | core | json       | JobTemplateSettings contains all the transcode settings saved in the template that will be applied to jobs created from it.                                                                                                                                                                                    |
| status_update_interval | core | string     | Specify how often MediaConvert sends STATUS_UPDATE events to Amazon CloudWatch Events. Set the interval, in seconds, between status updates. MediaConvert sends an update at this interval from the time the service begins processing your job to the time it completes the transcode or encounters an error. |
| tags                   | core | hstore_csv |
| type                   | core | string     | A job template can be of two types: system or custom. System or built-in job templates can't be modified or deleted by the user.                                                                                                                                                                               |
