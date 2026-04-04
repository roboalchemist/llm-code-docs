# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_incidents_incident_record.dataset.md

---
title: Systems Manager Incidents Incident Record
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Systems Manager Incidents Incident
  Record
---

# Systems Manager Incidents Incident Record

This table represents the Systems Manager Incidents Incident Record resource from Amazon Web Services.

```
aws.ssm_incidents_incident_record
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                           | Description |
| ---------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The Amazon Resource Name (ARN) of the incident record.                                                                                                                                                                                                                                              |
| automation_executions  | core | json       | The runbook, or automation document, that's run at the beginning of the incident.                                                                                                                                                                                                                   |
| chat_channel           | core | json       | The chat channel used for collaboration during an incident.                                                                                                                                                                                                                                         |
| creation_time          | core | timestamp  | The timestamp for when Incident Manager created the incident record.                                                                                                                                                                                                                                |
| dedupe_string          | core | string     | The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.                                                                                                                                                                        |
| impact                 | core | int64      | The impact of the incident on customers and applications. <p class="title"> <b>Supported impact codes</b> <ul> <li> <code>1</code> - Critical </li> <li> <code>2</code> - High </li> <li> <code>3</code> - Medium </li> <li> <code>4</code> - Low </li> <li> <code>5</code> - No Impact </li> </ul> |
| incident_record_source | core | json       | Details about the action that started the incident.                                                                                                                                                                                                                                                 |
| last_modified_by       | core | string     | Who modified the incident most recently.                                                                                                                                                                                                                                                            |
| last_modified_time     | core | timestamp  | The timestamp for when the incident was most recently modified.                                                                                                                                                                                                                                     |
| notification_targets   | core | json       | The Amazon SNS targets that are notified when updates are made to an incident.                                                                                                                                                                                                                      |
| resolved_time          | core | timestamp  | The timestamp for when the incident was resolved. This appears as a timeline event.                                                                                                                                                                                                                 |
| status                 | core | string     | The current status of the incident.                                                                                                                                                                                                                                                                 |
| summary                | core | string     | The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context of the incident.                                                                                                                                                             |
| tags                   | core | hstore_csv |
| title                  | core | string     | The title of the incident.                                                                                                                                                                                                                                                                          |
