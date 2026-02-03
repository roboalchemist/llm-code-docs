# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconvert_preset.dataset.md

---
title: AWS Elemental MediaConvert Preset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Elemental MediaConvert Preset
---

# AWS Elemental MediaConvert Preset

AWS Elemental MediaConvert Preset defines a reusable set of video and audio encoding settings for MediaConvert jobs. It allows you to standardize output formats, codecs, bitrates, resolutions, and other parameters across multiple transcoding tasks. Using presets simplifies job creation and ensures consistent media quality and delivery specifications.

```
aws.mediaconvert_preset
```

## Fields

| Title        | ID   | Type       | Data Type                                                                                                           | Description |
| ------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| arn          | core | string     | An identifier for this resource that is unique within all of AWS.                                                   |
| category     | core | string     | An optional category you create to organize your presets.                                                           |
| created_at   | core | timestamp  | The timestamp in epoch seconds for preset creation.                                                                 |
| description  | core | string     | An optional description you create for each preset.                                                                 |
| last_updated | core | timestamp  | The timestamp in epoch seconds when the preset was last updated.                                                    |
| name         | core | string     | A name you create for each preset. Each name must be unique within your account.                                    |
| settings     | core | json       | Settings for preset                                                                                                 |
| tags         | core | hstore_csv |
| type         | core | string     | A preset can be of two types: system or custom. System or built-in preset can't be modified or deleted by the user. |
