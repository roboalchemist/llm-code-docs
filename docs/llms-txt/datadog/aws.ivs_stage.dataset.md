# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_stage.dataset.md

---
title: Ivs Stage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ivs Stage
---

# Ivs Stage

This table represents the ivs_stage resource from Amazon Web Services.

```
aws.ivs_stage
```

## Fields

| Title                                    | ID   | Type       | Data Type                                                                         | Description |
| ---------------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string     |
| account_id                               | core | string     |
| active_session_id                        | core | string     | ID of the active session within the stage.                                        |
| arn                                      | core | string     | Stage ARN.                                                                        |
| auto_participant_recording_configuration | core | json       | Configuration object for individual participant recording, attached to the stage. |
| endpoints                                | core | json       | Summary information about various endpoints for a stage.                          |
| name                                     | core | string     | Stage name.                                                                       |
| tags                                     | core | hstore_csv |
